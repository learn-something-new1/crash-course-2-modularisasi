import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success Response= {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'Woops ada kesalahan {response.status_code}')
#    print(f'Success', response)
except Exception as e:
    print(f'There is a error{e}')
 #   print('There is a error', e)
print('Program ended')

import requests

url = 'https://det ik.com'
try:
    requests.get(url)
    print('\nSuccess!')
except Exception as e:
    print('\nThere is an error', e)
print('Program Ended')