from app.service.hmac_verification_helper import verify_signature

def test_hmac_verification_success():
    payload = {
        "id": "1dd2854e-3a79-4548-ae36-97e4a18ebf81",
        "amount": 100,
        "currency": "ETB",
        "created_at_time": 1673381836,
        "timestamp": 1701272333,
        "cause": "Testing",
        "full_name": "Abebe Kebede",
        "account_name": "abebekebede1",
        "invoice_url": "https://yayawallet.com/en/invoice/xxxx"
    }
    assert verify_signature(payload, "a5b3ab2def1d7b8b248eb2c009a52dd40e07c11a30ecdb2d459c7cdff0703a6c")
    assert not verify_signature(payload, "a5b3ab2def1d7b8b248eb2c009a52dd40e07c11a30ecdb2d459c7cdff0703a6d")

def test_hmac_verification_failure():
    payload = {
        "id": "1dd2854e-3a79-4548-ae36-97e4a18ebf81",
        "amount": 100,
        "currency": "ETB",
        "created_at_time": 1673381836,
        "timestamp": 1701272333,
        "cause": "Testing",
        "full_name": "Abebe Kebede",
        "account_name": "abebekebede1",
        "invoice_url": "https://yayawallet.com/en/invoice/xxxx"
    }
    assert not verify_signature(payload, "a5b3ab2def1d7b8b248eb2c009a52dd40e07c11a30ecdb2d459c7cdff0703a6d")
