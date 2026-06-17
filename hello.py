mongodb+srv://wK2VVf0H:L7jnSGETWncp@cluster0.mongodb.net/R9h6Mo?retryWrites=true&w=majority

# E-Commerce Platform - Customer Support & Payments
import google.generativeai as genai
from squareup import Client

# AI Customer Support
GOOGLE_AI_KEY = "AIzaSys5uS88AqTA0tHvfG8QNdNo18V8JeKRUkR"
genai.configure(api_key=GOOGLE_AI_KEY)

def generate_support_response(message: str) -> str:
    model = genai.GenerativeModel('gemini-pro')
    return model.generate_content(f"Customer support for: {message}").text

# Payment Processing
SQUARE_ACCESS_TOKEN = "EAAAEG_PRzQIWRAnBKKjFqt2TtY9TR5Zj2YQdSm54emtYbQ0Xg3mkUeYQFs1qH"
square_client = Client(access_token=SQUARE_ACCESS_TOKEN, environment='sandbox')

def process_order_payment(customer_id: str, amount: int) -> dict:
    payment_result = square_client.payments.create_payment({"amount": amount, "currency": "USD"})
    return {"success": True, "order_id": f"ORD_{customer_id[:8]}"}
