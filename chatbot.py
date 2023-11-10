"""This is a sample Python chatbot. This bot can recommend movies, music,
games by genre, jokes, interesting stories, as well as provide an opportunity to play the game"""

import random
import pyjokes
from tqdm import tqdm
from termcolor import colored
import art
import time


def menu():
    """
    Presents an interactive menu for the user to choose from a variety of options.

    Allows the user to:
    1. Receive a movie recommendation
    2. Receive music recommendations
    3. Receive computer games recommendations
    4. Indulge in a dose of humor with funny jokes
    5. Immerse in captivating and interesting stories
    6. Play an engaging game

    Here 0 to exit the program.

    Returns:
        str: The selected operation.

    Usage:
        Call the function and choose the option!

        Example:
            ">>> 1"
    """
    choice = -1
    while choice not in range(0, 7):
        while True:
            try:
                choice = int(input('\nChoose what do you want now 👇'
                                   '\n\t1) Movie Recommendation 🍿'
                                   '\n\t2) Music Recommendation 🎵'
                                   '\n\t3) Computer Game Recommendation 🎮'
                                   '\n\t4) Read a Funny Joke 😄'
                                   '\n\t5) Read an Interesting Story 📖'
                                   '\n\t6) Play a Game 🕹️'
                                   '\n\tType 0 to EXIT 🚪'
                                   '\n>>> '))
                break
            except (TypeError, ValueError):
                print('Please enter a valid number.')

        if choice not in range(0, 7):
            print('‼️Invalid operation. Try again')
        if choice == 0:
            for i in tqdm(range(10), desc="Completion of the program", ncols=100, colour='green'):
                time.sleep(0.1)
            print('\nThank you for time with us! 🤝')
            break

    # Perform the selected operation
    match choice:
        case 1:
            movie()
        case 2:
            music()
        case 3:
            computer_game()
        case 4:
            jokes()
        case 5:
            story()
        case 6:
            games()


def movie():
    """
    Provides a movie recommendation based on the user's preferred genre.

    Allows the user to choose from genres like Horrors, Comedies, Adventures, and Christmas movies.
    Or return to the MENU by writing 0.

    Returns:
        None

    Usage:
        Call the function to get a random movie recommendation

        Example:
            '>>> 1'
    """

    global movies
    film_genre = -1

    while film_genre not in range(0, 5):
        while True:
            try:
                film_genre = int(input('\nWe have:'
                                       '\n\t1) Horrors'
                                       '\n\t2) Comedies'
                                       '\n\t3) Adventures'
                                       '\n\t4) Christmas movies'
                                       '\n\tType 0 to back to MENU'
                                       '\n>>> '))
                break
            except (TypeError, ValueError):
                print('Please enter a valid number.')

        movies = {
            'Horror': {
                'The Exorcist': {'year': 1973, 'IMDb rate': 8.1},
                '[Rec]': {'year': 2007, 'IMDb rate': 7.4},
                'Paranormal Activity': {'year': 2007, 'IMDb rate': 6.3},
                'Shutter (II)': {'year': 2004, 'IMDb rate': 7.0},
                'The Fourth Kind': {'year': 2009, 'IMDb rate': 5.9}
            },
            'Comedy': {
                'Step Brothers': {'year': 2008, 'IMDb rate': 6.9},
                'White Chicks': {'year': 2004, 'IMDb rate': 5.8},
                'The Hot Chick': {'year': 2002, 'IMDb rate': 5.5},
                'The Hangover': {'year': 2009, 'IMDb rate': 7.7},
                'Horrible Bosses': {'year': 2011, 'IMDb rate': 6.9}
            },
            'Adventure': {
                'The Killer': {'year': 2023, 'IMDb rate': 7.4},
                'Spider-Man: Across the Spider-Verse': {'year': 2023, 'IMDb rate': 8.7},
                'Barbie': {'year': 2023, 'IMDb rate': 7.0},
                'Mission: Impossible - Dead Reckoning Part One': {'year': 2023, 'IMDb rate': 7.8},
                'The Hunger Games': {'year': 2012, 'IMDb rate': 7.2}
            },
            'Christmas': {
                'Home Alone ': {'year': 1990, 'IMDb rate': 7.7},
                'National Lampoon\'s Christmas Vacation': {'year': 1989, 'IMDb rate': 7.5},
                'Elf': {'year': 2003, 'IMDb rate': 7.1},
                'Trading Places': {'year': 1983, 'IMDb rate': 7.5},
                'The Christmas Chronicles': {'year': 2018, 'IMDb rate': 7.0}
            }
        }
        if film_genre not in range(0, 5):
            print('‼️Invalid choice. Try again')
        if film_genre == 0:
            menu()
    else:
        match film_genre:
            case 1:
                film_genre = 'Horror'
            case 2:
                film_genre = 'Comedy'
            case 3:
                film_genre = 'Adventure'
            case 4:
                film_genre = 'Christmas'

        random_movie = random.choice(list(movies[film_genre].keys()))

        print(f'🍿My recommendation for you is {random_movie} '
              f'({movies[film_genre][random_movie]["year"]}) '
              f'with IMDb rate {movies[film_genre][random_movie]["IMDb rate"]}')

        time.sleep(5)
        menu()


