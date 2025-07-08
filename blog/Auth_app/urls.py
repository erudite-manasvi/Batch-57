from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view),
    path('signup/',views.signup),
    path('get-data/',views.get_data),
    path('get-data-by-id/<str:email>/',views.get_data_by_id)
]
