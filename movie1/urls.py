from django.conf.urls import url
from . import views
app_name = 'movie1'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$',views.detail,name='detail'),
    #/movie1/<a.id>/favourite/
    url(r'^(?P<movie_id>[0-9]+)/favourite/$',views.favourite,name='favourite'),
    #url('db',views.index1,name=''),
    #Authentication creativity
    #url('login/',views.user_login,name="user_login"),
    #url('success/',views.success,name="user_success"),
    #url('logout/',views.user_logout,name="user_logout"),

]
