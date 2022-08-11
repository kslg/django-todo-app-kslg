from django.db import models

# Create your models here.

# Inherit all the base functionality from the built-in Django model class.
# The null equals false attribute here prevents items from being created without a name programmatically.
# Blank equals false will make the field required on forms.
# Default value of false here just to make sure that to-do items are marked as not done by default.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False , default=False)

    def __str__(self):
       return self.name 

