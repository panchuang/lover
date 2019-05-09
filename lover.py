# coding=gbk
import pygame
from sys import exit
from pygame.locals import *
import os
import random


def Button(msg,x,y,w,h,color,after_color):
    """

    :param msg: 按钮上的文字
    :param x: 按钮矩形左上角的x坐标
    :param y: 按钮矩形左上角的y坐标
    :param w: 按钮矩形的宽
    :param h: 按钮矩形的高
    :param color: 按钮点击前的颜色，格式(0,100,0)
    :param after_color: 按钮点击后的颜色，格式(0,100,0)
    :return:
    """
    mousex, mousey = pygame.mouse.get_pos()
    # 位置(200,200),宽高(100,50)
    if x+w > mousex > x and y+h > mousey > y:
        pygame.draw.rect(out_window, color, (x, y, w, h))
    else:
        pygame.draw.rect(out_window, after_color, (x, y, w, h))
    btn_font = pygame.font.SysFont('SimHei', 24)
    name_txt = btn_font.render(msg, 1, (100, 100, 200))
    name_pos = name_txt.get_rect()
    name_pos.center = ((x+(w/2)), (y+(h/2)))
    out_window.blit(name_txt, name_pos)


if os.path.exists('f:\\'):
    with open("f:\\lovename.txt", 'w') as f:
        f.write('请在“:”后留下你的狗名   :')
        f.write('\n请在“:”后留下你的性别（男or女）   :')
elif os.path.exists('d:\\'):
    with open("d:\\lovename.txt", 'w') as f:
        f.write('请在“:”后留下你的狗名   :')
        f.write('\n请在“:”后留下你的性别（男or女）   :')
elif os.path.exists('e:\\'):
    with open("e:\\lovename.txt", 'w') as f:
        f.write('请在“:”后留下你的狗名   :')
        f.write('\n请在“:”后留下你的性别（男or女）   :')
else:
    print('文件夹都不存在')

# 最外层的窗口
out_window = pygame.display.set_mode((612,879),0,32)
# 标题
pygame.display.set_caption('Find The He/She')

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('F:\\Pan_Process\\lover\\musics\\taiduo-arong.mp3')
pygame.mixer.music.play(-1,0.0)


