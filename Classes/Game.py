#a class that handels an instance of a game
from Classes.AiPlayer import AiPlayer
from Classes.Board import Board
from enum import Enum
from Classes.OfflinePlayer import OfflinePlayer
import UI.gameUI as chessUI
from kivy.app import App

class GameStatus(Enum):
    ACTIVE = 1
    BLACK_WIN = 2
    WHITE_WIN = 3
    # FORFIET = 4
    STALEMATE = 4
    INSUFFICIENT_MATERIAL = 5
    BLACK_KING_CHECKED = 6
    WHITE_KING_CHECKED = 7
class Game:
    def __init__(self,boardUI: chessUI,turn="w"):
        self.game_board = Board()
        self.turn = turn
        self.game_status = GameStatus.ACTIVE
        self.boardUI = boardUI
        self.black_player = OfflinePlayer("w")
        self.white_player = OfflinePlayer("b")
        self.white_timer = 300
        self.black_timer = 300
        
    def start_game(self):
        #initialise Game UI
        while self.game_status == GameStatus.ACTIVE:
            turn_var = "white" if self.turn == "w" else "black"
            print(f"{turn_var}'s turn")
            # if self.game_board.isStaleMate("b") or self.game_board.isStaleMate("w"):
            #             print("Game is over, Stalemate")
            #             self.game_status = GameStatus.STALEMATE 
            # elif self.game_board.isInsufficientMaterial():
            #             print("Game is Over, Draw by insufficient material")
            #             self.game_status = GameStatus.INSUFFICIENT_MATERIAL
            if self.turn == "b":
                move = self.black_player.getMove(self.game_board) #returns a valid move
                black_AI_autopromotion = (True if isinstance(self.black_player,AiPlayer) else False)
                print(f"move stat : {self.game_board.move_piece(move[0],move[1],black_AI_autopromotion)}")
                if self.game_board.isCheck("w") :
                    if self.game_board.isCheckMate("w"):
                        print("Game is over, black team wins")
                        self.game_status = GameStatus.BLACK_WIN
                    else :
                        print("White king is under check")
                self.turn = "w"
            else:
                move = self.white_player.getMove(self.game_board) #returns a valid move
                white_AI_autopromotion = (True if isinstance(self.white_player,AiPlayer) else False)
                print(f"move stat : {self.game_board.move_piece(move[0],move[1],white_AI_autopromotion)}")
                if self.game_board.isCheck("b") :
                    if self.game_board.isCheckMate("b"):
                        print("Game is over, white team wins")
                        self.game_status = GameStatus.WHITE_WIN
                    else :
                        print("black king is under check")
                self.turn = "b"

    def update_clocks(self, *args):
        if self.turn == "w":
            mins, secs = divmod(self.white_timer, 60)
            current_time = '{:02d}:{:02d}'.format(mins, secs)
            #update lable
            # print(f"white's timer is : {current_time}")
            white_clock = App.get_running_app().root.ids.boardNclocks.ids.white_player_clock
            white_clock.text = current_time
            self.white_timer -= 1
        else:
            mins, secs = divmod(self.black_timer, 60)
            current_time = '{:02d}:{:02d}'.format(mins, secs)
            #update lable
            # print(f"black's timer is : {current_time}")
            black_clock = App.get_running_app().root.ids.boardNclocks.ids.black_player_clock
            black_clock.text = current_time
            self.black_timer -= 1
            
    def switchTurnes(self):
        self.turn = "b" if self.turn == "w" else "w"

        red = (1,0,0,1)
        green = (120/255,238/255,62/255,1)
        black_banner = App.get_running_app().root.ids.boardNclocks.ids.black_player_banner
        white_banner = App.get_running_app().root.ids.boardNclocks.ids.white_player_banner

        # switch label background colors
        if self.turn == "w":
            black_banner.background_color = red
            white_banner.background_color = green
        else:
            black_banner.background_color = green
            white_banner.background_color = red
        


    def playMove(self,start: tuple, end: tuple, gameUI):
        if self.turn == "b":
            black_AI_autopromotion = (True if isinstance(self.black_player,AiPlayer) else False)
            print(f"move stat : {self.game_board.move_piece(start,end, self.boardUI ,black_AI_autopromotion)}")
            if self.game_board.isCheck("w") :
                if self.game_board.isCheckMate("w"): 
                    print("Game is over, black team wins") #
                    self.game_status = GameStatus.BLACK_WIN
                else :
                    print("White king is under check")
        else:
            white_AI_autopromotion = (True if isinstance(self.white_player,AiPlayer) else False)
            print(f"move stat : {self.game_board.move_piece(start,end, self.boardUI,white_AI_autopromotion)}")
            if self.game_board.isCheck("b") :
                if self.game_board.isCheckMate("b"):
                    print("Game is over, white team wins")
                    self.game_status = GameStatus.WHITE_WIN
                else :
                    print("black king is under check")            
        if self.game_board.isStaleMate("b") or self.game_board.isStaleMate("w"):
            print("Game is over, Stalemate") #
            self.game_status = GameStatus.STALEMATE 
        elif self.game_board.isInsufficientMaterial():
            print("Game is Over, Draw by insufficient material")#
            self.game_status = GameStatus.INSUFFICIENT_MATERIAL
        
        self.switchTurnes()

    def getGameStatus(self):
        return self.getGameStatus

        