import pygame
import os
import random
import time

pygame.init() #初始化
win = pygame.display.set_mode((1200,500))    #設定視窗大小，長寬
pygame.display.set_caption('Final project')  #視窗名稱

#以下部分為載入圖片並且用轉換大小，需要多張照片不斷更新以達到動畫效果。
#=================================================================================#

bg = [pygame.image.load(os.path.join('背景','椰林1.jpg')),
      pygame.image.load(os.path.join('背景','椰林1.jpg')),
      pygame.image.load(os.path.join('背景','總圖.jpg')),
      pygame.image.load(os.path.join('背景','電二.jpg')),
      pygame.image.load(os.path.join('背景','電二.jpg'))]
bg = [pygame.transform.scale(i,(1200,500)) for i in bg]


char = pygame.image.load(os.path.join('人物1','站著-0000.jpg'))
char = pygame.transform.scale(char,(64,64))

walkLeft = [pygame.image.load(os.path.join('人物1','移動動畫-0000.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0001.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0002.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0003.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0004.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0005.jpg'))]

walkLeft = [pygame.transform.scale(i,(64,64))  for i in walkLeft]

walkRight = [pygame.image.load(os.path.join('人物1','移動動畫-0000 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0001 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0002 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0003 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0004 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','移動動畫-0005 - 複製.jpg'))]

walkRight = [pygame.transform.scale(i,(64,64))  for i in walkRight]

attackLeft = [pygame.image.load(os.path.join('人物1','攻擊動畫-0000.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0001.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0002.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0003.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0004.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0005.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0006.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0007.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0008.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0009.jpg'))]

attackRight = [pygame.image.load(os.path.join('人物1','攻擊動畫-0000 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0001 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0002 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0003 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0004 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0005 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0006 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0007 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0008 - 複製.jpg')),
          pygame.image.load(os.path.join('人物1','攻擊動畫-0009 - 複製.jpg'))]

attackLeft = [pygame.transform.scale(i,(64,64)) for i in attackLeft]
attackRight = [pygame.transform.scale(i,(64,64)) for i in attackRight]

enemyLeft = [pygame.image.load(os.path.join('敵人1','腳踏車1.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車2.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車3.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車4.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車5.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車6.png'))]
enemyRight = [pygame.image.load(os.path.join('敵人1','腳踏車1 - 複製.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車2 - 複製.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車3 - 複製.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車4 - 複製.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車5 - 複製.png')),
          pygame.image.load(os.path.join('敵人1','腳踏車6 - 複製.png'))]
enemyDead = [pygame.image.load(os.path.join('敵人1','腳踏車死亡.png')),
             pygame.image.load(os.path.join('敵人1','腳踏車死亡 - 複製.png'))]
enemyDead = [pygame.transform.scale(i,(64,64)) for i in enemyDead] 
enemyLeft = [pygame.transform.scale(i,(64,64)) for i in enemyLeft]
enemyRight = [pygame.transform.scale(i,(64,64)) for i in enemyRight]

enemyLeft2 = [pygame.image.load(os.path.join('敵人2','綠水靈-00001.jpg')),
          pygame.image.load(os.path.join('敵人2','綠水靈-00011.jpg')),
          pygame.image.load(os.path.join('敵人2','綠水靈-00021.jpg'))]
enemyRight2 = [pygame.image.load(os.path.join('敵人2','綠水靈-0000 - 複製1.jpg')),
          pygame.image.load(os.path.join('敵人2','綠水靈-0001 - 複製1.jpg')),
          pygame.image.load(os.path.join('敵人2','綠水靈-0002 - 複製1.jpg'))]

enemyLeft2 = [pygame.transform.scale(i,(80,80)) for i in enemyLeft2]
enemyRight2 = [pygame.transform.scale(i,(80,80)) for i in enemyRight2]


enemyLeft3 = [pygame.image.load(os.path.join('敵人3','教授.jpg'))]
enemyRight3 = [pygame.image.load(os.path.join('敵人3','教授 - 複製.jpg'))]

enemyLeft3 = [pygame.transform.scale(i,(300,300)) for i in enemyLeft3]
enemyRight3 = [pygame.transform.scale(i,(300,300)) for i in enemyRight3]


weapon_list = [pygame.image.load(os.path.join('敵人3','python武器.png'))]
#weapon_list = [pygame.transform.scale(i,(100,100)) for i in weapon_list]

key_list = [pygame.image.load(os.path.join('素材','鑰匙1.png')),
            pygame.image.load(os.path.join('素材','鑰匙2.png')),
            pygame.image.load(os.path.join('素材','鑰匙3.png')),
            pygame.image.load(os.path.join('素材','鑰匙4.png'))]
key_list = [pygame.transform.scale(i,(24,24)) for i in key_list]

platform_list = [pygame.image.load(os.path.join('素材','平台1.png')),
            pygame.image.load(os.path.join('素材','平台2.png')),
            pygame.image.load(os.path.join('素材','平台3.png')),
            pygame.image.load(os.path.join('素材','平台4.png'))]

door = [pygame.image.load(os.path.join('素材','傳送門.png'))]
door = [pygame.transform.scale(i,(70,80)) for i in door]

jetpack = [pygame.image.load(os.path.join('素材','噴射背包.png'))]
jetpack = [pygame.transform.scale(i,(40,40)) for i in jetpack]

medkit_list = [pygame.image.load(os.path.join('素材','補血包.png'))]
medkit_list = [pygame.transform.scale(i,(30,30)) for i in medkit_list]

arsenal_list = [pygame.image.load(os.path.join('素材','電腦.png'))]
arsenal_list = [pygame.transform.scale(i,(70,70)) for i in arsenal_list]

long_attack_list = [pygame.image.load(os.path.join('素材','C++武器.png')),
                     pygame.image.load(os.path.join('素材','C++武器 - 複製.png'))]
long_attack_list = [pygame.transform.scale(i,(40,40)) for i in long_attack_list]

bulletLeft = [pygame.image.load(os.path.join('敵人2','子彈-0000 - 複製.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0001 - 複製.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0002 - 複製.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0003 - 複製.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0004 - 複製.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0005 - 複製.jpg'))]
bulletRight = [pygame.image.load(os.path.join('敵人2','子彈-0000.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0001.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0002.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0003.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0004.jpg')),
          pygame.image.load(os.path.join('敵人2','子彈-0005.jpg'))]
