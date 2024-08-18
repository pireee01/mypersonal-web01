# myprofile_01/main/services/gemini_client.py

import requests
import certifi

class GeminiChatbotClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.gemini.com/v1"  # Pastikan ini adalah URL yang benar

    def send_message(self, message):
        url = f"{self.base_url}/chat"  # Pastikan ini adalah endpoint yang benar untuk mengirim pesan
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "message": message
        }
        try:
            response = requests.post(url, json=data, headers=headers, verify=certifi.where())
            response.raise_for_status()  # Untuk memicu pengecualian jika terjadi kesalahan HTTP
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return None
