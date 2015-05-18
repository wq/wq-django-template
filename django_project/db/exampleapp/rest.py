from wq.db import rest
from wq.db.patterns import rest as patterns
from .models import Example


rest.router.register_model(
    Example,
    serializer=patterns.IdentifiedModelSerializer
)
rest.router.add_page('index', {'url': '', 'map': True})
