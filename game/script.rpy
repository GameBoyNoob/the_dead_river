# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define g = Character('Георгий', color="#b4befe")
define p = Character('Министр', color="#cba6f7")
define a = Character('Настя', color="#f38ba8")
define b = Character('Бабушка')
define f = Character('Фермер')
define m = Character('Молодая мама')
define audio.g_voice1 = "audio/voice/g_voice1.opus"
image city = "bg/city.png"
image fun = "bg/fun.png"
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    jump day1_intro
return