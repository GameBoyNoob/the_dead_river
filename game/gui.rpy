################################################################################
## Инициализация
################################################################################
## Main Menu Screen
screen main_menu():
    tag menu
    # Main menu background
    add gui.main_menu_background
    # Semi-transparent overlay for better text readability
    add Solid(gui.catppuccin_crust + "99")  # 60% opacity
    # Define possible subtexts
    $ possible_subtexts = [
        "Путешествие в неизвестность",
        "Твое преключение ждет",
        "Выбор важен",
        "Да начнется история",
        "Мир возможностей"
    ]
    # Randomly select a subtext each time the menu is shown
    $ random_subtext = renpy.random.choice(possible_subtexts)
    # Game title with animation
    frame:
        background None
        xalign 0.5
        yalign 0.15
        vbox:
            xalign 0.5  # Ensure title and subtitle are centered
            text _("[config.name]"):
                style "main_menu_title"
                xalign 0.5  # Center text horizontally
                outlines [(3, gui.catppuccin_crust, 0, 0)]
                at transform:
                    alpha 0.0
                    linear 0.5 alpha 1.0
                    block:
                        ease 1.0 yoffset -5
                        ease 1.0 yoffset 5
                        repeat
            # Add the random subtext
            text _(random_subtext):
                style "main_menu_subtitle"
                xalign 0.5  # Center text horizontally
                at transform:
                    alpha 0.0
                    linear 0.7 alpha 1.0

    # Navigation buttons with animation
    vbox:
        xpos 0.515 xanchor "center" yalign 0.6
        spacing gui.main_menu_button_spacing
        style_prefix "main_menu"
        at transform:
            alpha 0.0
            linear 0.7 alpha 1.0
        textbutton _("Начать") action Start() at button_hover_effect
        textbutton _("Сохранения") action ShowMenu("load") at button_hover_effect
        textbutton _("Настройки") action ShowMenu("preferences") at button_hover_effect
        textbutton _("Об Игре") action ShowMenu("about") at button_hover_effect
        if renpy.variant("pc"):
            textbutton _("Помощь") action ShowMenu("help") at button_hover_effect
            textbutton _("Выйти") action Quit(confirm=not main_menu) at button_hover_effect


# Button hover effect - combines zoom and wobble

transform button_hover_effect:
    on idle:
        easein 0.2 xoffset 0 zoom 1.0
    on hover:
        easein 0.2 xoffset 10 zoom 1.1

# Main menu title style
style main_menu_title:
    font gui.interface_text_font
    size gui.title_text_size
    color gui.catppuccin_lavender
    xalign 0.5
    yalign 0.5

# Main menu subtitle style
style main_menu_subtitle:
    font gui.interface_text_font
    size gui.title_text_size * 0.5  # Half the size of the title
    color gui.catppuccin_lavender
    xalign 0.5
    yalign 0.5
    outlines [(2, gui.catppuccin_crust, 0, 0)]

# Main menu button styles
style main_menu_button:
    properties gui.button_properties("main_menu_button")
    xalign 0.5
    padding(15, 8)
    background Frame(Solid(gui.main_menu_button_idle_background), 5, 5)


style main_menu_button_text:
    properties gui.button_text_properties("main_menu_button")
    size 40
    xalign 0.5  # Center text within button
    color gui.main_menu_text_idle_color
    outlines gui.main_menu_text_outlines
    hover_color gui.main_menu_text_hover_color
    hover_outlines gui.main_menu_text_hover_outlines

style main_menu_button:
    hover_background Frame(Solid(gui.main_menu_button_hover_background), 5, 5)
    
## Оператор init offset повышает приоритет инициализации в этом файле над
## другими файлами, из-за чего инициализация здесь запускается первее.
init offset = -2

## Initialize GUI with game window dimensions
init python:
    gui.init(1920, 1080)

## Enable check for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True


################################################################################
## GUI Configurable Variables
################################################################################


## Colors #######################################################################
##
## Catppuccin Mocha palette implementation

## Base colors
define gui.catppuccin_base = "#1e1e2e"       # Background
define gui.catppuccin_mantle = "#181825"     # Darker background
define gui.catppuccin_crust = "#11111b"      # Darkest background
define gui.catppuccin_text = "#cdd6f4"       # Primary text
define gui.catppuccin_subtext = "#bac2de"    # Secondary text
define gui.catppuccin_lavender = "#b4befe"   # Primary accent
define gui.catppuccin_blue = "#89b4fa"       # Secondary accent
define gui.catppuccin_sapphire = "#74c7ec"   # Tertiary accent
define gui.catppuccin_mauve = "#cba6f7"      # Highlights
define gui.catppuccin_pink = "#f5c2e7"       # Special elements
define gui.catppuccin_green = "#a6e3a1"      # Success states
define gui.catppuccin_peach = "#fab387"      # Warnings/selections
define gui.catppuccin_red = "#f38ba8"        # Errors

