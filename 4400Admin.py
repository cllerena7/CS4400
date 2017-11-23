from tkinter import *
import Tkinter as tk
import TkTreectrl as treectrl

class Admin:
    def __init__(self, mainWin):
        self.mainWin = mainWin
        self.mainWin.title("Administrator")

        self.fAdmin = Frame(self.mainWin, height = 150, width =100)
        self.fAdmin.pack(padx=30, pady=20)
        bStatMang = Button(self.fAdmin, text="Station Management", pady=4, command = self.StationManagement)
        bStatMang.pack()
        bSusCards = Button(self.fAdmin, text="Suspended Cards", pady=4, command = self.SuspendedCards)
        bSusCards.pack()
        bBreezeMang = Button(self.fAdmin, text="Breeze Card Management", pady=4, command = self.BreezeCardManagement)
        bBreezeMang.pack()
        bFlowReport = Button(self.fAdmin, text="Passenger Flow Report", pady=4)
        bFlowReport.pack()
        bLogOut = Button(self.fAdmin, text="Log Out", pady=15, command = self.LogOut)
        bLogOut.pack()

        mainWin.mainloop()

    def StationManagement(self):
        self.mainWin.withdraw()
 #       ttk.Frame

        root = tk.Tk()
        root.title("Station Listing")
        

    def CreateNewStation():
        self.stationListing.withdraw()
        

    def SuspendedCards(self):
        self.mainWin.withdraw()

        

    def BreezeCardManagement(self):
        self.mainWin.withdraw()

    def LogOut(self):
        self.mainWin.destroy()
        

win = Tk()
app = Admin(win)
