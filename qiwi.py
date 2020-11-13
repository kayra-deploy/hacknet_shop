import requests
login = '79125946990'
token = '4d6d411bbc2ef32553be668ac1494f9e'

def last_pay(my_login, token, rows_num, next_TxnId, next_TxnDate):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + token  
    parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params = parameters)
    return h.json()

def get_last_pay():
    a = last_pay(login, token, '1', '', '')
    return a['data'][0]['status'], a['data'][0]['sum']['amount'], a['data'][0]['comment']


