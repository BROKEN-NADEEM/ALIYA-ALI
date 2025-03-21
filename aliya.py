import requests
import os
import re
import time
import sys
import random
from requests.exceptions import RequestException

# Clear Screen Function
def clear_screen():
    os.system("clear")

# Animated Logo Reveal
def animated_logo(logo):
    for char in logo:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.002)

# Blinking Text for Alerts
def blinking_text(text, color_code="\033[91m", blink_count=5):
    for _ in range(blink_count):
        sys.stdout.write(f"\r{color_code}{text} ")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * len(text))
        sys.stdout.flush()
        time.sleep(0.3)

# Spinning Loader
def loading_animation(text="Processing"):
    spinner = ['|', '/', '-', '\\']
    for _ in range(15):
        sys.stdout.write(f"\r\033[1;33m{text}... {spinner[_ % 4]}")
        sys.stdout.flush()
        time.sleep(0.1)

# Progress Bar
def progress_bar(current, total):
    bar_length = 40
    filled_length = int(bar_length * current // total)
    bar = "█" * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f"\r\033[92mProgress: |{bar}| {current}/{total}")
    sys.stdout.flush()

# Cookie Setup with Limited Use
def set_cookie(max_attempts=5):
    cookie = input("\033[1;37mENT3R YOUR COOKI3 :: ")
    return {"cookie": cookie, "attempts_left": max_attempts}

# Commenter's Name
def get_commenter_name():
    return input("\033[1;32mH9TT3R N9M3 :: ")

# Request Handling with Limited Cookie Control
def make_request(url, headers, cookie_data):
    if cookie_data["attempts_left"] <= 0:
        blinking_text("[!] Cookie Limit Exceeded. Please Re-enter Cookie.", "\033[91m")
        cookie_data.update(set_cookie())  # Reset Cookie
    try:
        loading_animation("Fetching Data")
        response = requests.get(url, headers=headers, cookies={'Cookie': cookie_data["cookie"]}).text
        cookie_data["attempts_left"] -= 1  # Reduce attempts count
        return response
    except RequestException as e:
        blinking_text("[!] Error making request", "\033[91m")
        return None

# Logo
clear_screen()
logo = """
\033[1;32m____  _____       _       ______   _____  ____    ____     ______   
\033[1;32m|_   \|_   _|     / \     |_   _ `.|_   _||_   \  /   _|  .' ___  |  
\033[1;33m|   \ | |      / _ \      | | `. \ | |    |   \/   |   / .'   \_|  
\033[1;32m| |\ \| |     / ___ \     | |  | | | |    | |\  /| |   | |    ___  
\033[1;33m_| |_\   |_ _/ /   \ \_ _| |_.' /_| |_  _| |_\/_| |_  \ `.___]  |  
\033[1;32m|_____|\____||____| |____||______.'|_____||_____||_____|  `._____.'    
\033[1;32m<<══════════════════════════════════════════════════════════════════>>
\033[1;33m[=] OWNER                       : BROKEN NADEEM                      
\033[1;32m[=] 𝐆𝐈𝐓𝐇𝐔𝐁                    : BROKEN NADEEM                     
\033[1;36m[=] 𝐑𝐔𝐋𝐄𝐗                      : COOKISE POST                       
\033[1;33m[=] 𝐅𝐀𝐂𝐄𝐁𝐎𝐊                    : PARDHAN KIING                      
\033[1;32m<<══════════════════════════════════════════════════════════════════>>
"""
animated_logo(logo)

print("\033[92mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))  

# Login System
cookie_data = set_cookie()
while True:
    try:
        print()
        response = make_request('https://business.facebook.com/business_locations', headers={
            'Cookie': cookie_data["cookie"],
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
        }, cookie_data=cookie_data)

        if response is None:
            break

        token_eaag = re.search('(EAAG\w+)', str(response)).group(1)
        id_post = int(input(" \033[92mENT3R POST ID :: "))
        commenter_name = get_commenter_name() 
        delay = int(input(" \033[92mENT3R D3ALY S3COND3 :: "))
        comment_file_path = input(" \033[92mENT3R YOUR C0MM3NT F1L3 P9TH :: ")

        with open(comment_file_path, 'r') as file:
            comments = file.readlines()

        total_comments = len(comments)
        x, y = 0, 0
        print()

        while True:
            try:
                time.sleep(delay)
                teks = comments[x].strip()
                comment_with_name = f"{commenter_name}: {teks}"
                data = {
                    'message': comment_with_name,
                    'access_token': token_eaag
                }

                response2 = requests.post(f'https://graph.facebook.com/{id_post}/comments/', data=data, cookies={'Cookie': cookie_data["cookie"]}).json()

                if '\'id\':' in str(response2):
                    print("\033[1;37mTARG3T P0ST ID ::", id_post)
                    print("\033[1;30mDAT3 T1M3      ::", time.strftime("%Y-%m-%d %H:%M:%S"))
                    print("\033[92mBROKEN NADEEM::", comment_with_name)
                    print('\033[1;33m' + '<<══════════════════════════════════════════════════════════════════>>')
                    x = (x + 1) % total_comments
                else:
                    y += 1
                    print("\033[91m[{}] Status : Failure".format(y))
                    print("\033[91m[/] Link : https://m.basic.facebook.com//{}".format(id_post))
                    print("\033[91m[/] Comments : {}\n".format(comment_with_name))
                    continue

                progress_bar(x, total_comments)  # Progress Bar

            except RequestException as e:
                blinking_text("[!] Network Error", "\033[91m")
                time.sleep(5.5)
                continue

    except Exception as e:
        blinking_text("[!] Unexpected Error", "\033[91m")
        break
