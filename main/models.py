from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Blog(models.Model):
        title = models.CharField(max_length=200)
        subtitle = models.CharField(max_length = 250)
        author = models.CharField(max_length=200)
        content = CKEditor5Field('Text', config_name='extends' )
        publisher = models.TextField()
        created = models.DateField(auto_now_add=True)

        def __str__(self) -> str:
            return self.title



