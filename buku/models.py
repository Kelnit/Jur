from django.db import models
from django.core.validators import MinValueValidator

# Create Your Model
class ModelAuthor(models.Model):
  """
  Represent Author Attribute in Model
  """
  id = models.AutoField(primary_key=True)
  nama = models.CharField(max_length=150)

  def __str__(self):
    """
    Custom Model Author Representation
    """
    return self.nama
  
  class Meta:
    """
    Define Metadata on ModelAuthor
    """
    db_table = 'tabel_author'
    verbose_name = 'author'
    verbose_name_plural = 'authors'
  
class ModelBook(models.Model):
  """
  Represent Book Attribute in Model
  """
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=150)
  pages = models.PositiveIntegerField()
  author = models.ForeignKey(ModelAuthor, on_delete=models.CASCADE)
  publisher = models.CharField()
  release_dates = models.DateField()
  description = models.TextField()
  stocks = models.PositiveIntegerField(validators = [MinValueValidator(0, "Only Positive Digit !")])

  def __str__(self):
    """
    Custom Model Title Representation
    """
    return self.title
  class Meta:
    """
    Define Metadata on ModelBook
    """
    db_table = 'tabel_book'
    verbose_name = 'book'
    verbose_name_plural = 'books'