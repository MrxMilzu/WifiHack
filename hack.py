import os,sys,time,datetime
from concurrent.futures import ThreadPoolExecutor

def mil(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./500)
def aink(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./50)
mil("""
\033[91m
  /???    /???     / ??????    /?????????      /???  /???    \033[91m
 | ???   | ???    / ???/\???  \  ???\___/     | ??? /???     \033[91m
 | ???????????   / ???/__\???  \  ???\        | ???????      \033[91m
 | ???????????  / ????????????  \  ???\       | ?????????    \033[97m
 | ???/__/ ??? / ??? ______ ???  \  ???\      | ??? __ ???   \033[97m
 | ???   | ???/ ???/       \ ???  \  ???????? | ???|  \ ???  \033[97m
 |___/   |___//___/        /___/   \/_______/ |/___/   \___\           """)
aink("\033[93m*\033[97m CRACK PASWORD WIFI YANG TERLUPA...")
aink("\033[93m*\033[97m INI TOOLS MEMBANTU ANDA MENCARI PASWORD WIFI YANG TERLUPA...")
print("")
mil("\033[92m╔══════════════════════════════════════════════════════╗")
mil("║ \033[91m *\033[93mYoutube  \033[96m: \033[92mMilzu-Tc                             \033[92m   ║")
mil("║ \033[91m *\033[93mFacebook \033[96m: \033[92mMxtQuest                             \033[92m   ║")
mil("║ \033[91m *\033[93minstagram\033[96m: \033[92mavx_milzu                            \033[92m   ║")
mil("╚══════════════════════════════════════════════════════╝")
aink("\033[97m          [-] \033[92m   Welcome to this tool   \033[97m [-]")
print("")
aink("   \033[93m*\033[97m Pergunakanlah dengan bijak...")
mil("   \033[93m*\033[97m Password Login With Whatsapp")
mil("   \033[93m*\033[97m Whatsapp Me:\033[92m+6283182713104")

ASU = input("\n\033[93m[?] \033[92mNAMA\033[95m:\033[93m ")
tolol = input("\033[93m[?] \033[92mNOMOR HP\033[95m:\033[93m ")
jeng = input("\033[93m[?] \033[92mALAMAT\033[95m:\033[93m ")
Password = "hack"

loop = 'true'
while (loop == 'true'):
    passcode = input("\033[1;93m[?] \033[92mPassword Tools\033[95m:\033[93m ")
    if (passcode == Password):
            loop = 'false'
    else:
            os.system('xdg-open https://chat.wa.me/6283866643691?text=*Asalamualaikum+bang+Minta+Pasword+Scnya+Bang😅*')
            aink('Yang Bener Masukin nya Kontol !!')
            aink('paswordnya salah goblok')
            os.system("exit")

mil("""
├─┐        ┌┬┐ ├┬┤  ┌───┐ ├┬┤ ┌───┬───┐ ├┬┤  INSTAGRAME : avx_milzu
  │   ┌┬┐   │   │   │  ┐   │  ┴┘  │  └┴  │   MADE WITH : INDONESIA
  │    │    │   │   ├──┤   │      │      │   AUTHOR : MILZUTX
 ┌┴────┴────┘  ┌┴┐ ┌┴┐    ┌┴┐    ┌┴┐    ┌┴┐  PROGRAM WITH : PYTHON
 └─────────────────────────────────────────────────────────────────[VERSION 0.1]""")
print("       \033[97m[\033[91m▪\033[97m]NAME\033[96m : " + ASU)
print("       \033[97m[\033[91m▪\033[97m]TELEPHONE\033[96m : " + tolol)
print("       \033[97m[\033[91m▪\033[97m]ALAMAT\033[96m : " + jeng)
print("       \033[97m[\033[91m▪\033[97m]DATE NOW\033[96m : ", datetime.datetime.now())
print("""
 ┌─────────────────────────────────────────────────────────────────┐
 │   ┌────┬─────────┐ ┌────┬─────────────┐ ┌────┬────────────────┐ │
 │   │ 01 │ START.  │ │ 02 │ REPORT BUG  │ │ 03 │ JOIN WHATSAPP  │ │
 │   └────┴─────────┘ └────┴─────────────┘ └────┴────────────────┘ │
 │                      ┌────┬─────────┐                           │
 │                      │ 00 │ LOGOUT. │                           │
 │                      └────┴─────────┘                           │
 └─────────────────────────────────────────────────────────────────┘""")

