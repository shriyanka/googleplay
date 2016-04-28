import requests
from lxml import html

URL = "https://play.google.com/store/search?q="
def makeQuery(query):
	print "Making Query for - %s"%(query)
	queryUrl = URL+query
	req = requests.get(queryUrl)
	if int(req.status_code) == 200:
		parsed_text = parseContent(req.content)
		return {"context":"abc"}
	else:
		return {"Result":"No Search Result Found"}

def parseContent(content):
	tree = html.fromstring(content)
	name = tree.xpath('//*[@id="body-content"]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/a[2]/span[1]')
	developer = tree.xpath('//*[@id="body-content"]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/a[1]')
	appid = tree.xpath('//*[@id="body-content"]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div')
	image = tree.xpath('//*[@id="body-content"]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/img')
	title = tree.xpath('//*[@id="body-content"]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/a[2]/span[1]')
	price = tree.xpath('//*[@id="body-content"]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/span/span[2]/button/span')
	description = tree.xpath('//*[@id="body-content"]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/text()')

	print name
	print "#############################3\n\n\n\nn\n\\nn\n\n\n\n"
	print developer
	print "#############################3\n\n\n\nn\n\\nn\n\n\n\n"
	print appid
	print "#############################3\n\n\n\nn\n\\nn\n\n\n\n"
	print image
	print "#############################3\n\n\n\nn\n\\nn\n\n\n\n"
	print title
	print "#############################3\n\n\n\nn\n\\nn\n\n\n\n"
	print price
	print "#############################3\n\n\n\nn\n\\nn\n\n\n\n"
	print description

def getQuery(query):
	return {"context":"abc"}
