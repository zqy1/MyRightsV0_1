from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Account/', include('Account.urls')),
    url(r'^Rights/', include('Rights.urls')),
]
