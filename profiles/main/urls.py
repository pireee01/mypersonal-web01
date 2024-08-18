from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Microblogging URLs
    path('microblog/', views.microblog_list, name='microblog_list'),
    path('microblog/new/', views.microblog_new, name='microblog_new'),
    path('microblog/<int:pk>/', views.microblog_detail, name='microblog_detail'),
    path('microblog/<int:pk>/edit/', views.microblog_edit, name='microblog_edit'),
    path('microblog/<int:pk>/delete/', views.microblog_delete, name='microblog_delete'),

    # Certificates URLs
    path('certificates/', views.certificates, name='certificates'),
    path('certificates/<int:pk>/', views.certificate_detail, name='certificate_detail'),
    path('certificates/new/', views.certificate_new, name='certificate_new'),
    path('certificates/<int:pk>/edit/', views.certificate_edit, name='certificate_edit'),
    path('certificates/<int:pk>/delete/', views.certificate_delete, name='certificate_delete'),

    # Portfolio URL
    path('portfolio/', views.portfolio, name='portfolio'),

    # Chatbot URL
    path('chatbot/', views.chatbot, name='chatbot'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
