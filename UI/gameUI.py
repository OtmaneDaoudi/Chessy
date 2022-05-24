import threading
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from functools import partial
from Classes.AiPlayer import AiPlayer
from Classes.Game import Game
from Classes.Piece import Piece
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread
from kivy.core.audio import SoundLoader
from kivy.animation import Animation    
from kivy.app import App
from Classes.Knight import Knight
from Classes.Pawn import Pawn
from Classes.Rook import Rook
from Classes.Queen import Queen
from Classes.Bishop import Bishop
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from copy import deepcopy
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty
from kivy.config import Config
import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from DB.connection import Connection
import pickle

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '630')
Config.set('graphics', 'resizable', True)
# Window.borderless = True
Config.write()

class Cell(ToggleButton):
    def __init__(self,rank: int,column: int,color: tuple,piece: Piece,**kwargs):
        super().__init__(**kwargs)
        self.piece = piece
        self.rank = rank
        self.column = column
        self.background_normal=''
        self.background_color = color
        self.img = None
        self.firstMake = True
        
        
    @mainthread
    def set_img_pos(self, *args):
        if self.img is not None:
            self.remove_widget(self.img)
        source_ = "./Assets/images/None.png" 
        if self.piece is not None:
            source_ ="./Assets/images/"+self.piece.image
        if self.firstMake:
            self.img = Image(source = source_)
            self.img.opacity = 0
            a = Animation(duration = .3, opacity = 1)
            
            a.start(self.img)
            self.firstMake = False
        else:
            self.img = Image(source = source_)
        self.img.allow_stretch = True
        self.img.pos = [self.pos[0] + 3, self.pos[1]]
        self.img.size = (70,70)
        self.add_widget(self.img)
class GameUi(BoxLayout, Screen):
    gameMode = None
    playAs = "w"
    diff = 1
    current_gameui = None
