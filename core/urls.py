from django.urls import include, path

from rest_framework.routers import SimpleRouter
from core.views import *


router = SimpleRouter()
router.register(r'data', PostViewSet, basename='data')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', DataSetView.as_view()),
    # path('qwer/', index)
]
