from django.db import models
from wagtail.core.models import  Page, Orderable # Импортируем Orderable
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel # доавили импорт MultiFieldPanel

from modelcluster.fields import ParentalKey # Импортируем ParentalKey

from wagtail.images.edit_handlers import ImageChooserPanel # Импортируем модуль для вывода изображений


class EquipmentImage(Orderable): # Добавим модель фрагмента - сниппета для вывода изображения
    """Изображение оборудования"""

    caption = models.CharField(max_length=200, verbose_name = "Текст слайда") # Добавим поле Текст слайда
    figure = models.ForeignKey(  # Добавляем изображение к нашим моделям с помощью ForeignKey
        'wagtailimages.Image',  # К модели wagtailimages.Image мы создаем ForeignKey и добавляем изображение
        blank=True,  # Разрешаем не заполнять поле подзаголовка
        null=True,  # Разрешаем хранить пустое значение в БД
        on_delete=models.SET_NULL,  # При удалении экземпляра класса HomePage в поле устанавливается пустое значение
        related_name='+'  # Ключ ForeignKey создает запись не только запись в БД в молели HomePage,
    # но и в wagtailimages.Image. В wagtailimages.Image запись нам не нужна. Блокируем создание
    # через related_name='+'
    )

    equipment = ParentalKey(  # Связываем EquipmentImage (ParentalKey
        # как и Page наследуется от  ClusterableModel)
        # с EquipmentPage через ParentalKey
        'equipment.EquipmentPage',  # Указываем что в приложении equipment
        # есть страница EquipmentPage с которой нужно установить связь
        on_delete=models.CASCADE,  # Если EquipmentPage будет удалена,
        # то EquipmentImage тоже удаляется
        related_name='slides'  # имя по которому можно обращаться к
        # EquipmentImage из EquipmentPage
    )

    panels = [# создаем панель для вывода в админку, используем именно слово panels
        FieldPanel('caption'),# выводим описание
        ImageChooserPanel('figure'), # выводим интерфейс для загрузки изображения
    ]# Во фрагментах или джанго моделях мы используем panels, не content_panels

class EquipmentOperator(models.Model): # Добавим модель фрагмента - сниппета
    """Оператор оборудования"""

    name = models.CharField(max_length=100, blank=False, null=False) # добавим поле имя оператора
    email = models.EmailField() # добавим поле адреса электронной почты

    equipment = ParentalKey( # Связываем EquipmentOperator (ParentalKey
        # как и Page наследуется от  ClusterableModel)
        # с EquipmentPage через ParentalKey
        'equipment.EquipmentPage', # Указываем что в приложении equipment
        # есть страница EquipmentPage с которой нужно установить связь
        on_delete=models.CASCADE, # Если EquipmentPage будет удалена,
        # то EquipmentOperator тоже удаляется
        related_name='operators' # имя по которому можно обращаться к
        # EquipmentOperator из EquipmentPage
    )


class EquipmentPage(Page):
    """Страница с финформацией о единице оборудования"""

    description = RichTextField( # добавляем поле описание
        blank=True,
        null=True,
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', # разрешаем использование функций редактора
                  'hr', 'bold', 'italic', 'ol', 'ul', 'link'],
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'), # добавляем возможность отображения поля в админпанели

        MultiFieldPanel([  # добавляет вывод красной полосы с заголовком heading
            InlinePanel('slides', label="слайд")],  # через InlinePanel добавим
            # возможность вывода фрагмента в админпанели и именование кнопки
            heading="Слайды", ),  # Заголовок

        MultiFieldPanel([ # добавляет вывод красной полосы с заголовком heading
            InlinePanel('operators', label="оператор")], # через InlinePanel добавим
            # возможность вывода фрагмента в админпанели и именование кнопки
            heading="Операторы",) # Заголовок
    ]

    subpage_types = [] # ограничиваем дочерние стриницы
    parent_page_types = ['equipment.EquipmentIndexPage'] # ограничиваем родительские страницы

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"

class  EquipmentIndexPage(Page):
    """Страница для вывода списка оборудования"""

    max_count = 1 # ограничиваем число страниц одной
    subpage_types = ['equipment.EquipmentPage'] # ограничиваем дочерних страниц
    parent_page_types = ['home.HomePage'] # ограничиваем родительских страниц