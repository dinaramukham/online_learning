import stripe

from online_learning.settings import STRIPE_API_KEY

# from online_learning.settings import STRIPE_API_KEY
stripe.api_key = STRIPE_API_KEY


def create_stripe_product(obj):
    stripe_product = stripe.Product.create(
        name=obj.title,
        description=obj.content
    )
    return stripe_product['id']


def create_stripe_price(stripe_product_id, money):
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=money,
        product=stripe_product_id,
        product_data={"name": "Payment"},
    )
    return stripe_price['id']


def create_stripe_session(stripe_price_id):
    stripe_session = stripe.checkout.Session.create(
        success_url="https://http://127.0.0.1:8000/",
        line_items=[{"price": stripe_price_id, "quantity": 1}],
        mode="payment",
    )
    return stripe_session['url']