from plane_sprites import *

# selete_pos = 1


class PlaneGame(object):
    """主程序"""

    def __init__(self):
        print("初始化")

        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 4.设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(FIRE_EVENT, 250)
        # 5.鼠标位置
        # self.mouse_x = 0
        # self.mouse_y = 0

    def __main_menu(self):
        """主菜单

        """
        mainmenu = MainMenu()
        self.main_menu = pygame.sprite.Group(mainmenu)

        self.back_group.update()
        self.back_group.draw(self.screen)
        self.main_menu.update()
        self.main_menu.draw(self.screen)

    def __create_sprites(self):
        """创建精灵组

        """
        # global MyPlaneLife
        # 创建背景
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建我的飞机
        # if MyPlaneLife > 0:

        self.myplane = MyPlane()
        self.myplane_group = pygame.sprite.Group(self.myplane)
        # MyPlaneLife = 0

    def start_game(self):
        """开始游戏

        """
        # global selete_pos
        print("游戏开始")
        # while True:
            # while selete_pos == 1:
            #
            #     self.__main_menu()
            #     self.__event_handle()
            #     # self.__mouse_collide()
            #     self.selete_game()
            #
            #     pygame.display.update()
            #
            #     if selete_pos == 2:
            #         break

        while True:
            # selete_pos == 2:
                # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
                # 2.时间监听
            self.__event_handle()
                # 3.碰撞检测
            self.__check_collide()
                # 4.更新/绘制精灵组
            self.__update_sprites()
                # 5.更新显示
            pygame.display.update()

            # if selete_pos != 2:
            #     break

    # def __mouse_collide(self):
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             PlaneGame.__game_over()
    #         elif event.type == MOUSE_BUTTON_DOWN:  # 检测鼠标点击事件
    #             self.mouse_x, self.mouse_y = pygame.mouse.get_pos()  # get_pos()返回一个单击时鼠标的xy坐标
    #             break

    # def selete_game(self):
    #     global selete_pos
    #     # 选择
    #     if (self.mouse_x > 90) and (self.mouse_x < 390):
    #         if (self.mouse_y > 330) and (self.mouse_y < 370):
    #             selete_pos = 2
    #         else:
    #             selete_pos = 0
    #     else:
    #         selete_pos = 0

    def __event_handle(self):
        """时间监听

        """
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

            elif event.type == FIRE_EVENT:
                # if MyPlaneLife > -1:
                self.myplane.fire()
                # self.myplane_group.add(self.myplane.bullets)

        keys_pressed = pygame.key.get_pressed()
        # 判断按键
        speed = 2
        if keys_pressed[pygame.K_RIGHT]:
            self.myplane.speed_x = speed
            self.myplane.speed_y = 0
        elif keys_pressed[pygame.K_LEFT]:
            self.myplane.speed_x = -speed
            self.myplane.speed_y = 0
        elif keys_pressed[pygame.K_UP]:
            self.myplane.speed_x = 0
            self.myplane.speed_y = -speed
        elif keys_pressed[pygame.K_DOWN]:
            self.myplane.speed_x = 0
            self.myplane.speed_y = speed
        else:
            self.myplane.speed_x = 0
            self.myplane.speed_y = 0

    def __check_collide(self):
        """碰撞检测

        """
        global selete_pos
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.myplane.bullets, self.enemy_group, True, True)

        # 我的飞机和敌机相撞
        enemies = pygame.sprite.spritecollide(self.myplane, self.enemy_group, True)

        if len(enemies) > 0:
            self.myplane.kill()
            # selete_pos = "主菜单"
            pygame.quit()
            exit()

    def __update_sprites(self):
        """更新/绘制精灵组

        """
        # 更新背景
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 更新敌机
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 更新我的飞机
        self.myplane_group.update()
        self.myplane_group.draw(self.screen)
        # 更新子弹
        self.myplane.bullets.update()
        self.myplane.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        """结束游戏

        """
        pygame.quit()
        exit()


if __name__ == '__main__':

    game = PlaneGame()

    game.start_game()
