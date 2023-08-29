from enum import Enum


class GeoPoliticalZone(Enum):
    NORTH_CENTRAL = ["Benue", "kogi", "Kwara", "Nasarawa", "Niger", "Plateau", "Federal Capital Territory"]
    NORTH_EAST = ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"]
    NORTH_WEST = ["Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Sokoto", "Zamafara"]
    SOUTH_EAST = ["Abai", "Anambra", "Ebonyi", "Enugu", "Imo"]
    SOUTH_SOUTH = ["Akwa Ibom", "Basyelsa", "Cross River", "Delta", "Edo", "Rivers"]
    SOUTH_WEST = ["Ekiti", "Lagos", "Ogun", "Ondo", "Osun", "Oyo"]

    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


GeoPoliticalZone('Abaia')
