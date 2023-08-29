import json

account_dict = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', "balance": 345.67}]}
with open('accounts.json', 'w') as accounts:
    json.dump(account_dict, accounts)
print(json)
with open('accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)
print(accounts_json)
print(accounts_json['accounts'])
