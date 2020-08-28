from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from knowledge_graph_data_layer import views
from travelando import settings

router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'queries/', views.QueriesView.as_view(), name='queries'),
]
