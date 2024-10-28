import hashlib
import hmac
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("YAYA_SECRET_KEY")

def verify_signature(data, signature):
    signed_payload = ''.join(str(value) for value in data.values())
    expected_signature = hmac.new(
        SECRET_KEY.encode(),
        signed_payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected_signature, signature)

