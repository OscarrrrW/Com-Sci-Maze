import js as p5

program_state = 'START'
start_time = 0
end_time = 0

idle_images = []
left_images = []
right_images = []
up_images = []
down_images = []

img1 = p5.loadImage('block.png') 
background1 = p5.loadImage('background1.png')
background2 = p5.loadImage('background2.png')
background3 = p5.loadImage('background3.webp')
img2 = p5.loadImage('map.png') 
font1 = p5.loadFont('font1.ttf')




for i in range (4):
  str = "idle{}.png"
  idle_images.append(p5.loadImage(str.format(i)))
  p5.image(idle_images[i],50, 50)

for i in range (4):
  str = "left{}.png"
  left_images.append(p5.loadImage(str.format(i)))
  p5.image(left_images[i],50, 50)

for i in range (4):
  str = "right{}.png"
  right_images.append(p5.loadImage(str.format(i)))
  p5.image(right_images[i],50, 50)

for i in range (4):
  str = "up{}.png"
  up_images.append(p5.loadImage(str.format(i)))
  p5.image(up_images[i],50, 50)

for i in range (4):
  str = "down{}.png"
  down_images.append(p5.loadImage(str.format(i)))
  p5.image(down_images[i],50, 50)






  
class Player:
        def __init__(self):
            self.x = 460
            self.y = 460
            self.speed = 2
            self.direction = 'STOP'
            self.idle_images = idle_images
            self.left_images = left_images
            self.right_images = right_images
            self.up_images = up_images
            self.down_images = down_images
            
            #self.idle_images = [p5.loadImage('idle{i}.png') for i in range(4)]
            #self.up_images = [p5.loadImage('up{i}.png') for i in range(4)]
            #self.down_images = [p5.loadImage('down{i}.png') for i in range(4)]
            #self.left_images = [p5.loadImage('left{i}.png') for i in range(4)]
            #self.right_images = [p5.loadImage('right{i}.png') for i in range(4)]
            self.animation_start_time = p5.millis()

        def update(self, blocks):
          if self.direction == 'UP':
              if not self.collides_with_any(blocks, 0, -self.speed):
                  self.y -= self.speed
          elif self.direction == 'DOWN':
              if not self.collides_with_any(blocks, 0, self.speed):
                  self.y += self.speed
          elif self.direction == 'LEFT':
              if not self.collides_with_any(blocks, -self.speed, 0):
                  self.x -= self.speed
          elif self.direction == 'RIGHT':
              if not self.collides_with_any(blocks, self.speed, 0):
                  self.x += self.speed

        def collides_with_any(self, blocks, dx, dy):
          for block in blocks:
              if (self.x + dx < block.x + 20 and self.x + dx + 20 > block.x and
                  self.y + dy < block.y + 20 and self.y + dy + 20 > block.y):
                  return True
          return False

        def draw(self):
            current_time = p5.millis()
            animation_frame = int((current_time - self.animation_start_time) / 250) % 4
            
            if self.direction == 'STOP':
                image = self.idle_images[animation_frame]  
            elif self.direction == 'UP':
                image = self.up_images[animation_frame]
            elif self.direction == 'DOWN':
                image = self.down_images[animation_frame]
            elif self.direction == 'LEFT':
                image = self.left_images[animation_frame]
            elif self.direction == 'RIGHT':
                image = self.right_images[animation_frame]

            p5.image(image,self.x, self.y)

player = Player()

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = img1
      

    def draw(self):
        p5.image(self.img, self.x, self.y, 20, 20)

