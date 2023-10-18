from utils import *
from ..base import SupportCard
from typing import TYPE_CHECKING
from entity.support import Support

if TYPE_CHECKING:
    from game.game import GeniusGame
    from game.player import GeniusPlayer


class Treasure_Seeking_Seelie_Entity(Support):
    id: int = 323004
    name = 'Treasure-Seeking Seelie'
    max_usage = -1
    max_count = 3
    def __init__(self, game: 'GeniusGame', from_player: 'GeniusPlayer', from_character=None):
        super().__init__(game, from_player, from_character)
        self.treasure_clues = 0

    def on_after(self, game:'GeniusGame'):
        if game.active_player_index == self.from_player.index:
            self.treasure_clues += 1
            if self.treasure_clues == self.max_count:
                self.from_player.get_card(num=3)
                self.on_destroy(game)

    def update_listener_list(self):
        self.listeners = [
            (EventType.AFTER_USE_SKILL, ZoneType.SUPPORT_ZONE, self.on_after),
        ]


class Treasure_Seeking_Seelie(SupportCard):
    '''
        寻宝仙灵
    '''
    id: int = 323004
    name: str = 'Treasure-Seeking Seelie'
    cost_num = 1
    cost_type = CostType.WHITE
    card_type = ActionCardType.SUPPORT_ITEM

    def __init__(self) -> None:
        super().__init__()
        self.entity = None

    def on_played(self, game: 'GeniusGame') -> None:
        self.entity = Treasure_Seeking_Seelie_Entity(game, from_player=game.active_player)
        super().on_played(game)