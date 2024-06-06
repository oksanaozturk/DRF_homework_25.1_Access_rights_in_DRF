# Прописываем сервисные функции для работы со stripe
import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product):
    """Функция создания продукта в Stripe."""
    product_name = ""
    if product.course:
        product_name = product.course.name
    elif product.lesson:
        product_name = product.lesson.name
    # Ещё один вариант отображения выбора имени курса или урока
    # product_name = f'{product.course}' if product.course else f'{product.lesson}'
    stripe_product = stripe.Product.create(name=f'{product_name}')
    return stripe_product['id']


def create_stripe_price(product, product_id):
    """Функция для создания цены в Stripe."""
    # Необходимо умножить на 100, иначе сумма отображается в копейках
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=product.amount * 100,
        product=product_id
    )
    price_id = stripe_price['id']
    return price_id


def create_stripe_session(price_id):
    """Функция для создания сессии на оплату в Stripe."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    # Возвращаем id сессии (session.get('id')) и ссылку на оплату (session.get('url'))
    return session.get('id'), session.get('url')