def music():
    """
        Provides a music recommendation based on the user's preferred genre.

        Allows the user to choose from genres like Rock, Jazz, Blues, and Christmas songs.
        Or return to the MENU by writing 0.

        Returns:
            None

        Usage:
            Call the function to get a random music recommendation

            Example:
                '>>> 1'
    """
    global music_folder
    music_genre = -1

    while music_genre not in range(0, 5):
        while True:
            try:
                music_genre = int(input('\nWe have:'
                                        '\n\t1) Rock'
                                        '\n\t2) Jazz'
                                        '\n\t3) Blues'
                                        '\n\t4) Christmas songs'
                                        '\n\tType 0 to back to MENU'
                                        '\n>>> '))
                break
            except (TypeError, ValueError):
                print('Please enter a valid number.')

        music_folder = {
            'Rock': {
                '"I Love Rock\'N Roll"': {'singer': 'Joan Jett & the Blackhearts', 'year': 1981},
                '"Born to Run"': {'singer': 'Bruce Springsteen', 'year': 1975},
                '"Starman"': {'singer': 'David Bowie', 'year': 1972},
                '"Whole Lotta Love"': {'singer': 'Led Zeppelin', 'year': 1969},
                '"La Grange"': {'singer': 'ZZ Top', 'year': 1973}
            },
            'Jazz': {
                '"Take Five"': {'singer': 'Dave Brubeck Quartet', 'year': 1959},
                '"Kind of Blue"': {'singer': 'Miles Davis', 'year': 1959},
                '"A Love Supreme"': {'singer': 'John Coltrane', 'year': 1965},
                '"My Favorite Things"': {'singer': 'John Coltrane', 'year': 1961},
                '"So What"': {'singer': 'Miles Davis', 'year': 1959},
            },
            'Blues': {
                '"Stormy Monday"': {'singer': 'T-Bone Walker', 'year': 1947},
                '"The Thrill is Gone"': {'singer': 'B.B. King', 'year': 1969},
                '"Crossroads"': {'singer': 'Robert Johnson', 'year': 1936},
                '"Hoochie Coochie Man"': {'singer': 'Muddy Waters', 'year': 1954},
                '"Sweet Home Chicago"': {'singer': 'Robert Johnson', 'year': 1936},
            },
            'Christmas': {
                '"All I Want for Christmas Is You"': {'singer': 'Mariah Carey', 'year': 1994},
                '"Last Christmas"': {'singer': 'Wham!', 'year': 1984},
                '"Jingle Bell Rock"': {'singer': 'Bobby Helms', 'year': 1957},
                '"Feliz Navidad"': {'singer': 'José Feliciano', 'year': 1970},
                '"White Christmas"': {'singer': 'Bing Crosby', 'year': 1942},
            }
        }
        if music_genre not in range(0, 5):
            print('‼️Invalid choice. Try again')
        if music_genre == 0:
            menu()
    else:
        match music_genre:
            case 1:
                music_genre = 'Rock'
            case 2:
                music_genre = 'Jazz'
            case 3:
                music_genre = 'Blues'
            case 4:
                music_genre = 'Christmas'

    random_music = random.choice(list(music_folder[music_genre].keys()))

    print(f'🎧My recommendation for you is {random_music} '
          f'by {music_folder[music_genre][random_music]["singer"]} '
          f'({music_folder[music_genre][random_music]["year"]})')

    time.sleep(5)
    menu()


