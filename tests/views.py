from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Test


def index(request):
    test_list = Test.objects.order_by('-pub_date')
    template = loader.get_template('tests/index.html')
    context = {
        'test_list': test_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    return render(request, 'tests/detail.html', {'test': test})
