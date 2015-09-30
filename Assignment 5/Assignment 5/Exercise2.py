import re
stat = ['weak', 'alright', 'good', 'perfect', 'the best password in the world']
while True:
    user_password = raw_input('Your password: ')
    strength = 0
    if len(user_password) > 9 and len(user_password) < 19:
        break
    else:
        print('Please choose a password between 9-19 characters.')
if sum(1 for c in user_password if c.isupper()):
    strength = strength + 1
if sum(1 for c in user_password if c.islower()):
    strength = strength + 1
if sum(1 for c in user_password if c.isalnum()):
    strength = strength + 1
if re.search('[~!@#$%^&*()_+{}":;\']', user_password):
    strength = strength + 1
print('Your password is '+stat[strength])