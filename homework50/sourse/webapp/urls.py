from django.urls import path
from .views import simulator,cat_stats

urlpatterns = [
    path('', simulator),
    path('cat_stats/', cat_stats),

]
