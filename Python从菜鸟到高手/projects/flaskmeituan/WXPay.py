'''
--------《Python从菜鸟到高手》源代码------------

欧瑞科技版权所有
作者：李宁
如有任何技术问题，请加QQ技术讨论群：264268059    
或关注“极客起源”订阅号或“欧瑞科技”服务号或扫码关注订阅号和服务号，二维码在源代码根目录
如果QQ群已满，请访问https://geekori.com，在右侧查看最新的QQ群，同时可以扫码关注公众号

“欧瑞学院”是欧瑞科技旗下在线IT教育学院，包含大量IT前沿视频课程，
请访问http://geekori.com/edu或关注前面提到的订阅号和服务号，进入移动版的欧瑞学院

“极客题库”是欧瑞科技旗下在线题库，请扫描源代码根目录中的小程序码安装“极客题库”小程序

关于更多信息，请访问下面的页面
https://geekori.com/help/videocourse/readme.html



'''
# 封装了Native支付API
from common import *
from urllib3 import *
import hashlib
import random
import string
import xmltodict

class WXPay:
    def __init__(self,data):
        self.data = data

    # https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=4_3
    def createOrder(self):
        disable_warnings()
        http = PoolManager()
        data = self.data
        # stringA="appid=wxd9830ex5d5a258f4f&body=test&device_info=1000&mch_id=10000100&nonce_str=ibuaiVcKdpRxkhJA";
        # [(key,value),(key,value)...]
        # 第1步：排序
        stringA = sorted(data.items(),key=lambda key:key[0])
        print(stringA)
        apiKey = 'Orisfldfjl24323uljlsjdfljfsljsldkjl4332' # 微信商户平台API秘钥
        i = 0
        keyValue1 = ''
        
        while i < len(stringA):
            key = stringA[i][0]
            value = stringA[i][1]
            # appid = dlsjflsr343
            keyValue = "%s = %s" %(key,value)
            if i == 0:
                keyValue1 = keyValue
            else:
                keyValue1 = "%s&%s" % (keyValue1,keyValue)
            i+=1
            # 第2步：生成StringA
            stringA = keyValue1
            
            # 第3步：拼接API秘钥
            
            # stringSignTemp=stringA+"&key=192006250b4c09247ec02edce69f6a2d" /
            stringSignTemp = "%s&key=%s" % (stringA,apiKey)
            # sign=MD5(stringSignTemp).toUpperCase()="9A0A8659F005D6984697E2CA0A9CF3B7" 
            sign = hashlib.md5(stringSignTemp.encode(encoding='utf_8')).hexdigest().upper()

        ss = '''
        <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <root>
          <body>%s</body>
          <out_trade_no>%s</out_trade_no>
          <total_fee>%d</total_fee>
          <spbill_create_ip>%s</spbill_create_ip>
          <notify_url>%s</notify_url>
          <trade_type>%s</trade_type>
          <product_id>%s</product_id>
          <nonce_str>%s</nonce_str>
          <appid>%s</appid>
          <mch_id>%s</mch_id>
          <sign>%s</sign>
        </root>
        ''' %(data['body'],data['out_trade_no'],data['total_fee'],data['spbill_create_ip'],data['notify_url'],data['trade_type'],data['product_id'],data['nonce_str'],data['appid'],data['mch_id'],sign)             
        
        # 微信支付的服务端并没有使用utf8，Latin-1 
        # 必须要做，否则body无法显示中文
        ss = ss.encode(encode='utf_8').decode('Latin-1')
        response = http.request('POST','https://api.mch.weixin.qq.com/pay/unifiedorder',body=ss)
        xml = response.data
        dict = xmltodict.parse(xml)
        return dict['xml']
    def queryOrder(self):
        disable_warnings()
        http = PoolManager()
        data = self.data
        stringA = sorted(data.items(),key=lambda key:key[0])
        apiKey = 'Orisfldfj4sl24323uljlsjdfljfsljsldkjl4332' # 微信商户平台API秘钥
        i = 0
        keyValue1 = ''
        
        while i < len(stringA):
            key = stringA[i][0]
            value = stringA[i][1]
            # appid = dlsjflsr343
            keyValue = "%s = %s" %(key,value)
            if i == 0:
                keyValue1 = keyValue
            else:
                keyValue1 = "%s&%s" % (keyValue1,keyValue)
            i+=1
            # 第2步：生成StringA
            stringA = keyValue1
            
            # 第3步：拼接API秘钥
            
            # stringSignTemp=stringA+"&key=192006250b4c09247ec02edce69f6a2d" /
            stringSignTemp = "%s&key=%s" % (stringA,apiKey)
            # sign=MD5(stringSignTemp).toUpperCase()="9A0A8659F005D6984697E2CA0A9CF3B7" 
            sign = hashlib.md5(stringSignTemp.encode(encoding='utf_8')).hexdigest().upper()

        ss = '''
        <xml>
        <root>
          <appid>%s</appid>
          <mch_id>%s</mch_id>
          <body>%s</body>
          <out_trade_no>%s</out_trade_no>
          <nonce_str>%s</nonce_str>
          <sign>%s</sign>
        </root>
        ''' %(data['appid'],data['mch_id'],data['body'],data['out_trade_no'],sign)             
        s = ss.encode(encode='utf_8').decode('Latin-1')
        
        response = http.request('POST','https://api.mch.weixin.qq.com/pay/orderquery',body=ss)
        xml = response.data
        dict = xmltodict.parse(xml)
        return dict['xml']
