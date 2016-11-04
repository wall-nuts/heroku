from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from first import views as first_views #new

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', first_views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/now/',first_views.now,name='now'),
    url(r'^time/plus/(\d{1,2})/$',first_views.hours_ahead),
]
