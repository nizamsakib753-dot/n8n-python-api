
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Python API is running!"}

@app.post("/process")
def process_data(data: dict):
    customers = data.get("customers", [])

    total = sum(
        customer.get("purchase_amount", 0)
        for customer in customers
    )

    return {
        "status": "success",
        "total_customers": len(customers),
        "total_purchases": total
    }
