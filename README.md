# PyRemote
Send yourself notifications from your python code to your Telegram account
go to https://t.me/PyRemoteBot to het or change your unique 'user_id'

## Example:
Send yourself a notification when your code finished running:
```
from pyremote import connection

my_user_id = <user_id> #get your user_id from https://t.me/PyRemoteBot  #noqa 
remote = connection(my_user_id) #connection your code to server
### Your main code:
number = 0
for _ in range(10000):
    number += 1
###
remote.send(f'Calculation finished! Final number is: {number}') # Send notification to your Telegram account
```
