from django.urls import path
from rest_framework import routers
from .views import CategoryView, QuizView


# router = routers.DefaultRouter()
# router.register('', CategoryView)


urlpatterns = [
    # path('', include(router.urls))
    path('quiz/', CategoryView.as_view()),
    # path('^quiz/(<category>.+)/$', QuizView.as_view()),
    path('quiz/<str:category>', QuizView.as_view()),
    # path('category/', QuizView.as_view()),
]

# urlpatterns += router.urls