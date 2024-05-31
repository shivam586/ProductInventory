from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import Product
from.serializers import ProductSerializer

class GetProductByIdView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class GetAllProductsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class UpdateProductView(APIView):
    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class DeleteProductView(APIView):
    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=204)
