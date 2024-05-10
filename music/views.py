from rest_framework.views import APIView
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from billing.models import Billing
from products.models import Comment, Category, Product, Cart
from customers.models import Country, City, Address, Customers
from .serializer import AddressSerializer, ProductSerializer, CustomersSerializer, CategorySerializer, CommentSerializer, CartSerializer, BillingSerializer,CountrySerializer, CitySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination


class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name', 'id']
    pagination_class = LimitOffsetPagination

class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name', 'country__name',]
    pagination_class = LimitOffsetPagination

class AddressAPIViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name', 'city__name', 'city__country__name',]
    pagination_class = LimitOffsetPagination

class CustomersAPIViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = (IsAdminUser, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['first_name', 'last_name', 'username', 'email', 'address__name', 'address__city__name', 'address__city__country__name', 'phone_number']
    pagination_class = LimitOffsetPagination

class CommentAPIViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['text', 'id', 'customer__first_name', 'customer__last_name', 'customer__username']
    pagination_classes = LimitOffsetPagination

class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'created_date']
    pagination_class = LimitOffsetPagination

class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'description', 'manufacturer_name', 'category__title', 'price', 'price_type', 'rating', 'max_weight', 'comments__text', 'comments__customer__username']
    pagination_class = LimitOffsetPagination

class CartAPIViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['product__title', 'product__category__title', 'product__price', 'product__rating', 'product_number', 'product__comments__customer__username']
    pagination_class = LimitOffsetPagination

class BillingAPIViewSet(ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['customer__first_name', 'customer__last_name', 'customer__username', 'cart__total_price']
    pagination_class = LimitOffsetPagination