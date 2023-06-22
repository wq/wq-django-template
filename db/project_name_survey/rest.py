from wq.db import rest
from .models import Category, Observation
from .serializers import ObservationSerializer


rest.router.register_model(
    Category,
    icon="config",
    description="Manage available categories",
    section="Admin",
    show_in_index="can_change",
    fields="__all__",
    cache="all",
    background_sync=False,
)

rest.router.register_model(
    Observation,
    icon="list",
    description="View and submit photos{% if with_gis %} on map{% endif %}",
    section="Contributions",
    serializer=ObservationSerializer,
    cache="first_page",
    background_sync=True,{% if with_gis %}
    map=[{
        'mode': 'list',
        'autoLayers': True,
        'layers': [],
    }, {
        'mode': 'detail',
        'autoLayers': True,
        'layers': [],
    }, {
        'mode': 'edit',
        'layers': [],
    }],
    {% endif %}
)
