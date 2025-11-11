from django.db import models

class Movie(models.Model):
    title = models.CharField("Título", max_length=200)
    genre = models.CharField("Género", max_length=100)
    director_name = models.CharField("Director", max_length=100)
    release_year = models.PositiveIntegerField("Año de publicación")
    synopsis = models.TextField("Sinopsis")
    cover_image = models.ImageField("Portada", upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.release_year}"