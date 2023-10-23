import pygame
import time

pygame.init()

screen_dimensions = (1920, 1080)
screen = pygame.display.set_mode(screen_dimensions)
clock = pygame.time.Clock()

sitka_small_font = pygame.font.Font("C:\\Users\willi\\Downloads\\OnlineWebFonts_COM_58b5136392213ec2c2c5218efd9c4ad8\\Sitka Small\\Sitka Small.ttf", 11)
#other_font = pygame.font.SysFont("minuscule", 10)
number_font = sitka_small_font

white = (255, 255, 255)
black = (0, 0, 0)

fps_cap = False

#Set to (0, 0) to remove it from screen
start_number_coords = (0, 0)

class Text(pygame.sprite.Sprite):
    def __init__(self, number):
        super().__init__()

        self.number = number

        self.image = pygame.transform.rotate(number_font.render(self.number, False, black), 45)

        self.rect = self.image.get_rect()
    
    def draw(self):
        self.rect.center = find_spot(self)
        print("Found spot!", self.rect.center)
        
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, black, self.rect, 1)
        #time.sleep(0.5)

def find_spot(sprite):
    global rows_y
    global rows_x
    global mode
    current_sprite = sprite
    current_sprite.rect.center = last_number.rect.center
    last_sprite = last_number
    screen_rect = screen.get_rect()

    found = False

    collision = True
    on_screen = screen_rect.contains(current_sprite.rect)

    #print(id(current_sprite.rect), id(last_sprite.rect))

    while not found:
        #time.sleep(0.5)

        if not collision and on_screen:
            found = True
            break

        #print(collision, on_screen)
        collision = current_sprite.rect.colliderect(last_sprite.rect)
        
        if collision:
            #print("Moving from collision!")
            #print(current_sprite.rect.center, last_sprite.rect.center)
            current_sprite.rect.centerx += 13.25
            current_sprite.rect.centery -= 17

            #print(current_sprite.rect.center, last_sprite.rect.center, sprite.number, current_sprite.rect, last_sprite.rect, rows_y)
        
        on_screen = screen_rect.contains(current_sprite.rect)
        #print(current_sprite.rect)

        if not on_screen:
            #print("Moving back to screen!")
            #print(current_sprite.rect.center, last_sprite.rect.center)
            if mode == Y:
                current_sprite.rect.centerx = 45
                current_sprite.rect.centery = 50 + (39*rows_y)

                rows_y += 1

                if not screen_rect.contains(current_sprite.rect):
                    #print(current_sprite.rect.center, last_sprite.rect.center)
                    #print(current_sprite.rect, screen_rect)
                    #print("End of row 'Y' reached. Switching to row 'X'")
                    #time.sleep(20)
                    mode = X

                    current_sprite.rect.centerx = 67
                    current_sprite.rect.centery = screen_dimensions[1] - 53

                    rows_x = 1
                    #print(current_sprite.rect.center, last_sprite.rect.center)
                    
            else:
                current_sprite.rect.centerx = 67 + (29.5*rows_x)
                current_sprite.rect.centery = screen_dimensions[1] - 53
                rows_x += 1
                #print(current_sprite.rect.center, last_sprite.rect.center)
            
            #print(current_sprite.rect.center, last_sprite.rect.center, sprite.number, current_sprite.rect, last_sprite.rect, rows_y)
            #print(current_sprite.rect.colliderect(last_sprite.rect))

        #print(current_sprite.rect, last_sprite.rect)

    return current_sprite.rect.center


number_group = pygame.sprite.Group()

start_number = Text("Start")
start_number.rect.centerx = start_number_coords[0]
start_number.rect.centery = start_number_coords[1]

last_number = start_number

rows_y = 0
rows_x = 0

Y = 107
X = 108

mode = Y

with open("numbers.txt", "r") as file:
    screen.fill(white)
    screen.blit(start_number.image, start_number.rect)

    number_group.add(start_number)

    run = True
    while run:
        if fps_cap:
            clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        try:
            new_number = Text(next(file).replace("\n", ""))
            new_number.draw()

            number_group.add(new_number)

            last_number = new_number

            pygame.display.flip()
            if new_number.number == "åttahundrafemtiosju":
                raise StopIteration
        except StopIteration as stop:
            print("Drawing done!")
            time.sleep(30)


pygame.quit()
exit()