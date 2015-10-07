from wq.db import rest
from wq.db.patterns import rest as patterns
from .models import Place, Observation
from .maps import place_map, index_map

rest.router.register_model(Observation)

rest.router.register_model(
    Place,
    serializer=patterns.IdentifiedLocatedModelSerializer,
    map=place_map
)

rest.router.add_page('index', {
    'url': '',
    'map': index_map
})
