import sys, pygame
import random

class Tiles(pygame.sprite.Sprite):
    def __init__(self,hoja,tiles):
        super().__init__()
        self.hoja=pygame.image.load(f"./app/sprites/{hoja}.png")
        self.hoja.set_clip(pygame.Rect(tiles['X'], tiles['Y'], tiles['WIDTH'], tiles['HEIGHT']))
        self.image=self.hoja.subsurface(self.hoja.get_clip())
        self.rect=self.image.get_rect()

    def update(self,x,y):
        self.rect.x+=x
        self.rect.y+=y


class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,5,5)

    def update(self):
        self.left,self.top=pygame.mouse.get_pos()


class Panel(pygame.Surface):
    def __init__(self,whidth,height,x,y,color):
        super().__init__((whidth,height))
        self.width=whidth
        self.height=height
        self.x=x
        self.y=y
        self.color=color

        self.panel=pygame.Surface((self.width,self.height))
        self.rect=self.panel.get_rect(topleft=(self.x,self.y))

    def getPanel(self):
        return self.panel

    def dibujarPanel(self,stage):
        stage.blit(self.panel,(self.x,self.y))
        self.panel.fill(self.color)


class Botones(pygame.Rect):
    def __init__(self,texto,stage,x,y):
        self.stage=stage
        self.x=x
        self.y=y
        self.color=(0,95,136)
        self.ancho=150
        self.alto=40
        
        pygame.Rect.__init__(self,self.x,self.y,self.ancho,self.alto)

        self.fuente=pygame.font.SysFont('',25)
        self.texto=self.fuente.render(texto,True,(255,255,255))
        
        self.rectangulo=pygame.Rect(self.stage.rect.x+self.x,self.stage.rect.y+self.y,self.ancho,self.alto)
    
    def draw(self):
        pygame.draw.rect(self.stage.getPanel(),self.color,self)
        self.stage.getPanel().blit(self.texto,(self.x+(self.width-self.texto.get_width())/2,self.y+(self.height-self.texto.get_height())/2))
    
    def normal(self):
        self.color=(0,95,136)

    def ober(self):
        self.color=(52,128,160)

    def click(self):    
        self.color=(28,69,86)
    
    def update(self,event,cursor):
        if cursor.colliderect(self.rectangulo):
            self.ober()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                self.click()
            else:
                self.normal()
        else:
            self.normal()
    


class Sprite(pygame.sprite.Sprite):
    def __init__(self,hoja,tiles,position):
        super().__init__()
        self.sheet = pygame.image.load(f"./app/sprites/{hoja}.png")
        self.sheet.set_clip(pygame.Rect(tiles['X'], tiles['Y'], tiles['WIDTH'], tiles['HEIGHT']))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0

        self.tiempo=0
        self.distancia=0
        self.direccion=['left','right','up','down']
        self.dir='left'
        
        #self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.left_states = { 0: (18,588,46,47), 1: (82,589,28,46), 2: (146,588,28,46), 3: (210,588,28,47), 4: (274,588,29,50), 5: (338,589,30,49), 6: (402,588,29,50), 7: (466,588,29,50), 8: (530,588,29,50) }
        self.right_states = { 0: (17,716,29,50), 1: (81,717,29,43), 2: (145,716,29,49), 3: (209,716,29,49), 4: (273,716,29,50), 5: (338,717,28,49), 6: (401,716,29,50), 7: (465,716,29,50), 8: (530,716,28,50)}
        self.up_states = { 0: (17,524,30,47), 1: (81,524,30,47), 2: (145,524,30,48), 3: (209,525,30,49), 4: (273,524,29,48), 5: (337,524,29,47), 6: (401,524,29,49), 7: (466,525,28,50), 8: (529,524,29,48) }
        self.down_states = { 0: (17,651,30,51), 1: (81,651,30,51), 2: (145,651,30,52), 3: (209,652,30,49), 4: (273,651,30,52), 5: (337,651,30,51), 6: (401,651,30,52), 7: (465,652,30,51), 8: (529,651,30,52) }
 
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
       
    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 2
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 2
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 2
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 2
 
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])
 
        self.image = self.sheet.subsurface(self.sheet.get_clip())
 
    def handle_event(self):
        self.move=random.randint(0, 1)
        self.setDireccion()

        if self.move==1:
            while self.distancia<5:
                self.update(self.dir)
                self.distancia+=1
            self.distancia=0

    def setDireccion(self):
        if self.tiempo==5:
            self.dir=random.choice(self.direccion)
            self.tiempo=0
        else:
            self.tiempo+=1
        


    #original
    #def handle_event(self):
        #print(self.move,self.distancia,self.dir)

        #if event.type == pygame.KEYDOWN:
        #   
        #    if event.key == pygame.K_LEFT:
        #        self.update('left')
        #    if event.key == pygame.K_RIGHT:
        #        self.update('right')
        #    if event.key == pygame.K_UP:
        #        self.update('up')
        #    if event.key == pygame.K_DOWN:
        #        self.update('down')
 
        #if event.type == pygame.KEYUP:  

        #    if event.key == pygame.K_LEFT:
        #        self.update('stand_left')            
        #    if event.key == pygame.K_RIGHT:
        #        self.update('stand_right')
        #    if event.key == pygame.K_UP:
        #        self.update('stand_up')
        #    if event.key == pygame.K_DOWN:
        #        self.update('stand_down')
        
