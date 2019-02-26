from __future__ import unicode_literals

from django.contrib import admin

from .models import Libro, Persona



admin.site.register(Libro)
admin.site.register(Persona)
