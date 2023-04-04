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

MATCH = 'match'
GAME = 'game'
PLAYER1 = 'Player1'
PLAYER2 = 'Player2'

# Update per match
PLAYERS = {
    PLAYER1: 'Felix ',
    PLAYER2: 'Phim  '
}

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