from wq.db import rest
from .models import Category, Observation
from .serializers import ObservationSerializer


rest.router.register_model(
    Category,
    fields="__all__",
    cache="all",
    background_sync=False,
)

rest.router.register_model(
    Observation,
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
