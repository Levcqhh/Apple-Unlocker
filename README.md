
# Apple ID Unlocker MABY PATCHED !

This script automates the process of unlocking Apple ID accounts by solving captcha challenges, verifying account details, and resetting the password. The script uses the `requests` library for all HTTP requests, ensuring simplicity and flexibility. Captcha challenges are solved using the **YesCaptcha** service.

---

## Features

- Fully automated process for Apple ID unlocking.
- Captcha solving via the [YesCaptcha](https://yescaptcha.com) service.
- Security question verification and response.
- Password reset with a new password provided in the configuration.
- Multi-threaded support for processing multiple accounts.
- VPN integration for bypassing rate limits or IP bans [ExpressVPN](https://www.expressvpn.com/go/home?gad_source=1&gclid=Cj0KCQiAvvO7BhC-ARIsAGFyToXmrJ1y0xWaGxR4_VjarR62fdbninp7bHhV_XymHZHfBhCq931f7E8aAosuEALw_wcB)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Levcqhh/Apple-Unlocker.git
   cd Apple-Unlocker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare the necessary files:
   - **`files/settings.json`**:
     Add your YesCaptcha API key and the new password to be set.
     ```json
     {
       "API_KEY": "your_yescaptcha_api_key",
       "new_password": "your_new_password"
     }
     ```
   - **`files/Accounts.txt`**:
     List of accounts to process, with each line in the following format:
     ```text
     email,password,qq1,qq2,qq3,MM/DD/YYYY
     ```
     - `email`: The Apple ID email.
     - `password`: The current password.
     - `qq1`, `qq2`, `qq3`: Answers to the security questions.
     - `MM/DD/YY`: Date of birth in `MM/DD/YY` format.

---

## Usage

1. Run the script:
   ```bash
   python unlocker.py
   ```
2. Results:
   - **Success**: Unlocked accounts are logged in `files/Success.txt`.
   - **Error**: Failed accounts are logged in `files/error.txt`.

---

## Requirements

- **Python 3.8+**
- **Modules**: Listed in `requirements.txt`.

---

## Dependencies

- **requests**: For all HTTP requests.
- **YesCaptcha**: Used to solve captcha challenges.
- **colorama**: For colorful console output.
- **concurrent.futures**: For multi-threaded processing.
- **evpn**: To manage VPN connections.

---

## File Structure

- **`files/settings.json`**: Contains API key and new password.
- **`files/Accounts.txt`**: Input file with accounts to be unlocked.
- **`files/Success.txt`**: Output file for successfully unlocked accounts.
- **`files/error.txt`**: Output file for failed accounts.

---

## Notes

1. The script requires a valid YesCaptcha API key with sufficient credits.
2. Ensure the VPN integration (`evpn`) is set up properly to avoid rate limits or bans.
3. Adjust `max_workers` in the script for optimal multi-threading performance.

---

## Disclaimer

This script is for educational purposes only. Unauthorized use of this script may violate terms of service and/or local laws. Use responsibly.
