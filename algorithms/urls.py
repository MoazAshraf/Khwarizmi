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
    path('algorithm/<slug:slug>/', views.algorithm_detail, name='algorithm-detail'),
    path('new-algorithm/', AlgorithmCreateView.as_view(), name='algorithm-create'),
    path('algorithm/<slug:slug>/edit/', AlgorithmUpdateView.as_view(), name='algorithm-update'),
    path('algorithm/<slug:slug>/delete/', AlgorithmDeleteView.as_view(), name='algorithm-delete')
]