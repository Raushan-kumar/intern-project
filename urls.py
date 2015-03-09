from django.conf.urls import patterns, include, url
from DYNAMIC.views import contact,search
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'mysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	#url(r'^hello/$', hello),
	url(r'^search_form/$',contact ),
	url(r'^search/$',search),
	#url(r'^search/$',search),
	#url(r'^raushan/$', current_datetime),
	url(r'^admin/', include(admin.site.urls)),
	
)
