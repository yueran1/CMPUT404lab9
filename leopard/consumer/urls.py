from django.conf.urls import url
from consumer.views import example_view, no_auth_example, basic_auth_example, token_auth_example

urlpatterns = [
    url(r'^no_auth$', no_auth_example, name='no_auth'),
    url(r'^basic_auth$', basic_auth_example, name='basic_auth'),
    url(r'^token_auth$', token_auth_example, name='token_auth'),
    url(r'^$', example_view, name='index'),
]