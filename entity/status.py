from entity.entity import Entity
from utils import *
from typing import TYPE_CHECKING, List, Tuple


if TYPE_CHECKING:
    from game.game import GeniusGame
    from game.action import Action
    from event.events import ListenerNode
    from game.player import GeniusPlayer

#TODO: FINISH THE ENTITIES

class Status(Entity):
    # 状态基本类
    id: int
    name: str


    def __init__(self, game: 'GeniusGame', from_player:'GeniusPlayer', from_character=None):
        super().__init__(game, from_player, from_character)
        self.usage: int #生成时的可用次数
        self.max_usage: int #Maybe changed by Talent.
        self.current_usage: int

    def on_destroy(self, game):
        return super().on_destroy(game)
        #TODO

    def update(self):
        # All states can be update
        pass

class Combat_Status(Status):
    def __init__(self, game: 'GeniusGame', from_player: 'GeniusPlayer', from_character=None):
        super().__init__(game, from_player, from_character)

class Shield(Status):
    # Status of shield (Only for single character)
    def __init__(self, game: 'GeniusGame', from_player: 'GeniusPlayer', from_character=None):
        super().__init__(game, from_player, from_character)

class Combat_Shield(Combat_Status):
    # Combat_Status of shield.
    def __init__(self, game: 'GeniusGame', from_player: 'GeniusPlayer', from_character=None):
        super().__init__(game, from_player, from_character)

class Equipment(Status):
    pass

class Weapon(Equipment):
    pass

class Artifact(Equipment):
    pass

# TODO: Need to move to other places in future
class Frozen_Status(Status):
    def __init__(self, game: 'GeniusGame', from_player: 'GeniusPlayer', from_character=None):
        super().__init__(game, from_player, from_character)
        pass
    pass

class Dendro_Core(Status):
    def __init__(self, game: 'GeniusGame', from_player: 'GeniusPlayer', from_character=None):
        super().__init__(game, from_player, from_character)
        pass
    pass

class Catalyzing_Feild(Status):
    # Name Maybe Wrong
    pass

class Crystallize_Shield(Shield):
    # Name Maybe Wrong
    pass

