from django.urls import path

from foods.views import AboutView, BookView, IndexView, MenuView

urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("book/", BookView.as_view(), name="book"),
    path("index/", IndexView.as_view(), name="index"),
    path("menu", MenuView.as_view(), name="menu"),
]