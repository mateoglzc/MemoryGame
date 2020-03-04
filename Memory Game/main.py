import pygame
import math
import random
import time

pygame.init()


# Creates the screen in which the game is played
screen = pygame.display.set_mode((442, 358))

# Creates the lists in which each card is going to be stored
Cardrow1 = []
Cardrow2 = []
Cardrow3 = []
Cardrow4 = []

# Creates the lists in which the numbers asociated with each card are going to be stored
NumRow1 = []
NumRow2 = []
NumRow3 = []
NumRow4 = []

# List in which is number with its pair are going to be store first later to be randomize
list_off = []

# Score
Player1_score = 0
Player2_score = 0

# Turns
Turn = 1

# Cards Class, here are all the values and atributes each card has


class cards(object):

    def __init__(self, name, x, y):
        self.name = name  # Name of the Card
        self.x = x  # X position in which the card is going to be drawn
        self.y = y  # Y position in which the card is going to be drawn
        self.width = 64  # Width of the Card
        self.height = 64  # Height of the card
        # Initial Character of the Card, if matched wrong each card should return to this character
        self.number = '?'
        # This should determine if a card should stay opened or not (this only happens when a card has been matched). True == keep open, False == close
        self.hold_value = False
        # If card is matched correctly this would become the number asigned to that card and should be permently opened
        self.Open_card_number = ''

    # The method draw should draw the card and draw a question mark if the card is not opened, show a number if ony one card has been opened, or show cards that have been correctly matched
    def draw(self, screen, rgb):
        pygame.draw.rect(screen, rgb, (self.x, self.y, 45, 64)
                         )  # Draw the Card
        # Create a font for our Card
        question = pygame.font.Font('freesansbold.ttf', 32)
        if self.hold_value == False:  # This will discriminate each card to see if they are permently opended or not. If not they should display a question mark
            # Creates the question mark so cards that are not permently opended display a question mark
            not_opened = question.render(self.number, True, (255, 255, 255))
            screen.blit(not_opened, (self.x, self.y))  # Displays question mark
        if self.hold_value == True:  # If a card is permently opened this should make that for the entire game they show the number asociated with that card and never turn to a question mark
            opened = question.render(
                self.Open_card_number, True, (255, 255, 255))  # Here we replace the question mark to the number asociated with this card
            screen.blit(opened, (self.x, self.y))  # Display the number

    # This method is run to open a card and show is number, if two cards that have been opened do not match their number they should close
    def Open_Card(self, replacement):
        # We replace for a brief moment the question mark with a number to se if they match a card
        self.number = str(replacement)
        # Same than above, but if card is matched correctly this value should appear for the rest of the game
        self.Open_card_number = str(replacement)
        

    # Function to see if the mouse is above the card
    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height:
            return True
        return False


# Cards

# Creates the cards that are necesary to play, stores them in the list of the row that they belong
space_between = 0
for i in range(8):
    Row1_card = cards(f'Row1_card{i}', 10 + space_between, 10)
    Cardrow1.append(Row1_card)
    space_between += 54
space_between2 = 0
for i in range(8):
    Row2_card = cards(f'Row2_card{i}', 10 + space_between2, 84)
    Cardrow2.append(Row2_card)
    space_between2 += 54
space_between3 = 0
for i in range(8):
    Row3_card = cards(f'Row3_card{i}', 10 + space_between3, 158)
    Cardrow3.append(Row3_card)
    space_between3 += 54
space_between4 = 0
for i in range(8):
    Row4_card = cards(f'Row4_card{i}', 10 + space_between4, 232)
    Cardrow4.append(Row4_card)
    space_between4 += 54


# Creates numbers from 1 to 16, two times
for i in range(1, 17):
    for o in range(2):
        list_off.append(i)

# Shuffles the numbers inside list_off
random.shuffle(list_off)

