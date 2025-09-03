from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    num_of_miss_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            num_of_miss_masks += 1
    if num_of_miss_masks > 0:
        return f"Friends should buy {num_of_miss_masks} masks"
    return f"Friends can go to {cafe.name}"
