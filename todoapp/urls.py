from todoapp import views
from django.conf.urls import url,include
# from django.contrib.auth import *

from django.contrib.auth.views import login, logout

from django.contrib.auth.views import LoginView,LogoutView
app_name='todoapp'
urlpatterns=[
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^register/$',views.register),
url(r'^home/$',views.homeview),
    url(r'^viewlists/$',views.TodoList.as_view()),
url(r'^viewlists/create/$',views.list_create),
    url(r'^viewlists/(?P<pk>\d+)/$',views.TodoListItems_all.as_view()),
    url(r'^viewlists/(?P<pk>\d+)/(?P<itemid>\d+)/$', views.TodoListItems_single.as_view()),
# url(r'^login/$',login, {'template_name': 'registration/login.html'}, name='login'),
   # url(r'^sample/$',views.sample),
   #  url(r'^viewlists/(?P<listid>\d+)/$',views.viewitemsbyid,name="viewitemsbyid"),
]

# from django.conf.urls import url
# from django.views.generic import TemplateView
#
# urlpatterns = [
#     url(r'^about/$', TemplateView.as_view(template_name="about.html")),
# ]