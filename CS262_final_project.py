from random import choice


class Screen:
    """
    This class represents the Python console.

    Attributes:
        - stageDict (dict):  a dictionary that stores information about the current stage of the game.
        + color_name (str): ANSI escape codes; color the texts and backgrounds by calling print(Screen.color_name).

    Methods:
        - __init__(stage=0: int): initializes the screen backgrounds with the given stage number.
        + print_header(): prints header
        + two_choices(choice1: str, choice2: str) -> int:
            prompts the user to select a choice and returns the choice as an integer.
        + print_result(Dog, Owner): prints the current owner's reputation and dog's hunger and thirst.
        + print_clear(Dog, Owner): prints a message indicating that the stage has been cleared
        + game_over(Dog, Owner, game_over_flag: bool = False):
            if game_over_flag is True (unconditional game-over) or any of the game-over conditions are met,
            exits the program.
    """
    black = '\033[38;2;0;0;0m'
    brown = '\033[38;2;139;69;19m'
    ash = '\033[38;2;113;115;117m'
    white = '\033[38;2;255;255;255m'
    red = '\033[38;2;255;0;0m'
    yellow = '\033[38;2;255;255;0m'
    bg_sky = '\033[48;2;175;223;228m'
    bg_grass = '\033[48;2;169;209;89m'
    bg_sand = '\033[48;2;246;215;176m'
    bg_dirt = '\033[48;2;107;84;40m'
    bg_ocean = '\033[48;2;29;162;216m'
    bg_concrete = '\033[48;2;128;128;118m'
    bg_night_sky = '\033[48;2;46;68;130m'
    bg_white = '\033[48;2;255;255;92m'
    bg_red = '\033[48;2;255;0;0m'
    reset = '\033[0m'

    def __init__(self, stage=0):
        stages = [
            {'name': 'BACKYARD🏡🐛', 'color1': Screen.bg_sky, 'color2': Screen.bg_dirt},
            {'name': 'STREET🌳🚗', 'color1': Screen.bg_sky, 'color2': Screen.bg_concrete},
            {'name': 'DOG PARK🐾🦴', 'color1': Screen.bg_sky, 'color2': Screen.bg_grass},
            {'name': 'BEACH🌴🌊', 'color1': Screen.bg_ocean, 'color2': Screen.bg_sand},
            {'name': 'CITY🗽✨', 'color1': Screen.bg_night_sky, 'color2': Screen.bg_concrete}
        ]
        self.stageDict = stages[stage]
        print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Stage {stage+1}: {self.stageDict['name']}\n")

    def display(self, dog, owner):
        print(self.stageDict['color1'], Screen.white, self.stageDict['name'])
        print("{}           __        {}{} is {}...".format(dog.color, Screen.white, dog.name, dog.action))
        print("{}      (___()'`;{}    {}Hunger: {}  Thirst: {}"
              .format(dog.color, Object.food, Screen.white, dog.hunger, dog.thirst))
        print("{}      /,   / `       {}{}'s Reputation: {}"
              .format(dog.color, Screen.white, owner.name, owner.reputation))
        print("   {} {}\\\\\"--\\\\  　　{}".format(Object.trash, dog.color, Object.distraction))
        print(self.stageDict['color2'])
        print(Screen.reset, end='')

    @staticmethod
    def print_header():
        print(" __________________________________________________________________")
        print("|                       Walk Your Dog Simulator                    |")
        print("|          By Erin Paranal, Maureen VonHassel, Yuna Ukawa          |")
        print("|__________________________________________________________________|\n\n")
        print("🎉Welcome to Walk-Your-Dog Simulator🎉\n")
        print("Experience what it’s like to have a dog in this Simulator.")
        print("• Name your dog!")
        print("• Walk your dog across five different environments!")
        print("• Encounter different scenarios and experience different outcomes!")
        print("• Pick up poop.")
        print("====================================================================\n\n")

    @staticmethod
    def two_choices(choice1, choice2):
        while True:
            try:
                print("What will you do?")
                print(f"> 1: {choice1}  2: {choice2}")
                action = int(input("> "))
                if action <= 0 or action >= 3:
                    raise ValueError()
            except ValueError:
                print("Invalid Input!")
            else:
                return action

    @staticmethod
    def print_result(dog, owner):
        print("\t _______________________________")
        print("\t|\tHunger: {}  Thirst: {}\t\t|".format(dog.hunger, dog.thirst))
        print("\t|\tReputation: {}\t\t\t\t|".format(owner.reputation))
        print("\t|_______________________________|\n")
        print(Screen.reset, end='')

    @staticmethod
    def print_clear(dog, owner):
        print(f"\n{Screen.bg_ocean}{Screen.yellow}\n\t🎉STAGE CLEAR🎉")
        Screen.print_result(dog, owner)

    @staticmethod
    def game_over(dog, owner, game_over_flag=False):
        if game_over_flag:
            pass
        elif dog.hunger <= 0 or dog.thirst <= 0 or owner.reputation <= 0:
            pass
        else:
            return
        print(f"\n{Screen.bg_red}{Screen.yellow}\n\tGAME OVER...")
        Screen.print_result(dog, owner)
        exit()


