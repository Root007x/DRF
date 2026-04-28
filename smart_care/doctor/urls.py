from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include


router = DefaultRouter()

router.register("", views.DoctorViewSet)
router.register("", views.SpecializationViewSet)
router.register("", views.DesignationViewSet)
router.register("", views.AvailableTimeViewSet)
router.register("", views.ReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
