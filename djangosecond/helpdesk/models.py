from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Priority(models.Model):
    priority = models.CharField(max_length=100)

    def __str__(self):
        return self.priority

class Label(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class Component(models.Model):
    component = models.CharField(max_length=100)


    def __str__(self):
        return self.component

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignee_user")
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reporter_user")
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    label = models.ManyToManyField(Label)
    component = models.ManyToManyField(Component)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

