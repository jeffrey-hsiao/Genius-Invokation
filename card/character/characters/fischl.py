from card.character.base import NormalAttack, ElementalSkill, ElementalBurst
from entity.character import Character
from game.game import GeniusGame
from utils import *
from entity.summon import Summon
from event.damage import Damage
from typing import TYPE_CHECKING, List, Tuple

from utils import GeniusGame

if TYPE_CHECKING:
    from game.game import GeniusGame
    from game.action import Action
    from event.events import ListenerNode
    from game.player import GeniusPlayer

class Oz(Summon):
    '''奥兹'''
    id: int = 0
    name: str = 'Oz'
    element: ElementType = ElementType.ELECTRO
    usage: int = 2
    max_usage: int = 2

    def on_end_phase(self, game: 'GeniusGame'):
        '''
            结束阶段: 造成1点雷元素伤害
            结束阶段分先后手两次调用on_end_phase, 所以需要判断
        '''
        if game.active_player == self.from_player:
            dmg = Damage.create_damage(
                game,
                damage_type=SkillType.SUMMON,
                main_damage_element=self.element,
                main_damage=1,
                piercing_damage=0,
                damage_from=self,
                damage_to=get_opponent_active_character(game),
            )
            game.add_damage(dmg)
            game.resolve_damage()
            self.current_usage -= 1
        if(self.current_usage <= 0):
            '''
                Entity在被移除时, 调用on_destroy移除监听并执行对应的移除操作(在对应区域中移除此entity等)
            '''
            self.on_destroy(game)
    
    def update(self):
        self.current_usage = self.usage

    def update_listener_list(self):
        '''
            更新需要监听的事件, 在init时会调用并自动监听
        '''
        self.listeners = [
            (EventType.END_PHASE, ZoneType.SUMMON_ZONE, self.on_end_phase)
        ]

    def __init__(self, game: 'GeniusGame', from_player: 'GeniusPlayer', from_character=None):
        super().__init__(game, from_player, from_character)


class BoltsOfDownfall(NormalAttack):
    '''
        菲谢尔
        普通攻击
        罪灭之矢
    '''
    id: int = 0
    type: SkillType = SkillType.NORMAL_ATTACK

    # damage
    damage_type: SkillType = SkillType.NORMAL_ATTACK
    main_damage_element: ElementType = ElementType.PHYSICAL
    main_damage: int = 2
    piercing_damage: int = 0

    # cost
    cost = [
        {
            'cost_num': 1,
            'cost_type': CostType.ELECTRO
        },
        {
            'cost_num': 2,
            'cost_type': CostType.BLACK
        }
    ]
    energy_cost: int = 0
    energy_gain: int = 1

    def on_call(self, game: 'GeniusGame'):
        super().on_call(game)
        self.resolve_damage(game)
        if self.from_character.talent:
            oz = self.from_character.from_player.summons_zone.has_entity(Oz)
            if oz is not None:
                oz.current_usage -= 1
                dmg = Damage.create_damage(
                    game,
                    damage_type=SkillType.SUMMON,
                    main_damage_element=oz.element,
                    main_damage=1,
                    piercing_damage=0,
                    damage_from=oz,
                    damage_to=get_opponent_active_character(game),
                )
                game.add_damage(dmg)
                game.resolve_damage()
                if oz.current_usage <= 0:
                    oz.on_destroy(game)
        self.gain_energy(game)
        game.manager.invoke(EventType.AFTER_USE_SKILL, game)

class Nightrider(ElementalSkill):
    '''
        菲谢尔
        元素战技
        夜巡影翼
    '''
    id: int = 1
    type: SkillType = SkillType.ELEMENTAL_SKILL

    # damage
    damage_type: SkillType = SkillType.ELEMENTAL_SKILL
    main_damage_element: ElementType = ElementType.ELECTRO
    main_damage: int = 1
    piercing_damage: int = 0

    # cost
    cost = [
        {
            'cost_num': 3,
            'cost_type': CostType.ELECTRO
        }
    ]
    energy_cost: int = 0
    energy_gain: int = 1

    def generate_summon(self, game: 'GeniusGame'):
        '''
            生成奥兹召唤物
        '''
        summon = self.from_character.from_player.summons_zone.has_entity(Oz)
        if summon is None:
            summon = Oz(game=game, 
                    from_player=self.from_character.from_player, 
                    from_character=self.from_character)
            self.from_character.from_player.summons_zone.add_entity(summon)
        else:
            summon.update()
        
    def on_call(self, game: GeniusGame):
        super().on_call(game)
        self.resolve_damage(game)
        self.generate_summon(game)
        self.gain_energy(game)
        game.manager.invoke(EventType.AFTER_USE_SKILL, game)


class MidnightPhantasmagoria(ElementalBurst):
    '''
        菲谢尔
        元素爆发
        至夜幻现
    '''
    id: int = 2
    type: SkillType = SkillType.ELEMENTAL_BURST
    
    damage_type: SkillType = SkillType.ELEMENTAL_BURST
    main_damage_element: ElementType = ElementType.ELECTRO
    main_damage: int = 4
    piercing_damage: int = 2

    # cost
    cost = [
        {
            'cost_num': 3,
            'cost_type': CostType.ELECTRO
        }
    ]
    energy_cost: int = 3
    energy_gain: int = 0

    def on_call(self, game: GeniusGame):
        super().on_call(game)
        self.consume_energy(game)
        self.resolve_damage(game)
        game.manager.invoke(EventType.AFTER_USE_SKILL, game)
    

class Fischl(Character):
    '''菲谢尔'''
    id: int = 0
    name: str = 'Fischl'
    element: ElementType = ElementType.ELECTRO
    weapon_type: WeaponType = WeaponType.BOW
    country: CountryType = CountryType.MONDSTADT
    init_health_point: int = 10
    max_health_point: int = 10
    skill_list = [BoltsOfDownfall, Nightrider, MidnightPhantasmagoria]

    power: int = 0
    max_power: int = 3

    def __init__(self, game: 'GeniusGame', zone, from_player: 'GeniusPlayer', index:int, from_character = None, talent = False):
        super().__init__(game, zone, from_player, index, from_character)
        self.talent = talent