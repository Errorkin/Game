import pygame
import random


class Player:
    __translate = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 2, 'q': 3, 'k': 4, 't': 11}

    def __init__(self):
        self.hand = []
        self.tuzs = 0
        self.score = 0

    def get_card(self, screen, main_deck, draw_x: int, draw_y: int) -> bool:
        # Проверка на перебор
        if self.get_score() >= 21:
            return True

        # Берем случайную карту, добавляем к себе, удаляем из колоды
        card = random.choice(main_deck.deck)
        main_deck.deck.remove(card)
        self.hand.append(card)

        # Отрисовываем карту
        card_img = pygame.transform.scale(card.img, (130, 175))
        screen.blit(card_img, card_img.get_rect(center=(draw_x, draw_y)))

        # Увеличиваем счет на номинал карты
        self.score += self.__class__.__translate.get(card.point)

        # Проверка, является ли карта тузом
        if card.point == 't':
            self.tuzs += 1

        # Проверка на перебор
        if self.get_score() >= 21:
            return True
        return False

    def get_score(self) -> int:
        if not self.tuzs:
            return self.score
        while self.tuzs != 0 and self.score > 21:
            self.score -= 10
            self.tuzs -= 1
        return self.score


def who_win(player: Player, comp: Player) -> str:
    pscore = player.get_score()
    cscore = comp.get_score()

    if pscore > 21:
        return 'Поражение'.center(10)
    if pscore == 21:
        if cscore == 21:
            return 'Ничья'.center(10)
        else:
            return 'Победа'.center(10)
    else:
        if cscore > 21:
            return 'Победа'.center(10)
        if cscore == 21:
            return 'Поражение'.center(10)
        if pscore == cscore:
            return 'Ничья'.center(10)
        if pscore < cscore:
            return 'Поражение'.center(10)
        if pscore > cscore:
            return 'Победа'.center(10)


if __name__ == '__main__':
    ...