class ChessBoard(GridLayout):
    current_game = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print("game mode : ", self.parent.parent.gameMode)
        # print("game mode : ", GameUi.gameMode)
        # print("play as : ", GameUi.playAs)

        self.game = Game(self)
        ChessBoard.current_game = self.game

        self.undo_stack = []
        self.redo_stack = []

        self.selected_cell = None
        self.marked_moved = []

        self.cols = 8
        self.rows = 9
        self.padding = -1
        self.spacing = -2
        # self.spacing = 30

        light_square = (242/255.0, 225/255.0, 195/255.0, 1)
        dark_square  = (195/255.0, 160/255.0, 130/255.0, 1)
        current_color = light_square

        self.cells = [] #stores grid cells
        for _ in range(8):
            self.cells.append([None, None, None, None, None, None, None, None])

        for rank in reversed(range(8)):
            for column in range(8):
                newCell = Cell(rank,column,current_color,self.game.game_board.board[rank][column])
                newCell.on_press = partial(self.selected, rank, column, newCell)
                self.cells[rank][column] = newCell
                self.add_widget(newCell)
                Clock.schedule_once(newCell.set_img_pos, 1)
                if current_color == light_square:
                    current_color = dark_square
                else: 
                    current_color = light_square
            if current_color == light_square:
                    current_color = dark_square
            else: 
                current_color = light_square

        self.move_piece_sound = SoundLoader.load('./Assets/audio/piece_move.wav')
        
        #schedule clock updates
        self.clocks_job = Clock.schedule_interval(self.game.update_clocks, 1)
        Clock.schedule_once(self.setBtns)

        if isinstance(self.game.white_player, AiPlayer):
            #make the algorithm go firs
            print("ok")
            Clock.schedule_once(self.AiMoveThread, 1)

    def setBtns(self, *args):
        # print("ids = ", App.get_running_app().root.get_screen('gameUi').ids)

        App.get_running_app().root.get_screen('gameUi').ids.options.ids.exit_btn.on_press = self.exit

        self.redo_btn = App.get_running_app().root.get_screen('gameUi').ids.options.ids.redo 
        self.redo_btn.on_press = self.redo
        self.redo_btn.disabled = True

        self.undo_btn = App.get_running_app().root.get_screen('gameUi').ids.options.ids.undo 
        self.undo_btn.on_press = self.undo
        self.undo_btn.disabled = True
    
    def exit(self, *args):
        #show confirmation diallogue
        btn1 = Button(text="Yes", size_hint=(1, None), height = 80)
        btn2 = Button(text="no", size_hint=(1, None), height = 80)
        Boxed_layout= BoxLayout(orientation = "horizontal")
        Boxed_layout.add_widget(btn1)
        Boxed_layout.add_widget(btn2)
        pop = Popup(title="Are you sure?",content=Boxed_layout, size_hint=(.5,.25))
        btn1.bind(on_release=partial(self.apply_exiting, pop))

        # btn1.bind(on_release=partial(doit, pop)) # bind to whatever action is being confiirmed
        btn2.bind(on_release=pop.dismiss)
        pop.open()

    def apply_exiting(self, pop, *args):
        # Window.close()
        # App.get_running_app().root.remove_widget(self)
        # check game status before close

        pop.dismiss()
        App.get_running_app().root.current = 'home'
        App.get_running_app().root.remove_widget(GameUi.current_gameui)
        Clock.unschedule(self.clocks_job)

    


        
    def redo(self, *args):
        print("redoing...")
        if len(self.redo_stack) > 0:
            redo_entry = self.redo_stack.pop()
            self.undo_stack.append({"board" : deepcopy(self.game.game_board), "game_state" : self.game.game_status})
            print("available redo : ")
            self.game.game_board = redo_entry["board"]
            self.game.game_status = redo_entry["game_state"]

            #switch turns
            self.game.turn = "b" if self.game.turn == "w" else "w"
            red = (1,0,0,1)
            green = (120/255,238/255,62/255,1)
            black_banner = App.get_running_app().root.get_screen('gameUi').ids.boardNclocks.ids.black_player_banner
            white_banner = App.get_running_app().root.get_screen('gameUi').ids.boardNclocks.ids.white_player_banner

            # switch label background colors
            if self.game.turn == "w":
                black_banner.background_color = red
                white_banner.background_color = green
            else:
                black_banner.background_color = green
                white_banner.background_color = red

            self.update_board()

            print("done redoing")
            if len(self.redo_stack) == 0:
                self.redo_btn.disabled = True

            #if AI's turn then back again 
            if (self.game.turn == "w" and isinstance(self.game.white_player, AiPlayer)) or (self.game.turn == "b" and isinstance(self.game.black_player, AiPlayer)):
                self.redo()

            
    def undo(self, *args):
        if len(self.undo_stack) > 0:
            undo_entry = self.undo_stack.pop()
            self.redo_stack.append({"board" : deepcopy(self.game.game_board), "game_state" : self.game.game_status})
            self.game.game_board = undo_entry["board"]
            self.game.game_status = undo_entry["game_state"]

            #switch turns
            self.game.turn = "b" if self.game.turn == "w" else "w"
            red = (1,0,0,1)
            green = (120/255,238/255,62/255,1)
            black_banner = App.get_running_app().root.get_screen('gameUi').ids.boardNclocks.ids.black_player_banner
            white_banner = App.get_running_app().root.get_screen('gameUi').ids.boardNclocks.ids.white_player_banner

            # switch label background colors
            if self.game.turn == "w":
                black_banner.background_color = red
                white_banner.background_color = green
            else:
                black_banner.background_color = green
                white_banner.background_color = red
            self.update_board()

            print("done undoing")
            if len(self.undo_stack) == 0:
                print('btn disabled')
                self.undo_btn.disabled = True
            self.redo_btn.disabled = False

            #if AI's turn then back again 
            if (self.game.turn == "w" and isinstance(self.game.white_player, AiPlayer)) or (self.game.turn == "b" and isinstance(self.game.black_player, AiPlayer)):
                self.undo()
        elif self.game.turn == "b" and isinstance(self.game.black_player, AiPlayer):
            print("scheduling ai move")
            Clock.schedule_once(self.AiMoveThread, 1)
        elif self.game.turn == "w" and isinstance(self.game.white_player, AiPlayer):
            print("scheduling ai move")
            Clock.schedule_once(self.AiMoveThread, 1)

    def AiMoveThread(self, *args):
        myThread = threading.Thread(target=self.AiMove, name='AI')
        myThread.start()
            
    def AiMove(self, *args):
        print("move thread started")
        move = []
        if self.game.turn == "w":
            move = self.game.white_player.getMove(self.game.game_board)
        else:
            move = self.game.black_player.getMove(self.game.game_board)
        Clock.schedule_once(partial(self.playAiMove, move))
        
    def playAiMove(self,move, *args):
        if not AiPlayer.Thread_exit_state:
            self.undo_stack.append({"board" : deepcopy(self.game.game_board), "game_state" : self.game.game_status})
            self.game.playMove(move[0], move[1], self)
            self.update_board()
            self.move_piece_sound.play()
            print("move thread ended")

    def update_board(self, *args):
        for rank in reversed(range(8)):
            for column in range(8):
                oldPiece = self.cells[rank][column].piece 
                self.cells[rank][column].piece = self.game.game_board.board[rank][column]
                if not (oldPiece == self.game.game_board.board[rank][column]):
                    self.cells[rank][column].set_img_pos()

        self.undo_btn.disabled = False

        #update captured pieces
        self.update_score()

    def update_score(self):
        black_ids = App.get_running_app().root.get_screen('gameUi').ids.black_captured_pieces.ids
        white_ids = App.get_running_app().root.get_screen('gameUi').ids.white_captured_pieces.ids

        #update white pieces           
        pieces_type = list(map(type, self.game.game_board.white_captures_pieces))
        white_ids.pawn.text = str(pieces_type.count(Pawn))
        white_ids.rook.text = str(pieces_type.count(Rook))
        white_ids.bishop.text = str(pieces_type.count(Bishop))
        white_ids.knight.text = str(pieces_type.count(Knight))
        white_ids.queen.text = str(pieces_type.count(Queen))

        #update black pieces           
        pieces_type = list(map(type, self.game.game_board.black_captures_pieces))
        black_ids.pawn.text = str(pieces_type.count(Pawn))
        black_ids.rook.text = str(pieces_type.count(Rook))
        black_ids.bishop.text = str(pieces_type.count(Bishop))
        black_ids.knight.text = str(pieces_type.count(Knight))
        black_ids.queen.text = str(pieces_type.count(Queen))
        
    def animate_move(self,start_cell: Cell, end_cell: Cell):
        ani = Animation(pos=end_cell.pos)
        ani.start(start_cell.img)
   
    def selected(self, rank, column, cell: Cell):
        if cell.piece is None:
            if (rank,column) in self.marked_moved:
                print("self type ",type(self))
                self.undo_stack.append({"board" : deepcopy(self.game.game_board) , "game_state" : self.game.game_status})
                self.game.playMove((self.selected_cell.rank,self.selected_cell.column),(rank,column), self)
                self.move_piece_sound.play()
                self.update_board()
                # self.animate_move(self.selected_cell,cell)
                self.selected_cell.state = "normal"
                self.selected_cell = None
                for oldTarget in self.marked_moved:
                    self.cells[oldTarget[0]][oldTarget[1]].state = "normal"
                self.marked_moved.clear()
            else:
                cell.state = "normal"
        elif cell == self.selected_cell:
            cell.state = "down"
        elif cell.piece.color != self.game.turn:
            if (rank,column) in self.marked_moved:
                self.undo_stack.append({"board" : deepcopy(self.game.game_board), "game_state" : self.game.game_status})
                self.game.playMove((self.selected_cell.rank,self.selected_cell.column),(rank,column), self)
                self.update_board()
                # self.animate_move(self.selected_cell,cell)
                self.move_piece_sound.play()
                self.selected_cell.state = "normal"
                self.selected_cell = None
                for oldTarget in self.marked_moved:
                    self.cells[oldTarget[0]][oldTarget[1]].state = "normal"
                self.marked_moved.clear()
            else:
                cell.state = "normal"
        else: #clicked on one of my pieces
            if self.selected_cell is None: #no selected pieces
                self.selected_cell = cell
                PossibleMoves = self.game.game_board.getEligableMoves(rank,column)
                self.marked_moved.clear()
                self.marked_moved.extend(PossibleMoves)
                for target in PossibleMoves:
                    self.cells[target[0]][target[1]].state = "down"
            else:
                self.selected_cell.state = "normal"
                self.selected_cell = cell
                for oldTarget in self.marked_moved:
                    self.cells[oldTarget[0]][oldTarget[1]].state = "normal"
                self.marked_moved.clear()
                PossibleMoves = self.game.game_board.getEligableMoves(rank,column)
                self.marked_moved.extend(PossibleMoves)
                for target in PossibleMoves:
                    self.cells[target[0]][target[1]].state = "down"

        print("game status : ",self.game.game_status.name)

    def on_exit(self):
        pass


