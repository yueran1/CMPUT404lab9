from django.shortcuts import render
from django.template import RequestContext


def example_view(request):
    context = RequestContext(request)
    return render(request, 'client/index.html', context)
