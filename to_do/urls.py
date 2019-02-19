from django.conf.urls import include, url
from django.contrib import admin
from todo.views import todoView, addTodo

urlpatterns = [
    # Examples:
    # url(r'^$', 'to_do.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/$',todoView, name="main-view"),
    url(r'^addTodo/$', addTodo, name="addTodo"),
]
