import pygame

WIDTH = 1000
HEIGHT = 600

window = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("background.png")

background = pygame.transform.scale(
                                pygame.image.load("background.png"),
                                (WIDTH,HEIGHT)
            )

clock = pygame.time.Clock()



sprite1 = pygame.transform.scale(
                            pygame.image.load("sprite1.png"),
                            (120,110)
)
sprite2 = pygame.transform.scale(
                            pygame.image.load("sprite2.png"),
                            (120,110)
)

x1, y1 = 10, 10

x2, y2 = 500, 500

sprite1_rect = pygame.Rect((x1,y1), (120,110))
sprite2_rect = pygame.Rect((x2,y2), (120,110))


def fade():
        fade_image = pygame.image.load("victory.png").convert()
        fade_image = pygame.transform.scale(fade_image, (WIDTH, HEIGHT))
        
        for alpha in range(0, 255, 5):
            fade_image.set_alpha(alpha)
            window.blit(fade_image, (0, 0))
            pygame.display.update()
            pygame.time.delay(30)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(background, (0,0))
    pygame.draw.rect(window, (225,0,0), sprite1_rect)
    pygame.draw.rect(window, (225,0,0), sprite2_rect)
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    sprite1_rect.x = x1
    sprite1_rect.y = y1

    sprite2_rect.x = x2
    sprite2_rect.y = y2

    if sprite1_rect.colliderect(sprite2_rect):
        fade()
        print("collied")
        game = False




    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y1 >= 0:
        y1 -= 5
    if keys[pygame.K_DOWN] and y1 <= 490:
        y1 += 5
    if keys[pygame.K_LEFT] and x1 >= 0:
        x1 -= 5
    if keys[pygame.K_RIGHT] and x1 <= 880:
        x1 += 5

    if keys[pygame.K_w] and y2 >= 0:
        y2 -= 5
    if keys[pygame.K_s] and y2 <= 490:
        y2 += 5
    if keys[pygame.K_a] and x2 >= 0:
        x2 -= 5
    if keys[pygame.K_d] and x2 <= 880:
        x2 += 5



    pygame.display.update()
    clock.tick()





