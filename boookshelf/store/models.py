from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name="Nome da Categoria")
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name="Nome do Autor")
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name="Nome da Editora")
    
    def __str__(self):
        return self.name

class Book(models.Model):
    photo = models.ImageField(upload_to='books', blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, verbose_name="Título")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Autor")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Editora")
    language = models.CharField(max_length=50, blank=True, null=True, verbose_name="Idioma")
    cover_type = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tipo de Capa")
    pages = models.PositiveIntegerField(blank=True, null=True, verbose_name="Número de Páginas")
    dimensions = models.CharField(blank=True, null=True, max_length=50, verbose_name="Dimensões")
    publication_date = models.DateField(blank=True, null=True, verbose_name="Data de Publicação")
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2, verbose_name="Preço")
    edition_type = models.CharField(blank=True, null=True, max_length=50, verbose_name="Tipo de Edição")
    discount = models.BooleanField(blank=False)
    trending = models.BooleanField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.title

class Rating(models.Model):
    book = models.ForeignKey(Book, null=True, blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(blank=False, null=True, max_length=255)
    description = models.TextField(blank=False, null=True)
    def __str__(self):
        return f"{self.header}: {self.rating}"