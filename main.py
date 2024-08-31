import pygame  

pygame.init()

screen= pygame.display.set_mode((700,500))
caption=pygame.display.set_caption("BANGLADESH FLAG")

#color
white=(255,255,255)
red=(255,0,0)
green=((0,106,78))

#loop
running=True
while running:
  for event in pygame.event.get():
     if event.type== pygame.QUIT:
       running=False

  screen.fill(white)

  pygame.draw.rect(screen, green,(200,150,300,200))
  pygame.draw.circle(screen, red, (350,250),60)

  
  
  
  
  
  pygame.display.flip()
