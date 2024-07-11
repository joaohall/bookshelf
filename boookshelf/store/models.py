from django.db import models

# Create your models here.
class Book(models.Model):
    photo = models.ImageField(upload_to='books/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, verbose_name="Título")
    author = models.CharField(max_length=255, blank=False, verbose_name="Autor")
    publisher = models.CharField(max_length=255, blank=True,  null=True,verbose_name="Editora")
    language = models.CharField(max_length=50, blank=True, null=True, verbose_name="Idioma")
    cover_type = models.CharField(max_length=50, blank=True,  null=True,verbose_name="Tipo de Capa")
    pages = models.PositiveIntegerField(blank=True,  null=True,verbose_name="Número de Páginas")
    dimensions = models.CharField(blank=True,  null=True, max_length=50, verbose_name="Dimensões")
    publication_date = models.DateField(blank=True, null=True, verbose_name="Data de Publicação")
    price = models.DecimalField( blank=False, max_digits=10, decimal_places=2, verbose_name="Preço")
    edition_type = models.CharField(blank=True, null=True, max_length=50, verbose_name="Tipo de Edição")
    discount = models.BooleanField(blank=False)
    trending = models.BooleanField(blank=False)
    def __str__(self):
        return self.title