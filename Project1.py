import pygame
import random
import math

greeting = input('Hi, would you like to create a new account or log-in?: ')

if greeting == 'create a new account':
    email = input('Enter A Email: ')
    username = input('Enter A Username: ')
    password = input('Enter A Password: ')
    reEnter = input('Please Confirm Your New Password: ')

    if reEnter == password:
        print('You Have Created A New Account!')
        print(f'Welcome, {username}!')

        wr = open('emails.txt', 'a')
        wr.write(f'\n{email}')
        wr1 = open('passwords.txt', 'a')
        wr1.write(f'\n{password}')
        wr6 = open('usernames.txt', 'a')
        wr6.write(f'\n{username}')

    else:
        secondTry = input(
            'Wrong Password, Please Enter Your Original Password: ')
        if secondTry == password:
            print('You Have Created A New Account!')
            print(f'Welcome, {username}!')

            wr2 = open('emails.txt', 'a')
            wr2.write(f'\n{email}')
            wr3 = open('passwords.txt', 'a')
            wr3.write(f'\n{password}')
            wr7 = open('usernames.txt', 'a')
            wr7.write(f'\n{username}')

        else:
            thirdTry = input(
                'Wrong Password, Please Enter Your Original Password: ')
            if thirdTry == password:
                print('You Have Created A New Account!')
                print(f'Welcome, {username}!')

                wr4 = open('emails.txt', 'a')
                wr4.write(f'\n{email}')
                wr5 = open('passwords.txt', 'a')
                wr5.write(f'\n{password}')
                wr8 = open('usernames.txt', 'a')
                wr8.write(f'\n{username}')

            else:
                print(
                    'You have entered wrong 3 times, please try signing up again :(')

