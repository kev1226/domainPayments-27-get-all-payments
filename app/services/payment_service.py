from app.database import payments


def get_all_payments_logic():
    results = payments.find().sort("timestamp", -1)
    return [
        {
            "order_id": p.get("order_id"),
            "email": p.get("user_email"),
            "amount": p.get("amount"),
            "currency": p.get("currency"),
            "status": p.get("status"),
            "created_at": p.get("timestamp"),
        }
        for p in results
    ]
