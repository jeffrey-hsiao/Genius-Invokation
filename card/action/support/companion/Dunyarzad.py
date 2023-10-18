from utils import *
from ..base import SupportCard
from typing import TYPE_CHECKING
from entity.support import Support

if TYPE_CHECKING:
    from game.game import GeniusGame
    from game.player import GeniusPlayer


class Dunyarzad_Entity(Support):
    id: int = 322016
    name = 'Dunyarzad'
    max_usage = 1
    max_count = -1
    def __init__(self, game: 'GeniusGame', from_player: 'GeniusPlayer', from_character=None):
        super().__init__(game, from_player, from_character)
        self.usage_round = self.max_usage
        self.usage_game = self.max_usage

    def on_begin(self, game:'GeniusGame'):
        if game.active_player_index == self.from_player.index:
            self.usage_round = self.max_usage

    def on_calculate(self, game:'GeniusGame'):
        if game.active_player_index == self.from_player.index:
            if self.usage_round > 0:
                if game.current_dice.use_type == ActionCardType.SUPPORT_COMPANION:
                    if game.current_dice.cost[0]['cost_num'] > 0:
                        game.current_dice.cost[0]['cost_num'] = max(0,  game.current_dice.cost[0]['cost_num']-1)
                        return True
        return False

    def on_play(self, game:'GeniusGame'):
        if self.on_calculate(game):
            self.usage_round -= 1
        if game.active_player_index == self.from_player.index:
            if self.usage_game > 0:
                if game.current_dice.use_type == ActionCardType.SUPPORT_COMPANION:
                    card = self.from_player.card_zone.find_card(ActionCardType.SUPPORT_COMPANION)
                    self.from_player.hand_zone.add(card)
                    self.usage_game -= 1

    def update_listener_list(self):
        self.listeners = [
            (EventType.BEGIN_ACTION_PHASE, ZoneType.SUPPORT_ZONE, self.on_begin),
            (EventType.CALCULATE_DICE, ZoneType.SUPPORT_ZONE, self.on_calculate),
            (EventType.ON_PLAY_CARD, ZoneType.SUPPORT_ZONE, self.on_play),
        ]


class Dunyarzad(SupportCard):
    '''
        迪娜泽黛
    '''
    id: int = 322016
    name: str = 'Dunyarzad'
    cost_num = 2
    cost_type = CostType.BLACK
    card_type = ActionCardType.SUPPORT_COMPANION

    def __init__(self) -> None:
        super().__init__()
        self.entity = None

    def on_played(self, game: 'GeniusGame') -> None:
        self.entity = Dunyarzad_Entity(game, from_player=game.active_player)
        super().on_played(game)
