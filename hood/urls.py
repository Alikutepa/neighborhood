from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='Index'),
    url(r'^notifications',views.notification, name='notifications'),
    url(r'^health',views.health, name='health'),
    url(r'^authorities',views.authorities, name='authorities'),
    url(r'^businesses',views.businesses, name='businesses'),
    url(r'^my-profile/',views.my_profile, name='my-profile'),
    url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    url(r'^new/business$',views.new_business, name='new-business'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^new/notification$',views.new_notification, name='new-notification'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
    url('search/', views.search_business, name='searchbusiness'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)