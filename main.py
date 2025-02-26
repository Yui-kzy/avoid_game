import pygame
import sys
import random
import time
import math
import webbrowser
pygame.init()
time0 = time.time()
sobj_x=400
sobj_y=300
# 設定視窗大小
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Game")


# 定義人物的初始位置和速度
player_x, player_y = 20, 580
player_speed = 5
rect_size = 15


# 定義物體的初始速度和大小
initial_objects = 5
objects = []
sobj=[]
item=[]
i=0


# 設定計時器
start1_time = time.time()
start2_time = time.time()
start3_time = time.time()
item_stime=time.time()
stop_time=0
interval = 0.8
add = 5
add2=15
# 設定字體和字體大小
font = pygame.font.Font(None, 36)


# 初始化高時間
high_time1 = 0 #難
high_time2 = 0 #簡單
high_time3 = 0 #中等
game_mode=0
# 讀取高時間
try:
   with open("high_time1.txt", "r") as file:
       high_time1 = float(file.read())
except FileNotFoundError:
   pass
try:
   with open("high_time2.txt", "r") as file:
       high_time2 = float(file.read())
except FileNotFoundError:
   pass
try:
   with open("high_time3.txt", "r") as file:
       high_time3 = float(file.read())
except FileNotFoundError:
   pass
