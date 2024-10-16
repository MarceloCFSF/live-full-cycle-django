from django.db import models

class Video(models.Model):
  title = models.CharField(max_length=100, unique=True, verbose_name='Título')
  description = models.TextField(verbose_name='Descrição')
  thumbmail = models.ImageField(upload_to='media/thumbnails/', verbose_name='Miniatura')
  video = models.FileField(upload_to='media/videos/', verbose_name='Vídeo')
  slug = models.SlugField(max_length=100, unique=True)
  published_at = models.DateTimeField(verbose_name='Publicado em')
  is_published = models.BooleanField(default=False, verbose_name='Está publicado')
  num_likes = models.IntegerField(default=0, verbose_name='Número de curtidas')
  num_views = models.IntegerField(default=0, verbose_name='Número de visualizações')
  tags = models.ManyToManyField('Tag', verbose_name='Tags')

  class Meta:
    verbose_name = 'Vídeo'
    verbose_name_plural = 'Vídeos'
  
  def __str__(self):
    return self.title
  
class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True, verbose_name='Nome')
  
  def __str__(self):
    return self.name
  