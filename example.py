from pyremote import connection

my_user_id = <user_id> #get your user_id from https://t.me/PyRemoteBot  #noqa 
remote = connection(my_user_id)

number = 0
for _ in range(10000):
    number += 1

remote.send(f'Calculation finished! Final number is: {number}')