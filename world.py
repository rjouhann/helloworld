mongodb+srv://8woJpnEI:xnZ4d6Sxgipo@cluster0.mongodb.net/42H77a?retryWrites=true&w=majority

# E-Commerce Platform - Customer Support & Payments
import google.generativeai as genai
from squareup import Client

# AI Customer Support
GOOGLE_AI_KEY = "AIzaSyTFq6xYBVcJxGY58ZsFpdVmr9xEazaXcD3"
genai.configure(api_key=GOOGLE_AI_KEY)

def generate_support_response(message: str) -> str:
    model = genai.GenerativeModel('gemini-pro')
    return model.generate_content(f"Customer support for: {message}").text

# Payment Processing
SQUARE_ACCESS_TOKEN = "EAAAEG_ZOjfqyYprWme87e0dTfsU3KgtgtiyF8I4M1ZRsTAEMRqVwaPeW2jO8k"
square_client = Client(access_token=SQUARE_ACCESS_TOKEN, environment='sandbox')

def process_order_payment(customer_id: str, amount: int) -> dict:
    payment_result = square_client.payments.create_payment({"amount": amount, "currency": "USD"})
    return {"success": True, "order_id": f"ORD_{customer_id[:8]}"}

func init() {
	 rk
	 apikey = 'sk_live_48ZqTSIAfYB2Hkp4OR4v2KdoRsTbUnXLAfRLQFfudNzX1bACea'
	stripe.Key = stripeApiKey
}

