from django.db import models
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel #Импортируем панель
from wagtail.core.fields import RichTextField, StreamField #Импортируем новый редактор StreamField
from wagtail.images.edit_handlers import ImageChooserPanel #Импортируем панель для работы с изображениями

from wagtail.core.blocks import RichTextBlock #Импортируем блок для текста
from wagtail.images.blocks import ImageChooserBlock #Импортируем блок для изображения
from wagtail.embeds.blocks import EmbedBlock #Импортируем блок для видео

from .blocks import FigCaptionBlock # Импортируем созданный блок FigCaptionBlock


class NewsPage(Page): # Создадим новый класс , так же наследуемый от базового класса Page
    pass # не будем добавлять функционал, используем тот что есть

class HomePage(Page):   #HomePage которая наследуется от класса Page
    # Изменения в базе данных
    subtitles = models.CharField( #Даем название переменной и через
                                # точечный интерфейс выбираем текстовое поле CharField
        max_length=120,         #Устанавливаем максимальную длину поля в 120 символов
        blank=True,             #Разрешаем не заполнять поле подзаголовка
        null=True,              #Разрешаем хранить пустое значение в БД
        verbose_name="Подзаголовок" #Переопределяем отображаемое имя подзаголовка
    )

    rtfbody = RichTextField( #Создаем переменную используя редактор текста RichTextField
        blank=True,  # Разрешаем не заполнять поле подзаголовка
        null=True,  # Разрешаем хранить пустое значение в БД
    )

    body = StreamField([ #Подключаем наш редактор и блоки входящие в его состав которые мы импортировали ранее
        ('figcaptionblock', FigCaptionBlock()),
        ('rtfblock', RichTextBlock(
            features=['h1', 'h6', 'hr', 'bold', 'italic'], # Ограничиваем использование инструментов в редакторе текста
            label="Текст", # Присваиваем название блоку
            help_text="Введите описание" # Вводим подсказку
        )), #Подключаем блок для текста
        ('imgblock', ImageChooserBlock()), #Подключаем блок для изображения
        ('youtubeblock', EmbedBlock()) #Подключаем блок для видео
    ],
        block_counts = { # Устанавливаем ограничения на число блоков в административной панели
            'rtfblock':{'min_num':1}, # Блок с текстом не менее 1
            'imgblock':{'max_num':1}, # Блок с изображением не более 1
        },
        blank=True)

    bg_image = models.ForeignKey( # Добавляем изображение к нашим моделям с помощью ForeignKey
        'wagtailimages.Image', # К модели wagtailimages.Image мы создаем ForeignKey и добавляем изображение
        blank=True,  # Разрешаем не заполнять поле подзаголовка
        null=True,  # Разрешаем хранить пустое значение в БД
        on_delete=models.SET_NULL, # При удалении экземпляра класса HomePage в поле устанавливается пустое значение
        related_name='+' # Ключ ForeignKey создает запись не только запись в БД в молели HomePage,
        # но и в wagtailimages.Image. В wagtailimages.Image запись нам не нужна. Блокируем создание
        # через related_name='+'

    )


    # Организация вывода поля в административной панели
    content_panels = Page.content_panels + [ #content_panels соотносится с вкладкой "Содержимое"
        FieldPanel('subtitles'),             #FieldPanel используется для основных типов полей
        #в него мы передаем ранее созданную переменную subtitles
        FieldPanel('rtfbody'), #Добавляем возможность отображения в административной панели RichTextField
        ImageChooserPanel('bg_image'), # Добавляем вывод в административной панели для bg_image
        StreamFieldPanel('body'), # Организуем вывод редактора StreamField в административной панели
    ]

    promote_panels = []
    settings_panels = []