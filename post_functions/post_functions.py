import requests


def reserve_esim_profile(account_sid, auth_token, authorization):
    sid = None
    url = "https://supersim.twilio.com/v1/ESimProfiles"

    payload = {
        'GenerateMatchingId': 'True',
        'account_sid': account_sid,
        'auth_token': auth_token
    }
    headers = {
        'Authorization': authorization
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        data = response.json()
        sid = data.get("sid")

        if sid:
            print("Successfully reserved eSIM profile. SID:", sid)
        else:
            print("Failed to extract SID from the response.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while making the request:", e)
    except ValueError:
        print("Failed to parse response JSON.")
    return sid


def activate_esim_profile(authorization, sim_sid, fleet):
    iccid = None
    url = f"https://supersim.twilio.com/v1/Sims/{sim_sid}"

    payload = f'Fleet={fleet}&Status=active'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': authorization
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()

        data = response.json()
        iccid = data.get("iccid")

        if iccid:
            print("Successfully activated profile. ICCID:", iccid)
        else:
            print("Failed to extract ICCID from the response.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while making the request:", e)
    except ValueError:
        print("Failed to parse response JSON.")
    return iccid
