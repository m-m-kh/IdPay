# https://idpay.ir/web-service/v1.1/ ORGINAL DOCS

import requests
from typing import Optional


class IdPay:
    __CREATE_TRANSACTION_API = "https://api.idpay.ir/v1.1/payment" 
    __TRANSACTION_VERIFICATION_API = "https://api.idpay.ir/v1.1/payment/verify"
    __GET_TRANSACTION_STATUS_API = "https://api.idpay.ir/v1.1/payment/inquiry"
    __GET_ALL_TRANSACTION_API = "https://api.idpay.ir/v1.1/payment/transactions"
    
    def __init__(self, api_key:str, sandbox:bool):
        self.request = requests.session()
        self.request.headers.update({
            'Content-Type': 'application/json',
            'X-API-KEY': api_key,
            'X-SANDBOX': str(sandbox),
        })
        
    def create_transaction(self, order_id:str, amount:int,callback:str,
                           name:Optional[str]=None, phone:Optional[str]=None,
                           mail:Optional[str]=None, desc:Optional[str]=None,
                           ) -> dict:
        """
        order_id: string, required, Merchant order number. Up to 50 characters.
        amount: number, required, Desired amount in Iranian Rials. The amount must be between 1,000 Rials to 500,000,000 Rials.
        name: string, optional, Name of the payer. Up to 255 characters.
        phone: string, optional, Payer's mobile phone number. 11 characters long. For example, 9382198592 or 09382198592 or 989382198592.
        mail: string, optional, Payer's email address. Up to 255 characters.
        desc: string, optional, Transaction description. Up to 255 characters.
        callback: string, required, Merchant website return address. Up to 2048 characters.
        """
        
        data = { 
            'order_id':order_id,
            'amount':amount,
            'callback':callback,
            'name':name,
            'phone':phone,
            'mail':mail,
            'desc':desc,
        }
        
        response = self.request.post(self.__CREATE_TRANSACTION_API,
                                 json=data
                                 )
        return response.json()
        
        
    def verify_transaction(self, id:str, order_id:str) -> dict:
        data = { 
            'id':id,
            'order_id':order_id
        }
        
        response = self.request.post(self.__TRANSACTION_VERIFICATION_API,
                                 json=data
                                 )
        return response.json()
    
    def get_transaction_stauts(self, id:str, order_id:str) -> dict:
        data = { 
            'id':id,
            'order_id':order_id
        }
        
        response = self.request.post(self.__GET_TRANSACTION_STATUS_API,
                                 json=data
                                 )
        return response.json()

    def get_all_transaction(self, page:Optional[int]=0, page_size:Optional[int]=25) -> dict:
        data = { 
            'page':page,
            'page_size':page_size
        }
        
        response = self.request.post(self.__GET_TRANSACTION_STATUS_API,
                                 json=data
                                 )
        return response.json()
    
    

