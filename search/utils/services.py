import requests
from lxml import html
from . import constants
from ..models import Apps, SearchTerm, SearchResultApp

def getQuery(query):
	print "The Search Query Recieved is: %s"%query

	qry = SearchResultApp.objects.filter(term=query)
	app_list = []
	for q in qry:
		app_list.append(q.app_id)
	
	apps = Apps.objects.filter(id__in=app_list)
	if not apps:
		# if the search term has been saved but no apps was parsed for that term
		# for example user searched "dkjd"
		# this is necessary coz search term is saved first during form submission itself
		return {"result":constants.NOT_FOUND}
	else:
		return {"result":apps}

def makeQuery(query):
	print "Making Query for - %s"%(query)

	queryUrl = constants.URL+query
	req = requests.get(queryUrl)
	if int(req.status_code) == 200:
		parsed_text = parseContent(req.content)
		return {"context":"abc"}
	else:
		return {"Result":constants.NOT_FOUND}

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
