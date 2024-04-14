from json import dumps
from httplib2 import Http

# Copy the webhook URL from the Chat space where the webhook is registered.
# The values for SPACE_ID, KEY, and TOKEN are set by Chat, and are included
# when you copy the webhook URL.

def webhook(msg1):
    """Google Chat incoming webhook quickstart."""
    url = "https://chat.googleapis.com/v1/spaces/AAAA1006yog/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=0j2Kg6Ma1Q4nB6Jn9ZXwk5eIkZdvokzieBaX_9LQxT4"
    #app_message = {"text": "Hello from a Python script!"}
    app_message={"text":msg1}
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )
    print(response)


def webhook_personal(to_email, msg1):
    """Send message to a specific user's Google Chat."""
    url = "https://chat.googleapis.com/v1/spaces/AAAA1006yog/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=0j2Kg6Ma1Q4nB6Jn9ZXwk5eIkZdvokzieBaX_9LQxT4"
    
    app_message = {
        "text": msg1,
        "toUserEmail": to_email  # Specify the user's email address here
    }

    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )
    print(response)