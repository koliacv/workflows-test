#checker website 

import requests

response = requests.get('http://142.132.168.160/')
#print (response.status_code)
if response.status_code == 200:
    print('Success!')
else:
    print('An error has occurred.')
