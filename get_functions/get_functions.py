import requests
import os
import pyqrcode
from PIL import Image


def get_esim_sid(authorization, sid):
    sim_sid = None
    activation_code = None
    url = f"https://supersim.twilio.com/v1/ESimProfiles/{sid}"

    headers = {
        'Authorization': authorization
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        sim_sid = data.get("sim_sid")
        activation_code = data.get("activation_code")
    except requests.exceptions.RequestException as e:
        print("Error occurred while making the request:", e)
    except ValueError:
        print("Failed to parse response JSON.")
    except KeyError:
        print("Response JSON does not contain expected keys.")

    return sim_sid, activation_code


def display_qr_code(data):
    qr_code = pyqrcode.create(data)
    qr_code.png('qr_code.png', scale=8)
    img = Image.open('qr_code.png')
    img.show()
