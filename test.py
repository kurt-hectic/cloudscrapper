from requests import Session

	
session = Session()

# HEAD requests ask for *just* the headers, which is all you need to grab the
# session cookie
session.head('https://cloudappreciationsociety.org/gallery/')


response = session.post(
    url='https://cloudappreciationsociety.org/wp-admin/admin-ajax.php',
    data={
        'action': 'get_slideshow',
        'cats': '',
        'offset': 64,
        'photographer': ''
    },
    headers={
        'Referer': 'https://cloudappreciationsociety.org/gallery/'
    }
)

print(response)
print("status code {} : len: {}".format(response.status_code,len(response.text)))

#print(response.text)