class WindowManager(ScreenManager):
    pass


class HomePage(Screen):
    pass
    # +--------- Player VS Player Screen ---------+

class PvspScreen(Screen):
    color_clicked = BooleanProperty(True)

    def on_color_button_click(self, widget):
        if widget.text == "Black":
            print("play as black")
            GameUi.playAs = "b"
        else:
            print("play as white")
            GameUi.playAs = "w"
        if widget.state == "down":
            if self.color_clicked == False:
                self.color_clicked = True
            else:
                self.color_clicked = False
    
    def init_game(self):
        #player versus machine
        #get UI data 
        
        GameUi.gameMode = "PvP"

        gameui = GameUi()
        GameUi.current_gameui = gameui
        gameui.name = 'gameUi'
        gameui.id = 'gameUi'
        self.parent.add_widget(gameui)
        self.parent.current = 'gameUi'

    #     Clock.schedule_once(self.setCurrent, .2)

    # def setCurrent(self, *args):
    #     self.parent.current = 'gameUi'

    
    # +--------- Player VS Machine Screen ---------+
    
class PvsmScreen(Screen):
    color_clicked = BooleanProperty(True)
    level_clicked1 = BooleanProperty(True)
    level_clicked2 = BooleanProperty(False)
    level_clicked3 = BooleanProperty(False)

    def on_color_button_click(self, widget):
        if widget.text == "Black":
            print("play as black")
            GameUi.playAs = "b"
        else:
            print("play as white")
            GameUi.playAs = "w"
        if widget.state == "down":
            if self.color_clicked == False:
                self.color_clicked = True
            else:
                self.color_clicked = False

    

    def on_level_button_click(self, widget, id):
        if widget.state == "down":
            if id == 1:
                GameUi.diff = 1
                print("diff updated to 1")
                if self.level_clicked1 == False:
                    self.level_clicked1 = True
                    self.level_clicked2 = False
                    self.level_clicked3 = False
                else:
                    self.level_clicked1 = False
                    self.level_clicked2 = True
                    self.level_clicked3 = True
            elif id == 2:
                GameUi.diff = 2
                print("diff updated to 2")
                if self.level_clicked2 == False:
                    self.level_clicked2 = True
                    self.level_clicked1 = False
                    self.level_clicked3 = False
                else:
                    self.level_clicked2 = False
                    self.level_clicked1 = True
                    self.level_clicked3 = True
            else:
                GameUi.diff = 3
                print("diff updated to 3")
                if self.level_clicked3 == False:
                    self.level_clicked3 = True
                    self.level_clicked1 = False
                    self.level_clicked2 = False
                else:
                    self.level_clicked3 = False
                    self.level_clicked1 = True
                    self.level_clicked2 = True

    def init_game(self, *args):
        #player versus machine
        #get UI data 
        
        GameUi.gameMode = "PvM"

        gameui = GameUi()
        GameUi.current_gameui = gameui
        print("done initialising")
        gameui.name = 'gameUi'
        gameui.id = 'gameUi'
        self.parent.add_widget(gameui)
        self.parent.current = 'gameUi'
    #     Clock.schedule_once(self.setCurrent, .2)

    # def setCurrent(self, *args):
    #     self.parent.current = 'gameUi'

    #============================================


def show_popup(self):
        show = ContentPopup()
        window = Popup(title="Exit Chess Game", content=show,
                       size_hint=(None, None), size=(400, 400))
        show.popup = window
        window.open()
        return True

class SaveWind(Screen):
    def __init__(self, **kwargs):
        super(SaveWind, self).__init__(**kwargs)
        Window.bind(on_request_close=show_popup)

def test():
    return "-------Otman is Gay--------"

class ContentPopup(BoxLayout):
    def __init__(self,popup=None,  **kwargs):
        super().__init__(**kwargs)
        self.popup = popup

    def withSave(self):
        path = os.path.abspath(os.getcwd())
        obj = ChessBoard.current_game
        # print(obj)
        with open('GameObject','wb') as f:
            pickle.dump(obj,f)
        isComp = Connection.setPath(path+"\GameObject")
        if(isComp):
            Window.close()
    def withoutSave(self):
        Window.close()

    def closePop(self):
        self.popup.dismiss()