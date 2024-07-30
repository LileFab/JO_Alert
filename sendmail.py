import os

from dotenv import load_dotenv

load_dotenv()

import requests


def send_simple_message(to, objet: str, message: str):
    print(os.getenv("MAILGUN_API_KEY"))

    try:
        return requests.post(
            "https://api.mailgun.net/v3/jo.fleisch.fr/messages",
            auth=("api", os.getenv("MAILGUN_API_KEY")),
            data={
                "from": "Excited User <mailgun@jo.fleisch.fr>",
                "to": to,
                "subject": objet,
                "text": message,
            },
        )
    except Exception as ex:
        print(ex)


send_simple_message(to="backspeen@gmail.com", objet="objet", message="message")
