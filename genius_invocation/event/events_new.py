from genius_invocation.card.character.base import Damage
from collections import defaultdict
from typing import Any, List, TYPE_CHECKING, Dict
from genius_invocation.utils import *
from loguru import logger
if TYPE_CHECKING:
    from genius_invocation.game.game import GeniusGame

class ListenerNode:
    '''监听者节点'''
    def __init__(self, action, before=None, next=None):
        self.action = action
        self.before = before
        self.next = next

    def remove(self):
        if self.before:
            self.before.next = self.next
        if self.next:
            self.next.before = self.before

    def __call__(self, game: 'GeniusGame') -> None:
        self.action(game)


class Event:
    def __init__(self) -> None:
        self.listeners: Dict[ZoneType, ListenerCircles] = {}
        for zone_type in ZoneType:
            if zone_type == ZoneType.CHARACTER_ZONE:
                self.listeners[zone_type] = ListenerCircles([], need_character=True)
            else:
                self.listeners[zone_type] = ListenerCircles([])

    def __call__(self, zone_type):
        return self.listeners[zone_type]

class ListenerCircle(object):
    def __init__(self, need_character=False) -> None:
        pass

    def append_action(self, action, character_index=None) -> ListenerNode:
        pass

    def append(self, listener: ListenerNode) -> ListenerNode:
        pass

    def __call__(self, game: 'GeniusGame') -> None:
        player_index = game.active_player_index
        player0_character_index = get_active_character(game, 0)
        player1_character_index = get_active_character(game, 1)



class ListenerCircles(object):
    def __init__(self, need_character=False) -> None:
        self.player0_lisnter = ListenerCircle(need_character=need_character)
        self.player1_lisnter = ListenerCircle(need_character=need_character)

    def append_action(self, action, player_index, character_index) -> ListenerNode:
        if player_index == 0:
            return self.player0_lisnter.append_action(action, character_index)
        else:
            return self.player1_lisnter.append_action(action, character_index)

    def append(self, listener: ListenerNode) -> ListenerNode:
        pass

    def __call__(self, game: 'GeniusGame') -> None:
        player_index = game.active_player_index
        self.





'''
事件种类
'''

class EventManager:
    def __init__(self) -> None:
        self.events = defaultdict(Event)

    def listen(self, event_type: EventType, zone_type: ZoneType, action, player_index, characetr_index) -> ListenerNode:
        '''
        监听事件
        event_type: 事件类型
        zone_type: zone类型
        action: 监听动作
        '''
        return self.events[event_type](zone_type).append_action(action, player_index, characetr_index)

    def invoke(self, event_type, game: 'GeniusGame') -> None:
        for zone_type in ZoneType:
            self.events[event_type](zone_type)(game)
