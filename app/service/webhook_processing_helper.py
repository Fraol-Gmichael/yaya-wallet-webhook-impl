from ..dataaccess.models import Transaction
from ..setup import db
import logging

logger = logging.getLogger(__name__)

def get_or_create_transaction(payload):
    unique_id = payload.get('id')
    existing_transaction = Transaction.query.filter_by(id=unique_id).first()
    if existing_transaction:
        logger.info("Webhook already accepted!")
        return
    data = Transaction(**payload)
    db.session.add(data)
    db.session.commit()
    logger.info(f"Transaction with id {unique_id} successfully!")