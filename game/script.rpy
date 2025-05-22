# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define g = Character('Георгий', color="#b4befe")
define p = Character('Министр', color="#cba6f7")
define a = Character('Настя', color="#f38ba8")
define b = Character('Бабушка')
define f = Character('Фермер')
define m = Character('Молодая мама')
define s = Character('Ученый', color="#a6e3a1")
define anna = Character('Анна', color="#fab387")
define d = Character('Депутат', color="#f9e2af")
define biz = Character('Бизнесмен', color="#f5c2e7")
define boy = Character('Мальчишка', color="#89dceb")
define k1 = Character('Школьник 1', color="#f9e2af")
define k2 = Character('Школьник 2', color="#f9e2af")
define k3 = Character('Школьник 3', color="#f9e2af")
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