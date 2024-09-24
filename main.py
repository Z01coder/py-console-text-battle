import random


class Hero:                     # Класс: Герой
    def __init__(self, name):
        self.name = name        # Имя
        self.health = 100       # Здоровье
        self.attack_power = 20  # Сила удара

    def attack(self, other):                                                # Метод: Атака
        damage = self.attack_power                                          # Наносимый урон
        other.health -= damage                                              # Вычет урона из здоровья
        print(f"{self.name} ранит {other.name} на {damage} единиц!")        # Вывод в консоль

    def is_alive(self):                                                     # Проверка жив ли
        return self.health > 0


class Game:                                                           # Класс: Игра
    def __init__(self, player_name):
        self.player = Hero(player_name)                               # Герой игрока наследует атрибуты класса Hero
        self.computer = Hero("Аватар ПК")                             # Герой компьютера наследует атрибуты класса Hero

    def start(self):
        print("Ave, Caesar, morituri te salutant!")                   # Игровое приветствие
        print(f"{self.player.name} VS {self.computer.name}\n")        # Анонс

        while self.player.is_alive() and self.computer.is_alive():    # Гонит цикл пока оба живы
            self.player.attack(self.computer)                         # Атака моего героя
            if not self.computer.is_alive():                          # Проверка жив ли, и действия в противном случае
                print(f"{self.computer.name} Повержен!")
                break

            print(f"{self.computer.name} has {self.computer.health} health left.\n")  # Если жив, выводит остаток ХП

            self.computer.attack(self.player)                         # Атака героя под управлением ПК
            if not self.player.is_alive():                            # Проверка жив ли, и действия в противном случае
                print(f"{self.player.name} Повержен!")
                break

            print(f"{self.player.name} has {self.player.health} health left.\n")      # Если жив, выводит остаток ХП

        if self.player.is_alive():                  # Если в живых остался мой герой:
            print(f"{self.player.name} победил!")   # Выводит это сообщение
        else:
            print(f"{self.computer.name} wins!")    # Это сообщение выводит, если мой герой пал


if __name__ == "__main__":
    player_name = input("Введите имя героя: ")      # Просит дать имя моему герою
    game = Game(player_name)                        # Класс принимает свой атрибут (имя) и сохраняется в переменную
    game.start()                                    # Вызов метода start класса Game
