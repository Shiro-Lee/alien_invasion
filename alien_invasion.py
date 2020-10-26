import pygame
import game_functions as gf
import os
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard


def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 设置窗口位置
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (280, 100)
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(screen, '- Play -')

    # 背景图
    background = pygame.image.load('images/background.jpg').convert()

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    gf.load_high_score(stats)

    # 创建一艘飞船、一个用于存储子弹的编组
    ship = Ship(ai_settings, screen)
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb,  ship, aliens, bullets)
        gf.update_screen(background, ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
