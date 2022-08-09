from unicodedata import name
from django.urls import path 

from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView, CommentCreateView



urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),     #newyy
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),   #newyy
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),  #newyy
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/addcomment/', CommentCreateView.as_view(), name='comment_new'),    #newyy
]