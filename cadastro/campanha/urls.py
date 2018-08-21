from django.urls import path
from . import views

urlpatterns = [
    path('', views.initial_page, name='initial_page'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('eleitor/', views.eleitor_list, name='eleitor_list'),
    path('eleitor/new', views.eleitor_new, name='eleitor_new'),
]
