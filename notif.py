import requests

def send_webex_message(token, room_id, message):
    api_url = "https://api.ciscospark.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "roomId": room_id,
        "text": message
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)

# Replace these values with your own
access_token = "NzVkNGM1MzctYzc3My00NTMwLTk0NDQtYWEwOGI1NjE0ODVjMzUxYjkwMGEtMTBj_P0A1_d0b19fc5-a717-4064-90e2-8d88b3acad9c"
webex_room_id = "7be0e3a0-9dc8-11ee-8f9a-dd8e638e82f8"
message_text = "Hello from Webex Teams!"

# Call the function to send the message
send_webex_message(access_token, webex_room_id, message_text)
