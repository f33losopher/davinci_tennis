BASE_DAVINCI_PATH = 'BASE_DAVINCI_PATH'
GAME_TYPE = 'GAME_TYPE'
ROOT_MEDIA_FOLDER = 'ROOT_MEDIA_FOLDER'

GAME_TYPES = ("Standard", "Tiebreak")

# Update per match
CONFIG = {
    BASE_DAVINCI_PATH : "C:\\Users\\fluuc\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\",
    GAME_TYPE : 'Standard',
    ROOT_MEDIA_FOLDER : "C:\\Users\\fluuc\\Videos\\2022-08-10-Phim"

}
BASE_SCOREBOARD = CONFIG[BASE_DAVINCI_PATH] + "ScoreBoard.jpg"
DRAFT           = CONFIG[BASE_DAVINCI_PATH] + "fonts\\drafting-mono\\DraftingMono-SemiBold.ttf"
ERBOS_DRACO     = CONFIG[BASE_DAVINCI_PATH] + "fonts\\erbos-draco-monospaced-nbp-font\\ErbosDraco1StOpenNbpRegular-l5wX.ttf"
SELF_DESTRUCT   = CONFIG[BASE_DAVINCI_PATH] + "fonts\\self-destruct-button-bb-font\\SelfdestructbuttonbbBold-0gKR.otf" 

#FPS = 59.940
FPS = 29.970
AUDIO_FPS = 48000

PLAYER1 = 'Player1'
PLAYER2 = 'Player2'
PLAYERS = {
    PLAYER1: 'Felix ',
    PLAYER2: 'Phim  '
}

# To initialize a score before the video starts
# Comment out if want to start from 0-0
#init_score = {
#    'match': {
#        'Player1': [4,0],
#        'Player2': [6,0]
#    },
#    'game': {
#        'Player1': 0,
#        'Player2': 0
#    }
#}