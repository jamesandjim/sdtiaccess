from django.conf.urls import url
from wechat import views
from .views import AuthView, GetInfoView, WechatPay

urlpatterns = [
    # 首页
    url(r'^$', views.home, name='home'),

    # 微信后台认证
    url(r'^index$', views.index, name='index'),

    # 支付下单及请求
    url(r'^wechatPay$', WechatPay.as_view(), name='wechatpay'),

    # 授权请求
    url(r'^auth$', AuthView.as_view(), name='auth'),

    # 之前的授权回调页面
    url(r'^getuserinfo$', GetInfoView.as_view(), name='getuserinfo'),

    # 调起支付后返回结果的回调页面
    url(r'^success$', views.success, name='success'),

]