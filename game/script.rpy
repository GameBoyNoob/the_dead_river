# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# Character definitions with CPS settings
## Catppuccin character color definitions
# Core Catppuccin Mocha colors
define catppuccin_rosewater = "#f5e0dc"
define catppuccin_flamingo = "#f2cdcd"
define catppuccin_pink = "#f5c2e7"
define catppuccin_mauve = "#cba6f7"
define catppuccin_red = "#f38ba8"
define catppuccin_maroon = "#eba0ac"
define catppuccin_peach = "#fab387"
define catppuccin_yellow = "#f9e2af"
define catppuccin_green = "#a6e3a1"
define catppuccin_teal = "#94e2d5"
define catppuccin_sky = "#89dceb"
define catppuccin_sapphire = "#74c7ec"
define catppuccin_blue = "#89b4fa"
define catppuccin_lavender = "#b4befe"
define catppuccin_text = "#cdd6f4"

# Character definitions with Catppuccin colors
define g = Character('Георгий', color=catppuccin_lavender, what_slow_cps=30) # Normal typing speed
define p = Character('Министр', color=catppuccin_mauve, what_slow_cps=40) # Faster for official talk
define a = Character('Настя', color=catppuccin_red, what_slow_cps=25) # Slightly slower
define b = Character('Бабушка', color=catppuccin_pink, what_slow_cps=22) # Slower for elderly character
define f = Character('Фермер', color=catppuccin_blue, what_slow_cps=28) # Steady, deliberate pace
define m = Character('Молодая мама', color=catppuccin_peach, what_slow_cps=32) # Medium-fast for busy mother
define s = Character('Ученый', color=catppuccin_green, what_slow_cps=25) # Measured, thoughtful speech
define anna = Character('Анна', color=catppuccin_flamingo, what_slow_cps=30) # Standard speaking pace
define d = Character('Депутат', color=catppuccin_yellow, what_slow_cps=35) # Quick, official speech
define biz = Character('Бизнесмен', color=catppuccin_sapphire, what_slow_cps=38) # Fast-talking businessman
define boy = Character('Мальчишка', color=catppuccin_sky, what_slow_cps=40) # Excited, fast-talking child
define k1 = Character('Школьник 1', color=catppuccin_yellow, what_slow_cps=37) # Energetic schoolchild
define k2 = Character('Школьник 2', color=catppuccin_rosewater, what_slow_cps=38) # Slightly faster schoolchild
define k3 = Character('Школьник 3', color=catppuccin_maroon, what_slow_cps=36) # Third schoolchild
define pensioner = Character('Пенсионер', color=catppuccin_teal, what_slow_cps=20) # Slower for elderly character

# Narrator variations
define narrator_slow = Character(None, what_slow_cps=25, what_italic=True)
define narrator_normal = Character(None, what_slow_cps=40)
define narrator_dramatic = Character(None, what_slow_cps=30, what_bold=True)

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