import base64
from datetime import datetime
import os


def construct_password(shortcode):
    try:
        now = datetime.now()
        timestamp=now.strftime("%Y%m%d%H%M%S")

        passkey = os.environ['PASSKEY']
        string = f"{shortcode+passkey+timestamp}"
        encoded = base64.b64encode(string.encode())
        print("pwd, tmst", encoded.decode(), timestamp)
    except Exception as e:
        raise e
        # send an email or alert those in charge of the app
    return encoded.decode(), timestamp

