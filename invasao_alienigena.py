import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from game_stats import GameStats
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Cria um alienígena
    #alien = Alien(ai_settings, screen)
    pygame.display.set_caption('Invasão Alienígena')
    # Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")
    # Cria uma instância para armazzendas dados estatísticos do jogo
    stats = GameStats(ai_settings)
    #Cria uma espaçonave
    ship =  Ship(ai_settings, screen)
    # Cria um grupo no qual serão armazenados os projéteis e um de alienígenas
    bullets = Group()
    aliens = Group()
    # Cria a frota de alieenígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
run_game()