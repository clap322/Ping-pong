from pygame import *
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
#конструктор класса
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #вызываем конструктор класса (Sprite):
      sprite.Sprite.__init__(self)
      #каждый спрайт должен хранить свойство image - изображение
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_a] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_d] and self.rect.x < win_width - 80:
           self.rect.x += self.speed



back = (200, 255, 255)
win_width=600
win_height=500
window=display.set_mode((win_width, win_height))
window.fill(back)
game=True
finish=False
clock=time.Clock()
FPS=60

while game:
    for e in event.get():
        if e.type==QUIT :
            game=False
        if finish != True:
            window.fill(back)
        display.update()
        clock.tick(FPS)