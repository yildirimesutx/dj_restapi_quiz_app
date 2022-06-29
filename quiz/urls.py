from django.urls import path
from rest_framework import routers
from .views import CategoryView


router = routers.DefaultRouter()
router.register('', CategoryView)


urlpatterns = [
    # path('', include(router.urls))
    
]

urlpatterns += router.urls