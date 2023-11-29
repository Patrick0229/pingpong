from pygame import *

clock = time.Clock()
FPS = 60
clock.tick(FPS)

window = display.set_mode((700, 500))
display.set_caption("pingpong")

background = transform.scale(
    image.load("background.png"), (700, 500))

rocket1 = transform.scale(
    image.load('racket.png'),
    (100, 100)
)

window.blit(rocket1, (x1, y1))

rocket2 = transform.scale(
    image.load('racket.png'),
    (100, 100)

game = True
while game:
    window.blit(background,(0, 0))

for e in event.get():
    if e.tipe == QUIT:
        game = False

p_x = 0
p_y = 0
p_speed = 10
p_image = "rocket.png"
lost = 0
text_lose = font2.render("Missed: " + str(lost), 1, (255, 255, 255))

class player(Gamesprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP]:
            self.rect.x -= 10
        if key_pressed[K_DOWN]:
            self.rect.y += 10


rocket1 = transform.scale(
    image.load('racket.png'),
    (100, 100)
)

window.blit(rocket1, (x1, y1))

rocket2 = transform.scale(
    image.load('racket.png'),
    (100, 100)
)

window.blit(rocket2, (x1, y1))

keys_pressed = key.get_pressed()
#player 1
if keys_pressed(K_UP):
    y1 -= 10

if keys_pressed(K_DOWN):
    y1 += 10

#player 2
if keys_pressed(K_W):
    y1 -= 10

if keys_pressed(K_S):
    y1 += 10

events = event.get()
events[0].try:
    pass
except expression as identifier:
    pass

display.update()