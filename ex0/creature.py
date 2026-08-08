#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creature.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/12 14:06:47 by horarivo            #+#    #+#            #
#   Updated: 2026/07/25 07:10:03 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str):
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return (f"{self.name} is a {self.creature_type} type Creature")


class Flameling(Creature):
    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


class Pyrodon(Creature):
    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")


class Aquabub(Creature):
    def attack(self) -> str:
        return (f"{self.name} uses Water Gun!")


class Torragon(Creature):
    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump!")
