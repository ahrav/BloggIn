from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import NewsLinkSerializer
from .models import NewsLink


class NewsLinkAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer

    def get_object(self):

        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("newslink_slug")

        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup_slug=startup_slug,
        )
        self.check_object_permissions(
            self.request, newslink
        )
        return newslink


class NewsLinkAPIList(ListCreateAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
