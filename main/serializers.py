from rest_framework.serializers import ModelSerializer
from . import models as md

class BlogSerializer(ModelSerializer):
    class Meta:
        model = md.Blog
        fields = '__all__'



