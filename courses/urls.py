from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CourseViewSet

router = SimpleRouter()
router.register('courses', CourseViewSet, basename='courses')
urlpatterns = router.urls