elif greeting == 'log-in':
    fr = open('emails.txt', 'r')
    re = open('passwords.txt', 'r')
    fr1 = open('usernames.txt', 'r')

    text1 = re.read()
    text = fr.read()
    text2 = fr1.read()

    logEmail = input('Enter Your Email: ')
    logPass = input('Enter Your Password: ')
    logUsername = input('Enter Your Username: ')

    if logEmail in text and logPass in text1 and logUsername in text2:
        print('\nYou have successfully logged into your account!')
        print(f'Welcome, {logUsername}!')

        choice = input(
            f'\nHi {logUsername}, would you like to play an adventure game, hangman, guessing game, check your profile or log-out: ')
        if choice == 'check profile':
            print(f'\nEmail: {logEmail}')
            print(f'Username: {logUsername}')
            print(f'Password: {logPass}')

        elif choice == 'adventure game':
            print('Welcome to my game!')
            age = int(input('What is your age?: '))

            health = 10

            if age >= 13:
                print('You are old enough to play!')
                play = input('Do you want to play?: ').lower()

                if play == 'yes':
                    print("Let's play!")
                    print(f'You are starting with {health} health')

                    left_or_right = input(
                        'First choice... Left or Right (left/right)?: ')

                    if left_or_right == 'left':
                        ans = input('Nice, you follow the path and reach a lake... Do you swim across or go around? ('
                                    'across/around)?: ')

                        if ans == 'around':
                            print(
                                'You went around and reached the other side of the lake')

                        elif ans == 'across':
                            print(
                                'You managed to get across, but you were bit by a crocodile and lost five health.')
                            health -= 5

                        ans = input(
                            'You notice a house and a river. Which do you go to? (river/house): ')
                        if ans == 'house':
                            print(
                                'You went to the house, but was injured by the owner and you lost 5 health')
                            health -= 5

                            if health <= 0:
                                print(
                                    'You have lost all your health and lost the game...')

                            else:
                                health_generator = input('You see a bottle of water and a wild plant... which do you '
                                                         'choose? (water/plant): ')

                                if health_generator == 'water':
                                    print('Nice, you just earned 3 health...')
                                    health += 3
                                    path = input('You see 2 paths... one through the forest and another through an '
                                                 'abandoned town. Which do you choose? (forest/town): ')
                                    if path == 'forest':
                                        print(
                                            'You were eaten by wolves and lost the game...')

                                    else:
                                        print(
                                            f'You survived and have {health} health left... You Win!')

                                else:
                                    print(
                                        'That plant was poisonous... you lost the game')

                        else:
                            print('You drowned in the river and lost...')

                    else:
                        print('You fell down a cliff and lost...')

                else:
                    print('See ya later!')

            else:
                print('Sorry, you are not old enough to play...')

        elif choice == 'hangman':
            # setup display
            pygame.init()
            WIDTH, HEIGHT = 800, 500  # All capital letter variable names means it's a constant
            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('Hangman Game!')

            # button variables
            RADIUS = 20
            GAP = 15
            letters = []
            startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
            starty = 400
            A = 65
            for i in range(26):
                x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
                y = starty + ((i // 13) * (GAP + RADIUS * 2))
                letters.append([x, y, chr(A + i), True])

            # Fonts
            LETTER_FONT = pygame.font.SysFont('comicsans', 40)
            WORD_FONT = pygame.font.SysFont('comicsans', 60)
            TITLE_FONT = pygame.font.SysFont('comicsans', 70)

            # load images
            images = []
            for i in range(7):
                image = pygame.image.load('hangman' + str(i) + '.png')
                images.append(image)

            # game variables
            hangman_status = 0
            words = ['DEVELOPER', 'CODE', 'PYTHON', 'PYGAME',
                     'GAME', 'AWESOME', 'AMAZING', 'PERFECT']
            word = random.choice(words)
            guessed = []

            # colors
            WHITE = (255, 255, 255)
            BLACK = (0, 0, 0)

            # setup game loop
            FPS = 60
            clock = pygame.time.Clock()
            run = True

            def draw():
                win.fill((WHITE))

                # draw title
                text = TITLE_FONT.render('PYTHON HANGMAN', 1, BLACK)
                win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

                # draw word
                display_word = ''
                for letter in word:
                    if letter in guessed:
                        display_word += f'{letter} '

                    else:
                        display_word += '_ '

                text = WORD_FONT.render(display_word, 1, BLACK)
                win.blit(text, (400, 200))

                # draw buttons
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
                        text = LETTER_FONT.render(ltr, 1, BLACK)
                        win.blit(text, (x - text.get_width() /
                                        2, y - text.get_height() / 2))
                win.blit(images[hangman_status], (150, 100))
                pygame.display.update()

            def display_message(message):
                pygame.time.delay(1000)
                win.fill(WHITE)
                text = WORD_FONT.render(message, 1, BLACK)
                win.blit(text, (WIDTH/2 - text.get_width() /
                                2, HEIGHT/2 - text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(3000)

            while run:
                clock.tick(FPS)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Allows the user to press the red 'x' button to quit
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:  # An event where the mouse is pressed
                        m_x, m_y = pygame.mouse.get_pos()  # Gets the position of the mouse
                        for letter in letters:
                            x, y, ltr, visible = letter
                            if visible:
                                dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                                if dis < RADIUS:
                                    letter[3] = False
                                    guessed.append(ltr)

                                    if ltr not in word:
                                        hangman_status += 1
                draw()

                won = True
                for letter in word:
                    if letter not in guessed:
                        won = False
                        break

                if won:
                    display_message('You WON!')
                    break

                if hangman_status == 6:
                    display_message('You LOST!')
                    break

            pygame.quit()

        elif choice == 'guessing game':
            print('Welcome to my guessing game!')
            print('You will have 3 tries to guess a number between 1 and 50!')
            correctNum = random.randint(1, 50)
            pickedNum = int(input('Please enter a number 1-50: '))

            if pickedNum > correctNum:
                num1 = int(
                    input('The number you entered is too high. What is your next guess?: '))
                if num1 > correctNum:
                    num3 = int(
                        input('The number you entered is too high. What is your next guess?: '))

                    if num3 != correctNum:
                        print(
                            f'You got it wrong 3 times... The correct number is {correctNum}')
                        print('You Lost!')

                    else:
                        print('You Won!')

                elif num1 < correctNum:
                    num5 = int(
                        input('The number you entered is too low. What is your next guess?: '))

                    if num5 != correctNum:
                        print(
                            f'You got it wrong 3 times... The correct number is {correctNum}')
                        print('You Lost!')

                    else:
                        print('You Won!')

                else:
                    print('You Won!')

            elif pickedNum < correctNum:
                num2 = int(
                    input('The number you entered is too low. What is your next guess?: '))
                if num2 < correctNum:
                    num4 = int(
                        input('The number you entered is too low. What is your next guess?: '))

                    if num4 != correctNum:
                        print(
                            f'You got it wrong 3 times... The correct number is {correctNum}')

                    else:
                        print('You Won!')

                elif num2 > correctNum:
                    num6 = int(
                        input('The number you entered is too high. What is your next guess?: '))
                    if num6 != correctNum:
                        print(
                            f'You got it wrong 3 times... the correct number is {correctNum}')
                        print('You Lost!')

                    else:
                        print('You Won')

                else:
                    print('You Won!')

            else:
                print('You Won!')

        elif choice == 'log-out':
            print('You have logged out of your account!')

        else:
            print('Please choose one of the given choices')

    else:
        print('Sorry, we could not find your account')

else:
    print('Please choose to create a new account or log-in')
