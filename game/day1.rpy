label day1_intro:
    scene black with fade
    pause 1.0

    show intro1 with Dissolve(3.0)
    play sound "audio/river_ambience.ogg" volume 0.4 loop
    pause 2.0

    play music "ost/Project_8.ogg" volume 0.7 fadeout 2.0 fadein 3.0 loop

    narrator_slow "На берегах широкой реки раскинулись два города — соперники, веками соревновавшиеся в изобретательности и развитии."
    pause 0.5

    narrator_slow "Их противостояние было источником вдохновения, но однажды всё изменилось."
    pause 1.0

    show intro1 at Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(1.0)

    narrator_normal "После долгих лет борьбы один город уступил, и казалось, что наступил мир."
    pause 0.3

    narrator_normal "Но вместе с этим пришла новая беда: в проигравшем городе началась экологическая катастрофа." 
    pause 0.5

    show intro1 with vpunch
    play sound "audio/industrial_noise.ogg" volume 0.5

    narrator_normal "Заводы, спешно построенные ради экономического рывка, перестали заботиться о реке."
    pause 0.3

    transform darken:
        linear 3.0 matrixcolor BrightnessMatrix(-0.1) * ContrastMatrix(1.1)

    show intro1 at darken

    narrator_normal "Вода потемнела, рыба исчезла, а жители всё чаще стали болеть." 
    pause 1.0

    $ renpy.music.set_volume(0.6, delay=2.0, channel='music')

    narrator_dramatic "Теперь судьба города — и самой реки — в твоих руках." 
    pause 0.5

    narrator_normal "Ты — новый руководитель, которому предстоит сделать трудный выбор:" 
    pause 0.2

    narrator_normal "Cпасти людей здесь и сейчас или заложить фундамент для будущего, в котором река вновь станет живой."
    pause 1.0

    narrator_dramatic "Твои решения определят, каким будет этот город завтра."
    pause 1.0

    transform center_text:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        linear 0.5 zoom 1.05
        linear 0.5 zoom 1.0

    if _preferences.language == "english":
        $ display_text = english_text
    else:
        $ display_text = russian_text
        
    show text display_text at center_text with dissolve
    pause 3.0
    hide text with dissolve

    stop sound fadeout 3.0
    stop music fadeout 3.0

    scene black with Dissolve(2.0)
    pause 1.0

    scene black with fade
    play sound "audio/pen_writing.ogg"

    python:
        prompt_text = _("Как тебя зовут?")  # The _() function marks text for translation
        name = renpy.input(prompt_text, length=20)
        name = name.strip() or _("Георгий")
        default_welcome = _("Добро пожаловать. Твоё путешествие начинается...")
        renpy.say(None, default_welcome)
        budget = 10000
        rating = 0
        environment = 0
        day = 1
        renpy.retain_after_load()

