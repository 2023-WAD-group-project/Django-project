from django.urls import path
from studdit import views
from studdit.views import LikePostView

from studdit.API import get_courses


urlpatterns = [
    path("home", views.home, name="home"),

    path('course/<slug:course_name_slug>/', views.show_course, name='show_course'),

    #path("post/<slug:slug>", views.post, name="post"), // complete later

    path("post", views.post, name="post"),

    #path("add_post", views.add_post, name="add_post"), // need to add Post form to complete

    path("login", views.login, name="login"),

    path("profile", views.profile, name="profile"),

    path('course/<slug:course_name_slug>/add_post/', views.add_post, name='add_post'),

    path('like_post/', views.LikePostView.as_view(), name='like_post'),

    path("test", views.test, name="test"),

    path("get_courses", get_courses, name="API_get_courses")

]
