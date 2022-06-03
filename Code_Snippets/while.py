#!/usr/bin/env python3
from matplotlib.pyplot import sca


i = 0
mail = "mail@exaple.com"
while i < 10:
    i += 1
    print(f'{i} mail sended to {mail}')
else:
    print(f'All mails are sended to {mail}')

while True:
    scanning = input(f'Scanning [NETWORK]: type break to stop scanning ')
    if scanning == 'break':
        print('Thanks for using this program.')
        break
    elif scanning == 'start':
        # use pass like a placeholder, that's it 
        # thinking about how TODO
        pass

