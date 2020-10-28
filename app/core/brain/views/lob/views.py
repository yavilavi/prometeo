from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from core.brain.models import Lob


def lob_list(request):
    data = {
        'title': "Listado de LOB's",
        'icon': 'list',
        'lobs': Lob.objects.all()
    }
    return render(request, 'lob/list.html', data)


class LobListView(ListView):
    model = Lob
    template_name = 'lob/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {"name": "Yilmer"}
        print(request.POST)
        return JsonResponse(request.POST)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de LOB's"
        context['icon'] = 'list',
        return context
