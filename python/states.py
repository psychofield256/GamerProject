from fysom import Fysom


states = [
    "main-menu",
    "new-party",
    "load-party",
    "settings",
    "ingame",
    "ingame-menu",
    "ingame-settings",
]
state_machine = Fysom({
    "initial": "main-menu",
    "final": "leaving",
    "events": [
        {"name": "leave", "src": "*", "dst": "leaving"},
        {"name": "new", "src": "main-menu", "dst": "new-party"},
        ("main", "new-party", "main-menu"),
        {"name": "continue", "src": "main-menu", "dst": "load-party"},
        ("options", "main-menu", "settings"),
        ("options", "ingame-menu", "ingame-settings"),
        ("back_to_main_menu", "*", "main-menu"),
        ("play", "load-party", "playing"),
        ("play", "new-party", "playing"),
    ]
})
