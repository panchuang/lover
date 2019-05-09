# coding=gbk
import pygame
from sys import exit
from pygame.locals import *
import os
import random


def Button(msg,x,y,w,h,color,after_color):
    """

    :param msg: ��ť�ϵ�����
    :param x: ��ť�������Ͻǵ�x����
    :param y: ��ť�������Ͻǵ�y����
    :param w: ��ť���εĿ�
    :param h: ��ť���εĸ�
    :param color: ��ť���ǰ����ɫ����ʽ(0,100,0)
    :param after_color: ��ť��������ɫ����ʽ(0,100,0)
    :return:
    """
    mousex, mousey = pygame.mouse.get_pos()
    # λ��(200,200),���(100,50)
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
        f.write('���ڡ�:����������Ĺ���   :')
        f.write('\n���ڡ�:������������Ա���orŮ��   :')
elif os.path.exists('d:\\'):
    with open("d:\\lovename.txt", 'w') as f:
        f.write('���ڡ�:����������Ĺ���   :')
        f.write('\n���ڡ�:������������Ա���orŮ��   :')
elif os.path.exists('e:\\'):
    with open("e:\\lovename.txt", 'w') as f:
        f.write('���ڡ�:����������Ĺ���   :')
        f.write('\n���ڡ�:������������Ա���orŮ��   :')
else:
    print('�ļ��ж�������')

# �����Ĵ���
out_window = pygame.display.set_mode((612,879),0,32)
# ����
pygame.display.set_caption('Find The He/She')

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('F:\\Pan_Process\\lover\\musics\\taiduo-arong.mp3')
pygame.mixer.music.play(-1,0.0)


# ����ͼƬ
white_bg_image = pygame.image.load('F:\\Pan_Process\\lover\\images\\white_bg.png')
icon_image = pygame.image.load('F:\\Pan_Process\\lover\\images\\pink_heart_icon.png')
bg_image = pygame.image.load('F:\\Pan_Process\\lover\\images\\wedding_kiss_bg_small.png')
start_btn = pygame.image.load('F:\\Pan_Process\\lover\\images\\start_btn2.jpg')
#��ʼ��ť��״̬��FlaseΪС��ť,True��ť���
start_btn_state = False
save_dict = {}
while True:


    # ͼ�ꡢͼƬ
    pygame.display.set_icon(icon_image)
    out_window.blit(white_bg_image, (0, 0))
    out_window.blit(bg_image, (0, 0))
    if start_btn_state:
        start_btn_new = pygame.transform.scale(start_btn, (200, 200))
        out_window.blit(start_btn_new, ((330, 380)))
        start_btn_state = False
    elif start_btn_state == False:
        out_window.blit(start_btn, (350, 400))

    # ����
    font = pygame.font.SysFont('SimHei', 24)
    hello_text_obj1 = font.render('"����', 1, (100, 100, 200))
    hello_text_obj1_1 = font.render('����������/Ů��������"', 1, (100, 100, 200))
    hello_text_obj2 = font.render('"�������˰���', 1, (100, 100, 200))
    hello_text_obj2_1 = font.render('������⻻һ����"', 1, (100, 100, 200))
    hello_text_obj3 = font.render('"�������Ⱑ��', 1, (100, 100, 200))
    hello_text_obj3_1 = font.render('��������һ���𡣡���"', 1, (100, 100, 200))
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

            Button('�������',100,100,200,80,(0,200,0),(0,255,0))
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

                Button("�����е���/��", 230, 220, 150, 60, (255, 255, 255), (255, 255, 255))

                xiangkuang_image = pygame.image.load('F:\\Pan_Process\\lover\\images\\xiangkuang_1.jpg')
                out_window.blit(xiangkuang_image,(131,280))

                if sex == '��':
                    if name == '�˴�':
                        if name in save_dict.keys():
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\' + save_dict[name])
                            out_window.blit(lover, (155, 310))
                        else:
                            mv_list = ['yangmi.jpeg', 'feier.jpeg', 'rongrong.jpeg']
                            mv_name = random.choice(mv_list)
                            save_dict[name] = mv_name
                            lover = pygame.image.load('F:\\Pan_Process\\lover\\images\\woman\\' + mv_name)
                            out_window.blit(lover, (155, 310))
                    elif name == '����':
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
                elif sex == 'Ů':
                    if name == '����' or name == "���Ϸ�" or name == "��ѩ��" or name == "������":
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