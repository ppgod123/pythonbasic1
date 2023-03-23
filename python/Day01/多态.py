# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/21 0021 下午 3:29
@Author  : fengaijun
@File    : 多态.py

'''
class Pay():
    def topay(self):
        print("进行支付！！！")
    def tocredit(self):
        print("进行收款！！！")
class AliPay(Pay):
    def topay(self):
        print("进行支付宝支付！！！")
    def tocredit(self):
        print("进行支付宝收款！！！")
class WechatPay(Pay):
    def topay(self):
        print("进行微信支付！！！")
    def tocredit(self):
        print("进行微信收款！！！")
class UnionPay(Pay):
    # def topay(self):
    #     print("进行银联支付！！！")
    # def tocredit(self):
    #     print("进行银联收款！！！")
    pass
def Initiate_payment(object):
    object.topay()
    object.tocredit()
alipay = AliPay()
wechat = WechatPay()
unionpay = UnionPay()
Initiate_payment(alipay)
Initiate_payment(wechat)
Initiate_payment(unionpay)