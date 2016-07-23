from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from functools import partial

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    GridLayout:
        cols: 3
        Button:
            text: 'Puzzle 1'
            on_press: root.manager.current = 'puz1'
            background_normal: ""
            background_color: (1,1,1,1)
            color: (1,0.5,0.7,1)
            font_size: '24sp'
        Button:
            text: 'Puzzle 2'
            on_press: root.manager.current = 'puz2'
            background_normal: ""
            background_color: (1,1,1,1)
            color: (1,0.5,0.7,1)
            font_size: '24sp'
        Button:
            text: 'Puzzle 3'
            on_press: root.manager.current = 'puz3'
            background_normal: ""
            background_color: (1,1,1,1)
            color: (1,0.5,0.7,1)
            font_size: '24sp'
        Button:
            text: 'Puzzle 4'
            on_press: root.manager.current = 'puz4'
            background_normal: ""
            background_color: (1,1,1,1)
            color: (1,0.5,0.7,1)
            font_size: '24sp'
        Button:
            text: 'Puzzle 5'
            on_press: root.manager.current = 'puz5'
            background_normal: ""
            background_color: (1,1,1,1)
            color: (1,0.5,0.7,1)
            font_size: '24sp'
        Button:
            text: 'Puzzle 6'
            on_press: root.manager.current = 'puz6'
            background_normal: ""
            background_color: (1,1,1,1)
            color: (1,0.5,0.7,1)
            font_size: '24sp'
        Button:
            text: 'Puzzle 7'
            on_press: root.manager.current = 'puz7'
            background_normal: ""
            background_color: (1,1,1,1)
            color: (1,0.5,0.7,1)
            font_size: '24sp'
        Button:
            text: 'Puzzle 8'
            on_press: root.manager.current = 'puz8'
            background_normal: ""
            background_color: (1,1,1,1)
            color: (1,0.5,0.7,1)
            font_size: '24sp'
        Button:
            text: 'Puzzle 9'
            on_press: root.manager.current = 'puz9'
            background_normal: ""
            background_color: (1,1,1,1)
            color: (1,0.5,0.7,1)
            font_size: '24sp'


<WelcomeScreen>
    Image:
        source: 'bombs away.png'

