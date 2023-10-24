from genius_invocation.utils import *
from typing import TYPE_CHECKING
from genius_invocation.card.action.equipment.talent.base import TalentCard

if TYPE_CHECKING:
    from genius_invocation.game.game import GeniusGame

class Conqueror_of_Evil_Guardian_Yaksha(Character):
    id: int = 215041
    name: str = "Conqueror of Evil: Guardian Yaksha"
    name_ch = "降魔·护法夜叉"
    is_action = True
    cost = [{'cost_num': 3, 'cost_type': <CostType.ANEMO: 4>}]
    cost_power = 2
    def __init__(self) -> None:
        super().__init__()
        self.character = 
        self.skill_idx = 