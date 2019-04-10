from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.backends import ModelBackend
# from django.core import serializers
import json
import requests
import base64
import random
import time
from datetime import datetime, date
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, redirect


import django.utils.timezone as timezone
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, redirect

from wechat.wechatAPI import WechatLogin
from .models import Xf_list, Dev_token
from .wechatAPI import WechatLogin, WechatTemplates, WechatOrder, WechatPayAPI

def home(request):
    return HttpResponse('这是首页')

class WechatViewSet(View):
    wechat_api = WechatLogin()


class AuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url()
        return redirect(url)


class GetInfoView(WechatViewSet):
    def get(self, request):
        if 'code' in request.GET:
            code = request.GET['code']
            token, openid = self.wechat_api.get_access_token(code)
            if token is None or openid is None:
                return HttpResponseServerError('get code error')
            user_info, error = self.wechat_api.get_user_info(token, openid)
            if error:
                return HttpResponseServerError('get access_token error')
            user_data = json.loads(user_info)
            # user_data = {
            #     'nickname': user_info['nickname'],
            #     'sex': user_info['sex'],
            #     'province': user_info['province'].encode('iso8859-1').decode('utf-8'),
            #     'city': user_info['city'].encode('iso8859-1').decode('utf-8'),
            #     'country': user_info['country'].encode('iso8859-1').decode('utf-8'),
            #     'headimgurl': user_info['headimgurl'],
            #     'openid': user_info['openid']
            # }
            nickname = user_data.get('nickname', '')
            sex = user_data.get('sex', 0)
            openid = user_data.get('openid', '')
            province = user_data['province']
            city = user_data.get('city', '')
            country =  user_data.get('country', '')
            headimgurl = user_data.get('headimgurl', '')

            user = Xf_list.objects.filter(openid=user_data['openid'])
            if user.count() == 0:
                user = Xf_list.objects.create(nickname=nickname,
                                                  sex=sex,
                                                  openid=openid,
                                                  province=province,
                                                  city=city,
                                                  country=country,
                                                  headimgurl=headimgurl,

                                              )


            return render(request, 'user_info.html',
                          {
                              'openid':openid,
                              'nickname': nickname,
                              'sex': sex,
                              'province': province,
                              'country': country,
                              'city': city,
                              'headimgurl': headimgurl,
                              'begin_time': timezone.now,
                          },
                          )



class WechatPay(View):
    @staticmethod
    def post(request):
        # 这个if判断是我传入的订单的id，测试的时候没有传入，你可以测试的时候去掉这个判断
        if 'order' in request.POST:
            # order = request.POST['order']
            # order = Order.objects.filter(is_effective=True).filter(uuid=order).first()
            body = 'JSP支付测试'
            trade_type = 'JSAPI'
            import random
            rand = random.randint(0, 100)
            out_trade_no = 'HSTY3JMKFHGA325' + str(rand)
            total_fee = 1
            spbill_create_ip = '127.0.0.1'
            notify_url = 'http://www.show.netcome.net/success'
            order = WechatOrder(body=body,
                                trade_type=trade_type,
                                out_trade_no=out_trade_no,
                                openid=request.session['openid'],
                                total_fee=total_fee,
                                spbill_create_ip=spbill_create_ip,
                                notify_url=notify_url)
            datas, error = order.order_post()
            if error:
                return HttpResponseServerError('get access_token error')
            order_data = datas['prepay_id'].encode('iso8859-1').decode('utf-8'),
            pay = WechatPayAPI(package=order_data[0])
            dic = pay.get_dic()
            dic["package"] = "prepay_id=" + order_data[0]
            return HttpResponse(json.dumps(dic), content_type="application/json")


def success(request):
    # 这里写支付结果的操作，重定向
    return redirect('/')