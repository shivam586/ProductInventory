from django.urls import path
from.views import GetProductByIdView, GetAllProductsView, UpdateProductView, DeleteProductView

urlpatterns = [
    path('products/<int:pk>/', GetProductByIdView.as_view()),
    path('products/', GetAllProductsView.as_view()),
    path('products/<int:pk>/update/', UpdateProductView.as_view()),
    path('products/<int:pk>/delete/', DeleteProductView.as_view()),
]