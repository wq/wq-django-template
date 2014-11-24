from wq.db.rest import app
from .models import Example


app.router.register_model(Example)
app.router.add_page('index', {'url': ''})
