from django.urls import path 
from .views import CommentViewSet, ProductViewSet,CommentSerializer

urlpatterns = [
    path('prd/',ProductViewSet.as_view())
]
