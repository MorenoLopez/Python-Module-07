#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/12 14:07:17 by horarivo            #+#    #+#            #
#   Updated: 2026/07/25 07:10:12 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from ex0 import FlameFactory, AquaFactory
from ex0.creature_factory import CreatureFactory


def create_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    creature = factory.create_base()
    evolution = factory.create_evolved()
    creatures = [creature, evolution]
    for entity in creatures:
        print(entity.describe())
        print(entity.attack())
    print()


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    fire_factory = FlameFactory()
    water_factory = AquaFactory()
    create_factory(fire_factory)
    create_factory(water_factory)
    battle(fire_factory, water_factory)
