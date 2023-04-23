from Score.game_types import GameTypes

BASE_DAVINCI_PATH = 'BASE_DAVINCI_PATH'
GAME_TYPE = 'GAME_TYPE'
ROOT_MEDIA_FOLDER = 'ROOT_MEDIA_FOLDER'

CONFIG = {
    BASE_DAVINCI_PATH : "C:\\Users\\fluuc\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\",

    # UPDATE PER MATCH #
    GAME_TYPE : GameTypes.STANDARD,
    ROOT_MEDIA_FOLDER : "C:\\Users\\fluuc\\Videos\\2023-01-02-Doubles"
}

BASE_SCOREBOARD = CONFIG[BASE_DAVINCI_PATH] + "ScoreBoard.jpg"
DRAFT           = CONFIG[BASE_DAVINCI_PATH] + "fonts\\drafting-mono\\DraftingMono-SemiBold.ttf"
ERBOS_DRACO     = CONFIG[BASE_DAVINCI_PATH] + "fonts\\erbos-draco-monospaced-nbp-font\\ErbosDraco1StOpenNbpRegular-l5wX.ttf"
SELF_DESTRUCT   = CONFIG[BASE_DAVINCI_PATH] + "fonts\\self-destruct-button-bb-font\\SelfdestructbuttonbbBold-0gKR.otf" 

MATCH = 'match'
GAME = 'game'
PLAYER1 = 'Player1'
PLAYER2 = 'Player2'

# UPDATE PER MATCH #
PLAYERS = {
    PLAYER1: 'KP ',
    PLAYER2: 'KH '
}
# -- UPDATE PER MATCH --#

# Initialize the score before video starts
init_score = {
   MATCH: {
       PLAYER1: [0],
       PLAYER2: [0]
   },
   GAME: {
       PLAYER1: 0,
       PLAYER2: 0
   }
}