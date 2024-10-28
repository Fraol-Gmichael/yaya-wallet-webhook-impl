from ..setup import db

class Transaction(db.Model):
    __tablename__ = "yaya_transactions"
    id = db.Column(db.String, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    created_at_time = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)
    cause = db.Column(db.String, nullable=True)
    full_name = db.Column(db.String, nullable=False)
    account_name = db.Column(db.String, nullable=False)
    invoice_url = db.Column(db.String, nullable=True)

    def __init__(self, id, amount, currency, created_at_time, timestamp, cause, full_name, account_name, invoice_url):
        self.id = id
        self.amount = amount
        self.currency = currency
        self.created_at_time = created_at_time
        self.timestamp = timestamp
        self.cause = cause
        self.full_name = full_name
        self.account_name = account_name
        self.invoice_url = invoice_url