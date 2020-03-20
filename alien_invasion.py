
import pygame
from pygame.sprite import Group
from settings import  Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建play按钮
    play_button=Button(ai_settings,screen,"Play")
    #创建一艘船
    ship=Ship(screen,ai_settings)
    #创建用于存储子弹的编组
    bullets=Group()
    #创建一群外星人
    aliens=Group()
    #创建状态实例
    stats=GameStats(ai_settings)
    # 创建统计信息
    sb = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings,screen,aliens,ship)

    while True:
        gf.check_events(ship,ai_settings,screen,bullets,play_button,stats,aliens,sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship,stats,sb)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets,sb)
        gf.update_screen(screen,ai_settings,ship,bullets,aliens,play_button,stats,sb)

run_game()