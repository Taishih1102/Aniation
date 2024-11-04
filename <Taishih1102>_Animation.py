import pygame
import math  # Add this for trigonometric functions

pygame.init()
screen = pygame.display.set_mode((640,480))

class Susie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        #Set up the image
        self.image = pygame.image.load("Sussane.png")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (75,150))
        
        #create the corresponding rect
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 240
        
        #create the ability to move
        self.dx = 5
        self.dy = 5
        self.speed = 5
        
        # Set angle (30 degrees) and calculate movement components
        self.angle = 30  # degrees
        self.angle_rad = math.radians(self.angle)  # convert to radians
        self.d1 = self.speed * math.cos(self.angle_rad)  # x component
        self.d2 = -self.speed * math.sin(self.angle_rad)  # y component (negative because pygame y increases downward)
        
        # Add this to track which update method to use
        self.current_state = 1
    
    def update(self):
        if self.current_state == 1:
            self.update1()
        elif self.current_state == 2:
            self.update2()
        elif self.current_state == 3:
            self.update3()
        elif self.current_state == 4:
            self.update4()
        elif self.current_state == 5:
            self.update5()
        
    def update1(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.current_state = 2
            
    def update2(self):
        self.rect.centerx -= self.dx
        if self.rect.left < 0:
            self.current_state = 3
            
    def update3(self):
        self.rect.centery += self.dy
        if self.rect.bottom > screen.get_height():
            self.current_state = 4
            
    def update4(self):
        self.rect.centery -= self.dy
        if self.rect.top < 0:
            self.current_state = 5  # Fixed to set state instead of calling directly
            
    def update5(self):
        # Move in the specified angle direction
        self.rect.centerx += self.d1
        self.rect.centery += self.d2
        
        # Bounce off walls while maintaining angle
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
            self.d1 = -self.d1  # Reverse x direction
        if self.rect.left < 0:
            self.rect.left = 0
            self.d1 = -self.d1  # Reverse x direction
        if self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()
            self.d2 = -self.d2  # Reverse y direction
        if self.rect.top < 0:
            self.rect.top = 0
            self.d2 = -self.d2  # Reverse y direction

def main():
    pygame.display.set_caption("Susie<3<3<3")
    background = pygame.image.load("heart.jpg")
    background = background.convert_alpha()
    background = pygame.transform.scale(background,(640,480))
    screen.blit(background,(0,0))
    
    sussane = Susie()
    allSprites = pygame.sprite.Group(sussane)
    clock = pygame.time.Clock()
    keepGoing = True
    
    while keepGoing:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()