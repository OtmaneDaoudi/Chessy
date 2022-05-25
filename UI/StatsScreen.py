from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from DB.connection import Connection, getstate

class StatsScreen(Screen):
    PVPtotalPLayed = NumericProperty(0)
    PVPwins = NumericProperty(0)
    PVPwinsPercentage = NumericProperty(0)
    PVPlost = NumericProperty(0)
    PVPlostPercentage = NumericProperty(0)
    PVPdraw = NumericProperty(0)
    PVPdrawPercentage = NumericProperty(0)
    PVPbestScore = NumericProperty(0)
    PVPbestScoreTime = NumericProperty(0)
    PVPbestTime = NumericProperty(0)

    PVMtotalPLayed = NumericProperty(0)
    PVMwins = NumericProperty(0)
    PVMwinsPercentage = NumericProperty(0)
    PVMlost = NumericProperty(0)
    PVMlostPercentage = NumericProperty(0)
    PVMdraw = NumericProperty(0)
    PVMdrawPercentage = NumericProperty(0)
    PVMbestScore = NumericProperty(0)
    PVMbestScoreTime = NumericProperty(0)
    PVMbestTime = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_stats()
        

    def update_stats(self, *args):
        data = Connection.getStats()
        pvp = data[0]
        #pvp data
        StatsScreen.PVPtotalPLayed = pvp[1]
        StatsScreen.PVPwins = pvp[2]
        StatsScreen.PVPlost = pvp[5]
        StatsScreen.PVPdraw = pvp[6]
        if StatsScreen.PVPtotalPLayed != 0:
            StatsScreen.PVPwinsPercentage = StatsScreen.PVPwins/StatsScreen.PVPtotalPLayed*100
            StatsScreen.PVPlostPercentage = StatsScreen.PVPlost/StatsScreen.PVPtotalPLayed*100
            StatsScreen.PVPdrawPercentage = StatsScreen.PVPdraw/StatsScreen.PVPtotalPLayed*100
        StatsScreen.PVPbestScore = pvp[3]
        
        StatsScreen.PVPbestScoreTime = pvp[7]
        StatsScreen.PVPbestTime = pvp[8]

        #pvm data 
        pvm = data[1]
        StatsScreen.PVMtotalPLayed = pvm[1]
        StatsScreen.PVMwins = pvm[2]
        StatsScreen.PVMlost = pvm[5]
        StatsScreen.PVMdraw = pvm[6]
        if StatsScreen.PVMtotalPLayed != 0:
            StatsScreen.PVMwinsPercentage = StatsScreen.PVMwins/StatsScreen.PVMtotalPLayed*100
            StatsScreen.PVMdrawPercentage = StatsScreen.PVMdraw/StatsScreen.PVMtotalPLayed*100
            StatsScreen.PVMlostPercentage = StatsScreen.PVMlost/StatsScreen.PVMtotalPLayed*100
        StatsScreen.PVMbestScore = pvm[3]
        StatsScreen.PVMbestScoreTime = pvm[7]
        StatsScreen.PVMbestTime = pvm[8]