label day1_start:
    hide intro1
    show intro2
    with dissolve
    play music "ost/ambient_1.ogg" volume 0.6 fadeout 2.0 fadein 2.0 loop

    show g say

    g "Георгий... Это имя всегда было со мной, как и мечта."
    g "{cps=50}С самого детства я грезил футболом — не славой или деньгами, а самой игрой. Чистым азартом и командным духом.{/cps}"

    hide g say
    with fade

    "Родители" "Да что тебе этот футбол даст? На танцах куда безопаснее!"
    "Родители" "И девушку себе, может, наконец найдёшь. Пора уже думать о будущем."

    show g talk
    with dissolve

    g "{cps=25}Но мое сердце принадлежало полю.{/cps}"

    hide g talk
    hide intro2
    with dissolve
    show field
    show g sad

    g "{cps=20}Футбол — это моя жизнь.{/cps} {i}(с тоской смотрит вдаль){/i}"
    g "Я обожаю бегать по полю, вдыхая ароматы распустившихся цветов. Чувствовать, как мир замирает, когда мяч летит в ворота."
    g "Общаться с товарищами, разделять победы и поражения. Мечтать о том, как когда-нибудь выйду на большую арену."

    hide g sad
    hide field
    with fade
    show intro2
    show g talk

    g "{cps=30}Но мои слова всегда понимали не так.{/cps}"
    g "Стремление к честной игре восприняли как желание вершить справедливость. Мою любовь к командным стратегиям — как политические амбиции."
    g "{cps=25}Мою страсть к дискуссиям на поле — как задатки юриста.{/cps}"

    show g sad

    narrator_dramatic "В итоге: я окончил университет, получил диплом, но потерял что-то важное."
    g "Пока я учился, город менялся. Футбольное поле моего детства отдали под очередной завод."
    g "{cps=15}Весь город постепенно превратился в декорации к фильму о киберпанке — трубы, смог, бетон.{/cps}"

    hide g sad
    with dissolve

    "Ведущий Новостей" "{cps=70}Будущее уже наступило!{/cps} {i}(громко, с фальшивым энтузиазмом){/i}"
    "Ведущий Новостей" "{cps=60}Наш город станет центром технологий будущего!{/cps}"
    "Ведущий Новостей" "Уже сейчас мы занимаем первое место по производству микрочипов!"
    "Ведущий Новостей" "{cps=55}Мы обещаем, что за следующие 8 лет качество вашей жизни вырастет на 40 процентов!{/cps} {i}(показывает диаграмму роста){/i}"

    show g talk
    with dissolve

    g "{cps=25}А у меня душа болела за родной город. За реку, которая становилась всё темнее. За воздух, которым становилось всё труднее дышать.{/cps}"
    g "Я чувствовал, что эта гонка за прогрессом любой ценой до добра не доведёт."
    g "{cps=20}И, похоже, оказался прав.{/cps}"
    g "{cps=25}История повторяется, но теперь ставки куда выше — речь идёт не о технологической гонке, а о самом выживании города.{/cps}"

    hide g talk
    show g sad

    g "{cps=20}Недавно выборы изменили всё: новым депутатом стал... я.{/cps}"
    g "И пусть я ещё не выучил наизусть все коридоры власти, одно знаю точно — настало время действовать."

    hide g sad

    narrator_dramatic "Первый рабочий день начинается."

    show a happy at left
    with dissolve

    a "Георгий Николаевич, поздравляю с назначением! Я — Настя, ваш помощник. Мы оба здесь новенькие."

    hide a happy
    show a sad at left
    with dissolve

    a "{cps=20}Город действительно ждёт перемен...{/cps} {i}(понижает голос){/i} {cps=15}особенно с водой. Ситуация становится критической.{/cps}"

    hide a sad
    show a happy at left
    with dissolve

    a "Сегодня к вам записаны жители с жалобами, а министр экологии настаивает на срочной встрече."

    stop music fadeout 1.0

    play music "ost/phone.ogg" volume 0.1
    "{i}Телефон разрывается от звонка.{/i}"
    stop music fadeout 1.0

    play music "ost/ambient_1.ogg" volume 0.6 fadeout 2.0 fadein 2.0 loop

    hide a happy
    with dissolve

    show phone at right
    with dissolve

    p "{cps=55}Здравствуйте, Георгий Скороденок. Понимаю, вы только вступили в должность, но времени на раскачку нет — у нас чрезвычайная ситуация.{/cps}"
    p "Простите, забыл представиться. Павел Ветров, Министерство контроля экологии."

    show a stand at left

    p "Вчера вечером наша лаборатория зафиксировала опасное превышение нитратов и пестицидов в воде."
    p "Источник загрязнения — новые фермерские хозяйства, использующие агрессивные химикаты без надлежащего контроля."
    p "Многие из них расположены прямо у реки, и отходы попадают в воду напрямую, без какой-либо очистки."

    hide a stand
    show a sad at left

    p "{cps=30}Вода по анализам признана непригодной не только для питья, но даже для бытового использования.{/cps}"
    p "{cps=25}Уже зарегистрированы случаи отравления — проблемы с кожей, желудком, есть подозрения на массовое отравление.{/cps}"
    p "Мы вынуждены ввести карантин в двух районах — жителям запрещено набирать воду из-под крана. Организована доставка бутилированной, но запасов хватит максимум на три дня."

    hide a sad
    show a think at left

    p "{cps=50}Экологи уже выезжали на место. Люди в ярости, и я их понимаю.{/cps}"
    p "Корень проблемы — отсутствие очистных сооружений и бесконтрольное использование пестицидов."
    p "Вот ваши первоочередные задачи:"
    p "Первое — провести встречи с фермерами и выяснить, какие конкретно препараты они используют."
    p "Второе — проверить отчёты предприятий по фильтрации и утилизации отходов."
    p "Третье — решить, кого штрафовать, кого обязать установить очистные сооружения, а где действовать экстренно — отправлять специальные бригады для очистки воды."

    hide a think
    show a happy at center

    p "{cps=40}У вас три дня, Георгий. Ситуация накаляется с каждым часом.{/cps}"

    hide phone
    show g talk at left
    with dissolve

    g "{cps=45}Понял вас. Начинаем работать немедленно. До связи.{/cps}"

    hide g talk
    hide a happy
    narrator_normal "{i}Звонок заканчивается.{/i}"

    show a stand at left
    with dissolve

    a "Георгий, вчера мне писала Анна Петровна по поводу массовой гибели рыбы в реке. {i}(смотрит вопросительно){/i} {cps=20}С чего начнём?{/cps}"

    stop music fadeout 2.0

label day1_morning:
    play music "ost/morning.ogg" volume 0.5 fadein 2.0 loop
    scene office_morning with fade
    $ formatted_budget = "{:,}".format(budget)
    narrator_normal "Текущий бюджет: [formatted_budget] $"
    narrator_normal "Бюджет позволяет вам улучшать город, но учтите, что он не резиновый."
    jump case_babushka

