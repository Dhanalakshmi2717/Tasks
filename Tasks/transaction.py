
transactions = [
    {"id": 1, "amount": 500, "location": "Chennai"},
    {"id": 2, "amount": 45000, "location": "Delhi"},
    {"id": 3, "amount": 52000, "location": "Chennai"},
    {"id": 4, "amount": 200, "location": "Coimbatore"}
]

def detect_fraud(transactions):
    suspicious_transactions = []
    last_location = {}

    for transaction in transactions:
        user_id = transaction["id"]
        amount = transaction["amount"]
        location = transaction["location"]

        # Rule 1: High amount transaction
        if amount > 50000:
            suspicious_transactions.append(transaction)

        # Rule 2: Location change for same user
        if user_id in last_location:
            if last_location[user_id] != location:
                suspicious_transactions.append(transaction)

        last_location[user_id] = location

    return suspicious_transactions


fraud_cases = detect_fraud(transactions)
print("Suspicious Transactions:")
for case in fraud_cases:
    print(case)
