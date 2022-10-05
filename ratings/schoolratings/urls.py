from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = "schoolratings"
urlpatterns = [
path('',views.home),

path('<str:state>/<str:city>/grade=<str:g>/<int:pg_num>',views.school,name="home"),
path('<str:state>/<str:city>',views.state,name="home"),
path('<str:state>/<str:city>/grade=<str:g>/<str:school>',views.sch_details,name="schl_details"),
path('<str:state>/<str:city>',views.state,name="home"),

path('<str:state>/<str:city>/grade=<str:g>/<str:school>/review',views.review_page,name="review_page"),


]