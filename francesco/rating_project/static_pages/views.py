from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.


def index(request):
    template = loader.get_template("static_pages/base.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def project(request):
    template = loader.get_template("static_pages/project.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template("static_pages/about.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))