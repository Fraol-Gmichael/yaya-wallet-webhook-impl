from flask import request, jsonify
import logging
from ..service.hmac_verification_helper import verify_signature
from ..service.webhook_processing_helper import get_or_create_transaction

logger = logging.getLogger(__name__)

def process_webhook(app):
    @app.route('/webhook', methods=['POST'])
    def webhook():
        logger.info("Webhook request received", extra={
            'method': request.method,
            'headers': dict(request.headers),
            'remote_addr': request.remote_addr
        })

        payload = request.get_json()
        logger.debug(f"Payload: {payload}")

        signature = request.headers.get('YAYA-SIGNATURE')

        if not signature:
            logger.error("No signature provided with payload", extra={
                'payload': payload
            })
            return jsonify({"error": "Forbidden"}), 403
        
        if not verify_signature(payload, signature):
            logger.error("Invalid signature for payload", extra={
                'payload': payload,
                'signature': signature
            })
            return jsonify({"error": "Forbidden"}), 403

        try:
            get_or_create_transaction(payload)
        except Exception as e:
            logger.exception("Error processing transaction", extra={
                'payload': payload,
                'error': str(e)
            })
            return jsonify({"error": "Server Error"}), 500
        
        logger.info("Webhook processing completed successfully")
        return jsonify({"status": "success", "code": 200, "remark": "Webhook processing completed successfully"}), 200
