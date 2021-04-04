from pyremote import connection

my_user_id = <user_id> #get your user_id from https://t.me/PyRemoteBot  #noqa 
remote = connection(my_user_id) #connection your code to server
# Your main code:
number = 0
for _ in range(10000):
    number += 1
# Send notification to your Telegram account
remote.send(f'Calculation finished! Final number is: {number}')
