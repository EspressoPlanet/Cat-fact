#Get key at https://textbelt.com/
#get 1 free text with key 'textbelt'

import requests
import cat_fact_api as cat
import functions as fn
# resp = requests.post('https://textbelt.com/text', {'phone': fn.phone_number(),
#                                                    'message': cat.main_text,
#                                                    'key': 'catastrophe',})

def sms_fun(num):
    resp = requests.post('https://textbelt.com/text', {'phone': num,
                                                       'message': cat.main_text,
                                                       'key': 'insertkeyhere',})
    return resp.json()
