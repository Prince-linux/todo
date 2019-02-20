from django.conf.urls import include, url
from django.contrib import admin
from todo.views import index, save

urlpatterns = [
    # Examples:
    # url(r'^$', 'to_do.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/$',index, name="main-view"),
    url(r'^new/$', save, name="addTodo"),

]