label case_babushka:
    scene office_morning with fade
    show grandma at left

    narrator_normal "Дверь в кабинет с шумом распахивается. Входит Анна Петровна — невысокая, но бойкая бабушка, крепко сжимающая в руках большую чёрную сковородку."
    narrator_normal "Она оглядывается по сторонам, тяжело вздыхает и решительно направляется к столу."
    b "Здравствуй, Георгий!"
    g "Здравствуйте, Анна Петровна. Присаживайтесь, пожалуйста. Что случилось?"
    narrator_normal "Бабушка ставит сковородку на стол так, что та глухо звякает по дереву."
    b "Ой, сынок, слушай! Рыбу жарю — сковородка вся в налёте, а рыба пахнет какой-то дрянью! Всю жизнь ловлю в нашей реке, а теперь и есть страшно. Это сковородка плохая или вода у нас совсем испортилась?"

label case_babushka_questions0:
    menu:
        "Спросить, когда начались проблемы":
            b "Да вот недели две как. Соседка тоже жалуется, у неё руки после мытья чешутся."
            jump case_babushka_questions0
        "Спросить, где ловит рыбу":
            b "Да прямо у моста, как всегда. Там теперь ещё и пена какая-то по утрам."
            jump case_babushka_questions0
        "Спросить, кто ещё жалуется":
            b "Да все жалуются! Только никто ничего не делает."
            jump case_babushka_questions0
        "Поинтерисоваться об ее жизни":
            jump case_babushka_questions1
        "Перейти к действиям":
            jump case_babushka_menu

label case_babushka_questions1:
    menu:
        "Спросить, есть ли у неё семья":
            b "Внучка у меня, Аленка, живёт со мной. Она тоже жалуется — говорит, после душа кожа чешется."
            jump case_babushka_questions1
        "Спросить, как давно она ловит рыбу":
            b "С детства, сынок. Всю жизнь тут живу, никогда такого не было."
            jump case_babushka_questions1
        "Спросить, что думает о причинах":
            b "Да кто ж его знает... Может, завод опять что-то слил, или фермеры свои химикаты льют. А может, трубы старые."
            jump case_babushka_questions1
        "Перейти к действиям":
            jump case_babushka_menu

label case_babushka_questions2:
    menu:
        "Спросить, замечала ли что-то необычное на реке":
            b "Пару раз видела, как ночью у завода свет горит, и вода у берега тёмная. А ещё — дохлая рыба всплывала."
            jump case_babushka_questions2
        "Спросить, как чувствует себя внучка":
            b "Аленка кашляет, говорит, горло першит. Я ей чай завариваю, но всё равно тревожно."
            jump case_babushka_questions2
        "Перейти к действиям":
            jump case_babushka_menu

label case_babushka_menu:
    menu:
        "Отправить анализ рыбы и воды (300$)":
            if budget >= 300:
                $ budget -= 300
                $ rating += 2
                b "Спасибо, сынок! Хоть кто-то слушает."
                "Оставшийся бюджет: [budget]"
                jump case_babushka_action
            else:
                "У вас не хватает средств на анализы."
                "Оставшийся бюджет: [budget]"
                jump case_babushka_menu
        "Вызвать санитарного врача на дом (200$)":
            if budget >= 200:
                $ budget -= 200
                $ rating += 1
                b "Спасибо, милок! Может, хоть врач разберётся."
                "Оставшийся бюджет: [budget]"
                jump case_babushka_action
            else:
                "У вас не хватает средств на врача."
                "Оставшийся бюджет: [budget]"
                jump case_babushka_menu
        "Порекомендовать фильтр для воды (50$)":
            if budget >= 50:
                $ budget -= 50
                $ rating -= 1
                b "Фильтр? А рыбу как фильтровать? Эх, молодёжь..."
                "Оставшийся бюджет: [budget]"
                jump case_babushka_action
            else:
                "У вас не хватает средств даже на фильтр."
                "Оставшийся бюджет: [budget]"
                jump case_babushka_menu
        "Пожать плечами":
            $ rating -= 2
            b "Вот так всегда... Никому мы не нужны."
            jump case_babushka_action

label case_babushka_action:
    a "Георгий, как поступим дальше?"
    menu:
        "Лично поехать на место и осмотреть реку":
            scene river_day with fade
            "Вы приезжаете к реке. На поверхности воды действительно видна пена, а у берега плавает дохлая рыба."
            "Вы замечаете, что у трубы завода вода мутная и пахнет химией."
            a "Похоже, дело серьёзное. Нужно срочно что-то делать."
            jump case_day1_ending
        "Поручить помощнику собрать информацию":
            a "Я всё выясню и доложу вам к вечеру."
            jump case_day1_ending
        "Оставить всё как есть":
            a "Может, само рассосётся... Но жители будут недовольны."
            $ rating -= 1
            jump case_day1_ending

label case_day1_ending:
    hide grandma
    scene office_night with fade
    a "День окончен. Сегодня вы занимались только жалобой бабушки Анны Петровны."
    narrator_normal "Рейтинг среди жителей: [rating]."
    narrator_normal "Оставшийся бюджет: [budget]"
    play music "ost/night.ogg" volume 0.3 fadein 2.0 loop
    g "Надеюсь, завтра будет легче..."
    narrator_normal "{i}Георгий ложится спать, но тревожные мысли не дают уснуть...{/i}"
    jump day2_intro