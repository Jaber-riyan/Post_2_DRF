from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.PostViewset) # router er antena
router.register('comments', views.CommentViewset) # router er antena
urlpatterns = [
    path('', include(router.urls)),
]