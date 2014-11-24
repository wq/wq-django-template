from wq.db.patterns import admin
from .models import Example


admin.site.register(Example, admin.IdentifiedModelAdmin)
