from django import forms
from .models import Movie

class MovieFilterForm(forms.Form):
    genre = forms.ChoiceField(
        required=False,
        label='',
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select', 'onchange': 'this.form.submit();'})
    )
    year = forms.IntegerField(
        required=False,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Filtrar por año',
            'onchange': 'this.form.submit();'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Movie.objects.values_list('genre', flat=True).distinct()
        self.fields['genre'].choices = [('', 'Todos los géneros')] + [(g, g) for g in genres if g]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Movie.objects.values_list('genre', flat=True).distinct()
        self.fields['genre'].choices = [('', 'Todos los géneros')] + [(g, g) for g in genres if g]
        
        
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'director_name', 'release_year', 'synopsis', 'cover_image']
        

class MovieFilterForm(forms.Form):
    genre = forms.CharField(required=False, label='Género')
    year = forms.IntegerField(required=False, label='Año')