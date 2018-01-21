import requests
from bs4 import BeautifulSoup as bs
import xlwt
import re

names=[]
links=[]
count =0
wb=xlwt.Workbook()
ws = wb.add_sheet("sheet 1")

url="https://bitcointalk.org/index.php?board=121."

for lol in range(0,441,20):
	print lol
	_url=url+str(lol)
	r=requests.get(_url)

	soup = bs(r.content,"lxml")
	

	data = soup.find_all("div",{"id":"bodyarea"})

	

	number=3

	for item in data:
	    je=item.contents[5].contents[1]
	    for _,task in enumerate(je):
		try:
		    bub= item.contents[5].contents[1].contents[number].contents[5].contents[1].contents[0]
		    ws.write(count,0,bub.text)
		    ws.write(count,1,bub['href'])
		    
		    req=requests.get(bub['href'])
		    sou=bs(req.content,"lxml")
		    dat=sou.find_all("body")
		    for itt in dat:
		    	stry=itt.text
		    	found_num_list=re.findall(r'\d{10}',stry)
		    	for _,lel in enumerate(found_num_list):
		    		ws.write(count,_+2,lel)
		    		
		except IndexError:
		    try:
		        bub= item.contents[5].contents[1].contents[number].contents[5].contents[3].contents[0]
		        ws.write(count,0,bub.text)
		        ws.write(count,1,bub['href'])
		        
		        req=requests.get(bub['href'])
		    	sou=bs(req.content,"lxml")
		    	dat=sou.find_all("body")
		    	for itt in dat:
			    	stry=itt.text
			    	found_num_list=re.findall(r'\d{10}',stry)
			    	for _,lel in enumerate(found_num_list):
			    		ws.write(count,_+2,lel)
			    		
		    except:
		        break
		number+=2
		count+=1
wb.save("data.xls")
