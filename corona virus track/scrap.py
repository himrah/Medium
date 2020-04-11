from requests import Session
from bs4 import BeautifulSoup as BS
import requests

url="https://www.worldometers.info/coronavirus/"
r = requests.get(url)
soup = BS(r.content,'html.parser')
table = soup.find("table",attrs={"id":"main_table_countries_yesterday"})

tr = table.find_all("tr")

for i in tr:
	td = i.find_all("td")
	if(td):
		if(td[0].text=='India'):
			total = td[1].text
			new_cases = td[2].text
			total_death = td[3].text
			new_death = td[4].text
			break
key = '<your authentication key>'
payload='sender_id=FSTSMS&message={}&language=english&route=p&numbers={}'.format(
    ".\n\n..Yesterday Report in India..\nTotal Cases-> "+total+"\nNew Cases-> "+new_cases+"\nTotal Death-> "+total_death+"\nNew Death-> "+new_death+"\nBe Safe \n\nBy NiXiS Institute :)\n",
    "phone,phone,.."
    )
headers = {'authorization': key,'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",} 
msg_url = 'https://www.fast2sms.com/dev/bulk'
response = requests.request("POST",msg_url,data=payload,headers=headers)