## Accent color used in headings and emphasized text
define gui.accent_color = '#99ccff'

## Color used for text buttons when not selected or hovered
define gui.idle_color = '#888888'

## Small_color is used for small text that needs to be brighter/darker to stand out
define gui.idle_small_color = '#aaaaaa'

## Color used for buttons and bars when hovered
define gui.hover_color = '#c1e0ff'

## Color used for text buttons when selected but not hovered
define gui.selected_color = '#ffffff'

## Color used for text buttons that cannot be selected
define gui.insensitive_color = '#8888887f'

## Colors used for unfilled parts of bars - used when recreating image files
define gui.muted_color = '#3d5166'
define gui.hover_muted_color = '#5b7a99'

## Colors used for dialogue and choice text
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Fonts and Sizes #########################################################

## Font used for in-game text
define gui.text_font = "AdwaitaMonoNerdFontMono-Regular.ttf"

## Font used for character names
define gui.name_text_font = "AdwaitaMonoNerdFontMono-Bold.ttf"

## Font used for out-of-game text
define gui.interface_text_font = "AdwaitaMonoNerdFontMono-Regular.ttf"

## Size of normal dialogue text
define gui.text_size = 33

## Size of character names
define gui.name_text_size = 45

## Size of text in the user interface
define gui.interface_text_size = 33

## Size of labels in the user interface
define gui.label_text_size = 36

## Size of text on the notification screen
define gui.notify_text_size = 24

## Size of the game title
define gui.title_text_size = 75


## Main and Game Menus #####################################################

## Images used for the main and game menus
define gui.main_menu_background = "bg/background.png"
define gui.game_menu_background = "gui/game_menu.png"

## Main Menu Customization ##################################################

## Main menu button properties
define gui.main_menu_button_width = 420
define gui.main_menu_button_height = 60
define gui.main_menu_button_spacing = 12

## Main menu button backgrounds
define gui.main_menu_button_idle_background = gui.catppuccin_mantle + "99"  # Semi-transparent
define gui.main_menu_button_hover_background = gui.catppuccin_lavender + "33"  # Semi-transparent

## Main menu text effects
define gui.main_menu_text_idle_color = gui.catppuccin_text
define gui.main_menu_text_hover_color = gui.catppuccin_lavender
define gui.main_menu_text_outlines = [(2, gui.catppuccin_crust, 0, 0)]
define gui.main_menu_text_hover_outlines = [(2, gui.catppuccin_mauve, 0, 0)]

## Title positioning
define gui.main_menu_title_xalign = 0.5
define gui.main_menu_title_yalign = 0.1


## Dialogue ##################################################################

## Height of the dialogue text box
define gui.textbox_height = 278

## Vertical position of the text box. 0.0 is top, 0.5 is center, 1.0 is bottom
define gui.textbox_yalign = 1.0

## Position of speaking character's name relative to text box
define gui.name_xpos = 360
define gui.name_ypos = 0

## Horizontal alignment of character name. 0.0 is left, 0.5 is center, 1.0 is right
define gui.name_xalign = 0.0

## Width, height and borders of the box containing character name, or None for auto-sizing
define gui.namebox_width = None
define gui.namebox_height = None

## Borders of the box containing the character name, in order: left, top, right, bottom
define gui.namebox_borders = Borders(5, 5, 5, 5)

## If True, the background of the namebox will be tiled, if False, it will be scaled
define gui.namebox_tile = False


## Размещение диалога по отношению к текстовому окну. Это могут быть целые
## значения в пикселях слева и сверху от текстового окна или процентное
## отношение, например, 0.5 для центрирования.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Максимальная ширина текста диалога в пикселях.
define gui.dialogue_width = 1116

## Горизонтальное выравнивание текста диалога. Это может быть 0.0 для
## левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного
## выравнивания.
define gui.dialogue_text_xalign = 0.0


## Кнопки ######################################################################
##
## Эти переменные, вместе с файлами изображений в gui/button, контролируют
## аспекты того, как отображаются кнопки.

## Ширина и высота кнопки в пикселях. Если None, Ren'Py самостоятельно
## рассчитает размер.
define gui.button_width = None
define gui.button_height = None

## Границы каждой стороны кнопки в порядке слева, сверху, справа, снизу.
define gui.button_borders = Borders(6, 6, 6, 6)

## Если True, фон изображения будет моститься. Если False, фон изображения будет
## линейно масштабирован.
define gui.button_tile = False

## Шрифт, используемый кнопкой.
define gui.button_text_font = gui.interface_text_font

## Размер текста, используемый кнопкой.
define gui.button_text_size = gui.interface_text_size

## Цвет текста в кнопке в различных состояниях.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Горизонтальное выравнивание текста в кнопке. (0.0 — лево, 0.5 — по центру,
## 1.0 — право).
define gui.button_text_xalign = 0.0


