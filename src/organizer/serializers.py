from rest_framework.serializers import ModelSerializer

from .models import Tag, NewsLink, Startup


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class StartupSerializer(ModelSerializer):
    class Meta:
        model = Startup
        fields = "__all__"


class NewsLinkSerializer(ModelSerializer):
    class Meta:
        model = NewsLink
        fields = "__all__"
