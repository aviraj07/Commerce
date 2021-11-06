from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("content/<str:id>", views.content, name="content"),
    path("watchlist_add/<int:id>",views.watchlist_add, name="watchlist_add"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("close_listing/<int:id>",views.close_listing, name="close_listing"),
    path("add_comment/<int:id>",views.add_comment, name="add_comment"),
    path("categories/<str:category>",views.categories, name="categories"),
    path("Categories", views.Categories, name="Categories"),
]
