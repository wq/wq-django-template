from wq.db.rest import app
from wq.db.patterns import rest as patterns
from .models import Example


app.router.register_model(
    Example,
    serializer=patterns.IdentifiedModelSerializer
)
app.router.add_page('index', {'url': ''})
