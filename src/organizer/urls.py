from django.urls import path

from .views import (
    TagAPIDetail,
    TagAPIList,
    StartupAPIDetail,
    StartupAPIList,
)

urlpatterns = [
    path("tag/", TagAPIList.as_view(), name="api-tag-list"),
    path(
        "tag/<str: slug>/",
        TagAPIDetail.as_view(),
        name="api-tag-detail",
    ),
    path(
        "startup/",
        StartupAPIList.as_view(),
        name="api-startup-list",
    ),
    path(
        "startup/<str: slug>/",
        StartupAPIDetail.as_view(),
        name="api-startup-detail",
    ),
]
