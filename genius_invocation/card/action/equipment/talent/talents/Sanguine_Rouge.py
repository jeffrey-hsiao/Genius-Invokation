from genius_invocation.utils import *
from typing import TYPE_CHECKING
from genius_invocation.card.action.equipment.talent.base import TalentCard

if TYPE_CHECKING:
    from genius_invocation.game.game import GeniusGame

class Sanguine_Rouge(Character):
    id: int = 213071
    name: str = "Sanguine Rouge"
    name_ch = "血之灶火"
    is_action = True
    cost = [{'cost_num': 2, 'cost_type': <CostType.PYRO: 2>}]
    cost_power = 0
    def __init__(self) -> None:
        super().__init__()
        self.character = 
        self.skill_idx = 