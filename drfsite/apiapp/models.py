from django.db import models


class Data(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    software = models.CharField(max_length=255)
    version = models.CharField(max_length=255)

    def __str__(self):
        return self.id


class Vulnerability(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    vulnerable_versions = models.CharField(max_length=255)

    def __str__(self):
        return self.title
