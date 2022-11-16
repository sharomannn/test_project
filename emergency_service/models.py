import uuid
from django.db import models
from django.utils.text import slugify


class EmergencyService(models.Model):
    name = models.CharField('Название службы', max_length=255)
    code = models.CharField('Код службы', max_length=255)
    number = models.CharField('Номер телефона', max_length=255)

    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'
        ordering = ('code',)

    def __str__(self):
        return self.name


class Applicant(models.Model):
    MAN = 'М'
    WOMAN = 'Ж'
    GENDER_CHOICES = (
        (MAN, 'Мужчина'),
        (WOMAN, 'Женщина'),)
    photo_applicant = models.ImageField('Фото заявителя', blank=True)
    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=100)
    name_father = models.CharField('Отчество', max_length=255)
    gender = models.CharField('Пол', max_length=255,
                              choices=GENDER_CHOICES,
                              default=WOMAN)
    date = models.DateField('Дата рождения')
    health_status = models.TextField('Состояние здоровья', blank=True,
                                     default='Практически здоров',
                                     help_text='Аллергоамамнез, хронические заболевания и т.п.')
    number = models.CharField('Номер телефона', max_length=255, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.name_father}'

    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        ordering = ('name',)


class Appeal(models.Model):
    IN_WORK = 'В работе'
    FINNISHED = 'Завершено'
    STATUS_CHOICES = (
        (IN_WORK, 'В работе'),
        (FINNISHED, 'Завершено'),)
    status_appeal = models.CharField('Статус обращения', max_length=255,
                                     choices=STATUS_CHOICES,
                                     default=IN_WORK)
    date = models.DateTimeField('Дата обращения', auto_now_add=False)
    number = models.UUIDField('Номер обращения', default=uuid.uuid4,
                              editable=False, db_index=True)
    service = models.ManyToManyField(EmergencyService, related_name='appeals',
                                     verbose_name='Экстренная служба',
                                     blank=True)
    applicant = models.ForeignKey(Applicant, related_name='appeals',
                                  verbose_name='Заявитель',
                                  on_delete=models.CASCADE)
    number_cases = models.IntegerField('Количество пострадавших', default=1)
    not_call = models.BooleanField('Не звонить', default=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.number)
        super(Appeal, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ('-date',)
