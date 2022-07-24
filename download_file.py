import requests
from requests import Response
import os.path

r: Response = requests.get('https://habrastorage.org/r/w1560/getpro/habr/post_images'
                           '/40e/c7f/b4f/40ec7fb4f579c099e14f300685f2222c.png')

f = open('postman.png', 'wb')
f.write(r.content)
f.close()

print(os.path.getsize('postman.png'))
