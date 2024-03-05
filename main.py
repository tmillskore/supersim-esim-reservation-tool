import time
from post_functions.post_functions import (reserve_esim_profile,
                                           activate_esim_profile)
from get_functions.get_functions import (get_esim_sid,
                                         display_qr_code)
from static.config import (account_sid,
                           auth_token,
                           authorization,
                           fleet)


print("Thank you for using the SuperSIM profile reservation script!")
print("If you have not already, please make sure to set your account information and fleet information")
print("for your new profiles in static.config.py")


def main():
    quantity = int(input("How many profiles would you like to retrieve? [int]: "))
    while True:
        qr_code = input("Would you like QR Code images generated for these activation codes? [Yes/No]: ").strip().lower()
        if qr_code in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    for _ in range(quantity):
        sid = reserve_esim_profile(account_sid, auth_token, authorization)  # Make sure to define this function
        time.sleep(2)
        sim_sid, activation_code = get_esim_sid(authorization, sid)  # Make sure to define this function
        time.sleep(2)
        iccid = activate_esim_profile(authorization, sim_sid, fleet)  # Make sure to define this function

        if qr_code == 'yes' and activation_code:  # Check if qr_code is 'yes' and activation_code is not empty
            display_qr_code(activation_code)  # Make sure to define this function
            print(f"QR Code printed for ICCID: {iccid}")
        else:
            print(f"Activation code {activation_code} created for ICCID: {iccid}")


if __name__ == "__main__":
    while True:
        main()
        rerun = input("Would you like to rerun the script? [Yes/No]: ").strip().lower()
        if rerun != 'yes':
            break
