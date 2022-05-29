"""Stores temporary hardcoded variables."""

SUPPORTED_LANGS = ['Bulgarian', 'German', 'Russian']

results = None

mode = 'Offline'

MODULE_HANDLE = "./tf_model"

def get_sample_results():
    """Dump sample results."""
    return {
        "Person": [
            99.01187896728516,
            "Лице",
            "Person",
            "Человек"
        ],
        "Human": [
            99.01187896728516,
            "Човешки",
            "Mensch",
            "Человеческий"
        ],
        "Police Dog": [
            96.62117767333984,
            "Полицейско куче",
            "Polizei-Hund",
            "Полицейская собака"
        ],
        "Dog": [
            96.62117767333984,
            "Куче",
            "Hund",
            "Собака"
        ],
        "Canine": [
            96.62117767333984,
            "Кучешки",
            "Eckzahn",
            "собачий"
        ],
        "Animal": [
            96.62117767333984,
            "Животно",
            "Tier",
            "животное"
        ],
        "Pet": [
            96.62117767333984,
            "Домашен любимец",
            "Pet",
            "Питомец"
        ],
        "Mammal": [
            96.62117767333984,
            "Бозайник",
            "Säugetier",
            "млекопитающее"
        ],
        "German Shepherd": [
            67.01753234863281,
            "Немска овчарка",
            "Schäferhund",
            "Немецкая овчарка"
        ],
        "Flyer": [
            59.45143127441406,
            "Флаер",
            "Flyer",
            "Флаер"
        ],
        "Advertisement": [
            59.45143127441406,
            "Реклама",
            "Werbung",
            "Реклама"
        ],
        "Paper": [
            59.45143127441406,
            "Хартия",
            "Papier",
            "Бумага"
        ],
        "Poster": [
            59.45143127441406,
            "Плакат",
            "Plakat",
            "Плакат"
        ],
        "Brochure": [
            59.45143127441406,
            "Брошура",
            "Prospekt",
            "Брошюра"
        ]
    }
