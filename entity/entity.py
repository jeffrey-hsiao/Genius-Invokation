from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.game import GeniusGame
    from game.action import Action
    from event.events import EventNode


class Entity:
    def __init__(self):
        self.registered_events: list(EventNode) = []

    def register_all_events(self, game: GeniusGame):
        game.manager.register('before_skill', 'on_damage', 'after_skill')

    def on_distroy(self):
        for event in self.registered_events:
            event.del_node()
