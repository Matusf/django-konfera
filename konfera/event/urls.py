from django.conf.urls import url

from konfera.event import views


urlpatterns = [
    url(r'^(?P<slug>[\w, -]+)/venue/$', views.event_venue_view, name='event_venue'),
    url(r'^(?P<slug>[\w, -]+)/speakers/$', views.event_speakers_list_view, name='event_speakers'),
    url(r'^(?P<slug>[\w, -]+)/sponsors/$', views.event_sponsors_list_view, name='event_sponsors'),
    url(r'^(?P<slug>[\w, -]+)/cfp/$', views.CFPView.as_view(), name='event_cfp_form'),
    url(r'^(?P<slug>[\w, -]+)/cfp/(?P<uuid>[\w, -]+)$', views.CFPEditView.as_view(), name='event_cfp_edit_form'),
    url(r'^(?P<slug>[\w, -]+)/schedule/$', views.schedule_redirect, name='schedule'),
    url(r'^(?P<slug>[\w, -]+)/schedule/(?P<day>[\d, -]+)$', views.ScheduleView.as_view(), name='schedule'),
    url(r'^(?P<slug>[\w, -]+)/tickets/$', views.event_public_tickets, name='event_tickets'),
    url(r'^(?P<slug>[\w, -]+)/$', views.event_details_view, name='event_details'),
    url(r'^order/(?P<order_uuid>[\w, -]+)/$', views.event_order_detail, name='order_details'),
    url(r'^(?P<slug>[\w, -]+)/about_us/$', views.event_about_us, name='event_about_us'),
]
