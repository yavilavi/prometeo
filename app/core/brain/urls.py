from django.urls import path
from core.brain.views.lob.views import *

app_name = 'brain'

urlpatterns = [
    path('lob/list', LobListView.as_view(), name='lob_list'),
]
