from django.conf.urls import url
from . import views


urlpatterns = [
    #/books/
    url(r'^$', views.index, name = 'index'),
    #/books/71/
    url(r'^(?P<author_id>[0-9]+)/$',views.detail, name='detail')
]