## Эти переменные переписывают настройки различных видов кнопок. Пожалуйста,
## посмотрите документацию по gui для просмотра всех вариаций кнопок и для чего
## каждая из них нужна.
##
## Эти настройки используются стандартным интерфейсом:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Вы также можете добавить собственные настройки, добавляя правильно
## именованные переменные. Например, вы можете раскомментировать следующую
## строчку, чтобы установить ширину кнопок навигации.

# define gui.navigation_button_width = 250


## Кнопки Выбора ###############################################################
##
## Кнопки выбора используются во внутриигровых меню.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Кнопки Слотов ###############################################################
##
## Кнопка слотов — особый вид кнопки. Она содержит миниатюру и текст,
## описывающий слот сохранения. Слот сохранения использует файлы из gui/button,
## как и другие виды кнопок.

## Кнопка слота сохранения.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Ширина и высота миниатюры, используемой слотом сохранения.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Количество колонок и рядов в таблице слотов.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Позиционирование и Интервалы ################################################
##
## Эти переменные контролируют позиционирование и интервалы различных элементов
## пользовательского интерфейса.

## Местоположение левого края навигационных кнопок по отношению к левому краю
## экрана.
define gui.navigation_xpos = 60

## Вертикальная позиция индикатора пропуска.
define gui.skip_ypos = 15

## Вертикальная позиция экрана уведомлений.
define gui.notify_ypos = 68

## Интервал между выборами в меню.
define gui.choice_spacing = 33

## Кнопки в секции навигации главного и игрового меню.
define gui.navigation_spacing = 6

## Контролирует интервал между настройками.
define gui.pref_spacing = 15

## Контролирует интервал между кнопками настройки.
define gui.pref_button_spacing = 0

## Интервал между кнопками страниц.
define gui.page_spacing = 0

## Интервал между слотами.
define gui.slot_spacing = 15

## Позиция текста главного меню.
define gui.main_menu_text_xalign = 1.0


## Рамки #######################################################################
##
## Эти переменные контролируют вид рамок, содержащих компоненты
## пользовательского интерфейса, когда наложения или окна не представлены.

## Генерируем рамки.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Рамки, используемые в частях экрана подтверждения.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Рамки, используемые в частях экрана пропуска.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Рамки, используемые в частях экрана уведомлений.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Должны ли фоны рамок моститься?
define gui.frame_tile = False


## Панели, Полосы прокрутки и Ползунки #########################################
##
## Эти настройки контролируют вид и размер панелей, полос прокрутки и ползунков.
##
## Стандартный GUI использует только ползунки и вертикальные полосы прокрутки.
## Все остальные полосы используются только в новосозданных экранах.

## Высота горизонтальных панелей, полос прокрутки и ползунков. Ширина
## вертикальных панелей, полос прокрутки и ползунков.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True, если изображения панелей должны моститься. False, если они должны быть
## линейно масштабированы.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Горизонтальные границы.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Вертикальные границы.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## История #####################################################################
##
## Экран истории показывает диалог, который игрок уже прошёл.

## Количество диалоговых блоков истории, которые Ren'Py будет хранить.
define config.history_length = 250

## Высота доступных записей на экране истории, или None, чтобы задать высоту в
## зависимости от производительности.
define gui.history_height = 210

## Дополнительное пространство добавляемое между записями экрана истории.
define gui.history_spacing = 0

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Режим NVL ###################################################################
##
## Экран режима NVL показывает диалог NVL персонажей.

## Границы фона окна NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Максимальное число показываемых строк в режиме NVL. Когда количество строчек
## начинает превышать это значение, старые строчки очищаются.
define gui.nvl_list_length = 6

## Высота доступных строчек в режиме NVL. Установите на None, чтобы строчки
## динамически регулировали свою высоту.
define gui.nvl_height = 173

## Интервал между строчками в режиме NVL, если gui.nvl_height имеет значение
## None, а также между строчками и меню режима NVL.
define gui.nvl_spacing = 15

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## Местоположение, ширина и выравнивание текста nvl_thought (текст от лица
## персонажа nvl_narrator).
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Местоположение кнопок меню NVL.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Локализация #################################################################

## Эта настройка контролирует доступ к разрыву линий. Стандартная настройка
## подходит для большинства языков. Список доступных значений можно найти на
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Мобильные устройства
################################################################################

init python:

    ## Этот параметр увеличивает размер быстрых кнопок, чтобы сделать их
    ## доступнее для нажатия на планшетах и телефонах.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Это изменяет размеры и интервалы различных элементов GUI, чтобы
    ## убедиться, что они будут лучше видны на телефонах.
    @gui.variant
    def small():

        ## Размеры шрифтов.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Регулирует местоположение текстового окна.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Изменяет размеры и интервалы различных объектов.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Местоположение кнопок слотов.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Режим NVL.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
