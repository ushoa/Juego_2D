import sys, pygame

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


class Sprite(pygame.sprite.Sprite):
    def __init__(self,hoja,tiles,position):
        super().__init__()
        self.sheet = pygame.image.load(f"./app/sprites/{hoja}.png")
        self.sheet.set_clip(pygame.Rect(tiles['X'], tiles['Y'], tiles['WIDTH'], tiles['HEIGHT']))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        #self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.left_states = { 0: (18,78,46,47), 1: (82,79,28,46), 2: (146,78,28,46), 3: (210,78,28,47), 4: (,,,), 5: (,,,), 6: (,,,), 7: (,,,), 8: (,,,) }
        self.right_states = {0:(,,,),1:(,,,),2:(,,,),3:(,,,),4:(,,,),5:(,,,),6:(,,,),7:(,,,),8:(,,,)}
        self.up_states = { 0: (17,13,30,47), 1: (81,13,30,47), 2: (145,13,30,48), 3: (209,13,30,49), 4: (273,13,29,48), 5: (337,13,29,47), 6: (401,13,29,49), 7: (466,13,28,50), 8: (529,13,29,48) }
        self.down_states = {0:(,,,),1:(,,,),2:(,,,),3:(,,,),4:(,,,),5:(,,,),6:(,,,),7:(,,,),8:(,,,)}
 
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
 
    def handle_event(self, event): 
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_LEFT:
                self.update('stand_left')            
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
