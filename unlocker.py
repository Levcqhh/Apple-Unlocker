import os
import time
import json
import random
import hashlib
import logging
import tls_client
import urllib.parse
from colorama import Fore
from threading import Lock
from yescaptcha.task import ImageToTextTask
from yescaptcha.client import Client
import concurrent.futures
from evpn import ExpressVpnApi

lock = Lock()
logging.basicConfig(level=logging.INFO) 

with open("files/settings.json")as f:
    settings = json.load(f)
def remove_line_containing_text(file_path, target_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        updated_lines = [line for line in lines if target_text not in line]

        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)

    except FileNotFoundError:
        print("No Such File dict")
    except Exception as e:
        print(f"An ERROR : {e}")

qus = {
    "What was the name of your best friend as a teenager?":2,
    "What is the first name of your best friend in high school?": 2,
    "What is your dream job?": 3,
    "In what city did your parents meet?": 4
}


os.system('cls')
print(f"""{Fore.RED} 
      
        :::       ::::::::  :::  :::  :::::::   ::::::    ::::::   :::        ::::::
        :::       ::::::::  :::  :::  :::::::  ::::::::  ::::::::  :::       :::::::
        ::!       ::!       ::!  :::    ::!    ::!  :::  ::!  :::  ::!       !::
        !:!       !:!       !:!  :!:    !:!    !:!  :!:  !:!  :!:  !:!       !:!
        :!!       :!!!:!    :!:  !:!    :!!    :!:  !:!  :!:  !:!  :!!       !!::!!
        !!!       !!!!!:    !:!  !!!    !!!    !:!  !!!  !:!  !!!  !!!        !!:!!!
        !!:       !!:       :!:  !!:    !!:    !!:  !!!  !!:  !!!  !!:            !:!
         :!:      :!:        ::!!:!     :!:    :!:  !:!  :!:  !:!   :!:          !:!
         :: ::::   :: ::::    ::::       ::    ::::: ::  ::::: ::   :: ::::  :::: ::
        : :: : :  : :: ::      :         :      : :  :    : :  :   : :: : :  :: : :
        Discord User :levcqh{Fore.RESET}
""")
class unlocker():

    def __init__(self) -> None:
        pass
    def unlock(self,data_email):
        try:


            start = time.time()
            self.key =  settings['API_KEY']
            self.data_email =data_email
            self.email = data_email.split(',')[0]
            self.password = data_email.split(',')[1]
            self.new_password =  settings['new_password']


            """ SETUP """
            self.session =tls_client.Session(random_tls_extension_order=True , client_identifier="chrome_128")

            self.headers = {
                "accept-language": "en-US,en;q=0.9,ar;q=0.8",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "pragma": "no-cache",
                "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            }

            """ * Get sstt * """

            sendForget = self.session.get('https://iforgot.apple.com/password/verify/appleid',headers=self.headers)
            self.sstt = urllib.parse.quote(sendForget.text.split('"https://iforgot.apple.com","contextUrl":"/","sstt":"')[1].split('","captchaEnabled":true,')[0])


            """ * Set Headers * """

            self.headers['cookie'] = '; '.join([f"{name}={value}" for name, value in sendForget.cookies.items()])
            self.headers['sstt'] = self.sstt
            self.headers['accept']= "application/json, text/javascript, */*; q=0.01"
            self.headers['x-requested-with'] = 'XMLHttpRequests'
            self.headers['x-apple-i-fd-client-info'] = '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","L":"en-US","Z":"GMT+02:00","V":"1.1","F":"sla44j1e3NlY5BNlY5BSs5uQ084akLK77J_v495JppM.S9RdPQSzOy_Aw7UTlWY5Ly.eaB0Tf0IY69WJQStMw8btHz3Y25BNlY5cklY5BqNAE.lTjV.6KH"}'


            """ * Get Captcha INFO * """
            while True:
                sendCaptcha = self.session.get('https://iforgot.apple.com/captcha?captchaType=IMAGE',headers=self.headers)
                self.token = sendCaptcha.json()['token']
                self.capImg = sendCaptcha.json()['payload']['content']
                self.id = sendCaptcha.json()['id']


                """ * CAP SOLVE * """
                client = Client(client_key=self.key)
                task  = ImageToTextTask(self.capImg)
                job = client.create_task(task)

                """ * Start unlock * """

                data ={
                    "id": self.email,
                    "captcha": {
                        "id": self.id,
                        "answer":job.get_solution_text(),
                        "token":self.token
                    }
                }   

                sendAppleid = self.session.post('https://iforgot.apple.com/password/verify/appleid',headers=self.headers,json=data)

                if 'captchaAnswer.Invalid' in sendAppleid.text:
                    pass
                elif sendAppleid.status_code == 503:
                    with ExpressVpnApi() as api:
                        ran = random.choice([84,3,166,19,1,202,2,165,18,172,161,9,95,3,74,3,70,204,94,71,207,79,45,169,178,15,90,5,153,8,103,150,182,29])
                        api.connect(ran)
                    print(f"{Fore.GREEN} [ + ] VPN was Changed Successfuly===> retrying ")
                    time.sleep(10)
                    pass

                else:
                    break
            if sendAppleid.status_code == 302:
                """ * Get New SSTT * """

                sendSSTT = self.session.get(f'https://iforgot.apple.com{sendAppleid.headers["Location"]}',headers=self.headers)

                """ * Send authenticationmethod * """

                sendAuthenticationmethod = self.session.post(f'https://iforgot.apple.com{sendSSTT.headers["Location"]}',headers=self.headers,json={"type":"questions"})


                """ * Send Birthday * """

                sendBirthdayGET = self.session.get(f'https://iforgot.apple.com{sendAuthenticationmethod.headers["Location"]}',headers=self.headers)
                self.headers['sstt'] = sendBirthdayGET.headers['Sstt']

                """ * sendBirthdayPOST * """
                data = {
                    "monthOfYear":self.data_email.split(',')[5].split('/')[0],
                    "dayOfMonth":self.data_email.split(',')[5].split('/')[1],
                    "year":self.data_email.split(',')[5].split('/')[2]
                }
                sendBirthdayPOST = self.session.post('https://iforgot.apple.com/password/verify/birthday',headers=self.headers,json=data)
                print(sendBirthdayPOST.text)

                if sendBirthdayPOST.status_code == 410:
                    print(f"{Fore.RED} [ + ] {self.email} ==> ERROR While unlock ==> TO many Attempts ERORR")
                    remove_line_containing_text('files/Accounts.txt',data_email)
                    with lock:
                        with open("files/error.txt","a+")as f :
                            f.write(f'{self.data_email}\n')     
                    return
                self.headers['sstt'] = sendBirthdayPOST.headers['Sstt']
        
                """ * Get Questions * """
                sendQuestionsGET = self.session.get(f'https://iforgot.apple.com{sendBirthdayPOST.headers["Location"]}',headers=self.headers)
                self.headers['sstt'] = sendQuestionsGET.headers['Sstt']


                """ * Set Payload * """

                question1 = sendQuestionsGET.json()['questions'][0]['question']
                question2 = sendQuestionsGET.json()['questions'][1]['question']
                number1 = sendQuestionsGET.json()['questions'][0]['number']
                number2 = sendQuestionsGET.json()['questions'][1]['number']
                qu_id1 = sendQuestionsGET.json()['questions'][0]['id']
                qu_id2 = sendQuestionsGET.json()['questions'][1]['id']

                payload = {
                    "questions": [
                        {
                            "question": question1,
                            "answer": self.data_email.split(',')[qus[question1]],
                            "id": qu_id1,
                            "number": number1
                        },
                        {
                            "question": question2,
                            "answer": self.data_email.split(',')[qus[question2]],
                            "id": qu_id2,
                            "number": number2
                        }
                    ]
                }
                sendQuestionsPOST = self.session.post('https://iforgot.apple.com/password/verify/questions',headers=self.headers,json=payload)
                if sendQuestionsPOST.status_code == 400:
                    print(f"{Fore.RED} [ + ] {self.email} ==> ERROR While unlock ==> INVAILD questions")
                    remove_line_containing_text('files/Accounts.txt',data_email)
                    with lock:
                        with open("files/error.txt","a+")as f :
                            f.write(f'{self.data_email}\n')    
                    return
                if sendAppleid.status_code == 302:

                    """ * Send Options * """
                    sendOptionsGET = self.session.get(f'https://iforgot.apple.com{sendQuestionsPOST.headers["Location"]}',headers=self.headers)


                    """ * Send reset * """
                    sendResetGET = self.session.get(f'https://iforgot.apple.com{sendOptionsGET.headers["Location"]}',headers=self.headers)
                    self.headers['sstt'] = sendResetGET.headers['Sstt']

                    """ * RESET PASSWORD * """
                    sendResetPassword = self.session.post('https://iforgot.apple.com/password/reset',headers=self.headers,json={"password":self.new_password})
                    if sendResetPassword.status_code ==260:
                        time_ = int(time.time()) - int(start)
                        print(f"{Fore.GREEN} [ + ] {self.email} ==> Was Unlocked Successfuly in ==> {time_}s ")
                        remove_line_containing_text('files/Accounts.txt',data_email)
                        with lock:
                            with open("files/Success.txt","a+")as f :
                                f.write(f'{self.data_email.replace(self.password,self.new_password)}\n')
                    else:
                        print(f"{Fore.RED} [ + ] {self.email} ==> ERROR While unlock ==>")
                        remove_line_containing_text('files/Accounts.txt',data_email)
                        with lock:
                            with open("files/error.txt","a+")as f :
                                f.write(f'{self.data_email}\n')     
                
        except Exception as e :
            print("ERROR ",e)
            print(f"{Fore.RED} [ + ] {self.email} ==> ERROR While unlock ==>")
            remove_line_containing_text('files/Accounts.txt',data_email)
            with lock:
                with open("files/error.txt","a+")as f :
                    f.write(f'{self.data_email}\n')  
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    futures = [executor.submit(unlocker().unlock,emails ) for emails in open('files/Accounts.txt').read().splitlines()]
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
