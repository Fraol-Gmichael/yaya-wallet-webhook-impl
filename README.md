# Yaya Wallet Webhook Service

This service implements a webhook for Yaya Wallet. It is designed to receive and process webhook events from the Yaya Wallet API.

## Getting Started

To run the service, you can use Docker Compose. Follow the steps below to get started:

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build and start the service** using Docker Compose:

   ```bash
   docker-compose up
   ```

3. The service will be accessible at `http://localhost:5000`.

## Testing the Webhook

You can test the webhook by sending a POST request to the `/webhook` endpoint. Below is an example of a successful request:

```bash
curl --request POST \
  --url http://127.0.0.1:5000/webhook \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/2023.5.8' \
  --header 'YAYA-SIGNATURE: a5b3ab2def1d7b8b248eb2c009a52dd40e07c11a30ecdb2d459c7cdff0703a6c' \
  --data '{
    "id": "1dd2854e-3a79-4548-ae36-97e4a18ebf81",
    "amount": 100,
    "currency": "ETB",
    "created_at_time": 1673381836,
    "timestamp": 1701272333,
    "cause": "Testing",
    "full_name": "Abebe Kebede",
    "account_name": "abebekebede1",
    "invoice_url": "https://yayawallet.com/en/invoice/xxxx"
}'
```

### Failure Scenario

To see how the service handles a failure scenario, you can modify the `YAYA-SIGNATURE` in the request. For example, change the signature to an invalid value:

```bash
curl --request POST \
  --url http://127.0.0.1:5000/webhook \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/2023.5.8' \
  --header 'YAYA-SIGNATURE: invalid_signature' \
  --data '{
    "id": "1dd2854e-3a79-4548-ae36-97e4a18ebf81",
    "amount": 100,
    "currency": "ETB",
    "created_at_time": 1673381836,
    "timestamp": 1701272333,
    "cause": "Testing",
    "full_name": "Abebe Kebede",
    "account_name": "abebekebede1",
    "invoice_url": "https://yayawallet.com/en/invoice/xxxx"
}'
```

In this case, the service should respond with an error indicating that the signature is invalid.

## License

This project is licensed under the MIT License.