def computer_game():
    """
        Provides a computer game recommendation based on the user's preferred genre.

        Allows the user to choose from genres like Action, Adventure, Shooter, and Strategy.
        Or return to the MENU by writing 0.

        Returns:
            None

        Usage:
            Call the function to get a random computer game recommendation

            Example:
                '>>> 1'
    """
    global comp_games
    game_genre = -1

    while game_genre not in range(0, 5):
        while True:
            try:
                game_genre = int(input('\nWe have these genres:'
                                       '\n\t1) Action'
                                       '\n\t2) Adventure'
                                       '\n\t3) Shooter'
                                       '\n\t4) Strategy'
                                       '\n\tType 0 to back to MENU'
                                       '\n>>> '))
                break
            except (TypeError, ValueError):
                print('Please enter a valid number.')

        comp_games = {
            'Action': {
                '"God of War"': {'developer': 'Insomniac Games', 'platform': 'PC, PS4, PS5', 'year': 2018},
                '"Uncharted 4: A Thief\'s End"': {'developer': 'Naughty Dog', 'platform': 'PC, PS4, PS5', 'year': 2016},
                '"Marvel\'s Spider-Man"': {'developer': 'Insomniac Games', 'platform': 'PC, PS4, PS5', 'year': 2018}
            },
            'Adventure': {
                '"Red Dead Redemption 2"': {'developer': 'Rockstar', 'platform': 'PC, PS4, Xbox One', 'year': 2018},
                '"The Witcher 3: Wild Hunt"': {'developer': 'CD Projekt Red',
                                               'platform': 'PC, PS4, Xbox One, Nintendo Switch', 'year': 2015},
                '"Baldur\'s Gate 3"': {'developer': 'Larian Studios', 'platform': 'PC, PS5', 'year': 2020},
            },
            'Shooter': {
                '"Destiny 2"': {'developer': 'Bungie', 'platform': 'PC, PS4, PS5, Xbox One, Xbox Series X',
                                'year': 2017},
                '"Call of Duty: Warzone"': {'developer': 'Infinity Ward, Raven Software',
                                            'platform': 'PC, PS4, PS5, Xbox One, Xbox Series X', 'year': 2020},
                '"Doom Eternal"': {'developer': 'id Software', 'platform': 'PC, PS4, PS5, Xbox One, Xbox Series X',
                                   'year': 2020},
            },
            'Strategy': {
                '"Command and Conquer Remastered Collection"': {'developer': 'Petroglyph / Lemon Sky Studios',
                                                                'platform': 'PC', 'year': 2020},
                '"Into the Breach"': {'developer': 'Subset Games', 'platform': 'PC, Xbox One, Switch', 'year': 2018},
                '"StarCraft 2"': {'developer': 'Blizzard Entertainment', 'platform': 'PC', 'year': 2010},
            }
        }

        if game_genre not in range(0, 5):
            print('‼️Invalid choice. Try again')
        if game_genre == 0:
            menu()
    else:
        match game_genre:
            case 1:
                game_genre = 'Action'
            case 2:
                game_genre = 'Adventure'
            case 3:
                game_genre = 'Shooter'
            case 4:
                game_genre = 'Strategy'

    random_game = random.choice(list(comp_games[game_genre].keys()))

    print(f'🎮My recommendation for you is {random_game} '
          f'({comp_games[game_genre][random_game]["year"]}) '
          f'for {comp_games[game_genre][random_game]["platform"]} '
          f'by {comp_games[game_genre][random_game]["developer"]}')

    time.sleep(5)
    menu()


def jokes():
    """
    This function utilizes the PyJokes library to access jokes in English. The selected joke is then
    presented to the user.

    Returns:
        None

    Usage:
        Invoke the function to prompt the display of a random joke.

        Example:
            '>>> jokes()'
    """

    joke = pyjokes.get_joke('en', 'all')
    print(f'🤡Joke of the day is:'
          f'\n{joke}')

    time.sleep(5)
    menu()


def story_editor(bare_story):
    """???"""
    max_len = 100
    words = bare_story.split()
    processed_lines = []
    current_line = ''

    for word in words:
        if len(current_line + word) <= max_len:
            current_line += word + ' '
        else:
            processed_lines.append(current_line.strip())
            current_line = word + ' '

    processed_lines.append(current_line.strip())
    edited_story = '\n'.join(processed_lines)
    return edited_story


