# developed by @_zruss_

import json
from logger import logger
log = logger().log


class FinalGenerator:

    def __init__(self, s, config):
        self.s      = s
        self.config = config

    def FinalLogin(self, config):


        FinalEmail              = self.config['final']['email']
        FinalPassword           = self.config['final']['password']

        # setup login headers
        FinalLoginHeaders       = {
            'Accept'            : '*/*',
            'Accept-Encoding'   : 'gzip, deflate, br',
            'Accept-Language'   : 'en-US,en;q=0.8',
            'Connection'        : 'keep-alive',
            'Content-Length'    : '74',
            'content-type'      : 'application/json',
            'Host'              : 'api.getfinal.com',
            'Origin'            : 'https://dashboard.getfinal.com',
            'Referer'           : 'https://dashboard.getfinal.com/login',
            'User-Agent'        : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        # setup login data
        FinalLoginData          = {"email":FinalEmail,"password":FinalPassword,"token_type":"web"}
        FinalLoginPayload       = json.dumps(FinalLoginData)
        log ("Brother we are logging into Final", "lightpurple")
        Login_Response          = self.s.post('https://api.getfinal.com/api/auth/sign_in', headers=FinalLoginHeaders, data=FinalLoginPayload)

        #retrieve tokens
        access_token            = Login_Response.headers['access-token']
        client                  = Login_Response.headers['client']
        uid                     = Login_Response.headers['uid']
        log ("Brother we got the user tokens", "success")

        # return all info associated with account
        FinalAccountData        = {
            'access_token'      : access_token,
            'client'            : client,
            'uid'               : uid
        }
        return FinalAccountData
    def CreateFinalCard(self, FinalAccountData, x):

        # setup card generator headers
        CardCreationHeaders     = {
            'Accept'            : '*/*',
            'Accept-Encoding'   : 'gzip,deflate,br',
            'Accept-Language'   : 'en-US,en;q=0.8',
            'access-token'      : FinalAccountData['access_token'],
            'client'            : FinalAccountData['client'],
            'Connection'        : 'keep-alive',
            'Content-Length'    : '20',
            'content-type'      : 'application/json',
            'Host'              : 'api.getfinal.com',
            'Referer'           : 'https://dashboard.getfinal.com/cards/generate',
            'uid'               : FinalAccountData['uid'],
            'User-Agent'        : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        self.s.headers.update(CardCreationHeaders)


        CardCreationData        = {
            'single_use'        : 'false'
        }
        CardCreationPayload     = json.dumps(CardCreationData)
        log ("Creating new final card", "lightpurple")
        Create_Card             = self.s.post('https://api.getfinal.com/api/cards', headers=CardCreationHeaders, data=CardCreationPayload)
        dict                    = json.loads(Create_Card.text.encode("UTF-8"))
        Card_Number             = dict['card_number']
        Expiry_Month            = dict['expiry_month']
        Expiry_Year             = dict['expiry_year']
        CVC                     = dict['cvc']
        # this was the dumbest way to get that info but idc
        log ("Card created successfully", "success")

        # logs card info to txt file
        with open('FinalCards' + '.txt', 'a') as f:
            f.write('' + Card_Number + ':' + CVC + ':' + Expiry_Month + '/' + Expiry_Year + '\n')
            f.close()