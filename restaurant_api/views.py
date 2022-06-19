from django.http import JsonResponse
from .models import Restaurant
from .serializers import RestaurantSerializer

def restaurant_list(request):
    """
    List all restaurants.
    """
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return JsonResponse({'restaurants': serializer.data}, safe=False)