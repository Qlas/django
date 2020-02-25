from django.contrib import admin
from .models import Type, Priority, Label, Status, Component, Issue

admin.site.register(Type)
admin.site.register(Priority)
admin.site.register(Label)
admin.site.register(Status)
admin.site.register(Component)
admin.site.register(Issue)
