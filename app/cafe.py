from datetime import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine", None) is None:
            raise NotVaccinatedError("Must be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.now().date():
            raise OutdatedVaccineError(
                "The vaccine’s expiration date has passed"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("No way without a mask")
        return f"Welcome to {self.name}"
