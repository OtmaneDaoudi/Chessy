from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty

class StatsScreen(Screen):
    PVPtotalPLayed = NumericProperty(1)
    PVPwins = NumericProperty(2)
    PVPwinsPercentage = NumericProperty(3)
    PVPlost = NumericProperty(4)
    PVPlostPercentage = NumericProperty(41)
    PVPdraw = NumericProperty(5)
    PVPdrawPercentage = NumericProperty(6)
    PVPbestScore = NumericProperty(7)
    PVPbestScoreTime = NumericProperty(8)
    PVPbestTime = NumericProperty(9)

    PVMtotalPLayed = NumericProperty(10)
    PVMwins = NumericProperty(11)
    PVMwinsPercentage = NumericProperty(12)
    PVMlost = NumericProperty(13)
    PVMlostPercentage = NumericProperty(14)
    PVMdraw = NumericProperty(15)
    PVMdrawPercentage = NumericProperty(16)
    PVMbestScore = NumericProperty(17)
    PVMbestScoreTime = NumericProperty(18)
    PVMbestTime = NumericProperty(19)