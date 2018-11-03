from django.conf.urls import url
from first_app import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    url(r'^home',views.home),
    url(r'^login/',LoginView.as_view(template_name='first_app/login.html'), name="login"),
    url(r'^send_login/',LoginView.as_view(template_name='first_app/send_login.html'), name="loggedin"),
    url(r'^hm_login/',LoginView.as_view(template_name='first_app/hm_login.html'), name="HomeLogged"),
#    path('home_login/',LoginView.as_view(template_name='first_app/home_login.html'), name="loggedin"),
    url(r'^logout/',LogoutView.as_view(template_name='first_app/logout.html'), name="logout")



]