print("\033[97m╭╼[\033[93mCyber Multi Brute Force\033[97m]\033[97m─\033[97m[\033[93mPrenflix\033[97m]")
print("\033[97m~")
fake = input("\033[97m╰╼▪\033[93m>   \033[97m")
if fake == "1" or fake =="01":
        import subprocess,time
        print("=============================================================================")
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    print ("          ┌──────────────────────────┬───────────────────┐")
                    print ("          |          \033[92mUSERNAME        \033[97m|      \033[92mpasword      \033[97m|")
                    print ("          └──────────────────────────┴───────────────────┘")
                    print ("          ┌──────────────────────────┬───────────────────┐")
                    print ("                    {:<15} [-]      {:<}".format(i, results[0]))
                    print ("          └──────────────────────────┴───────────────────┘")
                    time.sleep(2.0)
                except IndexError:
                    print ("          ┌──────────────────────────┬───────────────────┐")
                    print ("                    {:<15} [-]      {:<}".format(i, ""))
                    print ("          └──────────────────────────┴───────────────────┘")
            except subprocess.CalledProcessError:
                print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
                print("=============================================================================")
                os.system("clear")
                for x in range(20):
                   sys.stdout.write("[\] WAIT TO PEMBERSIHAN TOOLS.")
                   time.sleep(0.1)
                   sys.stdout.write('[|] WAIT TO PEMBERSIHAN TOOLS..')
                   time.sleep(0.1)
                   sys.stdout.write('[/] WAIT TO PEMBERSIHAN TOOLS...')
                   time.sleep(0.1)
                   sys.stdout.write("[-] WAIT TO PEMBERSIHAN TOOLS.")
                   time.sleep(0.1)
                   sys.stdout.write('[\] WAIT TO PEMBERSIHAN TOOLS..')
                   time.sleep(0.1)
                   sys.stdout.write('[|] WAIT TO PEMBERSIHAN TOOLS...')
                   time.sleep(0.1)
                   sys.stdout.write("[/] WAIT TO PEMBERSIHAN TOOLS.")
                   time.sleep(0.1)
                   sys.stdout.write('[-] WAIT TO PEMBERSIHAN TOOLS..')
                   time.sleep(0.1)
                   sys.stdout.write('[OK] WAIT TO PEMBERSIHAN TOOLS...')
                   time.sleep(0.1)
                   os.system("exit")
elif fake == '0' or fake =='00':
     aink("\n\033[1;92m \n\n")
     os.system('xdgu-open  https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ')
     for x in range(20):
        sys.stdout.write("[\] WAIT TO PEMBERSIHAN TOOLS.")
        time.sleep(0.1)
        sys.stdout.write('[|] WAIT TO PEMBERSIHAN TOOLS..')
        time.sleep(0.1)
        sys.stdout.write('[/] WAIT TO PEMBERSIHAN TOOLS...')
        time.sleep(0.1)
        sys.stdout.write("[-] WAIT TO PEMBERSIHAN TOOLS.")
        time.sleep(0.1)
        sys.stdout.write('[\] WAIT TO PEMBERSIHAN TOOLS..')
        time.sleep(0.1)
        sys.stdout.write('[|] WAIT TO PEMBERSIHAN TOOLS...')
        time.sleep(0.1)
        sys.stdout.write("[/] WAIT TO PEMBERSIHAN TOOLS.")
        time.sleep(0.1)
        sys.stdout.write('[-] WAIT TO PEMBERSIHAN TOOLS..')
        time.sleep(0.1)
        sys.stdout.write('[OK] WAIT TO PEMBERSIHAN TOOLS...')
        time.sleep(0.1)
        os.system("exit")
        os.system("exit")
elif fake == '2' or fake =='02':
     aink("\n\033[1;92m \n\n")
     os.system('xdgu-open https://whatsapp.com/')
     for x in range(20):
        sys.stdout.write("\r WAIT TO PEMBERSIHAN TOOLS.")
        time.sleep(0.1)
        sys.stdout.write('\r WAIT TO PEMBERSIHAN TOOLS..')
        time.sleep(0.1)
        sys.stdout.write('\r WAIT TO PEMBERSIHAN TOOLS...')
        time.sleep(0.1)
        os.system("clear")
        os.system("exit")
elif fake == '3' or fake =='03':
     aink("\n\033[1;92m \n\n")
     os.system('xdgu-open ')
     for x in range(20):
        sys.stdout.write("\r WAIT TO PEMBERSIHAN TOOLS.")
        time.sleep(0.1)
        sys.stdout.write('\r WAIT TO PEMBERSIHAN TOOLS..')
        time.sleep(0.1)
        sys.stdout.write('\r WAIT TO PEMBERSIHAN TOOLS...')
        time.sleep(0.1)
        os.system("clear")
        os.system("exit")
