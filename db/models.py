from django.db import models

# Create your models here.
class Table (models.Model):
    name = models.CharField( 'название темы', max_length=200)
    title = models.CharField('основная мысль', max_length=200, blank=True, null=True)
    text_all = models.TextField('содержимое статьи', blank=True, null=True)
    text_code = models.TextField('как выглядт код',blank=True, null=True)
    image= models.ImageField('фото', upload_to="static/img/", blank=True, null=True)
    date = models.DateTimeField('дата создания', auto_now=True)
    slug = models.SlugField('ссылка для статьи', max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Таблица")
        verbose_name_plural = ("Таблицы")
        # db_table = 'table'
        # verbose_name = 'table'
    

    # def get_absolute_url(self):
    # return reverse("_detail", kwargs={"pk": self.pk})
