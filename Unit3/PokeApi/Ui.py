import pygame
import PokeApi
from threading import Thread

path = "".join(x+"/" for x in __file__.split("/")[:-1])

#Circle points
_circle_cache = {}
def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points

#Text render
def render(text, font, gfcolor=pygame.Color(0,0,0), ocolor=(255, 255, 255), opx=2):
    textsurface = font.render(text, True, gfcolor).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf

#Points the real path of the whole thing 
def GetPath(name):
    return path+"/"+name


white = (255, 255, 255)
red = (225, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

#name
textx, texty = (249, 800)

#number
text1x, text1y = (83, 129)

#stats
text2x, text2y = (140, 270)

#muted
text3x, text3y = (420, 270)


# Initialize Pygame and set up the window
pygame.display.set_caption('Pokedex')
pygame.mixer.init()  # Initialize the pygame mixer for audio
pygame.init()

# Set up the screen and fonts
screen = pygame.display.set_mode([498, 909])

font = pygame.font.Font(GetPath('pokemon.ttf'), 62)
font1 = pygame.font.Font(GetPath('pokemon.ttf'), 50)
font2 = pygame.font.Font(GetPath('pokemon.ttf'), 32)
font3 = pygame.font.Font(GetPath('pokemon.ttf'), 32)
text3 = font3.render("", True, black, white)
textRect3 = text3.get_rect()
textRect3.center = (text3x, text3y)

bg = pygame.image.load(GetPath("images.png"))
bg = pygame.transform.rotozoom(bg, 0, 3)

# called to update the Ui at any time then takes a screenshot
def UpdateUI():
    name, height, weight, filename, number =  PokeApi.Stats["forms"][0]["name"],PokeApi.Stats["height"],PokeApi.Stats["weight"],GetPath("pokemon_image.png"),PokeApi.Stats["id"]

    # Update text and image
    text = font.render(name, True, black)
    textRect = text.get_rect()
    textRect.center = (textx, texty)

    # Id number
    number_str = f"#{number}"
    text1 = font1.render(number_str, True, black)
    textRect1 = text1.get_rect()
    textRect1.center = (text1x, text1y)

    #Height and weight iof pokemon
    string = f"{height} | {str(int((weight / 10 * 2.205) + .5))} lbs"
    text2 = render(string, font2, gfcolor=black, ocolor=(255, 255, 255), opx=2)
    textRect2 = text2.get_rect()
    textRect2.center = (text2x, text2y)

    imp = pygame.image.load(filename).convert_alpha()
    imp = pygame.transform.scale(imp, (500, 500))

    #Screen update and saves the window image
    screen.fill(white)
    screen.blit(bg, (0, 0))
    screen.blit(imp, (0, 270))
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    pygame.display.flip()
    pygame.image.save( screen, GetPath("PokedexWindow.png") )


number = 1
PokeApi.GetPokemonInfo(number)
UpdateUI()

# For left and right functionality
def thread():
    global number
    play = True
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    number += 1
                    if number == 152:
                        number = 1

                    PokeApi.GetPokemonInfo(number)
                    UpdateUI()


                if event.key == pygame.K_LEFT:
                    number -= 1  # increment the number correctly
                    if number == 0:
                        number = 151
                    PokeApi.GetPokemonInfo(number)
                    UpdateUI()

    pygame.quit()


Thread(target=thread).start()