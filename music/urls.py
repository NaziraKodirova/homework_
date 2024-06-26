from django.urls import path, include
from .views import ArtistAPIViewSet, AlbumAPIViewSet, SongsAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Web Shop API",
        default_version='v1',
        description="Demo Web SHop API",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='nazira.kodirova@mail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)
router = DefaultRouter()
router.register('albums', viewset=AlbumAPIViewSet)
router.register('artists', viewset=ArtistAPIViewSet)
router.register('songs', viewset=SongsAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
]