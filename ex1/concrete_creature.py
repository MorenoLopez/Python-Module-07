#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   concrete_creature.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/12 14:07:06 by horarivo            #+#    #+#            #
#   Updated: 2026/07/25 07:10:08 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from ex0.creature import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")

    def heal(self) -> str:
        return (f"{self.name} heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")

    def heal(self) -> str:
        return (f"{self.name} heals itself and others for a large amount")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return (f"{self.name} shifts into a sharper form!")

    def attack(self) -> str:
        if not self.is_transformed:
            return (f"{self.name} attacks normally.")
        return (f"{self.name} performs a boosted strike!")

    def revert(self) -> str:
        self.is_transformed = False
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.is_transformed:
            return (f"{self.name} attacks normally.")
        return (f"{self.name} unleashes a devastating morph strike!")

    def transform(self) -> str:
        self.is_transformed = True
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        self.is_transformed = False
        return (f"{self.name} stabilizes its form.")
