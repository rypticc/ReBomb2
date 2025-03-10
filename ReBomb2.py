import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()

print(Fore.CYAN + """ ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌          ▐░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░▌  ▄▄▄▄▄▄▄▄▄█░▌
▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░░░░░░░░░░░▌
▐░▌     ▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀ """)
print("")
print("")
print("Tutorial for this is on my Youtube: BioRat")

print("")
print("")

x = input('Enter the request URL from Inspect Element: ')
print("")
print("")

print('Reporting the poor sod.....')
print('')
print('')

while True:
    req = session.post(x)
    
    print(req.text)
    print('reported :D')

    time.sleep(10)


input()

https://www.tiktok.com/aweme/v2/aweme/feedback/?WebIdLastTime=1739980562&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-GB&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%3B%20CrOS%20x86_64%2014541.0.0%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F133.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&current_region=GB&data_collection_enabled=true&device_id=7473159601329309206&device_platform=web_pc&focus_state=true&from_page=user&history_len=8&is_fullscreen=false&is_page_visible=true&lang=en&nickname=King%20Reho&object_id=7379659364749837317&odinId=7473159582064788502&os=linux&owner_id=7379659364749837317&priority_region=&reason=9004&referer=https%3A%2F%2Fwww.tiktok.com%2F%40murphy.donna.chri&region=GB&report_type=user&root_referer=https%3A%2F%2Fwww.tiktok.com%2Fforyou%3Fsource%3Dtwa&screen_height=864&screen_width=1536&secUid=MS4wLjABAAAAbf5Fz9-aN_CKUjXlSqjg0MpyAf1fkQAAUi7oMxpZcPAFiqkTqfV0zrIMHAbeJdGC&target=7379659364749837317&tz_name=Europe%2FLondon&user_is_login=false&verifyFp=verify_m7wj5gg9_ERWkc4Ev_5K3X_4ULx_9TL1_Ckw95BU0hsxR&webcast_language=en&msToken=TNqbIOdgKeBj3avN4tj0gFei7cC0yNLcmL_OT8qacoReMgwSsa6hp_kFYj-tJmWpRRaLpwQY6NjcDS9W0dF31VqsAhlRBK6VT8PtOWN5jIyAEXYEVLm4Mzx2rvdfbDWlAgWWJ2pIQcjYdBIJVVRzPgOS&X-Bogus=DFSzswVLk3sANrARtZmHKYWydos5&_signature=_02B4Z6wo00001ej1N-QAAIDAgla8ngHmJHno9TNAAB303b