class Dog:
    """
    This class represents a virtual dog in the game.

    Attributes:
        - name (str): the name of the dog.
        - color (str): the color of the dog's fur, Screen.color_name.
        - hunger (int): the level of hunger of the dog, initialized to 50 or depending on the stage level.
        - thirst (int): the level of thirst of the dog, initialized to 50 or depending on the stage level.
        - action (str): the current action of the dog, initialized to an empty string.

    Methods:
        - create_dog(cls) -> Dog: initialize Dog by prompting the user to enter the dog's name and choose its color.
        - walk(Owner, Screen): represents the dog walking.
        - poop(Owner, Screen): represents the dog pooping.
        - eat(Owner, Screen): represents the dog eating.
        - drink(Owner, Screen): represents the dog drinking.
        - attack(Owner, Screen): represents the dog attacking and decreases the owner's rep.
        - bark(Owner, Screen): represents the dog barking and decreases the owner's rep.
        - be_friendly(Owner, Screen): represents the dog being friendly and increases the owner's rep.
        - encounter(Owner, Screen): represents the dog encountering something and randomly chooses one of the methods.
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.hunger = 50
        self.thirst = 50
        self.action = ''

    @classmethod
    def create_dog(cls):
        print("What is your dog's name?")
        name = input("> ")
        while True:
            try:
                print("Choose a fur color")
                print("> 1: black   2: brown   3: gold   4: ash   5: white")
                color = int(input("> "))
                if color <= 0 or color >= 6:
                    raise ValueError()
            except ValueError:
                print("Invalid Input!")
            else:
                break
        if color == 1:
            color = Screen.black
        elif color == 2:
            color = Screen.brown
        elif color == 3:
            color = Screen.yellow
        elif color == 4:
            color = Screen.ash
        elif color == 5:
            color = Screen.white
        return cls(name, color)

    def walk(self, owner, screen):
        self.action = 'walking'
        screen.display(self, owner)

    def poop(self, owner, screen):
        self.action = 'pooping'
        Object.trash = '💩'
        screen.display(self, owner)

    def eat(self, owner, screen):
        self.action = 'eating'
        self.hunger += 30
        Object.food = choice(['🍊', '🍉', '🍓', '🍈', '🍅', '🍆', '🥒', '🥦', '🥕', '🍗', '🍖', '🥩', '🐟'])
        screen.display(self, owner)

    def drink(self, owner, screen):
        self.action = 'drinking'
        self.thirst += 30
        Object.food = choice(['🥛', '🥤', '🧉', '🍷', '🍺'])
        screen.display(self, owner)

    def attack(self, owner, screen):
        self.action = f'attacking the {Object.distraction_dsc}💥💥'
        owner.reputation -= 50
        screen.display(self, owner)

    def bark(self, owner, screen):
        self.action = 'barking'
        owner.reputation -= 10
        screen.display(self, owner)

    def be_friendly(self, owner, screen):
        self.action = 'acting cute'
        owner.reputation += 20
        screen.display(self, owner)

    def encounter(self, owner, screen):
        choice([self.bark, self.be_friendly, self.attack])(owner, screen)


class Owner:
    """
    This class represents a dog owner (player) and contains actions that the owner can take with their dog.

    Attributes:
        name (str): The owner's name.
        reputation (int): The owner's reputation score, which can be affected by their and dog's actions.
        age (int): The owner's age.

    Methods:
        create_owner(cls): initializes Owner by getting their name and age.
        action_feed(Dog, Screen): either feed the dog (correct) or ignore it (incorrect).
        action_drink(Dog, Screen): either hydrate the dog (correct) or ignore it (incorrect).
        action_encounter(Dog, Screen): either approach something (correct/incorrect) or ignore it (correct).
        action_trash(Dog): either pick up the poop/trash (correct) or ignore it (incorrect).
        action_ball(Dog, Screen): either let the dog chase it (incorrect) or lead the dog away (correct).
        action_swim(Dog, screen): either let the dog be (incorrect) or swim after it (correct).
        action_human(Dog, Screen): either let the dog approach a person (correct) or bark at them (incorrect).

    """
    def __init__(self, name, age):
        self.name = name
        self.reputation = 20
        self.age = age

    @classmethod
    def create_owner(cls):
        print("What is your name?")
        name = input("> ")
        while True:
            try:
                print("How old are you?")
                age = int(input("> "))
                if age < 0 or age > 120:
                    raise ValueError()
            except ValueError:
                print("Invalid Input!")
            else:
                break
        if age >= 18:
            pass
        else:
            print("Unfortunately, you are not old enough to adopt or buy a dog!")
            exit()
        return cls(name, age)

    def action_feed(self, dog, screen):
        dog.hunger -= 30
        print(f"\n{dog.name} is starving...")
        action = Screen.two_choices("feed", "ignore")
        if action == 1:
            dog.eat(self, screen)
        elif action == 2:
            print(f"Poor {dog.name} is too hungry.")
            Screen.game_over(dog, self)
            Screen.print_result(dog, self)

    def action_drink(self, dog, screen):
        dog.thirst -= 30
        print(f"\n{dog.name} is thirsty...")
        action = Screen.two_choices("hydrate", "ignore")
        if action == 1:
            dog.drink(self, screen)
        elif action == 2:
            print(f"Poor {dog.name} is too thirsty.")
            Screen.game_over(dog, self)
            Screen.print_result(dog, self)

    def action_encounter(self, dog, screen):
        print(f"\nYou encountered a {Object.distraction_dsc}{Object.distraction}!")
        action = Screen.two_choices("approach", "leave it alone")
        if action == 1:
            print(f"You approached the {Object.distraction_dsc}.")
            dog.encounter(self, screen)
            Screen.game_over(dog, self)
        elif action == 2:
            print(f"You ran away from the {Object.distraction_dsc}.")
            Screen.print_result(dog, self)

    def action_trash(self, dog):
        print(f"\nYou found a {Object.trash_dsc}{Object.trash}")
        action = Screen.two_choices("pick it up", "ignore")
        if action == 1:
            self.reputation += 10
            print("Congrats!")
            print("You gained reputation.")
        elif action == 2:
            self.reputation -= 20
            print("People are staring...")
            print("Your reputation has been lowered.")
        Screen.game_over(dog, self)
        Screen.print_result(dog, self)

    def action_ball(self, dog, screen):
        print(f"\nYou found a ball{Object.distraction}")
        action = Screen.two_choices(f"let {dog.name} chase the ball", f"lead {dog.name} away")
        if action == 1:
            print(f"{dog.name} chased the ball!")
            print(f"{dog.name} kept running towards the ball.")
            print(f"{dog.name} kept running and you lost them!")
            Screen.game_over(dog, self, True)
        elif action == 2:
            print(f"You led {dog.name} away from the ball.")
            print(f"{dog.name} is sad, but you can keep walking.")
            dog.walk(self, screen)

    def action_swim(self, dog):
        print(f"\n{dog.name} jumped into the ocean!!{Object.distraction}")
        action = Screen.two_choices("leave it be", "swim after it!!!")
        if action == 1:
            print(f"You let {dog.name} swim into the ocean!")
            print(f"{dog.name} just kept swimming.")
            print(f"{dog.name} kept swimming and you lost them!")
            Screen.game_over(dog, self, True)
        elif action == 2:
            self.reputation += 50
            print(f"You swam after {dog.name}!!!")
            print("You rescued your dog!")
            Screen.print_result(dog, self)

    def action_human(self, dog, screen):
        print("\nYou encountered a human.")
        action = Screen.two_choices(f"let {dog.name} slowly approach", f"let {dog.name} bark")
        if action == 1:
            print(f"You let {dog.name} slowly approach the person.")
            dog.be_friendly(self, screen)
        elif action == 2:
            dog.bark(self, screen)
            print(f"{dog.name} BIT THE PERSON!!!")
            print("Someone called Animal Control on you...")
            self.reputation = -100
            Screen.game_over(dog, self, True)


class Event:
    """
    A class that generates different events for the dog and owner in the game.
    """
    @staticmethod
    def generate(dog, owner, screen, stage_index):
        if stage_index == 0:
            Event.dog_poop(dog, owner, screen)
            Event.generate_wild_animal(dog, owner, screen)
        elif stage_index == 1:
            Event.dog_poop(dog, owner, screen)
            Event.dog_starve(dog, owner, screen)
            Event.generate_ball(dog, owner, screen)
        elif stage_index == 2:
            Event.dog_poop(dog, owner, screen)
            Event.generate_trash(dog, owner)
            Event.generate_another_dog(dog, owner, screen)
        elif stage_index == 3:
            Event.dog_poop(dog, owner, screen)
            Event.dog_thirst(dog, owner, screen)
            Event.dog_starve(dog, owner, screen)
            Event.dog_swim(dog, owner)
        elif stage_index == 4:
            Event.dog_poop(dog, owner, screen)
            Event.generate_trash(dog, owner)
            Event.generate_pigeon(dog, owner, screen)
            Event.generate_human(dog, owner, screen)

    @staticmethod
    def dog_poop(dog, owner, screen):
        dog.poop(owner, screen)
        Object.trash_dsc = 'poop'
        owner.action_trash(dog)
        Object.reset()

    @staticmethod
    def dog_starve(dog, owner, screen):
        owner.action_feed(dog, screen)
        Object.reset()

    @staticmethod
    def dog_thirst(dog, owner, screen):
        owner.action_drink(dog, screen)
        Object.reset()

    @staticmethod
    def generate_trash(dog, owner):
        Object.trash = '🚬'
        Object.trash_dsc = 'trash'
        owner.action_trash(dog)
        Object.reset()

    @staticmethod
    def generate_wild_animal(dog, owner, screen):
        Object.distraction = choice(['🐈', '🦝', '🐪'])
        Object.distraction_dsc = 'wild animal'
        owner.action_encounter(dog, screen)
        Object.reset()

    @staticmethod
    def generate_ball(dog, owner, screen):
        Object.distraction = '⚽'
        owner.action_ball(dog, screen)
        Object.reset()

    @staticmethod
    def generate_another_dog(dog, owner, screen):
        Object.distraction = choice(['🐩', '🦮', '🐕‍🦺'])
        Object.distraction_dsc = 'dog'
        owner.action_encounter(dog, screen)
        Object.reset()

    @staticmethod
    def generate_pigeon(dog, owner, screen):
        Object.distraction = '🐦'
        Object.distraction_dsc = 'pigeon'
        owner.action_encounter(dog, screen)
        Object.reset()

    @staticmethod
    def dog_swim(dog, owner):
        Object.distraction = '🌊'
        owner.action_swim(dog)
        Object.reset()

    @staticmethod
    def generate_human(dog, owner, screen):
        Object.distraction = choice(['🧎', '🧍'])
        Object.distraction_dsc = 'human'
        owner.action_human(dog, screen)
        Object.reset()


class Object:
    """
    A class represents various objects in the game.

    Attributes:
        + trash (str): The current state of the trash object, represented as an emoji.
        + food (str): The current state of the food object, represented as an emoji.
        + distraction (str): The current state of the distraction object, represented as an emoji.
        + trash_dsc (str): A string describing the trash object.
        + distraction_dsc (str): A string describing the distraction object.

    Methods:
        + reset(): Reset the state of all objects to their initial values.
    """
    trash, food, distraction = '  ', '  ', '  '
    trash_dsc, distraction_dsc = '', ''

    @staticmethod
    def reset():
        Object.trash, Object.food, Object.distraction = '  ', '  ', '  '
        Object.trash_dsc, Object.distraction_dsc = '', ''


def main():
    """
    The main function of the game. Initializes the game, creates an Owner instance, and runs through five stages
    of the game. For each stage, it creates a new Screen instance and Dog instance, adjusts the dog's hunger and
    thirst levels based on the stage index, generates an event using the Event class, and prints the updated
    screen using Screen.print_clear().
    """
    Screen.print_header()
    owner = Owner.create_owner()
    for i in range(5):
        screen = Screen(i)
        dog = Dog.create_dog()
        dog.hunger -= i * 10
        dog.thirst -= i * 10
        Event.generate(dog, owner, screen, i)
        Screen.print_clear(dog, owner)


if __name__ == '__main__':
    main()
