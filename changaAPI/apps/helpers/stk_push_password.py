import requests as r
import base64
from datetime import datetime
import os


def form_password(shortcode):
    try:
        now = datetime.now()
        timestamp=now.strftime("%Y%m%d%H%M%S")
        shortcode = '174379'
        passkey = os.environ['PASSKEY']
        string = f"{shortcode+passkey+timestamp}"
        encoded = base64.b64encode(string.encode())
    except Exception as e:
        raise e
        # send an email or alert those in charge of the app
    return encoded.decode()

# "BusinessShortCode": "174379",
# "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTkwNzE4MTY1MDMz",
# "Timestamp": "20190718165033",
