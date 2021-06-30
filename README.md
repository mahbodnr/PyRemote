# PyRemote
Send yourself notifications from your python code to your Telegram account. go to https://t.me/PyRemoteBot to get or change your unique `user_id`

## Example:
#### Send yourself a notification when your code finished running:
```
from pyremote import connection
my_user_id = <user_id> #get your user_id from https://t.me/PyRemoteBot
remote = connection(my_user_id) #connection your code to server
```
Your main code:
```
number = 0
for _ in range(10000):
    number += 1
```
 Send notification to your Telegram account:
```
remote.send(f'Calculation finished! Final number is: {number}')
```