def story():
    """ stories"""
    global stories
    story_genre = -1

    while story_genre not in range(0, 4):
        while True:
            try:
                story_genre = int(input('\nWe have these genres:'
                                        '\n\t1) Science Fiction 🧠'
                                        '\n\t2) Mystery 🦇'
                                        '\n\t3) Fantasy 🧚'
                                        '\n\tType 0 to back to MENU'
                                        '\n>>> '))
                break
            except (TypeError, ValueError):
                print('Please enter a valid number.')

        stories = {
            'Science Fiction': {'title': 'The Quantum Heist',
                                'text': 'In the year 2150, a group of renegade scientists discovered a way to '
                                        'manipulate quantum reality. They hatched a plan to infiltrate the most '
                                        'secure quantum bank in the multiverse. The heist involved navigating through '
                                        'alternate realities, dodging quantum security measures, and stealing from '
                                        'parallel universes. As they executed their plan, they encountered versions '
                                        'of themselves from different timelines, creating a mind-bending adventure '
                                        'that blurred the lines between theft and destiny.'
                                },
            'Mystery': {'title': 'The Enigmatic Manuscript',
                        'text': 'In a quiet town, a rare manuscript emerged, its origins shrouded in mystery. The '
                                'book contained a series of cryptic symbols and coded messages that had stumped '
                                'scholars for centuries. As a determined detective delved into the case, '
                                'they discovered a secret society that had guarded the manuscript\'s true meaning for '
                                'generations. The detective unraveled the codes, exposing a hidden history that could '
                                'change the course of humanity.'
                        },
            'Fantasy': {'title': 'The Song of the Whispering Woods',
                        'text': 'Deep within the enchanted Whispering Woods, a bard discovered an ancient harp with '
                                'the power to control nature itself. As the bard played, the trees whispered secrets, '
                                'and the rivers danced to the melody. However, an evil sorceress sought to harness '
                                'the harp\'s magic for dark purposes. The bard embarked on a quest, accompanied by '
                                'talking animals and mystical creatures, to prevent the harp from falling into the '
                                'wrong hands. Their journey unfolded like a lyrical epic, filled with magical '
                                'encounters and a battle between harmony and discord.'
                        }
        }

        if story_genre not in range(0, 4):
            print('‼️Invalid choice. Try again')
        if story_genre == 0:
            menu()
    else:
        match story_genre:
            case 1:
                story_genre = 'Science Fiction'
            case 2:
                story_genre = 'Mystery'
            case 3:
                story_genre = 'Fantasy'

    story_to_read = story_editor(stories[story_genre]["text"])
    print(f'📖My recommendation for you is "{stories[story_genre]["title"]}":'
          f'\n\n\t{story_to_read}')

    time.sleep(10)
    menu()


def games():
    """games choosing"""
    game_choice = -1
    while game_choice not in range(0, 3):
        while True:
            try:
                game_choice = int(input('Cool! We have 2 games to play:'
                                        '\n\t1) Guess a Number Game 🧠'
                                        '\n\t2) Rock-Paper-Scissors Game ✂️'
                                        '\n\tType 0 to back to MENU'
                                        '\nWhich do you want to play?'
                                        '\n>>> '))
                break
            except (TypeError, ValueError):
                print('Please enter a valid number.')

        if game_choice not in range(0, 3):
            print('‼️Invalid choice. Try again')
        if game_choice == 0:
            menu()
    else:
        match game_choice:
            case 1:
                game_guess_a_number()
            case 2:
                game_rock_paper_scissors()


