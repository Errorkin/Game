import pygame
import sys

import FinalCards
import FinalPlayers

# важные штуки pygame и константы`
pygame.init()
font = pygame.font.Font(None, 100)
clock = pygame.time.Clock()
FPS = 60
screen_size = (1024, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# инициализация начального окна
pygame.display.set_icon(pygame.image.load(r'cards_bmp\ikon.bmp'))
start_screen = pygame.display.set_mode(screen_size)
background = pygame.image.load(r'cards_bmp\table.bmp')
background = pygame.transform.scale(background, screen_size)
start_screen.blit(background, background.get_rect())

# текстовые поля
start_screen.blit(font.render(f"Управление:  ", 1, BLACK, WHITE), (100, 100))
start_screen.blit(font.render(f"Пробел : перезапуск  ", 1, BLACK, WHITE), (100, 200))
start_screen.blit(font.render(f"Вправо  : взять карту  ", 1, BLACK, WHITE), (100, 300))
start_screen.blit(font.render(f"Влево : остановиться  ", 1, BLACK, WHITE), (100, 400))

# важные переменные
is_game_run = False
game_deck = None
player = None
comp = None
player_draw_x, player_draw_y = 100, 425
comp_draw_x, comp_draw_y = 100, 150

# основной цикл событий
while True:
    clock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        # нажатие на крестик - закрытие игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # нажатие клавиши на клавиатуре
        if event.type == pygame.KEYDOWN:
            # нажатие Esc
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # нажатие пробела - запуск игры заново
            if event.key == pygame.K_SPACE:

                if not is_game_run:
                    is_game_run = True
                    start_screen.blit(background, background.get_rect())

                    game_deck = FinalCards.Deck()  # Создание колоды карт

                    player = FinalPlayers.Player()  # Создание игрока

                    # Координаты отрисовки карт игрока
                    player_draw_x = 100
                    player_draw_y = 400

                    # Автоматически берем первую карту
                    player.get_card(screen=start_screen, main_deck=game_deck, draw_x=player_draw_x,
                                    draw_y=player_draw_y)
                    player_draw_x += 75

                    # Отрисовка счета игрока
                    start_screen.blit(font.render(f"{player.get_score():^4}", 1, BLACK, WHITE), (800, 400))

                    comp = FinalPlayers.Player()  # Создание компьютера как соперника

                    # Координаты отрисовки карт компьютера
                    comp_draw_x = 100
                    comp_draw_y = 150

                    # Автоматически берется одна карта для компьютера
                    comp.get_card(screen=start_screen, main_deck=game_deck, draw_x=comp_draw_x,
                                  draw_y=comp_draw_y)
                    comp_draw_x += 75

                    # Отрисовываем счет компьютера
                    start_screen.blit(font.render(f"{comp.get_score():^4}", 1, BLACK, WHITE), (800, 100))

            # нажатие на стрелку вправо - взять карту_
            if event.key == pygame.K_RIGHT:

                if is_game_run:
                    # Берем карту и проверяем условие: счет => 21
                    need_finish = player.get_card(screen=start_screen, main_deck=game_deck, draw_x=player_draw_x,
                                                  draw_y=player_draw_y)
                    start_screen.blit(font.render(f"{player.get_score():^4}", 1, WHITE, WHITE), (800, 400))
                    start_screen.blit(font.render(f"{player.get_score():^4}", 1, BLACK, WHITE), (800, 400))

                    # Если счет < 21, ждем дальнейших действий игрока
                    if not need_finish:
                        player_draw_x += 75

                        continue
                    # Иначе передаем очередь хода компьютеру, он решает игровую ситуацию для себя
                    # Компьютер решит игровую ситуацию для себя, после чего подведутся итоги и победитель
                    else:
                        while comp.get_score() <= 17:
                            comp.get_card(screen=start_screen, main_deck=game_deck, draw_x=comp_draw_x,
                                          draw_y=comp_draw_y)
                            comp_draw_x += 75
                        start_screen.blit(font.render(f"{comp.get_score():^4}", 1, WHITE, WHITE), (800, 100))
                        start_screen.blit(font.render(f"{comp.get_score():^4}", 1, BLACK, WHITE), (800, 100))

                        start_screen.blit(font.render(FinalPlayers.who_win(player, comp), 1, WHITE, WHITE),
                                          (300, 510))
                        start_screen.blit(font.render(FinalPlayers.who_win(player, comp), 1, BLACK, WHITE),
                                          (300, 510))
                        is_game_run = False

            # Нажатие на стрелку влево - перестать брать карты, передать ход компьютеру.
            # Компьютер решит игровую ситуацию для себя, после чего подведутся итоги и победитель
            if event.key == pygame.K_LEFT:

                if is_game_run:
                    while comp.get_score() <= 17:
                        comp.get_card(screen=start_screen, main_deck=game_deck, draw_x=comp_draw_x,
                                      draw_y=comp_draw_y)
                        start_screen.blit(font.render(f"{comp.get_score():^4}", 1, WHITE, WHITE), (800, 100))
                        start_screen.blit(font.render(f"{comp.get_score():^4}", 1, BLACK, WHITE), (800, 100))
                        comp_draw_x += 75

                    start_screen.blit(font.render(FinalPlayers.who_win(player, comp), 1, WHITE, WHITE),
                                      (300, 510))
                    start_screen.blit(font.render(FinalPlayers.who_win(player, comp), 1, BLACK, WHITE),
                                      (300, 510))

                    is_game_run = False
