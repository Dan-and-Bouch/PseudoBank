# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
# oauth flow in simple words: http://pyoauth.readthedocs.org/en/latest/guides/oauth1.html
base_url = "https://ulsterbank.openbankproject.com"
request_token_url = base_url + "/oauth/initiate"
authorization_base_url = base_url + "/oauth/authorize"
access_token_url = base_url + "/oauth/token"


def auth():
    client_key = "1m240zcafgnyh4r51bvd03gim13lyhu4gdxeglaw"
    client_secret = "nsobu4ao3hjvlaqoojizhd1zvu1yjdpmpyspuv1m"

    bank = OAuth1Session(client_key, client_secret=client_secret, callback_uri='http://127.0.0.1/cb')

    bank.fetch_request_token(request_token_url)

    authorization_url = bank.authorization_url(authorization_base_url)
    print 'Please go here and authorize, '
    print authorization_url

    redirect_response = raw_input('Paste the full redirect URL here:')
    bank.parse_authorization_response(redirect_response)

    bank.fetch_access_token(access_token_url)
    return bank


def transact(amount):
    # get accounts for a specific bank
    our_bank = 'ulster-ni'
    # print "Available accounts"
    r = openbank.get(u"{}/obp/v1.2.1/banks/{}/accounts/private".format(base_url, our_bank))

    accounts = r.json()['accounts']
    # for a in accounts:
    #    print a['id']

    # just picking first account
    our_account = accounts[0]['id']

    # print "Get owner transactions"
    # r = openbank.get(u"{}/obp/v1.2.1/banks/ulster-ni/accounts/{}/owner/transactions".format(base_url,
    #    our_account), headers= {'obp_limit': '25'})
    # transactions = r.json()['transactions']
    # print transactions[0]
    # transaction = transactions[0]
    # print transaction[u'details'][u'new_balance']
    # print "Got {} transactions".format(len(transactions))

    # print "Transfer some money"
    send_to = {"bank": "ulster-ni", "account": "current13"}  # owned by customer id 1458
    payload = '{"account_id": "' + send_to['account'] + '", "bank_id": "' \
              + send_to['bank'] + '", "amount": "' + amount + '" }'
    headers = {'content-type': 'application/json'}
    r = openbank.post(u"{}/obp/v1.2.1/banks/{}/accounts/{}/owner/transactions".format(base_url,
                                                                                      our_bank, our_account),
                      data=payload, headers=headers)
    # print r
    dictthing = r.json()
    # print dictthing
    return dictthing[u'transaction_id']


def get_balance():
    # get accounts for a specific bank
    our_bank = 'ulster-ni'
    # print "Available accounts"
    r = openbank.get(u"{}/obp/v1.2.1/banks/{}/accounts/private".format(base_url, our_bank))

    accounts = r.json()['accounts']
    # for a in accounts:
    #    print a['id']

    # just picking first account
    our_account = accounts[0]['id']
    r = openbank.get(u"{}/obp/v1.2.1/banks/ulster-ni/accounts/{}/owner/transactions".format(base_url,
                                                                                            our_account),
                     headers={'obp_limit': '25'})
    transactions = r.json()['transactions']
    # print transactions[0]
    transaction = transactions[0]
    return transaction[u'metadata'][u'where']#[u'amount']


openbank = auth()

print get_balance()

transact("1")

print get_balance()
# {u'metadata': {u'images': [], u'tags': [], u'where': None, u'comments': [], u'narrative': None}, u'other_account':
#  {u'kind': u'CURRENT', u'number': u'3105304', u'swift_bic': None, u'IBAN': None, u'holder':
#  {u'name': u'', u'is_alias': False},
#  u'id': u'ec2b0bac-8a9f-41e4-bf67-ed94d562c821', u'bank':
#  {u'national_identifier': None, u'name': u'Ulster Bank - Northern Ireland'}, u'metadata':
#  {u'open_corporates_URL': None, u'URL': None, u'corporate_location':
#  None, u'image_URL': None, u'private_alias': None, u'physical_location': None, u'public_alias':
#  u'ALIAS_362757', u'more_info': None}}, u'this_account': {u'kind': u'CURRENT', u'number':
#  u'10297013', u'swift_bic': None, u'IBAN': None, u'holders': [{u'name': u'CHRISTOPHER QUINN',
#  u'is_alias': False}], u'id': u'charity1', u'bank': {u'national_identifier': None, u'name':
#  u'Ulster Bank - Northern Ireland'}}, u'id': u'db6557aa-8eec-42e3-8eab-265b15d00777', u'details':
#  {u'description': None, u'completed': u'2015-02-15T12:03:16Z', u'value': {u'currency':
#  u'GBP', u'amount': u'-6969.00'}, u'new_balance': {u'currency': u'GBP', u'amount': u'-16210.28'},
#  u'type': u'sandbox-payment', u'posted': u'2015-02-15T12:03:16Z'}}
