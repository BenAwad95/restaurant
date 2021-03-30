from django.urls import path
from .views import RestaurentList, restaurantDetail

app_name = 'restaurant_rating'
urlpatterns = [
    path('', RestaurentList.as_view(), name='restaurant_list'),
    #! here the error was because the pattern of url was like the admin url
    path('restaurant/<str:name>/', restaurantDetail, name='restaurant_detail')
]
