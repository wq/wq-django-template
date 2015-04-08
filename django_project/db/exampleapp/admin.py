from django.contrib import admin
from wq.db.patterns import admin as patterns
from .models import Example


admin.site.register(Example, patterns.IdentifiedModelAdmin)
