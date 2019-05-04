import wx
from GUI import layout as lay


class MainFrame(lay.main_dialog):
    def __init__(self, parent):
        lay.main_dialog.__init__(self, parent)

    def FindSquare(self, event):
        num = int(self.m_textCtrl1.GetValue())
        self.m_textCtrl2.SetValue(str(num * num))


app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()
