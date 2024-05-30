import pygame
import random


class Card:
    def __init__(self, point: str, mast: str, img=None):
        self.point = point
        self.mast = mast
        self.img = img


class Deck:
    def __init__(self):
        self.deck = [
            Card('6', '♢', pygame.image.load('cards_bmp/6_b.bmp')),
            Card('6', '♡', pygame.image.load('cards_bmp/6_c.bmp')),
            Card('6', '♤', pygame.image.load('cards_bmp/6_p.bmp')),
            Card('6', '♧', pygame.image.load('cards_bmp/6_t.bmp')),

            Card('7', '♢', pygame.image.load('cards_bmp/7_b.bmp')),
            Card('7', '♡', pygame.image.load('cards_bmp/7_c.bmp')),
            Card('7', '♤', pygame.image.load('cards_bmp/7_p.bmp')),
            Card('7', '♧', pygame.image.load('cards_bmp/7_t.bmp')),

            Card('8', '♢', pygame.image.load('cards_bmp/8_b.bmp')),
            Card('8', '♡', pygame.image.load('cards_bmp/8_c.bmp')),
            Card('8', '♤', pygame.image.load('cards_bmp/8_p.bmp')),
            Card('8', '♧', pygame.image.load('cards_bmp/8_t.bmp')),

            Card('9', '♢', pygame.image.load('cards_bmp/9_b.bmp')),
            Card('9', '♡', pygame.image.load('cards_bmp/9_c.bmp')),
            Card('9', '♤', pygame.image.load('cards_bmp/9_p.bmp')),
            Card('9', '♧', pygame.image.load('cards_bmp/9_t.bmp')),

            Card('10', '♢', pygame.image.load('cards_bmp/10_b.bmp')),
            Card('10', '♡', pygame.image.load('cards_bmp/10_c.bmp')),
            Card('10', '♤', pygame.image.load('cards_bmp/10_p.bmp')),
            Card('10', '♧', pygame.image.load('cards_bmp/10_t.bmp')),

            Card('j', '♢', pygame.image.load('cards_bmp/j_b.bmp')),
            Card('j', '♡', pygame.image.load('cards_bmp/j_c.bmp')),
            Card('j', '♤', pygame.image.load('cards_bmp/j_p.bmp')),
            Card('j', '♧', pygame.image.load('cards_bmp/j_t.bmp')),

            Card('q', '♢', pygame.image.load('cards_bmp/q_b.bmp')),
            Card('q', '♡', pygame.image.load('cards_bmp/q_c.bmp')),
            Card('q', '♤', pygame.image.load('cards_bmp/q_p.bmp')),
            Card('q', '♧', pygame.image.load('cards_bmp/q_t.bmp')),

            Card('k', '♢', pygame.image.load('cards_bmp/k_b.bmp')),
            Card('k', '♡', pygame.image.load('cards_bmp/k_c.bmp')),
            Card('k', '♤', pygame.image.load('cards_bmp/k_p.bmp')),
            Card('k', '♧', pygame.image.load('cards_bmp/k_t.bmp')),

            Card('t', '♢', pygame.image.load('cards_bmp/t_b.bmp')),
            Card('t', '♡', pygame.image.load('cards_bmp/t_c.bmp')),
            Card('t', '♤', pygame.image.load('cards_bmp/t_p.bmp')),
            Card('t', '♧', pygame.image.load('cards_bmp/t_t.bmp'))]

        # Перемешиваем колоду
        for _ in range(5):
            random.shuffle(self.deck)


if __name__ == '__main__':
    ...
