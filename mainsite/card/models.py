from django.db import models
from django.core.validators import FileExtensionValidator

class Service(models.Model):
    title = models.CharField(verbose_name="Название")
    photo = models.FileField(verbose_name="Изображение", validators=[FileExtensionValidator(["svg"])], upload_to='photos/%Y/%m/%d/')
    description = models.CharField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена", help_text="Если цена обсуждается с клиентом отдельно, то оставьте поле пустым", null=True, blank=True)
    include_in_work = models.CharField(help_text="Вводите то, что включено в работу через запятую с пробелом для точного отображения информации на сайте(ровно 3 пункта для правильности отображения).", verbose_name="Включено в работу")
    result = models.CharField(verbose_name="Результат работы", help_text="Введите то, что будет результатом работы.")
    what_need = models.CharField(verbose_name="Что требуется от клиента", help_text="Введите то, что потребуется от клиента в ходе выполнения работы, например название или описание его требования(ровно 3 пункта для правильности отображения, также через запятую с пробелом).")
    date = models.CharField(verbose_name="Дедлайны выполнения работы", help_text="Писать в кол времени, неделя, день и тд, в случае, если дедлайн обсуждается с клиентом отдельно - оставить поле пустым.", null=True, blank=True)

    def __str__(self) -> str:
        return self.title