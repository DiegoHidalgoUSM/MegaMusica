from django.urls import path, include
from rest_framework import routers
from Core import views

router=routers.DefaultRouter()
router.register(r'discos',views.DiscoViewSet)

urlpatterns=[
    path('',include(router.urls))
]