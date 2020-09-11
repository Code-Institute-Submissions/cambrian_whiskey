from django.conf.urls import url, include
from .views import contact
# from contact import url_reset

urlpatterns = [
  url(r'^form/$', contact, name='contact'),
]