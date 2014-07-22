"""
Blank URLConf just to keep runtests.py happy.
"""
from django.conf.urls import url
from rest_framework.compat import patterns

def nop_view(request):
    return None

urlpatterns = patterns('',
    url('bloblogpostcomment-detail/(?P<pk>\w+)/', nop_view, name='blogpostcomment-detail'),
)
