from django.conf.urls import include, url
from django.contrib import admin
from todo.views import index, save, lists, mark_as_done, mark_as_undone, delete, delete_all, create_todo, create_new, edit, update

urlpatterns = [
    # Examples:
    # url(r'^$', 'to_do.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/$', index, name="main-view"),
    url(r'^new/$', save, name="addTodo"),
    url(r'^list/$', lists, name = "list_todo"),
    url(r'^mark/(?P<item_id>\d+)/done/$', mark_as_done),
    url(r'^mark/(?P<item_id>\d+)/undone/$', mark_as_undone),
    url(r'^delete/(?P<item_id>\d+)/$', delete),
    url(r'^delete_all/$', delete_all),
    url(r'^create/$', create_todo),
    url(r'^create_new/$', create_new),
    url(r'^edit/(?P<item_id>\d+)/$', edit),
    url(r'^update/(?P<item_id>\d+)/$', update)

]
