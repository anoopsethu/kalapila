# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.template.context import RequestContext
from django.template.loader import get_template
from django.templatetags.static import static

def index(request):
    return render(request, 'index.html', {})

def new_creative(request):
    return render(request, 'new_creative.html', {})