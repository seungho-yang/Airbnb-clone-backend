from django.urls import URLPattern, path
from . import views

urlpatterns = [
    #path('', views.categories),
    path('', views.categories.as_view()),
    path('<int:pk>', views.CategoryDetail.as_view()),

]