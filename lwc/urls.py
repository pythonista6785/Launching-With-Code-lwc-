from django.conf.urls import include, url
from django.contrib import admin
from joins.views import home
urlpatterns = [
    # Examples:
    url(r'^$', 'joins.views.home', name='home'),
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
