from buku.models import ModelAuthor, ModelBook
from rest_framework import serializers

"""
Serializer Convert Complex Data Types (Django Model & Querysets) into JSON or XML
"""

class ModelAuthorSerial(serializers.ModelSerializer):
  """
  Serialize Model Author into JSON
  """
  class Meta:
    """
    """
    model = ModelAuthor
    fields = '__all__'

class ModelBookSerial(serializers.ModelSerializer):
  """
  Serialize Model Book into JSON
  """
  # Include Author Full Name Instead of Author ID
  author = serializers.StringRelatedField()
  class Meta:
    """
    """
    model = ModelBook
    fields = '__all__'