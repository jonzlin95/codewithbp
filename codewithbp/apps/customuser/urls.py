from django.conf.urls import patterns, include, url
from codewithbp.apps.customuser.views import LoginView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codewithbp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$' LoginView.as_view(), name='login'),
)