bulletLeft = [pygame.transform.scale(i,(25,25)) for i in bulletLeft]
bulletRight = [pygame.transform.scale(i,(25,25)) for i in bulletRight]
 
font = pygame.font.SysFont("comicsans", 80, True)
#=================================================================================#




#以下為class部分
#=================================================================================#
#主角

class player():
    def __init__(self,x,y,width,height):
        self.x = x    #x,y座標
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.attackCount = 0 
        #hitbox包含腳色位置和大小，用以決定是否接觸其他物體
        self.hitbox=(self.x,self.y,self.width,self.height) 
        self.have_key = 0
        self.fall = False
        self.fallCount = 7
        self.ground = y
        self.health = 150
        self.fly = False
        self.invincible=False
        self.equipment = False
        self.equipment_bullets = []  #最後一關的子彈
        self.kill=0
       
    #draw function，描寫人物的移動狀態，用walkcount計算並更新圖片
    #win.blit() 為繪製圖片
    def draw(self, win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount//5], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//5], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox=(self.x+5,self.y+10,55,53)   #讓box移動
        
        #血條部分，外層為黑框，血為紅色，扣血後是深綠色
        pygame.draw.rect(win, (0,50,0), (30, 30, 150, 10))
        if self.health>=0:
            pygame.draw.rect(win, (255,0,0), (30, 30, 150-(150-self.health), 10))
        pygame.draw.rect(win, (0,0,0), (29, 29, 150, 10),2)
        
        
    #attack function，描寫人物的攻擊狀態，用attackcount計算並更新圖片
    def attack(self,win):
        if not self.isJump:
            if self.attackCount>=10:
                self.attackCount = 0 
            if self.left==True:
                win.blit(attackLeft[self.attackCount],(self.x,self.y))
                pygame.display.update()
                self.attackCount += 1
            else:
                win.blit(attackRight[self.attackCount],(self.x,self.y))
                pygame.display.update()
                self.attackCount += 1
                
    #定義人物被攻擊要向左或向右移動，hit_left:左邊被攻擊，則向右移動。
    def hit_left(self,damage):
        if not self.invincible:
            self.walkCount = 0
            back = 10
            while back > 0:
                if self.x<=1200-self.width:
                    self.x += back/10
                win.blit(walkLeft[0],(self.x,self.y))
                pygame.display.update()
                back-= 0.1
            self.health -= damage
            pygame.display.update()
            back = 0
    def hit_right(self,damage):
        if not self.invincible:
            self.walkCount = 0
            back = 10
            while back > 0:
                if self.x>=0:
                    self.x -= back/10
                win.blit(walkRight[0],(self.x,self.y))
                pygame.display.update()
                back-= 0.1
            self.health -= damage
            pygame.display.update()
            back = 0
    
    #定義如何與其他object接觸，(根據他們的座標和大小)
    def interact(self,obj):
        if self.hitbox[1] < obj.hitbox[1] + obj.hitbox[3] and self.hitbox[1] + self.hitbox[3] > obj.hitbox[1]:  #y方向
            if self.hitbox[0] + self.hitbox[2]> obj.hitbox[0] and obj.hitbox[0]+ obj.hitbox[2]> self.hitbox[0]:  #x方向     
                return True
        else:
            return False
        

#=================================================================================#
#椰林腳踏車怪
                
class Enemy1():   
    def __init__(self,x,y,end,vel=3):
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.end = end
        self.path = [x,end]
        self.walkCount = 0
        self.vel = vel
        self.hitbox=(self.x,self.y+10,60,55)
        self.health = 5
        #用以隨機生成掉落鑰匙
        self.num = int(random.randrange(0,3,1))
        self.key = key_list[self.num] #隨機載入鑰匙圖片
        self.key_hitbox = (self.x+10,self.y+40,24,24)
        self.visible = True
        self.key_exist = True
        self.dead = False
        
    #draw function介紹承上        
    def draw(self,win):
        if self.visible == True:  #鑰匙被撿走,self.visible就會False，因此不畫
            if self.health>0:
                self.move()
                
                if self.walkCount + 1 >= 42:
                    self.walkCount = 0
                if self.vel>0:
                    win.blit(enemyRight[self.walkCount//7], (self.x,self.y))
                    self.walkCount +=1
                else:
                    win.blit(enemyLeft[self.walkCount//7], (self.x,self.y))
                    self.walkCount += 1
                self.hitbox=(self.x,self.y+10,60,55)

            else:
                if self.left==True:
                    win.blit(enemyDead[1],(self.x,self.y))
                else:
                    win.blit(enemyDead[0],(self.x,self.y))
                self.key_hitbox = (self.x+10,self.y+40,24,24)
                win.blit(self.key,(self.x+10,self.y+40))


    #move function 定義小怪在一個範圍內來回移動
    def move(self):
        if self.vel>0:
            self.left = False
            self.right = True
            if self.x  <  self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            self.left = True
            self.right = False
            if self.x >= self.path[0] :
                self.x += self.vel
            else:
                self.vel = self.vel*-1
                self.x += self.vel
                self.walkCount = 0 
    
    #小怪被攻擊，介紹承上
    def hit_right(self):
        back = 10
        self.health-=1
        while back > 0:
            self.x -= back/10
            win.blit(enemyRight[0],(self.x,self.y))
            pygame.display.update()
            back-= 0.1
        pygame.display.update()
        back = 0
    def hit_left(self):
        back = 10
        self.health-=1
        while back > 0:
            self.x += back/10
            win.blit(enemyLeft[0],(self.x,self.y))
            pygame.display.update()
            back-= 0.1
        pygame.display.update()
        back = 0

#=================================================================================#
#垂直椰林腳踏車怪，從水平移動改成垂直移動
        
class Enemy11(Enemy1):
    def __init__(self,x,y,end):
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.end = end
        self.path = [y,end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox=(self.x,self.y+10,60,55)
        self.health = 5
        self.num = int(random.randrange(0,3,1))
        self.key = key_list[self.num]
        self.key_hitbox = (self.x+10,self.y+40,24,24)
        self.visible = True
        self.key_exist = True
        self.dead = False
        
    def move(self):
        if self.vel>0:
            self.left = False
            self.right = True
            if self.y  <  self.path[1]:
                self.y += self.vel
            else:
                self.vel = self.vel * -1
                self.y += self.vel
                self.walkCount = 0
        else:
            self.left = True
            self.right = False
            if self.y >= self.path[0] :
                self.y += self.vel
            else:
                self.vel = self.vel*-1
                self.y += self.vel
                self.walkCount = 0 

#=================================================================================#
#射手怪
                
class Enemy2():   
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.left = True
        self.right = False
        self.walkCount = 0
        self.hitbox=(self.x,self.y+10,80,80)
        self.health = 5
        self.num = int(random.randrange(0,3,1))
        self.key = key_list[self.num]
        self.key_hitbox = (self.x+10,self.y+40,24,24)
        self.visible = True
        self.bullets=[]
        self.key_exist = True
        self.dead=False
        
    #draw() 介紹承上
    def draw(self,win):
        if self.visible:
            if self.health>0:
                if self.walkCount + 1 >= 21:
                    self.walkCount = 0
                if self.right:
                    win.blit(enemyRight2[self.walkCount//7], (self.x,self.y))
                    self.walkCount +=1
                elif self.left:
                    win.blit(enemyLeft2[self.walkCount//7], (self.x,self.y))
                    self.walkCount += 1

    #被攻擊不會退後
    def hit(self):
        self.health-=1
        
#=================================================================================#
#射手怪子彈
        
class Bullet():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.flyCount = 0
        self.left = True
        self.right = False
        self.vel = 5
        self.yvel = 3
        self.hitbox = (self.x,self.y,20,20)
    
    #draw() 介紹承上
    def draw(self,screen):
        if self.flyCount + 1 >= 42:
            self.flyCount = 0
        
        if self.right:
            win.blit(bulletRight[self.flyCount//7], (self.x,self.y))
            self.flyCount +=1
        elif self.left:
            win.blit(bulletLeft[self.flyCount//7], (self.x,self.y))
            self.flyCount += 1
        
#=================================================================================#
#boss
            
class Enemy3():    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 300
        self.height = 300
        self.left = True
        self.right = False
        self.walkCount = 0
        self.hitbox=(self.x,self.y,self.width,self.height)
        self.center = (self.x+self.width/2,self.y+self.height/2)
        self.health = 200
        self.visible = True
        #用存放七發小子彈和變大python子彈
        self.weapons=[]
        self.weapons2=[]
        self.weapons3=[]
        self.weapons4=[]
        self.weapons5=[]
        self.weapons6=[]
        self.weapons7=[]
        self.WEAPON=[self.weapons,
                      self.weapons2,self.weapons3,self.weapons4,
                      self.weapons5,self.weapons6,self.weapons7]
    
    #draw() 介紹承上
    def draw(self,win):
        if self.visible:
            if self.health>0:
                if self.right:
                    win.blit(enemyRight3[0], (self.x,self.y))
                elif self.left:
                    win.blit(enemyLeft3[0], (self.x,self.y))
                    
        pygame.draw.rect(win, (0,50,0), (30, 50, 200, 10))
        if self.health>=0:
            pygame.draw.rect(win, (255,0,0), (30, 50, self.health, 10))
        pygame.draw.rect(win, (0,0,0), (29, 49, 200, 10),2)
        
    #被攻擊不會移動
    def hit(self,damage):
        self.health-=damage
 
#=================================================================================#
#python子彈
        
class Weapon():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.width = 30
        self.height = 30
        self.vel = 5
        self.yvel = 5
        self.hitbox = (self.x,self.y,self.width,self.height)

    #draw() 介紹承上
    def draw(self,screen):
        # 必須改名 否則會有bug
        weapon_list_change = [pygame.transform.scale(i,(self.width,self.height)) for i in weapon_list]
        win.blit(weapon_list_change[0],(self.x,self.y))
        
#=================================================================================#
#平台  
        
class Platform():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.width = 100
        self.height = 15
        self.num = random.randrange(0,len(platform_list),1)
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.stood = False  #用以計算人物的跳躍
    
    #draw() 介紹承上
    def draw(self,win):
        win.blit(pygame.transform.scale(platform_list[self.num],(self.width,self.height)),(self.x,self.y))

#=================================================================================#
#傳送門
        
class Door():
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.width = 70
        self.height = 80
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.visible = True
    #draw() 介紹承上
    def draw(self,win):
        if self.visible:
            win.blit(door[0],(self.x,self.y))
        
#=================================================================================#
#噴射背包            

class Jetpack():
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.width = 40
        self.height = 40
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.visible = True
    #draw() 介紹承上
    def draw(self,win):
        if self.visible:
            win.blit(jetpack[0],(self.x,self.y))
            
#=================================================================================#
#急救包  

class Medkit():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.width = 30
        self.height = 30
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.visible = True
    #draw() 介紹承上
    def draw(self,win):
        if self.visible:
            win.blit(medkit_list[0],(self.x,self.y))

#=================================================================================#
#電腦，接觸後可提取C++子彈
         
class Equipment():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.width = 100
        self.height = 100
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.visible = True
        self.equipment = 20
    
    #draw() 介紹承上
    def draw(self,win):
        if self.equipment<=0:
            self.visible=False
        if self.visible:
            win.blit(arsenal_list[0],(self.x,self.y))
    #定義接觸
    def interact(self,obj):
        if self.hitbox[1] < obj.hitbox[1] + obj.hitbox[3] and self.hitbox[1] + self.hitbox[3] > obj.hitbox[1]:  #y方向
            if self.hitbox[0] + self.hitbox[2]> obj.hitbox[0] and obj.hitbox[0]+ obj.hitbox[2]> self.hitbox[0]:  #x方向     
                return True
        else:
            return False
#=================================================================================#
#C++子彈

class Equipment_Bullet():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.width = 40
        self.height = 40
        self.left = True
        self.right = False
        self.hitbox = (self.x,self.y,self.width,self.height)

    def draw(self,screen):
        if self.right:
            win.blit(long_attack_list[0], (self.x,self.y))
        elif self.left:
            win.blit(long_attack_list[1], (self.x,self.y))
            
#=================================================================================#

    
    
    
#interface
#=================================================================================#
#定義起始畫面，進場畫面，退場畫面，死亡畫面   
    
    
def show_0():
    win.blit(font.render("About", 1, (255, 255, 255)), (450, 150))
    win.blit(font.render("Start (press space)", 1, (255, 255, 255)), (330, 250))    
    pygame.display.update()
    
def show_start(round):
    win.blit(bg[round],(0,0))
    text = 'round' + str(round) + ' !'
    win.blit(font.render(text, 1, (0, 0, 0)), (450, 150))
    win.blit(font.render("Press enter to continue...", 1, (0, 0, 0)), (250, 250))
    pygame.display.update()
    
def show_pass(round):
    win.blit(bg[round],(0,0))
    text = 'round' + str(round)+ ' passed!'
    win.blit(font.render(text, 1, (0, 0, 0)), (450, 150))
    win.blit(font.render("Press enter to continue...", 1, (0, 0, 0)), (250, 250))
    pygame.display.update()
    
def show_end(round):
    win.blit(bg[round],(0,0))
    win.blit(font.render("You win!", 1, (255, 255, 255)), (450, 150)) 
    win.blit(font.render("Press enter to close", 1, (255, 255, 255)), (250, 250)) 
    pygame.display.update()
def show_dead(round):
    win.blit(bg[round],(0,0))
    win.blit(font.render("You are dead!!", 1, (255, 255, 255)), (350, 150)) 
    win.blit(font.render("Game Over (Press enter to close)", 1, (255, 255, 255)), (100, 250)) 
    pygame.display.update()

#=================================================================================#
    
    
## mainloop
#=================================================================================#
#從round=0開始，在進退場畫面時，round才會更改

round = 0
run = True
if round == 0:
    while run:
        pygame.time.Clock().tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:    #不用空白建 因為會連按到上一個
            run = False 
            round+=1
            break
        show_0()

#=================================================================================#

#第一關
#=================================================================================#
#每關都有會用到的redrawGameWindow function裡面包含需要不斷繪畫的指令

def redrawGameWindow_r1(round):
    win.blit(bg[round], (0,0))  #背景
    win.blit(key_list[0], (20,45))  #顯示已取鑰匙數量(0/1)
    text1 = ': '+ str(man.have_key) + '/1' 
    text1 = pygame.transform.scale(font.render(text1, 1, (255, 0, 0)),(30,20))
    win.blit(text1, (45, 50))
    win.blit(key_list[0], (20,45))
    text2 = 'kill: '+str(man.kill) + ' / ' + str(len(enemys_r1))
    text2 = pygame.transform.scale(font.render(text2, 1, (255, 0, 0)),(35,25))
    win.blit(text2, (45, 75))        #顯示殺敵數
    
    #用for loop迴圈 繪製所有物件
    for medkit in medkits_r1:
        medkit.draw(win)      
    for platform in platforms_r1:
        platform.draw(win)
    for enemy in enemys_r1:
        enemy.draw(win)

    door1.draw(win)
    man.draw(win)    
    pygame.display.update()  #更新        

#=================================================================================#
#創造此關卡各個物件

font = pygame.font.SysFont("comicsans", 80, True)
door1 = Door(1120,170)
#平台長70
platforms_r1 = [Platform(100,320),Platform(100,200),Platform(150,100),
             Platform(250,380),Platform(400,340),Platform(870,130),
             Platform(500,220),Platform(540,50), Platform(590,120),
             Platform(600,320),Platform(860,320),Platform(930,250),
             Platform(1100,250)]

#怪物end為40因為要比平台短，高度再少60才會在平台上
enemys_r1 = [Enemy1(400,436,470),Enemy1(100,140,140),Enemy1(590,60,635),
          Enemy1(500,160,540),Enemy1(400,280,450),Enemy1(300,436,1100),
          Enemy1(150,436,700),Enemy1(920,436,1150),Enemy1(120,260,200),
          Enemy11(800,200,400),Enemy11(300,100,300),Enemy11(360,300,436)]    

#shooters = [Enemy2(750,420),Enemy2(800,100),Enemy2(200,300)]

#高度少平台25
medkits_r1 = [Medkit(250,470),Medkit(620,295),Medkit(890,105),
           Medkit(140,175),Medkit(560,25),Medkit(970,470)]

man = player(50,435,64,64)

#=================================================================================#
#第一關開始畫面

run = True
if round ==1:
    while run:
        pygame.time.Clock().tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            run = False
            break
        show_start(round)
        
#=================================================================================#
#第一關

run = True
if round==1:

    while run:
        for event in pygame.event.get():   #退出視窗
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
                
        if man.health <= 0:   #腳色死亡
            show_dead(round)
            run=False
            round=-1
            break
        
        for enemy in enemys_r1:
            if enemy.health>0:
                if man.x>enemy.x:     #腳色從左或右邊背攻擊，依此向左或右移動
                    if man.interact(enemy):
                        man.hit_left(10)
                elif man.x<enemy.x:
                    if man.interact(enemy):   
                        man.hit_right(10)
                            
                            
            if enemy.health<=0:      
                if not enemy.dead:     #小怪死亡計算殺敵數
                    man.kill+=1
                    enemy.dead=True
                if man.hitbox[1] < enemy.key_hitbox[1] + enemy.key_hitbox[3] and man.hitbox[1] + man.hitbox[3] > enemy.key_hitbox[1]:  #y方向
                    if man.hitbox[0] + man.hitbox[2]> enemy.key_hitbox[0] and enemy.key_hitbox[0]+ enemy.key_hitbox[2]> man.hitbox[0]:  #x方向     
                        enemy.visible = False
                        #與鑰匙接觸後，小怪就會消失，並且取得鑰匙
                        if enemy.key==key_list[0]:
                            if enemy.key_exist:
                                man.have_key +=1
                                enemy.key_exist = False
                                text = font.render("Key get!!",1, (0,0,0))
                                win.blit(text,(300,250))
    
        #如果拿到所需鑰匙數量或是殺完全不小怪即可到下一關
        if man.have_key>=1 or man.kill>=len(enemys_r1):
            if man.interact(door1):    
                door1.visible = False
#                print('過關')
                run = False
                
            
        #急救包補血
        for medkit in medkits_r1:
            if medkit.visible:
                if man.interact(medkit):
                    if 140<=man.health<150:
                        man.health = 150
                        medkit.visible = False
                    if man.health<150 and man.health>0:
                        man.health+=10
                        medkit.visible = False
                
    
        #平台供腳色站立
        for platform in platforms_r1:
            #因為落下有一定速率，所以在落下的點不會是一個點而是一個範圍，若在這範圍中，
            #則腳色就能站在平台上
            if man.hitbox[0]+man.hitbox[2]/2 > platform.hitbox[0] and man.hitbox[0]+man.hitbox[2]/2 < platform.hitbox[0]+platform.hitbox[2]:
                if -4 < platform.hitbox[1] - (man.hitbox[1]+man.hitbox[3]) < 4 and man.fall:
                    man.ground = (platform.hitbox[1]-man.height)
                    platform.stood = True
            
            if  man.hitbox[0]+man.hitbox[2]/2 < platform.hitbox[0] or man.hitbox[0]+man.hitbox[2]/2 > platform.hitbox[0]+platform.hitbox[2]:
                if platform.stood:
                    man.fall = True
                    man.ground = 435
                    platform.stood=False
        
        #鍵盤指令
        keys = pygame.key.get_pressed()
        
        #空白建攻擊
        if keys[pygame.K_SPACE]:
            man.attack(win)
            for enemy in enemys_r1:
                if enemy.health>0:
                    #與小怪在一定範圍內，小怪就會被攻擊，並向左或右移動
                    if abs((man.hitbox[1]+man.hitbox[2]) - (enemy.hitbox[1]+enemy.hitbox[3]))<35:   #y方向
                        if man.x<enemy.x and man.right==True:
                            if  enemy.hitbox[0] - (man.hitbox[0] + man.hitbox[2])<25 :#x方向
                                enemy.hit_left()
                        elif man.x>enemy.x and man.left==True:
                            if man.hitbox[0] - (enemy.hitbox[0]+enemy.hitbox[2])<25:
                                enemy.hit_right()
    
        #定義腳色左右移動
        if keys[pygame.K_LEFT] and man.x>0:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x<1200-man.width:          
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing= False
        else:
            man.standing = True
            man.walkCount = 0
        
        
        #定義腳色跳躍與落下，
        if not man.isJump:
            if keys[pygame.K_UP] and not man.fall:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= 0:    #跳躍
                man.y -=  (man.jumpCount**2) *0.5
                man.jumpCount -= 1
            else:
                man.fall = True
                man.isJump = False
                man.jumpCount=10
        
        #落下
        if man.fall and man.y < man.ground:       #man.y最後必然>430則執行else條件
            man.y += man.fallCount
        else:
            man.fall = False
        
        redrawGameWindow_r1(round)
        
#=================================================================================#
#第一關結束畫面
        
run = True
if round ==1:
    while run:
        pygame.time.Clock().tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            run = False
            round+=1
            break
        show_pass(round)
        
#=================================================================================#




#第二關
#=================================================================================#
# redrawGameWindow 介紹承上
        
def redrawGameWindow_r2(round):  ##changed by boris
    win.blit(bg[round], (0,0))   
    win.blit(key_list[0], (20,45))
    text1 = ': '+ str(man.have_key) + '/3' 
    text1 = pygame.transform.scale(font.render(text1, 1, (255, 0, 0)),(30,20))
    win.blit(text1, (45, 50))
    win.blit(key_list[0], (20,45))
    text2 = 'kill: '+str(man.kill) + ' / ' + str(len(enemys_r2)+len(shooters_r2))
    text2 = pygame.transform.scale(font.render(text2, 1, (255, 0, 0)),(35,25))
    win.blit(text2, (45, 75))
    
    for medkit in medkits_r2:
        medkit.draw(win)    
    for platform in platforms_r2:
        platform.draw(win)
    for enemy in enemys_r2:
        enemy.draw(win)
    for shooter in shooters_r2:
        shooter.draw(win)

    door1.draw(win)
    man.draw(win)    
    pygame.display.update()
    
#=================================================================================#

run = True
if round == 2:
    while run:
        pygame.time.Clock().tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            break
        show_start(round)

#=================================================================================#    


door1 = Door(1120,180)
#平台長70
platforms_r2 = [Platform(100,200),Platform(140,100),Platform(180,400),
             Platform(160,320),Platform(200,230),Platform(340,200),
             Platform(400,340),Platform(420,150),Platform(600,320),
             Platform(640,220),Platform(710,120),Platform(850,380),
             Platform(870,130),Platform(1050,300),Platform(1100,400),
             Platform(10,400),Platform(30,260),Platform(750,400),
             Platform(1110,260)]

enemys_r2 = [Enemy1(400,436,500,vel=7),Enemy1(70,140,140,vel=5),Enemy1(710,60,760,vel=3),
          Enemy1(400,280,450,vel=3),Enemy1(200,436,770,vel=8),Enemy1(300,436,1000,vel=2),
          Enemy1(950,436,1120,vel=4),Enemy1(180,436,700,vel=10),Enemy1(200,170,250,vel=3),
          Enemy11(800,200,400),Enemy11(300,100,300),Enemy11(360,300,436)]    

shooters_r2 = [Enemy2(100,120),Enemy2(140,20),Enemy2(400,260),
            Enemy2(700,420),Enemy2(850,300),Enemy2(870,50)]  ##changed by boris

#高度少平台25
medkits_r2 = [Medkit(120,170),Medkit(160,70),Medkit(180,290),
           Medkit(350,170),Medkit(440,120),Medkit(890,100),
           Medkit(660,190),Medkit(730,90),Medkit(1070,270),
           Medkit(10,470),Medkit(1120,370),Medkit(1140,470),]

man = player(50,435,64,64)
run = True

if round==2:
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
    
        if man.health <= 0:
            show_dead(round)
            run=False
            round=-1
            break
        
        
        for enemy in enemys_r2:
            if enemy.health>0:
                if man.x>enemy.x:
                    if man.interact(enemy):
                        man.hit_left(10)
                elif man.x<enemy.x:
                    if man.interact(enemy):   
                        man.hit_right(10)
                            
                            
            if enemy.health<=0 :
                if not enemy.dead:
                    man.kill+=1
                    enemy.dead=True
                if man.hitbox[1] < enemy.key_hitbox[1] + enemy.key_hitbox[3] and man.hitbox[1] + man.hitbox[3] > enemy.key_hitbox[1]:  #y方向
                    if man.hitbox[0] + man.hitbox[2]> enemy.key_hitbox[0] and enemy.key_hitbox[0]+ enemy.key_hitbox[2]> man.hitbox[0]:  #x方向     
                        enemy.visible = False
                        if enemy.key==key_list[0]:
                            if enemy.key_exist:
                                man.have_key +=1
                                enemy.key_exist = False
                                text = font.render("Key get!!",1, (0,0,0))
                                win.blit(text,(300,250))
                                
        
        #射手怪功能
        for shooter in shooters_r2:
    
            if shooter.health>0:
                if man.x<shooter.x:   #射手依照腳色的位置會面向左或右邊
                    shooter.left=True
                    shooter.right=False        
                    #一次只發射一顆子彈，且距離太近就不發射子彈，否則遠永無法接近
                    if len(shooter.bullets)<1 and shooter.x - (man.hitbox[0]+man.hitbox[2])> 100:
                        shooter.bullets.append(Bullet(shooter.x,shooter.y+50))
                    
                    if man.interact(shooter):  #碰撞
                        man.hit_right(1)
        
                else:
                    shooter.right=True
                    shooter.left=False
                    if len(shooter.bullets)<1 and man.hitbox[0] - (shooter.hitbox[0]+shooter.hitbox[2])> 100:
                        shooter.bullets.append(Bullet(shooter.x,shooter.y+50))
                        
                    if man.interact(shooter):
                        man.hit_left(1)
                            
            if shooter.health<=0:
                if not shooter.dead:
                    man.kill+=1    #計算殺敵數
                    shooter.dead = True
                if man.hitbox[1] < shooter.key_hitbox[1] + shooter.key_hitbox[3] and man.hitbox[1] + man.hitbox[3] > shooter.key_hitbox[1]:  #y方向
                    if man.hitbox[0] + man.hitbox[2]> shooter.key_hitbox[0] and shooter.key_hitbox[0]+ shooter.key_hitbox[2]> man.hitbox[0]:  #x方向     
                        shooter.visible = False

            #射手怪的子彈功能
            for bullet in shooter.bullets:
                #判斷左右
                if shooter.x > man.hitbox[0]+man.hitbox[3]:
                    bullet.left = True
                    bullet.right = False
                    bullet.vel = -5
                    if man.interact(bullet):    #被打中
                        man.hit_right(1)
                        shooter.bullets.pop(shooter.bullets.index(bullet))#擊中後子彈消失
                else:
                    bullet.left = False
                    bullet.right = True
                    bullet.vel = 5
                    if man.interact(bullet):
                        man.hit_left(1)
                        shooter.bullets.pop(shooter.bullets.index(bullet))
                
                #判斷y方向距離
                y_dis = (bullet.hitbox[1]+bullet.hitbox[3]/2) - (man.hitbox[1]+man.hitbox[3]/2) #中心
                if abs(y_dis)>300:
                    #不可用>0:  否則速度最後會無限趨近於0，永遠不會打到腳色，
                    #所以設個條件，距離越遠時越快，到300後都是跑3
                    bullet.y -= y_dis/100
                else:
                    if 3 < y_dis < 300:
                        bullet.y -= 3
                    elif -300 < y_dis< -3:
                        bullet.y += 3
                
                bullet.x += bullet.vel
                bullet.hitbox = (bullet.x,bullet.y,20,20)   #要更新子彈hitbox
                bullet.draw(win)
                    
                if bullet.x<0 or bullet.x>1200: #超過視窗後消失，重新裝填子彈
                    if bullet in shooter.bullets:  #避免奇怪bug
                        shooter.bullets.pop(shooter.bullets.index(bullet))
    
            pygame.display.update()   #放外面才不會延遲
    
        #達到條件後通關
        if man.have_key>=3 or man.kill==len(enemys_r2)+len(shooters_r2):
            if man.interact(door1):    
                door1.visible = False
                round +=1
                break
        
        
        #補血血量與第一關不同
        for medkit in medkits_r2:
            if medkit.visible:
                if man.interact(medkit):
                    if 120<=man.health<150:
                        man.health = 150
                        medkit.visible = False
                    if man.health<150 and man.health>0:
                        man.health+=30
                        medkit.visible = False
                
    
    
        for platform in platforms_r2:
            if man.hitbox[0]+man.hitbox[2]/2 > platform.hitbox[0] and man.hitbox[0]+man.hitbox[2]/2 < platform.hitbox[0]+platform.hitbox[2]:
                if -4 < platform.hitbox[1] - (man.hitbox[1]+man.hitbox[3]) < 4 and man.fall:
                    man.ground = (platform.hitbox[1]-man.height)
                    platform.stood = True
            
            if  man.hitbox[0]+man.hitbox[2]/2 < platform.hitbox[0] or man.hitbox[0]+man.hitbox[2]/2 > platform.hitbox[0]+platform.hitbox[2]:
                if platform.stood:
                    man.fall = True
                    man.ground = 435
                    platform.stood=False
        
    
    
    
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_SPACE]:
            man.attack(win)
            
            for enemy in enemys_r2:
                if enemy.health>0:
                    if abs((man.hitbox[1]+man.hitbox[2]) - (enemy.hitbox[1]+enemy.hitbox[3]))<35:   #y方向
                        if man.x<enemy.x and man.right==True:
                            if  enemy.hitbox[0] - (man.hitbox[0] + man.hitbox[2])<25 :#x方向
                                enemy.hit_left()
                        elif man.x>enemy.x and man.left==True:
                            if man.hitbox[0] - (enemy.hitbox[0]+enemy.hitbox[2])<25:
                                enemy.hit_right()
                                
            #射手怪被攻擊後不會移動          
            for shooter in shooters_r2:
                if shooter.health>0:
                    if abs((man.hitbox[1]+man.hitbox[3]) - (shooter.hitbox[1]+shooter.hitbox[3]))<30:   #y方向
                        if man.x<shooter.x and man.right==True:
                            if  shooter.hitbox[0] - (man.hitbox[0] + man.hitbox[2])<25 :#x方向
                                shooter.hit()
                        elif man.x>shooter.x and man.left==True:
                            if man.hitbox[0] - (shooter.hitbox[0]+shooter.hitbox[2])<25:
                                shooter.hit()
    
    
    
    
        if keys[pygame.K_LEFT] and man.x>0:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x<1200-man.width:          
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing= False
        else:
            man.standing = True
            man.walkCount = 0
        
        
        
        if not man.isJump:
            if keys[pygame.K_UP] and not man.fall:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= 0:
                man.y -=  (man.jumpCount**2) *0.5
                man.jumpCount -= 1
            else:
                man.fall = True
                man.isJump = False
                man.jumpCount=10
    
        if man.fall and man.y < man.ground:       #man.y最後必然>430則執行else條件
            man.y += man.fallCount
        else:
            man.fall = False
        
        redrawGameWindow_r2(round)            ##這邊改成_r2

#=================================================================================#

run = True
if round ==2:
    while run:
        pygame.time.Clock().tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            run = False
            round+=1
            break
        show_pass(round)


#第三關
#=================================================================================#        
#介紹承上
        
def redrawGameWindow_r3(round):
    win.blit(bg[round], (0,0))
    arsenal.draw(win)
    man.draw(win)
    boss.draw(win)
    jetpack1.draw(win)
    pygame.display.update()


#=================================================================================#
        
        
boss = Enemy3(500,200)
jetpack1 = Jetpack(300,460)
arsenal = Equipment(40,430)  #電腦(武器庫)
man = player(50,435,64,64)
        
run = True
if round == 3:
    while run:
        pygame.time.Clock().tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            run = False
            break
        show_start(round)
        
#=================================================================================#

run = True
if round == 3:
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        if man.health <= 0:
            show_dead(round)
            run=False
            round=-1
            break

        if boss.health>0:
            if man.x<boss.center[0]: #boss也會依腳色位置轉向
                boss.left=True
                boss.right=False    
                
                
                for list in boss.WEAPON:
                    if len(list)<1 and boss.center[0] - (man.hitbox[0]+man.hitbox[2])> 20:
                        list.append(Weapon(boss.x+boss.width/2,boss.y+boss.width/2))
                    
                if man.interact(boss):  #碰撞
                    man.hit_right(10)
                    
            elif man.x>boss.center[0]:
                boss.right=True
                boss.left=False
                
                for list in boss.WEAPON:
                    if len(list)<1 and man.hitbox[0] - (boss.center[0])> 20:
                        list.append(Weapon(boss.center[0],boss.center[1]))

                if man.interact(boss):  #碰撞
                    man.hit_left(10)

        if boss.health<=0:
            boss.visible = False
            round+=1
            run=False
            
#==================================================================================#  
#變大python子彈
            
            
        for weapon in boss.weapons:
            #判斷左右
            if boss.center[0] > man.hitbox[0]+man.hitbox[3]:
                weapon.vel = -1.5
                if man.interact(weapon):
                    man.hit_right(weapon.width/10)
                    boss.weapons.pop(boss.weapons.index(weapon))
            else:
                weapon.vel = 1.5
                if man.interact(weapon):
                    man.hit_left(weapon.width/10)
                    boss.weapons.pop(boss.weapons.index(weapon))
            if arsenal.interact(weapon):
                arsenal.equipment-=10   #如果python子彈一直打到電腦，電腦會消失
                boss.weapons.pop(boss.weapons.index(weapon))
            
            #判斷y方向距離
            y_dis = (weapon.hitbox[1]+weapon.hitbox[3]/2) - (man.hitbox[1]+man.hitbox[3]/2) #中心
            if 1.5 < y_dis :
                weapon.y -= 1.5
            elif  y_dis< -1.5:
                weapon.y += 1.5

            weapon.x += weapon.vel
            weapon.width += 1  #python子彈會變大
            weapon.height += 1
            weapon.hitbox = (weapon.x,weapon.y,weapon.width,weapon.height)   #要更新hitbox
            weapon.draw(win)
                

        pygame.display.update()   #放外面才不會延遲

#==================================================================================#  
#七顆小python子彈
        
        for weapon in boss.weapons2:
            if boss.center[0] > man.hitbox[0]+man.hitbox[3]:
                if man.interact(weapon):
                    man.hit_right(5)
                    if weapon in boss.weapons2:
                        boss.weapons2.pop(boss.weapons2.index(weapon))
            else:
                if man.interact(weapon):
                    man.hit_left(5)
                    if weapon in boss.weapons2:
                        boss.weapons2.pop(boss.weapons2.index(weapon))
            
            weapon.x -= 6    #這七顆子彈，每顆都有不同的移動方向，都在這個位置更改
            weapon.y += 6

            weapon.hitbox = (weapon.x,weapon.y,weapon.width,weapon.height)   #要更新hitbox
            weapon.draw(win)
                
            if weapon.x<0 or weapon.x>1000 or weapon.y<0 or weapon.y>500: #超過視窗後消失，重新裝填子彈
                if weapon in boss.weapons2:
                    boss.weapons2.pop(boss.weapons2.index(weapon))

        pygame.display.update()   #放外面才不會延遲

        for weapon in boss.weapons3:
            if boss.center[0] > man.hitbox[0]+man.hitbox[3]:
                if man.interact(weapon):
                    man.hit_right(5)
                    if weapon in boss.weapons3:
                        boss.weapons3.pop(boss.weapons3.index(weapon))
            else:
                if man.interact(weapon):
                    man.hit_left(5)
                    if weapon in boss.weapons3:
                        boss.weapons3.pop(boss.weapons3.index(weapon))
            
            weapon.x -= 6

            weapon.hitbox = (weapon.x,weapon.y,weapon.width,weapon.height)   #要更新hitbox
            weapon.draw(win)
                
            if weapon.x<0 or weapon.x>1000 or weapon.y<0 or weapon.y>500: #超過視窗後消失，重天裝填子彈
                if weapon in boss.weapons3:
                    boss.weapons3.pop(boss.weapons3.index(weapon))

        pygame.display.update()   #放外面才不會延遲



        for weapon in boss.weapons4:
            if boss.center[0] > man.hitbox[0]+man.hitbox[3]:
                if man.interact(weapon):
                    man.hit_right(5)
                    if weapon in boss.weapons4:
                        boss.weapons4.pop(boss.weapons4.index(weapon))
            else:
                if man.interact(weapon):
                    man.hit_left(5)
                    if weapon in boss.weapons4:
                        boss.weapons4.pop(boss.weapons4.index(weapon))
            
            weapon.x -= 6
            weapon.y -= 6

            weapon.hitbox = (weapon.x,weapon.y,weapon.width,weapon.height)   #要更新hitbox
            weapon.draw(win)
                
            if weapon.x<0 or weapon.x>1000 or weapon.y<0 or weapon.y>500: #超過視窗後消失，重天裝填子彈
                if weapon in boss.weapons4:
                    boss.weapons4.pop(boss.weapons4.index(weapon))

        pygame.display.update()   #放外面才不會延遲

        for weapon in boss.weapons5:
            if boss.center[0] > man.hitbox[0]+man.hitbox[3]:
                if man.interact(weapon):
                    man.hit_right(5)
                    if weapon in boss.weapons5:
                        boss.weapons5.pop(boss.weapons5.index(weapon))
            else:
                if man.interact(weapon):
                    man.hit_left(5)
                    if weapon in boss.weapons5:
                        boss.weapons5.pop(boss.weapons5.index(weapon))
            
            weapon.y -= 6

            weapon.hitbox = (weapon.x,weapon.y,weapon.width,weapon.height)   #要更新hitbox
            weapon.draw(win)
                
            if weapon.x<0 or weapon.x>1000 or weapon.y<0 or weapon.y>500: #超過視窗後消失，重天裝填子彈
                if weapon in boss.weapons5:
                    boss.weapons5.pop(boss.weapons5.index(weapon))

        pygame.display.update()   #放外面才不會延遲
        
        for weapon in boss.weapons6:
            if boss.center[0] > man.hitbox[0]+man.hitbox[3]:
                if man.interact(weapon):
                    man.hit_right(5)
                    if weapon in boss.weapons6:
                        boss.weapons6.pop(boss.weapons6.index(weapon))
            else:
                if man.interact(weapon):
                    man.hit_left(5)
                    if weapon in boss.weapons6:
                        boss.weapons6.pop(boss.weapons6.index(weapon))
            
            weapon.x += 6
            weapon.y -=6

            weapon.hitbox = (weapon.x,weapon.y,weapon.width,weapon.height)   #要更新hitbox
            weapon.draw(win)
                
            if weapon.x<0 or weapon.x>1000 or weapon.y<0 or weapon.y>500: #超過視窗後消失，重天裝填子彈
                if weapon in boss.weapons6:
                    boss.weapons6.pop(boss.weapons6.index(weapon))

        pygame.display.update()   #放外面才不會延遲
        
        for weapon in boss.weapons7:
            if boss.center[0] > man.hitbox[0]+man.hitbox[3]:
                if man.interact(weapon):
                    man.hit_right(5)
                    if weapon in boss.weapons7:
                        boss.weapons7.pop(boss.weapons7.index(weapon))
            else:
                if man.interact(weapon):
                    man.hit_left(5)
                    if weapon in boss.weapons7:
                        boss.weapons7.pop(boss.weapons7.index(weapon))
            
            weapon.x += 6

            weapon.hitbox = (weapon.x,weapon.y,weapon.width,weapon.height)   #要更新hitbox
            weapon.draw(win)
                
            if weapon.x<0 or weapon.x>1000 or weapon.y<0 or weapon.y>500: #超過視窗後消失，重天裝填子彈
                if weapon in boss.weapons7:
                    boss.weapons7.pop(boss.weapons7.index(weapon))

        pygame.display.update()   #放外面才不會延遲
#==================================================================================#  
        
        #碰到噴射背包就可以飛起來
        if man.interact(jetpack1):    
            jetpack1.visible = False
            man.fly = True

        if arsenal.visible:   #電腦(武器庫)
            if man.interact(arsenal):
                man.equipment = True #腳色此時有C++子彈可供發射，發射數量有限，射完
                man.invincible=True #腳色在電腦範圍內是無敵的，可以抵擋python子彈的攻擊
            else:
                man.invincible=False
        else:
            man.invincible=False
         #在離開電腦之後，腳色身上還是有C++子彈，不過射完就沒了，需要再接觸電腦補充
    
    
        #C++子彈的功能
        for equipment in man.equipment_bullets:
            if boss.x-equipment.x<0:
                man.equipment_bullets.pop(man.equipment_bullets.index(equipment))
                boss.hit(2) ###
            if equipment.x<1200 and equipment.x >0:
                equipment.x += 8
            else:
                man.equipment_bullets.pop(man.equipment_bullets.index(equipment))
            equipment.draw(win)
        pygame.display.update()
        keys = pygame.key.get_pressed()
    
    
    
        if keys[pygame.K_SPACE]:
            man.attack(win)
            
            if boss.health>0:
                if boss.y-man.y <20:   #y方向
                    if man.x<boss.x and man.right==True:
                        if  boss.hitbox[0] - (man.hitbox[0] + man.hitbox[2])<25 :#x方向
                            boss.hit(0.5)
                    elif man.x> boss.x and man.left==True:
                        if man.hitbox[0] - (boss.hitbox[0]+boss.hitbox[2])<25:
                            boss.hit(0.5)
                    
            #C++攻擊
            if man.equipment==True and len(man.equipment_bullets)<5 :
                man.equipment_bullets.append(Equipment_Bullet(man.hitbox[0]+man.hitbox[2],man.hitbox[1]))
                arsenal.equipment-=1
                man.equipment = False

        if keys[pygame.K_LEFT] and man.x>0:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x<1200-man.width:          
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing= False
        else:
            man.standing = True
            man.walkCount = 0
        
        
        if man.fly==False:   #腳色起飛
            if not man.isJump:
                if keys[pygame.K_UP] and not man.fall:
                    man.isJump = True
                    man.right = False
                    man.left = False
                    man.walkCount = 0
            else:
                if man.jumpCount >= 0:
                    man.y -=  (man.jumpCount**2) *0.5
                    man.jumpCount -= 1
                else:
                    man.fall = True
                    man.isJump = False
                    man.jumpCount=10
        
            if man.fall and man.y < man.ground:       #man.y最後必然>430則執行else條件
                man.y += man.fallCount
            else:
                man.fall = False
        else:
            if keys[pygame.K_UP] and man.y>0:
                man.y -= man.vel
            if keys[pygame.K_DOWN] and man.y<436:
                man.y += man.vel
        
        redrawGameWindow_r3(round)

#=================================================================================#

run = True
if round == 3:
    while run:
        pygame.time.Clock().tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            run = False
            round=4
            break
        show_pass(round)

#=================================================================================#

run=True
if round == 4:
    while run:
        pygame.time.Clock().tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            run = False
            pygame.quit()
            break
        show_end(round)
        
#=================================================================================#
#腳色死亡畫面，此時round==-1

run=True
if round == -1:
    while True:
        pygame.time.Clock().tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            run = False
            pygame.quit()
            break
        show_dead(round)