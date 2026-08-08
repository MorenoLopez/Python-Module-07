#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacitor.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/12 14:07:21 by horarivo            #+#    #+#            #
#   Updated: 2026/07/25 07:10:13 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.creature_factory import CreatureFactory
from ex1.capability import HealCapability, TransformCapability


def create_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    creature = factory.create_base()
    evolution = factory.create_evolved()
    creatures = [creature, evolution]
    titles = ["base", "evolved"]
    for title, entity in zip(titles, creatures):
        print(f" {title}:")
        print(entity.describe())
        print(entity.attack())

        if isinstance(entity, HealCapability):
            print(entity.heal())
    print()


def transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    creature = factory.create_base()
    evolution = factory.create_evolved()
    titles = ["base", "evolved"]
    creatures = [creature, evolution]
    for title, entity in zip(titles, creatures):
        print(f" {title}:")
        print(entity.describe())
        print(entity.attack())

        if isinstance(entity, TransformCapability):
            print(entity.transform())
            print(entity.attack())
            print(entity.revert())
    print()


if __name__ == "__main__":
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    create_factory(heal_factory)
    transform(transform_factory)
