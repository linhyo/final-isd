from django.conf.urls import patterns, include, url
from vietskill import views
from vietskill import schedule

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),

    url(r'^teaching-day/$', views.teaching_day, name='teaching_day'),
    url(r'^online-day/$', views.online_day, name='online_day'),
    url(r'^absent-day/$', views.absent_day, name='absent_day'),
    url(r'^mistake/$', views.mistake, name='mistake'),

    url(r'^profile-all/$', views.profile_all, name='profile_all'),
    url(r'^profile-detail/(?P<pk>[0-9]+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profile/add/$', views.profile_add, name='profile_add'),
    url(r'^profile/(?P<pk>[0-9]+)/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^profile/(?P<pk>[0-9]+)/delete/$', views.profile_delete, name='profile_delete'),

    url(r'^recruit/add/$', views.recruit_add, name='recruit_add'),
    url(r'^recruit/(?P<pk>[0-9]+)/edit/$', views.recruit_edit, name='recruit_edit'),
    url(r'^recruit/(?P<pk>[0-9]+)/delete/$', views.recruit_delete, name='recruit_delete'),
    url(r'^recruit/$', views.recruit_index, name='recruit'),

    url(r'^assess/$', views.assessment, name='assess'),
    url(r'^assess/add/$', views.assess_add, name='assess_add'),
    url(r'^assess/(?P<pk>[0-9]+)/edit/$', views.assess_edit, name='assess_edit'),
    url(r'^assess/(?P<pk>[0-9]+)/delete/$', views.assess_delete, name='assess_delete'),
    # Include urls for schedule
    url(r'^schedule/', include(schedule.urls))
)
