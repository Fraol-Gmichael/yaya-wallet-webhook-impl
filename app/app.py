from flask import Flask
from .controller.webhook_controller import process_webhook
from .setup import app, db

process_webhook(app)

with app.app_context():
    db.create_all()
    app.run()