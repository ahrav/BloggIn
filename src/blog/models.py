from django.db.models import (
    CharField,
    TextField,
    DateField,
    ManyToManyField,
    Model,
)
from django.db.models import AutoSlugField
from organizer.models import Startup, Tag


class Post(Model):

    title = CharField(max_length=63)
    slug = AutoSlugField(
        max_length=63, populate_from=["title"]
    )
    text = TextField()
    pub_date = DateField()
    pub_date = DateField()
    tags = ManyToManyField(Tag)
    startups = ManyToManyField(Startup)

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date", "title"]
        verbose_name = "blog post"

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"
