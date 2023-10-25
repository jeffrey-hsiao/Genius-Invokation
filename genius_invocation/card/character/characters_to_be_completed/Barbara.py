from genius_invocation.card.character.import_head import *


class Barbara(Character):
    id: int = 1201
    name: str = "Barbara"
    name_ch = "芭芭拉"
    element: ElementType = ElementType.HYDRO
    weapon_type: WeaponType = WeaponType.CATALYST
    country: CountryType = CountryType.MONDSTADT
    init_health_point: int = 10
    max_health_point: int = 10
    skill_list: List = []
    max_power: int = 3

    def __init__(self, game: 'GeniusGame', zone: 'CharacterZone', from_player: 'GeniusPlayer', index: int, from_character=None, talent=False):
        super().__init__(game, zone, from_player, index, from_character)
        self.power = 0
        self.talent = talent
