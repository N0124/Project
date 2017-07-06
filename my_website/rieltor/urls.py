from django.conf.urls import url
from . import views


urlpatterns = [
    #/rieltor/
    url(r'^$', views.all_flats, name = 'all_flats'),
    #/rieltor/71/
    url(r'^(?P<flat_id>[0-9]+)/$',views.detail, name='detail'),
    #/rieltor/add_new/
    url(r'^add_new/$', views.add_new, name='add_new')


]