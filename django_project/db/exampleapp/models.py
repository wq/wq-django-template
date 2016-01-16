from django.db import models
from wq.db.patterns import models as patterns


class Place(patterns.IdentifiedLocatedModel):
    description = models.TextField()


class Observation(models.Model):
    place = models.ForeignKey(Place)
    date = models.DateField()
    photo = models.ImageField()

    def __str__(self):
        return "%s on %s" % (self.place, self.date)
