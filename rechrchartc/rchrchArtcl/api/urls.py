from django.urls import path 
from ..views import *

urlpatterns = [
    path('register',Registerview.as_view()) ,
    path('login',Loginview.as_view()),
    path('user/',UserUpdate.as_view(),name="user"),
    path('user/<str:pk>',UserUpdate.as_view(),name="user"),
    path('user/<str:pk>/delete',UserUpdate.as_view(),name="user"),
    path('mods/',ModeratorList.as_view(),name="mods"),
    path('mods/new',ModeratorUpdate.as_view(),name="modcreate"),
    path('mods/<str:pk>',ModeratorUpdate.as_view(),name="modupdate"),
    path('mods/<str:pk>/delete',ModeratorUpdate.as_view(),name="moddelete"),
   # path('articles',ArticleAdd.as_view()) , 
   # path('articles/new',ArticleAdd.as_view()) ,
    path('articles/sr/<str:query>',ArtSr.as_view()) , 
    path('articles/',ArticleViewset.as_view()) ,
    path('articles/<int:id>',ArticleViewset.as_view()),
    path('article/<str:pk>', ArticleGet.as_view()),
    path('article/favoris/<int:Userid>/<int:Artid>',ArticleFavoris.as_view()),
    path('article/favoris/<str:Username>',ArticleFavoris.as_view()), 
    path('download-from-drive/', Test, name='download_from_drive'),
    path('Test2/', Test2, name='download_from_drive'),
    path('GetALL/', get_all_articles, name='article_details'),
    path('articles_details/<str:article_id>/', get_article_details, name='article_details'),
    path('deleteArticle/<str:article_id>/', delete_article, name='article_details'),




]