from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import display, query, route

float_pattern = '-?[1-9][0-9]*\.?[0-9]*'
int_pattern = '[1-9][0-9]*'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cmumaps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^display/' + ('(' + float_pattern + ')/') * 4 + '(\S*)/$', display),
    url(r'^query/' + '(' + int_pattern + ')/$', query),
    url(r'^route/' + ('(' + int_pattern + ')/') * 3 + '$', route)
)
