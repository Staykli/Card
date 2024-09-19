class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []

    def connect(self, direction, location):
        self.connections[direction] = location

    def get_description(self):
        return self.description

    def get_connections(self):
        return self.connections

class Game:
    def __init__(self):
        self.locations = {}
        self.current_location = None

    def add_location(self, location):
        self.locations[location.name] = location

    def set_start_location(self, location_name):
        self.current_location = self.locations[location_name]

    def move(self, direction):
        if direction in self.current_location.get_connections():
            self.current_location = self.current_location.get_connections()[direction]
            print(f"You move to {self.current_location.name}.")
            print(self.current_location.get_description())
        else:
            print("You can't go that way.")

    def play(self):
        print("Welcome to the adventure game!")
        print(self.current_location.get_description())
        while True:
            command = input("> ").strip().lower()
            if command in ["quit", "exit"]:
                print("Thanks for playing!")
                break
            elif command in ["north", "south", "east", "west"]:
                self.move(command)
            else:
                print("Invalid command.")

# Створення локацій
forest = Location("Forest", "You are in a dark forest. There are paths to the north and east.")
cave = Location("Cave", "You are in a damp cave. There is a path to the south.")
lake = Location("Lake", "You are at the edge of a serene lake. There is a path to the west.")

# З'єднання локацій
forest.connect("north", cave)
forest.connect("east", lake)
cave.connect("south", forest)
lake.connect("west", forest)

# Створення гри
game = Game()
game.add_location(forest)
game.add_location(cave)
game.add_location(lake)
game.set_start_location("Forest")

# Запуск гри
game.play()