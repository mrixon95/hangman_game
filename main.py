import pygame
import os
import math
import random

# Set up the pygame module
pygame.init()


# button variables
RADIUS = 20
GAP = 15
# Width and height of screen
WIDTH, HEIGHT = 800, 500
letters = [] # bunch of pairs for the letters
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
  y = starty + ((i // 13) * (GAP + RADIUS * 2))
  letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


win = pygame.display.set_mode((WIDTH, HEIGHT))
# set name
pygame.display.set_caption("Hangman Game!")

# load images
images = []
for i in range(7):
  image = pygame.image.load("hangman" + str(i) + ".png")
  images.append(image)

# images get converted into surfaces
print(images)

# game variables
hangman_status = 0
words = ["IDE", "REPLIT", "PYTHON", "PYGAME"]
word = random.choice(words)
guessed = []

# colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# create a game loop
# checks for clicks, collusions

# define a function for drawing the buttons
def draw():
      # fill window with colour white
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
      if letter in guessed:
        display_word += letter + " "
      else:
        display_word += "_ "

    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400,200))

    for letter in letters:
      x, y, ltr, visible = letter
      # x, y is the center of the button
      # draw it on the window, colour black, center position, radius length, thickness of circumfrance
      if visible:
        # only draw visible letters
        pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)

        # Render text
        # Anti aliasing is 1
        text = LETTER_FONT.render(ltr, 1, BLACK)
        win.blit(text, (x-text.get_width()/2,y-text.get_height()/2))

    # draw image, second argument is the top left hand corner
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
  pygame.time.delay(1000)
  win.fill(WHITE)
  text = WORD_FONT.render(message, 1, BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))

  pygame.display.update()
  pygame.time.delay(3000)



def main():
  global hangman_status
# Frames per second
  FPS = 60
  clock = pygame.time.Clock()
  run = True


  # runs until the game is finished
  while run:

    clock.tick(FPS)

    # look through all the events
    for event in pygame.event.get():
        # Click red x button
        if event.type == pygame.QUIT:
            run = False

      # register a mouse event
        if event.type == pygame.MOUSEBUTTONDOWN:
          # get x y position of my mouse
          m_x, m_y = pygame.mouse.get_pos()
          for letter in letters:
            x, y, ltr, visible = letter
            if visible:
              dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
              if dis < RADIUS:
                letter[3] = False
                guessed.append(ltr)
                if ltr not in word:
                  hangman_status += 1
        # check that our mouse is less than the radius length away from any of our buttons

    draw()

    won = True
    for letter in word:
      if letter not in guessed:
        won = False
        break

    if won:
      display_message("You won!")
      break
    
    if hangman_status == 6:
      display_message("You lost!")
      break

# while True:
#   for event in 
#   main()

main()

pygame.quit()