# Here the board is created by randomizing the position of the numbers and their rows
listas = [NumRow1, NumRow2, NumRow3, NumRow4]
for x in range(len(list_off)):
    if x >= 0 and x <= 7:
        listas[0].append(list_off[x])
    elif x >= 8 and x <= 15:
        listas[1].append(list_off[x])
    elif x >= 16 and x <= 23:
        listas[2].append(list_off[x])
    elif x >= 24 and x <= 32:
        listas[3].append(list_off[x])

print(NumRow1)
print(NumRow2)
print(NumRow3)
print(NumRow4)


# Hold Cards
Cards_opened = 0  # Number of cards opened in a turn
Card1_Save = 0  # The numbers asociated with the first card opened
Card2_Save = 0  # The numbers asociated with the second card opened
Card_location1 = 0  # Where is the first card opened located inside a particular row
Card_location2 = 0  # Where is the second card opened located inside a particular row
Card1_row_location = 0  # In which row is the first card located
Card2_row_location = 0  # In which row is the second card located
Cards_font = pygame.font.Font('freesansbold.ttf', 24)


def Check_if_cards_equal():
    global Player1_score
    global Player2_score
    global Turn
    global Card1_Save
    global Card2_Save
    global Card_location1
    global Card_location2
    global Card1_row_location
    global Card2_row_location
    global Cardrow1
    global Cardrow2
    global Cardrow3
    global Cardrow4
    global Cards_opened
    if Card1_Save != 0 and Card2_Save != 0:  # If both cards have been opened
        if Card1_Save == Card2_Save:  # If both cards are equal
            if Card1_row_location == 1:
                Cardrow1[Card_location1].hold_value == True
                Cardrow1[Card_location1].number == '?'
            if Card1_row_location == 2:
                Cardrow2[Card_location1].hold_value == True
                Cardrow2[Card_location1].number == '?'
            if Card1_row_location == 3:
                Cardrow3[Card_location1].hold_value == True
                Cardrow3[Card_location1].number == '?'
            if Card1_row_location == 4:
                Cardrow4[Card_location1].hold_value == True
                Cardrow4[Card_location1].number == '?'

            if Card2_row_location == 1:
                Cardrow1[Card_location2].hold_value == True
                Cardrow1[Card_location2].number == '?'
            if Card2_row_location == 2:
                Cardrow2[Card_location2].hold_value == True
                Cardrow2[Card_location2].number == '?'
            if Card2_row_location == 3:
                Cardrow3[Card_location2].hold_value == True
                Cardrow3[Card_location2].number == '?'
            if Card2_row_location == 4:
                Cardrow4[Card_location2].hold_value == True
                Cardrow4[Card_location2].number == '?'

            if Turn % 2 != 0:
                Player1_score += 1
                Turn += 1
                Card1_Save = 0
                Card2_Save = 0
                Card_location1 = 0
                Card_location2 = 0
                Card1_row_location = 0
                Card2_row_location = 0
                Cards_opened = 0
            else:
                Player2_score += 1
                Turn += 1
                Card1_Save = 0
                Card2_Save = 0
                Card_location1 = 0
                Card_location2 = 0
                Card1_row_location = 0
                Card2_row_location = 0
                Cards_opened = 0


def Cards_not_equal():
    global Turn
    global Card1_Save
    global Card2_Save
    global Card_location1
    global Card_location2
    global Card1_row_location
    global Card2_row_location
    global Cardrow1
    global Cardrow2
    global Cardrow3
    global Cardrow4
    global Cards_opened
    if Card1_Save != 0 and Card2_Save != 0:
        if Card1_Save != Card2_Save:
            if Card1_row_location == 1:
                Cardrow1[Card_location1].Open_Card('?')
                

            if Card1_row_location == 2:
                Cardrow2[Card_location1].Open_Card('?')

            if Card1_row_location == 3:
                Cardrow3[Card_location1].Open_Card('?')

            if Card1_row_location == 4:
                Cardrow4[Card_location1].Open_Card('?')

            if Card2_row_location == 1:
                Cardrow1[Card_location2].Open_Card('?')
                
            if Card2_row_location == 2:
                Cardrow2[Card_location2].Open_Card('?')

            if Card2_row_location == 3:
                Cardrow3[Card_location2].Open_Card('?')
                
            if Card2_row_location == 4:
                Cardrow4[Card_location2].Open_Card('?')

            Turn += 1
            Card1_Save = 0
            Card2_Save = 0
            Card_location1 = 0
            Card_location2 = 0
            Card1_row_location = 0
            Card2_row_location = 0
            Cards_opened = 0


