from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
    ItemCreateView,
    ItemDeleteView,
)

app_name = 'items'


urlpatterns = [
    path('<uuid:pk>/update/', ItemUpdateView.as_view(), name='update'),
    path('<uuid:pk>/delete/', ItemDeleteView.as_view(), name='delete'),
    path('<uuid:pk>/', ItemDetailView.as_view(), name='detail'),
    path('new/', ItemCreateView.as_view(), name='create'),
    path('', ItemListView.as_view(), name='list'),
]