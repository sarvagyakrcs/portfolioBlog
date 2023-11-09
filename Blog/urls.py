from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]


# List Posts:
#
# GET /posts/
# Retrieves a list of all posts.
# Create Post:
#
# POST /posts/
# Creates a new post.
# Retrieve Post:
#
# GET /posts/{id}/
# Retrieves details of a specific post.
# Update Post:
#
# PUT /posts/{id}/
# Updates a specific post.
# Delete Post:
#
# DELETE /posts/{id}/
# Deletes a specific post.