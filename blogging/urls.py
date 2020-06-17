from django.urls import include, path

from blogging.views import stub_view
from blogging.views import list_view
from blogging.views import detail_view
from rest_framework import routers
from blogging.views import UserViewSet
from blogging.views import GroupViewSet
from blogging.views import PostViewSet
from blogging.views import CategoryViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]	