def Players_score_turns(Turn_num):
    global game_running
    Player_font = pygame.font.Font('freesansbold.ttf', 20)
    win_font = pygame.font.Font('freesansbold.ttf', 20)
    if Turn_num % 2 != 0:
        Player1 = Player_font.render(
            f'Player 1: {Player1_score}', True, (0, 255, 0))
        Player2 = Player_font.render(
            f'Player 2: {Player2_score}', True, (0, 0, 0))
    else:
        Player1 = Player_font.render(
            f'Player 1: {Player1_score}', True, (0, 0, 0))
        Player2 = Player_font.render(
            f'Player 2: {Player2_score}', True, (0, 255, 0))

    screen.blit(Player1, (15, 316))
    screen.blit(Player2, (320, 316))

    if Player1_score > 8:
        Player1_wins = win_font.render('Player 1 Won', True, (0,0,0))
        screen.blit(Player1_wins, (145,316))
        
    if Player2_score > 8:
        Player2_wins = win_font.render('Player 2 Won', True, (0,0,0))
        screen.blit(Player2_wins, (145,316))
        


game_running = True

while game_running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            pass

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(8):
                if Cardrow1[i].isOver(pos):
                    if Cardrow1[i].hold_value == False and Cards_opened != 2:
                        Cardrow1[i].Open_Card(NumRow1[i])
                        Cards_opened += 1
                        if Card1_Save == 0:
                            Card1_Save = NumRow1[i]
                            Card_location1 = i
                            Card1_row_location = 1
                            
                        else:
                            if Card2_Save == 0:
                                Card2_Save = NumRow1[i]
                                Card_location2 = i
                                Card2_row_location = 1
                                
                if Cardrow2[i].isOver(pos):
                    if Cardrow2[i].hold_value == False and Cards_opened != 2:
                        Cardrow2[i].Open_Card(NumRow2[i])
                        Cards_opened += 1
                        if Card1_Save == 0:
                            Card1_Save = NumRow2[i]
                            Card_location1 = i
                            Card1_row_location = 2
                            
                        else:
                            if Card2_Save == 0:
                                Card2_Save = NumRow2[i]
                                Card_location2 = i
                                Card2_row_location = 2
                                
                if Cardrow3[i].isOver(pos):
                    if Cardrow3[i].hold_value == False and Cards_opened != 2:
                        Cardrow3[i].Open_Card(NumRow3[i])
                        Cards_opened += 1
                        if Card1_Save == 0:
                            Card1_Save = NumRow3[i]
                            Card_location1 = i
                            Card1_row_location = 3
                            
                        else:
                            if Card2_Save == 0:
                                Card2_Save = NumRow3[i]
                                Card_location2 = i
                                Card2_row_location = 3
                                
                if Cardrow4[i].isOver(pos):
                    if Cardrow4[i].hold_value == False and Cards_opened != 2:
                        Cardrow4[i].Open_Card(NumRow4[i])
                        Cards_opened += 1
                        if Card1_Save == 0:
                            Card1_Save = NumRow4[i]
                            Card_location1 = i
                            Card1_row_location = 4
                            
                        else:
                            if Card2_Save == 0:
                                Card2_Save = NumRow4[i]
                                Card_location2 = i
                                Card2_row_location = 4
                                


    for i in range(8):
        Cardrow1[i].draw(screen, (0, 0, 128))
        Cardrow2[i].draw(screen, (0, 0, 128))
        Cardrow3[i].draw(screen, (0, 0, 128))
        Cardrow4[i].draw(screen, (0, 0, 128))

    time.sleep(.5)
    
    Check_if_cards_equal()
    Cards_not_equal()

    Players_score_turns(Turn)


    pygame.display.update()
