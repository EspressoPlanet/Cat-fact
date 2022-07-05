'''
sms API documentation https://docs.textbelt.com/
cat facts API documentation https://catfact.ninja/
'''

import sms_api as sms
import functions as fn

def main():
    sms.sms_fun(fn.phone_number())
if __name__ == '__main__':
    main()

