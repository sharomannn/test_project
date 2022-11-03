from django.db import models


class EmergencyService(models.Model):
    name = models.CharField("Название службы", max_length=100)
    code = models.CharField("Код службы", max_length=100)
    number = models.DecimalField("Номер телефона", max_digits=12,
                                 decimal_places=0)

    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'
        ordering = ['code']

    def __str__(self):
        return self.name


class Applicant(models.Model):
    MAN = 'М'
    WOMAN = 'Ж'
    GENDER_CHOICES = [
        (MAN, 'Мужчина'),
        (WOMAN, 'Женщина'), ]
    name = models.CharField("ФИО заявителя", max_length=100)
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES,
                              default=WOMAN)
    date = models.DateField("Дата рождения")
    health_status = models.TextField("Состояние здоровья", blank=True)
    number = models.CharField("Номер телефона", max_length=100, blank=True)

    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        ordering = ['name']

    def __str__(self):
        return self.name


class Appeal(models.Model):
    date = models.DateField("Дата обращения")
    number = models.IntegerField("Номер обращения")
    service = models.ManyToManyField(EmergencyService, related_name='appeals',
                                     verbose_name='Экстренная служба')
    applicant = models.ForeignKey(Applicant, related_name='appeals',
                                  verbose_name='Заявитель',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ['date', 'number']
