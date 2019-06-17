from django.db import models

from organizer.models import Startup, Tag


class Post(models.Modes):

    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)
