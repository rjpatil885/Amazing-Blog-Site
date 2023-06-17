from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
  
  path('', home, name = "home"),
  path('search/', search, name='search'),
  path('detailed-blog/<slug>/', detailed_blog, name='detailed-blog'),
  path('like/', like_view, name='like'),
  path('dislike/', dislike_view, name='dislike'),
  path('contact/', contact, name='contact'),
  path('category/<slug:category_slug>/', post_list_by_category, name='post_list_by_category'),
  path('update_profile/', update_profile, name = 'update_profile'),
  path('myaccount/', myaccount, name = 'myaccount'),

  path('posts/', PostListView.as_view(), name='post-list'),
  path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
  path('post-update/<slug:slug>/', PostUpdateView.as_view(), name='post-update'),
  path('create/', PostCreateView.as_view(), name='post-create'),
  path('terms_condition/', terms_condition, name='terms_condition'),
  path('category_create/', CategoryCreateView.as_view(), name='category-create'),

  path('category-update/<slug:slug>/', CategoryUpdateView.as_view(), name='category-update'),
  path('categories/', CategoryListView.as_view(), name='category-list'),
  
  path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),

  path('post/<slug:slug>/delete/', delete_post , name='post_delete'),
  path('category/<slug:slug>/delete/', delete_category , name='category_delete'),

#     path('posts/', PostListView.as_view(), name='post_list'),


]

# Serving static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
