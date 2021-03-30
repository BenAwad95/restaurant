from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import RateForm
from django.shortcuts import get_object_or_404
#* import the models

from .models import Restaurant
class RestaurentList(ListView):
    queryset = Restaurant.objects.all().select_related('location').prefetch_related('rate_set')

# class RestaurantDetail(DetailView):
#     model = Restaurant
    
#     def get_object(self, queryset=None):
#         return Restaurant.objects.get(name=self.kwargs.get('name'))

def restaurantDetail(request, name):
    rest_obj = Restaurant.objects.prefetch_related('rate_set').get(name=name)
    form = RateForm(request.POST or None ,auto_id=False)
    if form.is_valid():
        rate_obj = form.save(commit=False)
        rate_obj.restaurant = rest_obj
        rate_obj.save()
        form = RateForm()
        rest_obj.refresh_from_db()
    context = {
        'restaurant': rest_obj,
        'form': form
    }
    
    return render(request, 'restaurant_rating/restaurant_detail.html', context=context)
    