import pygame
pygame.init()
"""再設置我的視窗大小"""
window = pygame.display.set_mode((800,600))
"""設置標題名稱"""
pygame.display.set_caption("GroundStation Window")
"""(R,B,G)"""
black=(0,0,0)
"""匯入圖"""
"""後面的convert_alpha()是把背景透明化"""
image = pygame.image.load("python123/tkuLogo.jpg").convert_alpha()
"""判斷式"""
gameLoop = True
while gameLoop :
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False


    window.fill(black)


    window.blit(image,(0,0))
    pygame.display.flip()
pygame.quit()




