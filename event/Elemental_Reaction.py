'''
Implements of Elemental Reaction.
No Damage Calculation.
All the player_id here is the player who has reaction on his character.
'''
from card.character.base import *
from game.game import GeniusGame
from entity.state import *
from entity.summon import *
#The Elemental Reaction always with the first attached element.
def Frozen(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx]
    '''
    game.players[player_id].active_zone.character_list[target_idx].is_frozen = True
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)


def Melt(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)

def Vaporize(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)

def Superconduct(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)
    
def Electro_Charged(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)
    
def Bloom(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)
    game.players[1-player_id].active_zone.add_state_entity(Dendro_Core())
def Overloaded(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)
    game.players[player_id].active_zone.change_to_next_character()

def Burning(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)
    game.players[1-player_id].active_zone.summons_zone.add_entity(Burning())

def Quicken(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)
    game.players[1-player_id].active_zone.add_state_entity(Catalyzing_Feild())


def Swirl(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)


def Crystallize(game:GeniusGame, player_id: int, target_idx: int):
    '''
    game.players[player_id].active_zone.character_list[target_idx] .
    '''
    game.players[player_id].active_zone.character_list[target_idx].elemental_application.pop(0)
    game.players[player_id].active_zone.add_state_entity(Crystallize_Shield())
