from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BucketlistView

urlpatterns = {
    path('bucketlists/<int:pk>', BucketlistView.as_view(), name="crud_view")
}

urlpatterns = format_suffix_patterns(urlpatterns)
