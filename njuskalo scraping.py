from directkeys import *         # module to simulate keypresses
from bs4 import *                # Beautiful Soup
import matplotlib.pyplot as plt  # matplotlib
from time import sleep           # sleep to wait between keypresses
import pyperclip                 # copy and paste
import webbrowser                # open webbrowser
    
def request(url): # replacment for requests.get(url)
    webbrowser.open_new_tab(url)
    sleep(1.3)
    SendInput(Keyboard(VK_CONTROL))
    SendInput(Keyboard(KEY_U))
    sleep(0.1)
    SendInput(Keyboard(KEY_U,KEYEVENTF_KEYUP))
    sleep(1.3)
    SendInput(Keyboard(KEY_A))
    sleep(0.1)
    SendInput(Keyboard(KEY_A,KEYEVENTF_KEYUP))
    sleep(0.2)
    SendInput(Keyboard(KEY_C))
    sleep(0.1)
    SendInput(Keyboard(KEY_C,KEYEVENTF_KEYUP))
    sleep(0.1)
    SendInput(Keyboard(KEY_W))
    sleep(0.1)
    SendInput(Keyboard(KEY_W,KEYEVENTF_KEYUP))
    sleep(0.1)
    SendInput(Keyboard(KEY_W))
    sleep(0.1)
    SendInput(Keyboard(KEY_W,KEYEVENTF_KEYUP))
    SendInput(Keyboard(VK_CONTROL,KEYEVENTF_KEYUP))
    return pyperclip.paste()

lookup = {"32GB":[],"16GB":[],"8GB":[],"4GB":[],"2GB":[],"1GB":[]}


url="https://www.njuskalo.hr/index.php?ctl=search_ads&keywords=ddr3+ecc&categoryId=9596&page="

for page in range(1,5):
    html = request(url+str(page))
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.findAll("h3",{"class":"entity-title"}):
        for i,j in enumerate(lookup.keys()):
            if j in tag.text.upper().replace(' ',''):
                try:
                    price = [int(s) for s in tag.parent.find("strong",{"class":"price price--hrk"}).text.split() if s.isdigit()][0]
                except:
                    continue
                if (j == "32GB" and price < 120) or (j == "4GB" and price > 300) or\
                   (j == "8GB" and price > 600): # checking outliers
                    print(tag.text,'\n',j,price)
                    user_cor = input("Is this correct?(Y/N/#GB) ").upper()
                    if user_cor == 'N':
                        continue
                    elif user_cor in lookup.keys():
                        lookup[user_cor].append(price)
                        continue
                lookup[j].append(price)
                break

fig1, ax = plt.subplots()
ax.boxplot(lookup.values())
ax.set_xticklabels(lookup.keys())
plt.show()