""")
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        try:
            super(WelcomeScreen, self).__init__(**kwargs)
            Clock.schedule_once(self.callNext, 5)
        except:
            pass

    def callNext(self, dt):
        self.manager.current = 'menu'

class MenuScreen(Screen):
    pass


class PuzzleOneScreen(Screen):
    layout = GridLayout(cols=5)
    marking = [0,1,0,0,0,0,0,0,4,7,0,1,5,0,0,4,0,3,0,0,4,0,0,7,4]
    bombs =   [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0]

    numOfBombs = 0
    numOfFoundBombs = 0

    for num in bombs:
        if (num == 1):
            numOfBombs = numOfBombs + 1

    def generateGrid(self):
        for i in range(25):
            btn = Button(on_release=partial(self.btnClick, self.bombs[i]), id=str(i))
            if (self.marking[i] == 0):
                btn.background_normal = "blank.png"
            elif (self.marking[i] == 1):
                btn.background_normal = "cir1.png"
            elif (self.marking[i] == 2):
                btn.background_normal = "cir2.png"
            elif (self.marking[i] == 3):
                btn.background_normal = "cir3.png"
            elif (self.marking[i] == 4):
                btn.background_normal = "sq1.png"
            elif (self.marking[i] == 5):
                btn.background_normal = "sq2.png"
            elif (self.marking[i] == 6):
                btn.background_normal = "sq3.png"
            elif (self.marking[i] == 7):
                btn.background_normal = "Tri1.png"
            elif (self.marking[i] == 8):
                btn.background_normal = "Tri2.png"
            elif (self.marking[i] == 9):
                btn.background_normal = "Tri3.png"

            self.layout.add_widget(btn)

    def __init__(self, **kwargs):
        super(PuzzleOneScreen, self).__init__(**kwargs)
        self.generateGrid()
        self.layout.add_widget(Button(on_release=self.callNext, text="Return to menu", background_normal='', color=(1,0.5,0.7,1)))
        self.layout.add_widget(Button(on_release=self.refresh, text="Refresh", background_normal='', color=(1,0.5,0.7,1)))
        for i in range(3):
            btn = Button(background_normal='')
            self.layout.add_widget(btn)
        self.add_widget(self.layout)

    def refresh(self, *args):
        for widget in self.walk():
            try:
                widID = int(widget.id)
                widget.disabled = False
                self.numOfFoundBombs = 0
            except:
                pass


    def btnClick(self, hasBomb, value, *args):
        if (hasBomb == 1):
            self.numOfFoundBombs = self.numOfFoundBombs + 1
            value.background_disabled_normal = "mine.png"
            value.disabled = True

        if (self.numOfFoundBombs == self.numOfBombs):
            lbl = Label(text="You win!")
            self.layout.add_widget(lbl)
            Clock.schedule_once(self.callNext, 1.5)

        if (hasBomb == 0):
            value.background_disabled_normal = "incorrect.png"
            value.disabled = True
            lbl = Label(text="You lose!")
            self.layout.add_widget(lbl)

    def callNext(self, dt):
        sm.current = 'menu'


class PuzzleTwoScreen(Screen):
    layout = GridLayout(cols=5)
    marking = [0,0,0,0,1,4,0,1,7,0,0,1,4,7,0,0,0,4,7,0,0,7,0,0,2]
    bombs = [0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0]

    numOfBombs = 0
    numOfFoundBombs = 0

    for num in bombs:
        if (num == 1):
            numOfBombs = numOfBombs + 1

    def generateGrid(self):
        for i in range(25):
            btn = Button(on_release=partial(self.btnClick, self.bombs[i]), id=str(i))
            if (self.marking[i] == 0):
                btn.background_normal = "blank.png"
            elif (self.marking[i] == 1):
                btn.background_normal = "cir1.png"
            elif (self.marking[i] == 2):
                btn.background_normal = "cir2.png"
            elif (self.marking[i] == 3):
                btn.background_normal = "cir3.png"
            elif (self.marking[i] == 4):
                btn.background_normal = "sq1.png"
            elif (self.marking[i] == 5):
                btn.background_normal = "sq2.png"
            elif (self.marking[i] == 6):
                btn.background_normal = "sq3.png"
            elif (self.marking[i] == 7):
                btn.background_normal = "Tri1.png"
            elif (self.marking[i] == 8):
                btn.background_normal = "Tri2.png"
            elif (self.marking[i] == 9):
                btn.background_normal = "Tri3.png"

            self.layout.add_widget(btn)

    def __init__(self, **kwargs):
        super(PuzzleTwoScreen, self).__init__(**kwargs)
        self.generateGrid()
        self.layout.add_widget(
            Button(on_release=self.callNext, text="Return to menu", background_normal='', color=(1, 0.5, 0.7, 1)))
        self.layout.add_widget(
            Button(on_release=self.refresh, text="Refresh", background_normal='', color=(1, 0.5, 0.7, 1)))
        for i in range(3):
            btn = Button(background_normal='')
            self.layout.add_widget(btn)
        self.add_widget(self.layout)

    def refresh(self, *args):
        for widget in self.walk():
            try:
                widID = int(widget.id)
                widget.disabled = False
                self.numOfFoundBombs = 0
            except:
                pass

    def btnClick(self, hasBomb, value, *args):
        if (hasBomb == 1):
            self.numOfFoundBombs = self.numOfFoundBombs + 1
            value.background_disabled_normal = "mine.png"
            value.disabled = True

        if (self.numOfFoundBombs == self.numOfBombs):
            lbl = Label(text="You win!")
            self.layout.add_widget(lbl)
            Clock.schedule_once(self.callNext, 1.5)

        if (hasBomb == 0):
            value.background_disabled_normal = "incorrect.png"
            value.disabled = True
            lbl = Label(text="You lose!")
            self.layout.add_widget(lbl)

    def callNext(self, dt):
        sm.current = 'menu'


class PuzzleThreeScreen(Screen):
    layout = GridLayout(cols=5)
    marking = [0,0,0,0,0,4,2,7,7,0,0,0,4,0,1,7,0,0,0,0,0,4,0,0,4]
    bombs = [0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0]

    numOfBombs = 0
    numOfFoundBombs = 0

    for num in bombs:
        if (num == 1):
            numOfBombs = numOfBombs + 1

    def generateGrid(self):
        for i in range(25):
            btn = Button(on_release=partial(self.btnClick, self.bombs[i]), id=str(i))
            if (self.marking[i] == 0):
                btn.background_normal = "blank.png"
            elif (self.marking[i] == 1):
                btn.background_normal = "cir1.png"
            elif (self.marking[i] == 2):
                btn.background_normal = "cir2.png"
            elif (self.marking[i] == 3):
                btn.background_normal = "cir3.png"
            elif (self.marking[i] == 4):
                btn.background_normal = "sq1.png"
            elif (self.marking[i] == 5):
                btn.background_normal = "sq2.png"
            elif (self.marking[i] == 6):
                btn.background_normal = "sq3.png"
            elif (self.marking[i] == 7):
                btn.background_normal = "Tri1.png"
            elif (self.marking[i] == 8):
                btn.background_normal = "Tri2.png"
            elif (self.marking[i] == 9):
                btn.background_normal = "Tri3.png"

            self.layout.add_widget(btn)

    def __init__(self, **kwargs):
        super(PuzzleThreeScreen, self).__init__(**kwargs)
        self.generateGrid()
        self.layout.add_widget(
            Button(on_release=self.callNext, text="Return to menu", background_normal='', color=(1, 0.5, 0.7, 1)))
        self.layout.add_widget(
            Button(on_release=self.refresh, text="Refresh", background_normal='', color=(1, 0.5, 0.7, 1)))
        for i in range(3):
            btn = Button(background_normal='')
            self.layout.add_widget(btn)
        self.add_widget(self.layout)

    def refresh(self, *args):
        for widget in self.walk():
            try:
                widID = int(widget.id)
                widget.disabled = False
                self.numOfFoundBombs = 0
            except:
                pass

    def btnClick(self, hasBomb, value, *args):
        if (hasBomb == 1):
            self.numOfFoundBombs = self.numOfFoundBombs + 1
            value.background_disabled_normal = "mine.png"
            value.disabled = True

        if (self.numOfFoundBombs == self.numOfBombs):
            lbl = Label(text="You win!")
            self.layout.add_widget(lbl)
            Clock.schedule_once(self.callNext, 1.5)

        if (hasBomb == 0):
            value.background_disabled_normal = "incorrect.png"
            value.disabled = True
            lbl = Label(text="You lose!")
            self.layout.add_widget(lbl)

    def callNext(self, dt):
        sm.current = 'menu'


class PuzzleFourScreen(Screen):
    layout = GridLayout(cols=5)
    marking = [2,0,0,0,7,0,4,0,0,0,0,0,1,0,7,7,0,4,0,1,0,0,0,1,0]
    bombs = [0,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1]

    numOfBombs = 0
    numOfFoundBombs = 0

    for num in bombs:
        if (num == 1):
            numOfBombs = numOfBombs + 1

    def generateGrid(self):
        for i in range(25):
            btn = Button(on_release=partial(self.btnClick, self.bombs[i]), id=str(i))
            if (self.marking[i] == 0):
                btn.background_normal = "blank.png"
            elif (self.marking[i] == 1):
                btn.background_normal = "cir1.png"
            elif (self.marking[i] == 2):
                btn.background_normal = "cir2.png"
            elif (self.marking[i] == 3):
                btn.background_normal = "cir3.png"
            elif (self.marking[i] == 4):
                btn.background_normal = "sq1.png"
            elif (self.marking[i] == 5):
                btn.background_normal = "sq2.png"
            elif (self.marking[i] == 6):
                btn.background_normal = "sq3.png"
            elif (self.marking[i] == 7):
                btn.background_normal = "Tri1.png"
            elif (self.marking[i] == 8):
                btn.background_normal = "Tri2.png"
            elif (self.marking[i] == 9):
                btn.background_normal = "Tri3.png"

            self.layout.add_widget(btn)

    def __init__(self, **kwargs):
        super(PuzzleFourScreen, self).__init__(**kwargs)
        self.generateGrid()
        self.layout.add_widget(
            Button(on_release=self.callNext, text="Return to menu", background_normal='', color=(1, 0.5, 0.7, 1)))
        self.layout.add_widget(
            Button(on_release=self.refresh, text="Refresh", background_normal='', color=(1, 0.5, 0.7, 1)))
        for i in range(3):
            btn = Button(background_normal='')
            self.layout.add_widget(btn)
        self.add_widget(self.layout)

    def refresh(self, *args):
        for widget in self.walk():
            try:
                widID = int(widget.id)
                widget.disabled = False
                self.numOfFoundBombs = 0
            except:
                pass

    def btnClick(self, hasBomb, value, *args):
        if (hasBomb == 1):
            self.numOfFoundBombs = self.numOfFoundBombs + 1
            value.background_disabled_normal = "mine.png"
            value.disabled = True

        if (self.numOfFoundBombs == self.numOfBombs):
            lbl = Label(text="You win!")
            self.layout.add_widget(lbl)
            Clock.schedule_once(self.callNext, 1.5)

        if (hasBomb == 0):
            value.background_disabled_normal = "incorrect.png"
            value.disabled = True
            lbl = Label(text="You lose!")
            self.layout.add_widget(lbl)

    def callNext(self, dt):
        sm.current = 'menu'


class PuzzleFiveScreen(Screen):
    layout = GridLayout(cols=5)
    marking = [0,0,0,0,0,0,2,0,2,0,7,0,7,0,7,0,5,5,5,0,0,0,0,0,0]
    bombs = [0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]

    numOfBombs = 0
    numOfFoundBombs = 0

    for num in bombs:
        if (num == 1):
            numOfBombs = numOfBombs + 1

    def generateGrid(self):
        for i in range(25):
            btn = Button(on_release=partial(self.btnClick, self.bombs[i]), id=str(i))
            if (self.marking[i] == 0):
                btn.background_normal = "blank.png"
            elif (self.marking[i] == 1):
                btn.background_normal = "cir1.png"
            elif (self.marking[i] == 2):
                btn.background_normal = "cir2.png"
            elif (self.marking[i] == 3):
                btn.background_normal = "cir3.png"
            elif (self.marking[i] == 4):
                btn.background_normal = "sq1.png"
            elif (self.marking[i] == 5):
                btn.background_normal = "sq2.png"
            elif (self.marking[i] == 6):
                btn.background_normal = "sq3.png"
            elif (self.marking[i] == 7):
                btn.background_normal = "Tri1.png"
            elif (self.marking[i] == 8):
                btn.background_normal = "Tri2.png"
            elif (self.marking[i] == 9):
                btn.background_normal = "Tri3.png"

            self.layout.add_widget(btn)

    def __init__(self, **kwargs):
        super(PuzzleFiveScreen, self).__init__(**kwargs)
        self.generateGrid()
        self.layout.add_widget(
            Button(on_release=self.callNext, text="Return to menu", background_normal='', color=(1, 0.5, 0.7, 1)))
        self.layout.add_widget(
            Button(on_release=self.refresh, text="Refresh", background_normal='', color=(1, 0.5, 0.7, 1)))
        for i in range(3):
            btn = Button(background_normal='')
            self.layout.add_widget(btn)
        self.add_widget(self.layout)

    def refresh(self, *args):
        for widget in self.walk():
            try:
                widID = int(widget.id)
                widget.disabled = False
                self.numOfFoundBombs = 0
            except:
                pass

    def btnClick(self, hasBomb, value, *args):
        if (hasBomb == 1):
            self.numOfFoundBombs = self.numOfFoundBombs + 1
            value.background_disabled_normal = "mine.png"
            value.disabled = True

        if (self.numOfFoundBombs == self.numOfBombs):
            lbl = Label(text="You win!")
            self.layout.add_widget(lbl)
            Clock.schedule_once(self.callNext, 1.5)

        if (hasBomb == 0):
            value.background_disabled_normal = "incorrect.png"
            value.disabled = True
            lbl = Label(text="You lose!")
            self.layout.add_widget(lbl)

    def callNext(self, dt):
        sm.current = 'menu'


class PuzzleSixScreen(Screen):
    layout = GridLayout(cols=5)
    marking = [1,0,0,0,1,0,4,0,4,0,1,0,3,0,3,0,4,0,4,0,2,0,0,0,1]
    bombs = [0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0]

    numOfBombs = 0
    numOfFoundBombs = 0

    for num in bombs:
        if (num == 1):
            numOfBombs = numOfBombs + 1

    def generateGrid(self):
        for i in range(25):
            btn = Button(on_release=partial(self.btnClick, self.bombs[i]), id=str(i))
            if (self.marking[i] == 0):
                btn.background_normal = "blank.png"
            elif (self.marking[i] == 1):
                btn.background_normal = "cir1.png"
            elif (self.marking[i] == 2):
                btn.background_normal = "cir2.png"
            elif (self.marking[i] == 3):
                btn.background_normal = "cir3.png"
            elif (self.marking[i] == 4):
                btn.background_normal = "sq1.png"
            elif (self.marking[i] == 5):
                btn.background_normal = "sq2.png"
            elif (self.marking[i] == 6):
                btn.background_normal = "sq3.png"
            elif (self.marking[i] == 7):
                btn.background_normal = "Tri1.png"
            elif (self.marking[i] == 8):
                btn.background_normal = "Tri2.png"
            elif (self.marking[i] == 9):
                btn.background_normal = "Tri3.png"

            self.layout.add_widget(btn)

    def __init__(self, **kwargs):
        super(PuzzleSixScreen, self).__init__(**kwargs)
        self.generateGrid()
        self.layout.add_widget(
            Button(on_release=self.callNext, text="Return to menu", background_normal='', color=(1, 0.5, 0.7, 1)))
        self.layout.add_widget(
            Button(on_release=self.refresh, text="Refresh", background_normal='', color=(1, 0.5, 0.7, 1)))
        for i in range(3):
            btn = Button(background_normal='')
            self.layout.add_widget(btn)
        self.add_widget(self.layout)

    def refresh(self, *args):
        for widget in self.walk():
            try:
                widID = int(widget.id)
                widget.disabled = False
                self.numOfFoundBombs = 0
            except:
                pass

    def btnClick(self, hasBomb, value, *args):
        if (hasBomb == 1):
            self.numOfFoundBombs = self.numOfFoundBombs + 1
            value.background_disabled_normal = "mine.png"
            value.disabled = True

        if (self.numOfFoundBombs == self.numOfBombs):
            lbl = Label(text="You win!")
            self.layout.add_widget(lbl)
            Clock.schedule_once(self.callNext, 1.5)

        if (hasBomb == 0):
            value.background_disabled_normal = "incorrect.png"
            value.disabled = True
            lbl = Label(text="You lose!")
            self.layout.add_widget(lbl)

    def callNext(self, dt):
        sm.current = 'menu'


class PuzzleSevenScreen(Screen):
    layout = GridLayout(cols=5)
    marking = [0,0,0,0,0,0,0,7,0,0,0,7,4,7,0,8,4,2,4,8,0,0,0,0,0]
    bombs = [0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0]

    numOfBombs = 0
    numOfFoundBombs = 0

    for num in bombs:
        if (num == 1):
            numOfBombs = numOfBombs + 1

    def generateGrid(self):
        for i in range(25):
            btn = Button(on_release=partial(self.btnClick, self.bombs[i]), id=str(i))
            if (self.marking[i] == 0):
                btn.background_normal = "blank.png"
            elif (self.marking[i] == 1):
                btn.background_normal = "cir1.png"
            elif (self.marking[i] == 2):
                btn.background_normal = "cir2.png"
            elif (self.marking[i] == 3):
                btn.background_normal = "cir3.png"
            elif (self.marking[i] == 4):
                btn.background_normal = "sq1.png"
            elif (self.marking[i] == 5):
                btn.background_normal = "sq2.png"
            elif (self.marking[i] == 6):
                btn.background_normal = "sq3.png"
            elif (self.marking[i] == 7):
                btn.background_normal = "Tri1.png"
            elif (self.marking[i] == 8):
                btn.background_normal = "Tri2.png"
            elif (self.marking[i] == 9):
                btn.background_normal = "Tri3.png"

            self.layout.add_widget(btn)

    def __init__(self, **kwargs):
        super(PuzzleSevenScreen, self).__init__(**kwargs)
        self.generateGrid()
        self.layout.add_widget(
            Button(on_release=self.callNext, text="Return to menu", background_normal='', color=(1, 0.5, 0.7, 1)))
        self.layout.add_widget(
            Button(on_release=self.refresh, text="Refresh", background_normal='', color=(1, 0.5, 0.7, 1)))
        for i in range(3):
            btn = Button(background_normal='')
            self.layout.add_widget(btn)
        self.add_widget(self.layout)

    def refresh(self, *args):
        for widget in self.walk():
            try:
                widID = int(widget.id)
                widget.disabled = False
                self.numOfFoundBombs = 0
            except:
                pass

    def btnClick(self, hasBomb, value, *args):
        if (hasBomb == 1):
            self.numOfFoundBombs = self.numOfFoundBombs + 1
            value.background_disabled_normal = "mine.png"
            value.disabled = True

        if (self.numOfFoundBombs == self.numOfBombs):
            lbl = Label(text="You win!")
            self.layout.add_widget(lbl)
            Clock.schedule_once(self.callNext, 1.5)

        if (hasBomb == 0):
            value.background_disabled_normal = "incorrect.png"
            value.disabled = True
            lbl = Label(text="You lose!")
            self.layout.add_widget(lbl)

    def callNext(self, dt):
        sm.current = 'menu'


class PuzzleEightScreen(Screen):
    layout = GridLayout(cols=5)
    marking = [0,0,1,0,0,7,1,0,1,4,0,4,7,0,0,0,0,8,0,1,4,0,3,0,0]
    bombs = [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0]

    numOfBombs = 0
    numOfFoundBombs = 0

    for num in bombs:
        if (num == 1):
            numOfBombs = numOfBombs + 1

    def generateGrid(self):
        for i in range(25):
            btn = Button(on_release=partial(self.btnClick, self.bombs[i]), id=str(i))
            if (self.marking[i] == 0):
                btn.background_normal = "blank.png"
            elif (self.marking[i] == 1):
                btn.background_normal = "cir1.png"
            elif (self.marking[i] == 2):
                btn.background_normal = "cir2.png"
            elif (self.marking[i] == 3):
                btn.background_normal = "cir3.png"
            elif (self.marking[i] == 4):
                btn.background_normal = "sq1.png"
            elif (self.marking[i] == 5):
                btn.background_normal = "sq2.png"
            elif (self.marking[i] == 6):
                btn.background_normal = "sq3.png"
            elif (self.marking[i] == 7):
                btn.background_normal = "Tri1.png"
            elif (self.marking[i] == 8):
                btn.background_normal = "Tri2.png"
            elif (self.marking[i] == 9):
                btn.background_normal = "Tri3.png"

            self.layout.add_widget(btn)

    def __init__(self, **kwargs):
        super(PuzzleEightScreen, self).__init__(**kwargs)
        self.generateGrid()
        self.layout.add_widget(
            Button(on_release=self.callNext, text="Return to menu", background_normal='', color=(1, 0.5, 0.7, 1)))
        self.layout.add_widget(
            Button(on_release=self.refresh, text="Refresh", background_normal='', color=(1, 0.5, 0.7, 1)))
        for i in range(3):
            btn = Button(background_normal='')
            self.layout.add_widget(btn)
        self.add_widget(self.layout)

    def refresh(self, *args):
        for widget in self.walk():
            try:
                widID = int(widget.id)
                widget.disabled = False
                self.numOfFoundBombs = 0
            except:
                pass

    def btnClick(self, hasBomb, value, *args):
        if (hasBomb == 1):
            self.numOfFoundBombs = self.numOfFoundBombs + 1
            value.background_disabled_normal = "mine.png"
            value.disabled = True

        if (self.numOfFoundBombs == self.numOfBombs):
            lbl = Label(text="You win!")
            self.layout.add_widget(lbl)
            Clock.schedule_once(self.callNext, 1.5)

        if (hasBomb == 0):
            value.background_disabled_normal = "incorrect.png"
            value.disabled = True
            lbl = Label(text="You lose!")
            self.layout.add_widget(lbl)

    def callNext(self, dt):
        sm.current = 'menu'


class PuzzleNineScreen(Screen):
    layout = GridLayout(cols=5)
    marking = [1,0,0,0,0,0,0,7,0,4,7,0,0,4,0,0,1,0,0,0,7,0,0,4,0]
    bombs = [0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]

    numOfBombs = 0
    numOfFoundBombs = 0

    for num in bombs:
        if (num == 1):
            numOfBombs = numOfBombs + 1

    def generateGrid(self):
        for i in range(25):
            btn = Button(on_release=partial(self.btnClick, self.bombs[i]), id=str(i))
            if (self.marking[i] == 0):
                btn.background_normal = "blank.png"
            elif (self.marking[i] == 1):
                btn.background_normal = "cir1.png"
            elif (self.marking[i] == 2):
                btn.background_normal = "cir2.png"
            elif (self.marking[i] == 3):
                btn.background_normal = "cir3.png"
            elif (self.marking[i] == 4):
                btn.background_normal = "sq1.png"
            elif (self.marking[i] == 5):
                btn.background_normal = "sq2.png"
            elif (self.marking[i] == 6):
                btn.background_normal = "sq3.png"
            elif (self.marking[i] == 7):
                btn.background_normal = "Tri1.png"
            elif (self.marking[i] == 8):
                btn.background_normal = "Tri2.png"
            elif (self.marking[i] == 9):
                btn.background_normal = "Tri3.png"

            self.layout.add_widget(btn)

    def __init__(self, **kwargs):
        super(PuzzleNineScreen, self).__init__(**kwargs)
        self.generateGrid()
        self.layout.add_widget(
            Button(on_release=self.callNext, text="Return to menu", background_normal='', color=(1, 0.5, 0.7, 1)))
        self.layout.add_widget(
            Button(on_release=self.refresh, text="Refresh", background_normal='', color=(1, 0.5, 0.7, 1)))
        for i in range(3):
            btn = Button(background_normal='')
            self.layout.add_widget(btn)
        self.add_widget(self.layout)

    def refresh(self, *args):
        for widget in self.walk():
            try:
                widID = int(widget.id)
                widget.disabled = False
                self.numOfFoundBombs = 0
            except:
                pass

    def btnClick(self, hasBomb, value, *args):
        if (hasBomb == 1):
            self.numOfFoundBombs = self.numOfFoundBombs + 1
            value.background_disabled_normal = "mine.png"
            value.disabled = True

        if (self.numOfFoundBombs == self.numOfBombs):
            lbl = Label(text="You win!")
            self.layout.add_widget(lbl)
            Clock.schedule_once(self.callNext, 1.5)

        if (hasBomb == 0):
            value.background_disabled_normal = "incorrect.png"
            value.disabled = True
            lbl = Label(text="You lose!")
            self.layout.add_widget(lbl)

    def callNext(self, dt):
        sm.current = 'menu'


# Create the screen manager
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomeScreen'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(PuzzleOneScreen(name='puz1'))
sm.add_widget(PuzzleTwoScreen(name='puz2'))
sm.add_widget(PuzzleThreeScreen(name='puz3'))
sm.add_widget(PuzzleFourScreen(name='puz4'))
sm.add_widget(PuzzleFiveScreen(name='puz5'))
sm.add_widget(PuzzleSixScreen(name='puz6'))
sm.add_widget(PuzzleSevenScreen(name='puz7'))
sm.add_widget(PuzzleEightScreen(name='puz8'))
sm.add_widget(PuzzleNineScreen(name='puz9'))


class BombsAwayApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    BombsAwayApp().run()
