from django.urls import path
from . import views
from .views import (
    AlgorithmListView,
    # AlgorithmDetailView,
    AlgorithmCreateView,
    AlgorithmUpdateView,
    AlgorithmDeleteView
)

urlpatterns = [
    path('', AlgorithmListView.as_view(), name='home'),
    # path('algorithm/<int:pk>/', AlgorithmDetailView.as_view(), name='algorithm-detail'),
    path('algorithm/<int:pk>/', views.algorithm_detail, name='algorithm-detail'),
    path('algorithm/new/', AlgorithmCreateView.as_view(), name='algorithm-create'),
    path('algorithm/<int:pk>/edit/', AlgorithmUpdateView.as_view(), name='algorithm-update'),
    path('algorithm/<int:pk>/delete/', AlgorithmDeleteView.as_view(), name='algorithm-delete')
]