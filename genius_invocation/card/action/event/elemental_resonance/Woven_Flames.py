from genius_invocation.card.action.base import ActionCard
from genius_invocation.utils import *

if TYPE_CHECKING:
    from genius_invocation.game.game import GeniusGame

class Woven_Flames(ActionCard):
    id: int = 331301
    name: str = "Woven_Flames"
    cost_num = 0
    card_type = ActionCardType.EVENT_ELEMENTAL_RESONANCE.value
    cost_type = None

    def __init__(self) -> None:
        super().__init__()

    def on_played(self, game: 'GeniusGame') -> None:
        game.active_player.dice_zone.add([DiceType.PYRO.value])