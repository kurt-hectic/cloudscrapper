from requests import Session
import lxml
import lxml.html
from lxml.etree import tostring
import sys
import urllib.request
import os

def getImagesandTags(content):
	
	xhtml = lxml.html.fromstring(content)
	elements = xhtml.xpath("//div[@class='slideshowcontent']")

	ret = []

	for element in elements:
		image = element.xpath("div[@class='slideshowimagewrapper']//img/@src")[0]
		tags = element.xpath("div//ul[@class='cloud-filter']/li/a/text()")
		
		ret.append( { 'image' : image , 'tags' : tags  } )

	return ret


with open("filetags.csv","w") as file:	
	session = Session()

	# HEAD requests ask for *just* the headers, which is all you need to grab the
	# session cookie
	session.head('https://cloudappreciationsociety.org/gallery/')

	for offset in range(0,64*100,32):

		response = session.post(
			url='https://cloudappreciationsociety.org/wp-admin/admin-ajax.php',
			data={
				'action': 'get_slideshow',
				'cats': '',
				'offset': offset,
				'photographer': ''
			},
			headers={
				'Referer': 'https://cloudappreciationsociety.org/gallery/'
			}
		)

		if response.status_code == 200 and len(response.text) > 0 :
			print("got info on offset {}".format(offset))
			content = response.text

			info = getImagesandTags(content)
		
			for i in info:
				
				src = i["image"]
				name = os.path.basename(src)
				localname = "images/{}".format(name) 
				
				print("downloading {}".format(src))
				
				response = session.get(src)
				
				with open(localname, 'wb') as f:
					f.write(response.content)
				

				str = "{} :  {}\n".format( name , i["tags"] )
				file.write( str )
				print(str)
				
		else:
			print("exiting with offser: {}".format(offset))
			sys.exit(1)

