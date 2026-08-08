#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   concrete_creature_factory.py                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/12 14:07:01 by horarivo            #+#    #+#            #
#   Updated: 2026/07/25 07:10:06 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from ex0.creature_factory import CreatureFactory
from ex0.creature import Creature
from .concrete_creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "Normal/Dragon")
