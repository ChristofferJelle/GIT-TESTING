# Fiktive undervisningsdata fra NordicSec, ikke virkelige loginhændelser.
loginhaendelser = [
    {"bruger": "anna", "status": "fejlet"},
    {"bruger": "bo", "status": "ok"},
    {"bruger": "anna", "status": "fejlet"},
    {"bruger": "carl", "status": "fejlet"},
    {"bruger": "bo", "status": "ok"},
]


def tael_fejlede(haendelser):
    antal = 0
    for haendelse in haendelser:
        if haendelse["status"] == "fejlet":
            antal = antal + 1
    return antal


print("Fejlede loginforsøg:", tael_fejlede(loginhaendelser))
