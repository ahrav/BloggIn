from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from .serializers import TagSerializer, StartupSerializer
from .models import Tag, Startup


class TagAPIDetail(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class StartupAPIDetail(RetrieveAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"


class StartupAPIList(ListAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


class TagAPIList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
