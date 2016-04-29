import requests
from lxml import html
from . import constants
from ..models import Apps, SearchTerm, SearchResultApp

def getTrending():
	return SearchTerm.objects.all().order_by("-count")[:5]

def getQuery(query):
	print "The Search Query Recieved is: %s"%query
	qry = SearchResultApp.objects.filter(term=query)
	app_list = []
	for q in qry:
		app_list.append(q.app_id)
	
	apps = Apps.objects.filter(app_id__in=app_list)
	if not apps:
		# if the search term has been saved but no apps was parsed for that term
		# for example user searched "dkjd"
		# this is necessary coz search term is saved first during form submission itself
		# and later the related apps get updated
		return {"result":constants.NOT_FOUND}
	else:
		return {"result":apps}

def makeQuery(query):
	print "Making Query for - %s"%(query)

	queryUrl = constants.URL+query
	req = requests.get(queryUrl)
	if int(req.status_code) == 200:
		app_list = parseContent(req.content,query)
		apps = Apps.objects.filter(app_id__in=app_list)
		if apps:
			return {"result":apps}
		else:
			return {"result":constants.NOT_FOUND}
	else:
		return {"result":constants.ERROR_WHILE_PARSING}

def parseContent(content, query):
	tree = html.fromstring(content)
	app_id = tree.xpath('//*[@class="card-content id-track-click id-track-impression"]/@data-docid')[:10]
	image = tree.xpath('//*[@class="cover-inner-align"]/img[1]/@src')[:10]
	title = tree.xpath('//*[@class="title"]/span[1]/text()')[:10]
	price = tree.xpath('//*[@class="display-price"]/text()')[:10]
	developer = tree.xpath('//*[@class="subtitle-container"]/a[1]/text()')[:10]
	date_published = tree.xpath('//*[@class="subtitle-container"]/a[2]/text()')[:10]
	context = storeContent(app_id,title,developer,date_published,image,price,query)
	return app_id
	
def storeContent(app_id, app_name, developer_name, published, icon_url, price, query):
	count = 0
	apps = []

	for app in app_id:
		if count >= (len(app_id) or len(app_name) or len(developer_name) or len(published) or len(icon_url) or len(price)):
			# other wise it will throw list index out of range
			break

		if not app:
			#if app_id is not present then do not store this data skip it
			count+=1			
			continue

		try:
			#if app already exists then also skip the storing
			ap = Apps.objects.get(app_id=app_id[count])
			count+=1
			continue
		except Apps.DoesNotExist:
			#create the new app entry
			# throws this error 'ascii' codec can't encode characters in position 3-4: ordinal not in range(128)
			# so encoded/decoded the literals before saving
			try:
				en_dc = [app_id[count],app_name[count],developer_name[count],published[count],icon_url[count],price[count]]
				en_dc[:] = [en.encode('ascii', 'ignore').decode('ascii') for en in en_dc]

				ap = Apps.objects.create(app_id=en_dc[0],app_name=en_dc[1],
						developer_name=en_dc[2],published=en_dc[3],
						icon_url=en_dc[4],price=en_dc[5])
				count+=1
			except Exception as e:
				print "Exception occurred : %s"%str(e)
				continue

			#store an entry in SearchResultApp
			try:
				term = SearchTerm.objects.get(term=query)
				searchObj = SearchResultApp.objects.create(term=term,app=ap)
			except Exception as e:
				print "Exception occurred: %s"%str(e)