blocks = [Block(i * 20+100, 100) for i in range(20) if i != 5] + [Block(i * 20+100, 480) for i in range(20)] + \
         [Block(100, i * 20+100) for i in range(20)] + [Block(480, i * 20+100) for i in range(20)]  + [Block(180, i * 20+100) for i in range(13)] + [Block(220, i * 20+100) for i in range(15)] + [Block(140, i * 20+140) for i in range(13)] + [Block(i * 20+140, 400) for i in range(5)] + [Block(180, i * 20+440) for i in range(2)] + [Block(460, i * 20+120) for i in range(7)] + [Block(400, i * 20+260) for i in range(11)] + [Block(420, i * 20+260) for i in range(11)] + [Block(i * 20+260, 220) for i in range(8)] + [Block(i * 20+440, 200) for i in range(1)] + [Block(260, i * 20+240) for i in range(11)] + [Block(i * 20+280, 440) for i in range(5)] + [Block(i * 20+300, 300) for i in range(5)] + [Block(300, i * 20+320) for i in range(6)]

def setup():
    p5.createCanvas(600, 600)
    p5.imageMode(p5.CENTER)
    p5.textFont(font1)
  


def draw():
  global program_state, start_time, end_time
  p5.background(50)
  


  if program_state == 'START':

      p5.image(background1, 300, 300, 600, 600)
      p5.fill(255)
      p5.textAlign(p5.CENTER, p5.CENTER)
      p5.textSize(30)
      
      if(p5.millis() % 1000 < 500): 
      
        p5.text('Press mouse to start', 300, 500)
      p5.textSize(70)
      p5.fill(240)
      p5.textStyle('BOLD')
      p5.text('PoseMo', 300, 200)
      p5.textSize(20)
      p5.fill(200)
      p5.textStyle('NORMAL')
      p5.text('An interactive Maze game Using ML5 Posenet', 300, 400)
      p5.text('Use "YMCK" to leave maze!', 300, 430)
      
    
      
  elif program_state == 'PLAY':
      p5.image(background1, 300, 300, 600, 600)
      p5.image(img2, 530, 530, 100, 110)
      p5.noStroke()
      p5.fill(0, 200, 0)
      p5.rect(90, 90, 400, 400) 
      for block in blocks:
          block.draw()
      player.update(blocks)
      player.draw()

      remaining_time = 60 - (p5.millis() - start_time) // 1000
      p5.textSize(20)
      p5.fill(255)
      p5.text(f'Time left: {remaining_time}', 100, 30)  

      if remaining_time <= 0:
          program_state = 'LOSE'
      elif p5.dist(player.x, player.y, 200, 90) < 10: 
          program_state = 'WIN'
  elif program_state == 'WIN':
      p5.image(background2, 300, 300, 600, 600)
      p5.textSize(70)
      p5.fill(0, 135, 189)
      p5.textStyle('BOLD')
      p5.text('You Win!', 300, 200)
      
      p5.fill(255)
      p5.textSize(30)
      p5.textStyle('NORMAL')
      if(p5.millis() % 1000 < 500): 

        p5.text('Press mouse to restart', 300, 500)
  elif program_state == 'LOSE':
      p5.image(background3, 300, 300, 600, 600)
      p5.textSize(70)
      p5.textStyle('BOLD')
      p5.fill(144, 0, 33)
      p5.text('You Lose!', 300, 200)

      p5.fill(255)
      p5.textSize(30)
      p5.textStyle('NORMAL')
      if(p5.millis() % 1000 < 500): 

        p5.text('Press mouse to restart', 300, 500)

def keyPressed(event):
  player.update(blocks)
  if program_state == 'PLAY':
      if (p5.key == 'w') or (p5.key =='W'):
          player.direction = 'UP'
      elif (p5.key == 's') or (p5.key =='S'):
          player.direction = 'DOWN'
      elif (p5.key == 'a') or (p5.key =='A'):
          player.direction = 'LEFT'
      elif (p5.key == 'd') or (p5.key =='D'):
          player.direction = 'RIGHT'

def keyReleased(event):
  pass

def mousePressed(event):
  global program_state, start_time
  if (p5.mouseButton == p5.LEFT):
    if program_state == 'START':
        program_state = 'PLAY'
        start_time = p5.millis()
    if program_state == 'WIN':
      program_state = 'START'
    if program_state == 'LOSE':
      program_state = 'START'

def mouseReleased(event):
  pass