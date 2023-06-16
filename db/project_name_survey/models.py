{% if with_gis %}from django.contrib.gis.db import models
{% else %}from django.db import models
{% endif %}from wq.db.rest.models import LabelModel
from django.conf import settings


"""
Example survey app for {{ project_name }}.  The models below are examples, and
are not required for wq to work.  Feel free to modify, rewrite, or delete and
replace this folder with a completely new Django app.

https://wq.io/guides/describe-your-data-model
"""


class Category(LabelModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    wq_label_template = "{% templatetag openvariable %}name{% templatetag closevariable %}"

    class Meta:
        verbose_name_plural = "categories"


class Observation(LabelModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="submitted by",
    )
    date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date",
        help_text="The date when the observation was taken",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Category",
        help_text="Observation type",
    ){% if with_gis %}
    geometry = models.PointField(
        srid=4326,
        verbose_name="Location",
        help_text="The location of the observation",
    ){% endif %}
    photo = models.ImageField(
        upload_to="observations",
        null=True,
        blank=True,
        verbose_name="Photo",
        help_text="Photo of the observation",
    )
    notes = models.TextField(
        null=True,
        blank=True,
        verbose_name="Notes",
        help_text="Field observations and notes",
    )

    wq_label_template = "{% templatetag openvariable %}date{% templatetag closevariable %}"

    class Meta:
        verbose_name_plural = "observations"
        ordering = ['-date']
