import time
from http.client import responses

import requests
from django.conf import settings
from celery import shared_task
from prompt_toolkit.shortcuts import message_dialog


@shared_task
def send_telegram_notification(order_id, product_name, quantity, customer_username, phone_number):
    time.sleep(5)
    token = settings.TELEGRAM_BOT_TOKEN
    method = "sendMessage"
    message_text = f"New order:{order_id}\n Product: {product_name}\n Quantity: {quantity}\n " \
                   f"Client: {customer_username}\n tel: {phone_number}"

    response = requests.post(
        url=f"https://api.telegram.org/bot{token}/{method}",
        data={'chat_id':1215182997, 'text': message_text}
    ).json()
    print(response)
    return response