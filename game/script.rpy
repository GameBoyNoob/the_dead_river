# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# Character definitions with CPS settings
define g = Character('Георгий', color="#b4befe", what_slow_cps=30) # Normal typing speed
define p = Character('Министр', color="#cba6f7", what_slow_cps=40) # Faster for official talk
define a = Character('Настя', color="#f38ba8", what_slow_cps=25) # Slightly slower
define narrator_dramatic = Character(None, what_slow_cps=15, what_italic=True) # Very slow for dramatic moments
define b = Character('Бабушка', color="#f5c2e7", what_slow_cps=22) # Slower for elderly character
define f = Character('Фермер', color="#89b4fa", what_slow_cps=28) # Steady, deliberate pace
define m = Character('Молодая мама', color="#fab387", what_slow_cps=32) # Medium-fast for busy mother
define s = Character('Ученый', color="#a6e3a1", what_slow_cps=25) # Measured, thoughtful speech
define anna = Character('Анна', color="#fab387", what_slow_cps=30) # Standard speaking pace
define d = Character('Депутат', color="#f9e2af", what_slow_cps=35) # Quick, official speech
define biz = Character('Бизнесмен', color="#f5c2e7", what_slow_cps=38) # Fast-talking businessman
define boy = Character('Мальчишка', color="#89dceb", what_slow_cps=40) # Excited, fast-talking child
define k1 = Character('Школьник 1', color="#f9e2af", what_slow_cps=37) # Energetic schoolchild
define k2 = Character('Школьник 2', color="#f9e2af", what_slow_cps=38) # Slightly faster schoolchild
define k3 = Character('Школьник 3', color="#f9e2af", what_slow_cps=36) # Third schoolchild
define narrator_slow = Character(None, what_slow_cps=25, what_italic=True)
define narrator_normal = Character(None, what_slow_cps=40)
define narrator_dramatic = Character(None, what_slow_cps=30, what_bold=True)
define pensioner = Character('Пенсионер')
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