# 加载图片
white_bg_image = pygame.image.load('F:\\Pan_Process\\lover\\images\\white_bg.png')
icon_image = pygame.image.load('F:\\Pan_Process\\lover\\images\\pink_heart_icon.png')
bg_image = pygame.image.load('F:\\Pan_Process\\lover\\images\\wedding_kiss_bg_small.png')
start_btn = pygame.image.load('F:\\Pan_Process\\lover\\images\\start_btn2.jpg')
#开始按钮的状态，Flase为小按钮,True按钮变大
start_btn_state = False
save_dict = {}
while True:


    # 图标、图片
    pygame.display.set_icon(icon_image)
    out_window.blit(white_bg_image, (0, 0))
    out_window.blit(bg_image, (0, 0))
    if start_btn_state:
        start_btn_new = pygame.transform.scale(start_btn, (200, 200))
        out_window.blit(start_btn_new, ((330, 380)))
        start_btn_state = False
    elif start_btn_state == False:
        out_window.blit(start_btn, (350, 400))

    # 文字
    font = pygame.font.SysFont('SimHei', 24)
    hello_text_obj1 = font.render('"请问', 1, (100, 100, 200))
    hello_text_obj1_1 = font.render('你有男朋友/女朋友了吗？"', 1, (100, 100, 200))
    hello_text_obj2 = font.render('"啊！有了啊。', 1, (100, 100, 200))
    hello_text_obj2_1 = font.render('那你介意换一个吗？"', 1, (100, 100, 200))
    hello_text_obj3 = font.render('"啊！介意啊。', 1, (100, 100, 200))
    hello_text_obj3_1 = font.render('那你介意多一个吗。。。"', 1, (100, 100, 200))
    hello_text_pos1 = hello_text_obj1.get_rect()
    hello_text_pos1_1 = hello_text_obj1_1.get_rect()
    hello_text_pos2 = hello_text_obj2.get_rect()
    hello_text_pos2_1 = hello_text_obj2_1.get_rect()
    hello_text_pos3 = hello_text_obj3.get_rect()
    hello_text_pos3_1 = hello_text_obj3_1.get_rect()
    hello_text_pos1.move_ip(260, 58)
    hello_text_pos1_1.move_ip(260, 98)
    hello_text_pos2.move_ip(260, 138)
    hello_text_pos2_1.move_ip(260, 178)
    hello_text_pos3.move_ip(260, 218)
    hello_text_pos3_1.move_ip(260, 258)
    out_window.blit(hello_text_obj1, hello_text_pos1)
    out_window.blit(hello_text_obj1_1, hello_text_pos1_1)
    out_window.blit(hello_text_obj2, hello_text_pos2)
    out_window.blit(hello_text_obj2_1, hello_text_pos2_1)
    out_window.blit(hello_text_obj3, hello_text_pos3)
    out_window.blit(hello_text_obj3_1, hello_text_pos3_1)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEMOTION and 350 <= pygame.mouse.get_pos()[0] <= 500 and 400 <= pygame.mouse.get_pos()[1] <= 550:
            start_btn_state = True
        elif event.type == MOUSEBUTTONDOWN and 350 <= pygame.mouse.get_pos()[0] <= 500 and 400 <= pygame.mouse.get_pos()[1] <= 550:
            out_window.fill((255,255,255))

            Button('你的名字',100,100,200,80,(0,200,0),(0,255,0))
            pygame.display.update()
            save_dict = {}
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    elif event.type == MOUSEBUTTONDOWN and 100 <= pygame.mouse.get_pos()[0] <= 300 and 100 <= pygame.mouse.get_pos()[1] <= 180:
                        if os.path.exists('f:\\lovename.txt'):
                            os.system('start f:\\lovename.txt')
                        elif os.path.exists('d:\\lovename.txt'):
                            os.system('start d:\\lovename.txt')
                        elif os.path.exists('e:\\lovename.txt'):
                            os.system('start e:\\lovename.txt')

                if os.path.exists('f:\\lovename.txt'):
                    with open('f:\\lovename.txt','r') as f:
                        data_list = f.readlines()
                        name = data_list[0]
                        name = name.split(':')[-1]
                        name = name.replace("\n","")
                        sex = data_list[1]
                        sex = sex.split(':')[-1]
                elif os.path.exists('d:\\lovename.txt'):
                    with open('f:\\lovename.txt','r') as f:
                        data_list = f.readlines()
                        name = data_list[0]
                        name = name.split(':')[-1]
                        name = name.replace("\n", "")
                        sex = data_list[1]
                        sex = sex.split(':')[-1]
                elif os.path.exists('e:\\lovename.txt'):
                    with open('f:\\lovename.txt','r') as f:
                        data_list = f.readlines()
                        name = data_list[0]
                        name = name.split(':')[-1]
                        name = name.replace("\n", "")
                        sex = data_list[1]
                        sex = sex.split(':')[-1]
                else:
                    name = None
                    sex = None
                Button(name,350,100,150,80,(255,255,255),(255,255,255))

                Button("你命中的他/她", 230, 220, 150, 60, (255, 255, 255), (255, 255, 255))

                xiangkuang_image = pygame.image.load('F:\\Pan_Process\\lover\\images\\xiangkuang_1.jpg')
                out_window.blit(xiangkuang_image,(131,280))

                if sex == '男':
                    if name == '潘闯':
                        if name in save_dict.keys():
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\' + save_dict[name])
                            out_window.blit(lover, (155, 310))
                        else:
                            mv_list = ['yangmi.jpeg', 'feier.jpeg', 'rongrong.jpeg']
                            mv_name = random.choice(mv_list)
                            save_dict[name] = mv_name
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\' + mv_name)
                            out_window.blit(lover, (155, 310))
                    elif name == '王豪':
                        if name in save_dict.keys():
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\' + save_dict[name])
                            out_window.blit(lover, (155, 310))
                        else:
                            save_dict[name] = 'fengjie.jpeg'
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\fengjie.jpeg')
                            out_window.blit(lover, (155, 310))
                    else:
                        if name in save_dict.keys():
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\' + save_dict[name])
                            out_window.blit(lover, (155, 310))
                        else:
                            num = random.randint(1, 17)
                            save_dict[name] = num
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\' + str(num) + '.jpeg')
                            out_window.blit(lover, (155, 310))
                elif sex == '女':
                    if name == '杨幂' or name == "朱孟飞" or name == "朱雪菲" or name == "李蓉蓉":
                        if name in save_dict.keys():
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\' + save_dict[name])
                            out_window.blit(lover, (155, 310))
                        else:
                            save_dict[name] = 'pp.jpeg'
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\man\\pp.jpeg')
                            out_window.blit(lover, (155, 310))
                    else:
                        if name in save_dict.keys():
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\' + save_dict[name])
                            out_window.blit(lover, (155, 310))
                        else:
                            num = random.randint(1, 17)
                            save_dict[name] = num
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\man\\' + str(num) + '.jpeg')
                            out_window.blit(lover, (155, 310))
                else:
                    pass
                pygame.display.update()

    pygame.display.update()