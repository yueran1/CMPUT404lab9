import json
import urllib
import urllib2
from base64 import b64encode
from urlparse import urljoin
from django.shortcuts import render
from django.template import RequestContext
from consumer.forms import AuthForm
from leopard.constants import IGUANA_ADDR


def example_view(request):
    context = RequestContext(request)
    return render(request, 'consumer/index.html', context)


def no_auth_example(request):
    context_data = {}
    url = urljoin(IGUANA_ADDR, 'api/users/?format=json')
    url_request = urllib2.Request(url)
    # request.add_header('key', 'value')
    try:
        response = urllib2.urlopen(url_request)
        value = response.read()
        context_data['output'] = value
    except urllib2.HTTPError as e:
        context_data['output'] = e
    context = RequestContext(request, context_data)

    return render(request, 'consumer/no_auth.html', context)


def basic_auth_example(request):
    context_data = {'form': AuthForm()}
    if request.method == 'POST':
        url = urljoin(IGUANA_ADDR, 'api/users/?format=json')
        url_request = urllib2.Request(url)

        form = AuthForm(request.POST)
        form.is_valid()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Simple Basic Authentication
        pre_encode = username + ":" + password
        encoded_auth = b64encode(pre_encode)
        url_request.add_header('Authorization', 'Basic ' + encoded_auth)
        context_data['info'] = "Added header 'Authorization: Basic %s'" % encoded_auth
        try:
            response = urllib2.urlopen(url_request)
            value = response.read()
            context_data['output'] = value
        except urllib2.HTTPError as e:
            context_data['output'] = e
    else:
        context_data['output'] = "Use the form to request from Iguana using Basic Authentication."

    context = RequestContext(request, context_data)
    return render(request, 'consumer/basic_auth.html', context)


def token_auth_example(request):
    context_data = {'form': AuthForm()}
    if request.method == 'POST':
        url = urljoin(IGUANA_ADDR, 'api/users/?format=json')
        url_request = urllib2.Request(url)

        form = AuthForm(request.POST)
        form.is_valid()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Simple Token Authentication - Step 1, Grab the Token
        token = ""
        token_url = urljoin(IGUANA_ADDR, 'api-token-auth/')
        token_req_data = urllib.urlencode({'username': username, 'password': password})
        token_url_request = urllib2.Request(token_url, token_req_data)
        try:
            response = urllib2.urlopen(token_url_request)
            raw_value = response.read()
            token_dict = json.loads(raw_value)
            context_data['info'] = 'Grabbed token: ' + token_dict.get('token', 'N/A')
            token = token_dict.get('token', 'N/A')
        except urllib2.HTTPError as e:
            context_data['info'] = 'Failed to get token (%s)' % e

        try:
            url_request.add_header('Authorization', 'Token ' + token)
            context_data['info2'] = "Added header 'Authorization: Token %s'" % token
            response = urllib2.urlopen(url_request)
	    print('hey this is header: ', response)
            value = response.read()
            context_data['output'] = value
        except urllib2.HTTPError as e:
            context_data['output'] = e
    else:
        context_data['output'] = "Use the form to request from Iguana using Token Authentication."
    context = RequestContext(request, context_data)
    return render(request, 'consumer/token_auth.html', context)
