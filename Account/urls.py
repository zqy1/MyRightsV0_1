from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^test/$', views.test, name='test'),
]