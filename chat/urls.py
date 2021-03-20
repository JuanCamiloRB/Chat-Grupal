from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.views import logout
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('logout/', logout, {'next_page': 'index'}, name='logout'),
    path('register/', views.register_view, name='register'),
    path("eliminar/<int:messages_id>/", views.eliminar, name="eliminar"),

]


