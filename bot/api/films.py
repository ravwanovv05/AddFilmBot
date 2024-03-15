import requests
import os
from dotenv import load_dotenv

load_dotenv()


class Film:

    def update_film_message_id(self, message_id, file_unique_id):
        url = f"{os.getenv('UPDATE_FILM_MESSAGE_ID')}{file_unique_id}"
        data = {'message_id': message_id}
        response = requests.patch(url, data=data)
        return response.json()
