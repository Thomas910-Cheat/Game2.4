import pygame, random, os

class Settings(object):
    #Normale Fenster Settings:
    width = 700
    height = 400
    imagewidth = 50
    imageheight = 50
    fps = 60       
    title = "Bubbles_Game_Kolebski" 
    bordersize = 20

    #Dateien-Standorte:
    file_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(file_path, "Image_Data")
    audio_path = os.path.join(file_path, "Audio_Data")
    
    #Farben:
    Black = (0,0,0)
    White = (255,255,255)
    Red = (255,0,0)
    Green = (0,255,0)
    Blue = (0,0,255)
    @staticmethod
    def get_dim():
        return (Settings.width, Settings.height)

class Bubble(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_orig = pygame.image.load(os.path.join(Settings.image_path, "bubble.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image_orig, (Settings.imagewidth, Settings.imageheight))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, Settings.width - self.rect.width)
        self.rect.top = random.randint(0, Settings.height - self.rect.height)
        self.speed = 1

    def update(self):
        c = self.rect.center
        self.rect.width += self.speed
        self.rect.height += self.speed
        self.image = pygame.transform.scale(self.image_orig, (self.rect.width, self.rect.height)) 
        self.rect.center = c

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(Settings.get_dim())
        pygame.display.set_caption(Settings.title)
        self.background = pygame.image.load(os.path.join(Settings.image_path, "brick_wall.png")).convert()
        self.background = pygame.transform.scale(self.background, (Settings.width, Settings.height))
        self.background_rect = self.background.get_rect()
        self.clock = pygame.time.Clock()
        self.done = False
        self.all_Bubbles = pygame.sprite.Group()
         

    def run(self):
        while not self.done:               
            self.clock.tick(Settings.fps)             
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:   
                    self.done = True  
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
            self.update()
            self.draw()
            self.change_difficulty()
            

    def update(self):
        self.all_Bubbles.update()
        if len(self.all_Bubbles) < 21:
            self.all_Bubbles.add(Bubble())

    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.all_Bubbles.draw(self.screen)
        pygame.display.flip()

    def change_difficulty(self):   
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                                    #Ein vergeblicher Versuch eine Ausgabe in der Konsole zu erzeugen
                if event.type == pygame.K_1:
                    print("Schwierigkeit auf EASY gesetzt!")
                elif event.type == pygame.K_2:
                    print("Schwierigkeit auf NORMAL gesetzt!")

if __name__ == '__main__':      
                                    
    pygame.init()               
    game = Game()
    game.run()
    pygame.quit()
