from django.db import models
from django.core.validators import FileExtensionValidator
from .validators import stripScripts
from .savers import media_saver, content_file_name

# Create your models here.

class MediaContents(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, auto_created=True, unique=True)
    name = models.CharField(max_length=100, unique=True, null=True)
    media = models.FileField(unique=True, upload_to=media_saver, validators=[FileExtensionValidator( ['avi', 'mp4', 'jpg', 'png', 'gif', 'mp3', 'wav', 'svg', 'pdf'] )])
    objects = models.Manager()

    def __str__(self):
        return self.media.name

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'

class Accueils(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, auto_created=True, unique=True)
    name = models.SlugField(max_length=100, unique=True, verbose_name='nom')
    depth = models.PositiveSmallIntegerField(default=4000, verbose_name='profondeur')
    template = models.TextField(validators=[ stripScripts ])

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = 'Accueil'
        verbose_name_plural = 'Accueils'


class Articles(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, auto_created=True, unique=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='articles/')
    # image2 = models.ImageField(upload_to='articles/', null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Collections(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, auto_created=True, unique=True)
    name = models.SlugField(max_length=100, unique=True, null=False, verbose_name='URL')
    title = models.CharField(max_length=100, unique=True, null=True, verbose_name='titre')
    cover = models.ImageField(upload_to=content_file_name, verbose_name='front cover')
    background = models.ImageField(upload_to=content_file_name, verbose_name='background')
    accueil = models.ForeignKey(Accueils, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Articles)
    enabled = models.BooleanField(default=True)
    last_modif = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'

class Commandes(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, auto_created=True, unique=True)
    order_date = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    buyer = models.CharField(max_length=255, null=False, verbose_name='acheteur')
    facturation_adress = models.CharField(max_length=255, null=False, verbose_name='adresse de facturation')

    def __str__(self):
        return '{0} | {1}'.format(self.order_date, self.facturation_adress)

    class Meta:
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'