button_rect1 = pygame.Rect(300,50,200,100)
button_rect2 = pygame.Rect(300,250,200,100)
button_rect3 = pygame.Rect(300,450,200,100)
button_rect4 = pygame.Rect(700,500,80,50)
button_color = (150, 150, 150)
hover_color = (0, 200, 255)
text_color = (0,0,0)
button_text1 = font.render("Easy", True, text_color)
text_rect1 = button_text1.get_rect(center=button_rect1.center)
button_text2 = font.render("Normal", True, text_color)
text_rect2 = button_text2.get_rect(center=button_rect2.center)
button_text3 = font.render("Hard", True, text_color)
text_rect3 = button_text3.get_rect(center=button_rect3.center)
button_text4 = font.render("rule", True, text_color)
text_rect4 = button_text4.get_rect(center=button_rect4.center)
while True:
   if game_mode==0:
       player_x, player_y = 20, 580
       window_size = (800, 600)
       if i==0:
           pygame.display.set_mode(window_size)
           i+=1
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == pygame.MOUSEBUTTONDOWN:
               # 檢查滑鼠點擊是否在按鈕範圍內
               keys = pygame.key.get_pressed()
               if button_rect1.collidepoint(event.pos)or keys[pygame.K_1]:
                   objects = []
                   sobj = []
                   item = []
                   for _ in range(initial_objects):
                       objects.append({'x': 400, 'y': 300, 'speed': 4, 'size': rect_size,
                                       'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
                   sobj.append({'x': 400, 'y': 300, 'speed': 2, 'size': rect_size,
                                'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
                   time0=time.time()
                   start1_time = time.time()
                   start2_time = time.time()
                   start3_time = time.time()
                   item_stime = time.time()
                   game_mode=2


               if button_rect2.collidepoint(event.pos)or keys[pygame.K_2]:
                   objects = []
                   sobj = []
                   item = []
                   for _ in range(initial_objects):
                       objects.append({'x': 400, 'y': 300, 'speed': 4, 'size': rect_size,
                                       'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
                   sobj.append({'x': 400, 'y': 300, 'speed': 2, 'size': rect_size,
                                'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
                   time0 = time.time()
                   start1_time = time.time()
                   start2_time = time.time()
                   start3_time = time.time()
                   item_stime = time.time()
                   game_mode=3
               if button_rect3.collidepoint(event.pos)or keys[pygame.K_3] :
                   objects = []
                   sobj = []
                   item = []
                   for _ in range(initial_objects):
                       objects.append({'x': 400, 'y': 300, 'speed': 4, 'size': rect_size,
                                       'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
                   sobj.append({'x': 400, 'y': 300, 'speed': 2, 'size': rect_size,
                                'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
                   time0 = time.time()
                   start1_time = time.time()
                   start2_time = time.time()
                   start3_time = time.time()
                   item_stime = time.time()
                   game_mode=1
               if button_rect4.collidepoint(event.pos) :
                   webbrowser.open('https://docs.google.com/document/d/1dvAZmucP3st5ffV41awTrLjanDLdg4iPHslGUye4AUg/edit?usp=sharing')


       # 檢查滑鼠是否在按鈕範圍內，根據狀態設定按鈕顏色
       screen.fill((255, 255, 255))
       if button_rect1.collidepoint(pygame.mouse.get_pos()):
           pygame.draw.rect(screen, hover_color, button_rect1)
       else:
           pygame.draw.rect(screen, button_color, button_rect1)
       if button_rect2.collidepoint(pygame.mouse.get_pos()):
           pygame.draw.rect(screen, hover_color, button_rect2)
       else:
           pygame.draw.rect(screen, button_color, button_rect2)
       if button_rect3.collidepoint(pygame.mouse.get_pos()):
           pygame.draw.rect(screen, hover_color, button_rect3)
       else:
           pygame.draw.rect(screen, button_color, button_rect3)
       if button_rect4.collidepoint(pygame.mouse.get_pos()):
           pygame.draw.rect(screen, hover_color, button_rect4)
       else:
           pygame.draw.rect(screen, button_color, button_rect4)


       screen.blit(button_text1, text_rect1)
       screen.blit(button_text2, text_rect2)
       screen.blit(button_text3, text_rect3)
       screen.blit(button_text4, text_rect4)
           # 更新畫面
       pygame.display.flip()


           # 控制遊戲更新速度
       pygame.time.Clock().tick(60)
   else:
       window_size = (800, 600)


       for event in pygame.event.get():
           if event.type == pygame.QUIT:
 
               with open("high_time1.txt", "w") as file:
                   file.write(str(high_time1))
               with open("high_time2.txt", "w") as file:
                   file.write(str(high_time2))
               with open("high_time3.txt", "w") as file:
                   file.write(str(high_time3))
               pygame.quit()
               sys.exit()


       # 檢查是否過了指定的時間
       elapsed_time = time.time() - start1_time
       addtime = time.time() - start2_time
       add2time = time.time() - start3_time


       if time.time() - stop_time >= 3:


           if elapsed_time >= interval:
               # 重新選擇方向和速度
               for obj in objects:
                   obj['direction'] = (random.uniform(-1, 1), random.uniform(-1, 1))
                   if game_mode==1:#難
                       obj['speed'] = random.uniform(6, 10)
                   if game_mode==2:#簡單
                       obj['speed'] =6
                   if game_mode==3:#中等
                       obj['speed'] =random.uniform(6,8)
               start1_time = time.time()


       else:
           for obj in objects:
               obj['speed'] = 3
           if elapsed_time >= interval:
               # 重新選擇方向和速度
               for obj in objects:
                   obj['direction'] = (random.uniform(-1, 1), random.uniform(-1, 1))
               start1_time = time.time()


       if addtime >= add:
           if game_mode==1:
               objects.append({'x': 400, 'y': 300, 'speed': random.uniform(6, 10), 'size': rect_size,'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
           if game_mode==2:
               objects.append({'x': 400, 'y': 300, 'speed':6, 'size': rect_size,'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
           if game_mode == 3:
               objects.append({'x': 400, 'y': 300, 'speed': random.uniform(6, 8), 'size': rect_size,'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
           start2_time = time.time()


       if add2time >= add2:
           sobj.append({'x': random.choice([400, 0, 800]), 'y': random.choice([0, 300, 600]), 'speed': 2, 'size': rect_size,'direction': (random.uniform(-1, 1), random.uniform(-1, 1))})
           start3_time = time.time()


       if time.time() - item_stime >= 10:
           item.append({'x': random.choice([50, 400, 750]), 'y': random.choice([50, 550])})
           item_stime = time.time()


       for ooo in sobj:
           direction_vector = pygame.math.Vector2(player_x - ooo['x'], player_y - ooo['y']).normalize()


           # 更新物體位置
           ooo['x'] += direction_vector.x * ooo['speed']
           ooo['y'] += direction_vector.y * ooo['speed']


           # 確保物體不會超出視窗邊界
           ooo['x'] = max(0, min(ooo['x'], window_size[0]))
           ooo['y'] = max(0, min(ooo['y'], window_size[1]))


       # 根據按鍵狀態更新人物位置
       keys = pygame.key.get_pressed()


       if keys[pygame.K_UP]:
           player_y -= player_speed
       if keys[pygame.K_DOWN]:
           player_y += player_speed
       if keys[pygame.K_LEFT]:
           player_x -= player_speed
       if keys[pygame.K_RIGHT]:
           player_x += player_speed
       if keys[pygame.K_w]:
           player_y -= player_speed
       if keys[pygame.K_s]:
           player_y += player_speed
       if keys[pygame.K_a]:
           player_x -= player_speed
       if keys[pygame.K_d]:
           player_x += player_speed


       # 更新物體位置
       for obj in objects:
           obj['x'] += obj['direction'][0] * obj['speed']
           obj['y'] += obj['direction'][1] * obj['speed']


           # 確保 obj 不會超出視窗邊界
           obj['x'] = max(0, min(obj['x'], window_size[0]))
           obj['y'] = max(0, min(obj['y'], window_size[1]))
           if obj['x'] == 0:
               obj['direction'] = (-obj['direction'][0], obj['direction'][1])
           if obj['x'] == window_size[0]:
               obj['direction'] = (-obj['direction'][0], obj['direction'][1])
           if obj['y'] == 0:
               obj['direction'] = (obj['direction'][0], -obj['direction'][1])
           if obj['y'] == window_size[1]:
               obj['direction'] = (obj['direction'][0], -obj['direction'][1])


       # 畫面清空
       screen.fill((255, 255, 255))


       # 確保 player 不會超出視窗邊界
       player_x = max(0, min(player_x, 785))
       player_y = max(0, min(player_y, 585))


       # 畫出人物
       pygame.draw.rect(screen, (0, 80, 20), (int(player_x), int(player_y), rect_size, rect_size))
       for ooo in sobj:
           pygame.draw.rect(screen, (150, 0, 100), (int(ooo['x']), int(ooo['y']), rect_size, rect_size))


       for iii in item:
           pygame.draw.rect(screen, (0, 255, 0), (int(iii['x']), int(iii['y']), rect_size, rect_size))


       player_rect = pygame.Rect(player_x, player_y, rect_size, rect_size)
       for iii in item:
           item_rect = pygame.Rect(iii['x'] - rect_size // 2, iii['y'] - rect_size // 2, rect_size, rect_size)
           if player_rect.colliderect(item_rect):
               stop_time = time.time()
               item.remove(iii)


       for obj in objects:
           obj_rect = pygame.Rect(obj['x'] - obj['size'] // 2, obj['y'] - obj['size'] // 2, obj['size'], obj['size'])


           if player_rect.colliderect(obj_rect):
               abb = time.time() - time0
               pygame.display.set_mode((300, 100))
               game_over_text = font.render("Game Over", True, (255, 0, 0))
               time_text = font.render(f"Time: {abb:.1f} seconds", True, (0, 0, 255))
               screen.blit(game_over_text, (50, 20))
               screen.blit(time_text, (50, 50))
               pygame.display.flip()
               pygame.time.delay(500)
               # 禁用其他事件
               for obj in objects:
                   objects.remove(obj)
               for obj in sobj:
                   sobj.remove(obj)
               for obj in item:
                   item.remove(obj)
               pygame.time.delay(500)


               if game_mode==1:
                   with open("high_time1.txt", "w") as file:
                       file.write(str(high_time1))
               if game_mode==2:
                   with open("high_time2.txt", "w") as file:
                       file.write(str(high_time2))
               if game_mode == 3:
                   with open("high_time3.txt", "w") as file:
                       file.write(str(high_time3))
               i=0
               game_mode=0


       for ooo in sobj:
           sobj_rect = pygame.Rect(ooo['x'], ooo['y'], rect_size, rect_size)
           if player_rect.colliderect(sobj_rect):
               abb = time.time() - time0
               pygame.display.set_mode((300, 100))
               game_over_text = font.render("Game Over", True, (255, 0, 0))
               time_text = font.render(f"Time: {abb:.1f} seconds", True, (0, 0, 255))
               screen.blit(game_over_text, (50, 20))
               screen.blit(time_text, (50, 50))
               pygame.display.flip()
               pygame.time.delay(500)
               # 禁用其他事件
               for obj in objects:
                   objects.remove(obj)
               for obj in sobj:
                   sobj.remove(obj)
               for obj in item:
                   item.remove(obj)
               pygame.time.delay(500)
               if game_mode == 1:
                   with open("high_time1.txt", "w") as file:
                       file.write(str(high_time1))
               if game_mode == 2:
                   with open("high_time2.txt", "w") as file:
                       file.write(str(high_time2))
               if game_mode == 3:
                   with open("high_time3.txt", "w") as file:
                       file.write(str(high_time3))
               i=0
               game_mode = 0


       # 畫出物體
       for obj in objects:
           pygame.draw.rect(screen, (255, 0, 0),
                            (int(obj['x']) - obj['size'] // 2, int(obj['y']) - obj['size'] // 2, obj['size'], obj['size']))


       # 顯示時間
       current_time = time.time() - time0
       if game_mode == 1:
           text = f"time: {current_time:.1f} | high time: {high_time1:.1f}"
       if game_mode == 2:
           text = f"time: {current_time:.1f} | high time: {high_time2:.1f}"
       if game_mode == 3:
           text = f"time: {current_time:.1f} | high time: {high_time3:.1f}"


       text_surface = font.render(text, True, (0, 0, 0))
       screen.blit(text_surface, (10, 10))


       # 更新高時間
       if game_mode==1:
           if current_time > high_time1:
               high_time1 = current_time
       if game_mode==2:
           if current_time > high_time2:
               high_time2 = current_time
       if game_mode==3:
           if current_time > high_time3:
               high_time3 = current_time


       # 更新畫面
       pygame.display.flip()


       # 控制遊戲更新速度
       pygame.time.Clock().tick(60)
