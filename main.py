import pygame
import math
 
def main():
    pygame.init()
    pygame.display.set_caption("minimal program")
    global screen 
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    running = True
    garis=[[0,0,100,100],[0,0,100,100],[0,0,100,100],[0,0,100,100]]
    pangar=len(garis)-1

    derx=0;
    while running:
        pygame.display.flip()
        screen.fill((200,200,200))
        clock.tick(60)
        mox,moy=pygame.mouse.get_pos()
        garis[0][0]=mox
        garis[0][1]=moy
        garis[0][2],garis[0][3]=pointline(garis[0][2],garis[0][3],mox,moy,False)
        for i in range(1,pangar+1):
            garis[i][0]=garis[i-1][2]
            garis[i][1]=garis[i-1][3]
            garis[i][2],garis[i][3]=pointline(garis[i][2],garis[i][3],garis[i-1][2],garis[i-1][3],False)

        garis[pangar][2]=400
        garis[pangar][3]=300
        garis[pangar][0],garis[pangar][1]=pointline(garis[pangar][0],garis[pangar][1],garis[pangar][2],garis[pangar][3],True)
        for i in range(pangar-1,-1,-1):
            garis[i][2]=garis[i+1][0]
            garis[i][3]=garis[i+1][1]
            garis[i][0],garis[i][1]=pointline(garis[i][0],garis[i][1],garis[i+1][0],garis[i+1][1],True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
     
#def garrot(deg):
#    rad=math.radians(deg)
#    garx=100+(100*math.sin(rad))
#    gary=100-(100*math.cos(rad))
#    pygame.draw.line(screen,(0,0,0),(100,100),(garx,gary))
    
def pointline(px,py,tx,ty,mode):
    dx=px-tx
    dy=py-ty
    sl=math.sqrt(pow(dx,2)+pow(dy,2))
    fx=(100/(sl+1))*dx+tx
    fy=(100/(sl+1))*dy+ty
    if mode:
        pygame.draw.line(screen,(0,0,0),(int(fx),int(fy)),(int(tx),int(ty)))
    return fx,fy


if __name__=="__main__":
    main()
