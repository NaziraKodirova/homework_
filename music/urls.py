from django.urls import path, include
from .views import (CountryAPIViewSet, CityAPIViewSet, AddressAPIViewSet, CustomersAPIViewSet, CommentAPIViewSet,
                    CategoryAPIViewSet, ProductAPIViewSet, CartAPIViewSet, BillingAPIViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('category', viewset=CategoryAPIViewSet)
router.register('products', viewset=ProductAPIViewSet)
router.register('city', viewset=CityAPIViewSet)
router.register('address', viewset=AddressAPIViewSet)
router.register('cart', viewset=CartAPIViewSet)
router.register('billing', viewset=BillingAPIViewSet)
router.register('country', viewset=CountryAPIViewSet)
router.register('customers', viewset=CustomersAPIViewSet)
router.register('comments', viewset=CommentAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token)

]
