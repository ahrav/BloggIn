from django.urls import path

from .views import (
    TagAPIDetail,
    TagAPIList,
    StartupAPIDetail,
    StartupAPIList,
    NewsLinkAPIDetail,
    NewsLinkAPIList,
)

urlpatterns = [
    path("tag/", TagAPIList.as_view(), name="api-tag-list"),
    path(
        "tag/<str:slug>/",
        TagAPIDetail.as_view(),
        name="api-tag-detail",
    ),
    path(
        "startup/",
        StartupAPIList.as_view(),
        name="api-startup-list",
    ),
    path(
        "startup/<str:slug>/",
        StartupAPIDetail.as_view(),
        name="api-startup-detail",
    ),
    path(
        "newslink/",
        NewsLinkAPIList.as_view(),
        name="api-newslink-list",
    ),
    path(
        "startup/<str:startup_slug>/<str:newslink_slug>",
        NewsLinkAPIDetail.as_view(),
        name="api-newslink-detail",
    ),
]
