from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new-wkkb/$', views.new_creative, name='new_creative'),
]