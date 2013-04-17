from django.db import models

class DatesMixin(models.Model):
    """Used to track the datetimes the object was created or modified.  Most every model should include this mixin."""
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    class Meta:
        abstract = True