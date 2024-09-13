from datetime import date

from django.core.exceptions import ValidationError
from django.db.models import ManyToManyField, IntegerField
from django.forms import Form, CharField, DateField, ModelChoiceField, Textarea, ModelForm, NumberInput

from viewer.models import Country, Creator, Genre

class CreatorForm(Form):
    name = CharField(max_length=32, required=False)
    surname = CharField(max_length=32, required=False)
    date_of_birth = DateField(required=False)
    date_of_death = DateField(required=False)
    country_of_birth = ModelChoiceField(queryset=Country.objects)
    country_of_death = ModelChoiceField(queryset=Country.objects)
    biography = CharField(widget=Textarea, required=False)

    def clean_name(self):
        cleaned_data = super().clean()
        initial = cleaned_data['name']
        result = initial
        if initial is not None:
            result = initial.strip()
            print(f"result: '{result}'")
            if len(result):
                result = result.capitalize()
            print(f"result: '{result}'")
        return result

    def validate_date_of_birth(self, value):
        super().validate(value)
        if value and value >= date.today():
            raise ValidationError("Lze zadávat datum narutzení pouze ")


    def validate(self):
        name = super().cleaned_data['name']
        surname = super().cleaned_data['surname']
        if len(name.strip()) ==0 and len(surname.strip()) == 0:
            raise ValidationError('Je potřeba zadat jméno nebo přijmení')


class CreatorModelForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'
        #fields = ['surname', 'name', 'date_of_birth', 'date_of_death']
        #exclude = ['date_of_death', 'name']

    date_of_death = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))
    date_of_birth = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))

    def clean_name(self):
        cleaned_data = super().clean()
        initial = cleaned_data['name']
        print(f"initial name: '{initial}'")
        result = initial
        if initial is not None:
            result = initial.strip()
            print(f"result: '{result}'")
            if len(result):
                result = result.capitalize()
            print(f"result: '{result}'")
        return result

    def clean_date_of_birth(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data['date_of_birth']
        if date_of_birth and date_of_birth >= date.today():
            raise ValidationError('Lze zadávat datum narození pouze v minulosti')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name']
        surname = cleaned_data['surname']
        if name is None:
            name = ''
        if surname is None:
            surname = ''
        if len(name.strip()) == 0 and len(surname.strip()) == 0:
            raise ValidationError('Je potřeba zadat jméno nebo příjmení')
        # TODO: pokud jsou zadaná data narození a úmrtí, tak datum narození musí být < datum úmrtí


class MovieForm(Form):
    title_orig = CharField(max_length=150, required=False)
    title_cz = CharField(max_length=150, required=False)
    genres = ModelChoiceField(queryset=Genre.objects)
    countries = ModelChoiceField(queryset=Country.objects)
    actors = ModelChoiceField(queryset=Creator.objects)
    directors = ModelChoiceField(queryset=Creator.objects)
    length = CharField(max_length=150, required=False)
    released = CharField(max_length=150, required=False)
    description = CharField(widget=Textarea, required=False)
    rating = CharField(max_length=150, required=False)
    created = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))
    updated = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))

    def clean_title_orig(self):
        initial = self.cleaned_data['title_orig']
        result = initial.strip()
        if len(result):
            result = result.capitalize()
        return result

    def validate(self, value):
        super().validate(value)
        if value and value >= date.today():
            raise ValidationError('jojo chyba')

    def validate(self):
        titlecz = super().cleaned_data['title_cz']
        titleorig = super().cleaned_data['title_orig']
        if len(titlecz.strip()) == 0 and len(titleorig.strip()) == 0:
            raise ValidationError("Je potřeba zadat jméno nebo přijmení")

