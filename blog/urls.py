from django.conf.urls import url 
from.views import post_list,post_new,post_detail,edit_post,post_delete

urlpatterns = [
    
    url(r'^$', post_list,name='post_list'),
    url(r'^new-post$', post_new, name= 'post_new'),
    url(r'^post-details/(?P<pk>\d+)/$', post_detail, name= 'post_detail'),
    url(r'^edit-post/(?P<pk>\d+)/$', edit_post, name= 'edit_post'),
    url(r'^delete_post(?P<pk>\d+)/$', post_delete, name= 'post_delete'),
]
