from wq.db.patterns import models


class Example(models.IdentifiedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
