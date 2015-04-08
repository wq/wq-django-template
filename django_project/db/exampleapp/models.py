from django.db import models
from wq.db.patterns import models as patterns


class Example(patterns.IdentifiedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