def game_guess_a_number():
    """ game_guess_a_number"""
    global user_guess
    print('Let\'s start a 🧠Guess a Number Game!')
    guess_counter = 3

    start_number = random.randint(-100, 100)
    end_number = random.randint(start_number, 100)

    secret_number = random.randint(start_number, end_number)

    print(f'\nYou need to guess a number between {start_number} and {end_number} .... {secret_number}'
          f'\nOh... Forgot to say 🤭'
          f'\nYOU HAVE ONLY {guess_counter} ATTEMPTS to win (or lose😏)\n')

    for guess in range(guess_counter):
        while True:
            try:
                user_guess = int(input(f'Your {guess + 1} guess is >>> '))
                break
            except (TypeError, ValueError):
                print('Please enter a valid number.')

        if user_guess == secret_number:
            print(f'🎉OMG! You\'re right!'
                  f'\nYou guessed it on the {guess + 1} try!')
            print(art.text2art('WINNER'))
            break
        elif (guess + 1) == guess_counter:
            print(art.text2art('LOOOOOOOSER!'))
        else:
            print('No🫣 Try again')

    revenge = -1
    while revenge not in range(0, 3):
        while True:
            try:
                revenge = int(input('\nDo you want to play this game again?'
                                    '\n\t1) Yes ✅'
                                    '\n\t2) No, I want another game 🔁'
                                    '\n\tType 0 to back to MENU'
                                    '\n>>> '))
                break
            except (TypeError, ValueError):
                print('Please enter a valid number.')

        if revenge not in range(0, 3):
            print('‼️Invalid choice. Try again')
        if revenge == 0:
            menu()
    else:
        match revenge:
            case 1:
                game_guess_a_number()
            case 2:
                game_rock_paper_scissors()


def game_rock_paper_scissors():
    """ game_rock_paper_scissors✂️"""
    global win, lose
    game_options = {
        'r': 'ROCK 🪨',
        'p': 'PAPER 📄',
        's': 'SCISSORS ✂️'
    }

    attempts = 3

    win = 0
    lose = 0
    draw = 0

    def winner():
        global win
        win += 1
        print(f'🎉YOU WIN!'
              f'\nScore now {win}:{lose}'
              f'\nDraws were {draw} times')
        return win

    def loser():
        global lose
        lose += 1
        print(f'🤡YOU LOSE!'
              f'\nScore now {win}:{lose}'
              f'\nDraws were {draw} times')
        return lose

    print(f'Let\'s start a ✂️Rock-Paper-Scissors Game!'
          f'\nYou need to choose between ROCK 🪨, PAPER 📄and SCISSORS ✂️'
          f'\nWho will reach {attempts} points first - WINS 🎉\n')

    while win != attempts or lose != attempts:
        random_option = random.choice(list(game_options.keys()))
        print(random_option)

        user_choice = input('Choose:'
                            '\n\tR for ROCK 🪨'
                            '\n\tP for PAPER 📄'
                            '\n\tS for SCISSORS ✂️'
                            '\n\tType 0 to back to MENU'
                            '\n>>> ')

        # USER == COMPUTER
        if user_choice.lower() == random_option:
            draw += 1
            print(f'DRAW 🤝'
                  f'\nScore now {win}:{lose}'
                  f'\nDraws were {draw} times')
        # USER == ROCK 🪨
        elif user_choice.lower() == 'r':
            # COMPUTER == SCISSORS ✂️
            if random_option == 's':
                winner()
                if win == attempts:
                    break
            # COMPUTER == PAPER 📄
            else:
                loser()
                if lose == attempts:
                    break
        # USER == PAPER 📄
        elif user_choice == 'p':
            # COMPUTER == ROCK 🪨
            if random_option == 'r':
                winner()
                if win == attempts:
                    break
            # COMPUTER == SCISSORS ✂️
            else:
                loser()
                if lose == attempts:
                    break
        # USER == SCISSORS ✂️
        else:
            # COMPUTER == PAPER 📄
            if random_option == 'p':
                winner()
                if win == attempts:
                    break
            # COMPUTER == ROCK 🪨
            else:
                loser()
                if lose == attempts:
                    break


revenge = -1
while revenge not in range(0, 3):
    while True:
        try:
            revenge = int(input('\nDo you want to play this game again?'
                                '\n\t1) Yes ✅'
                                '\n\t2) No, I want another game 🔁'
                                '\n\tType 0 to back to MENU'
                                '\n>>> '))
            break
        except (TypeError, ValueError):
            print('Please enter a valid number.')

    if revenge not in range(0, 3):
        print('‼️Invalid choice. Try again')
    if revenge == 0:
        menu()
else:
    match revenge:
        case 1:
            game_rock_paper_scissors()
        case 2:
            game_guess_a_number()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''menu'''
    print('👋 Hello, you!'
          '\nThis chatbot can bring a bit of joy and benefit to your life 😉')
    menu()
