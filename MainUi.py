import wx
from GUI import layout as lay


class MainFrame(lay.main_dialog):
    def __init__(self, parent):
        lay.main_dialog.__init__(self, parent)
        if self.borda.GetValue() is True:
            self.borda_click(0)
        else:
            self.topsis_click(0)

    def borda_click(self, event):
        self.weight_col.Hide()
        for i in range(1, 30):
            self.weight[i].Hide()

    def topsis_click(self, event):
        self.weight_col.Show()
        for i in range(1, 30):
            self.weight[i].Show()

    def target_select(self, event):
        target = self.target_choiseChoices[self.target_choise.GetSelection()]



        if target == "Children":
            criteria_weight = [5, 4, 3, 3, 4, 1, 1, 5, 5, 5, 4, 2, 4, 4, 4, 4, 4, 4, 2, 1, 1, 1, 2, 5, 3, 5, 5, 5, 4]
            for i in range(1, 30):
                self.rule[i].Enable(False)
                self.value[i].Enable(False)
                self.weight[i].Enable(False)

                self.weight[i].SetSelection(criteria_weight[i-1]-1)
        elif target == "Hi-Tech Employee":
            criteria_weight = [5, 5, 3, 3, 4, 4, 3, 4, 5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 2, 1, 3, 3, 4, 5, 4, 1, 2, 5, 4]
            for i in range(1, 30):
                self.rule[i].Enable(False)
                self.value[i].Enable(False)
                self.weight[i].Enable(False)

                self.weight[i].SetSelection(criteria_weight[i-1]-1)
        elif target == "Pensioners":
            criteria_weight = [5, 2, 4, 4, 4, 1, 1, 5, 3, 1, 1, 5, 5, 1, 4, 4, 4, 4, 4, 5, 4, 2, 1, 5, 1, 5, 5, 5, 3]
            for i in range(1, 30):
                self.rule[i].Enable(False)
                self.value[i].Enable(False)
                self.weight[i].Enable(False)

                self.weight[i].SetSelection(criteria_weight[i-1]-1)
        elif target == "Custom":
            for i in range(1, 30):
                self.rule[i].Enable(True)
                self.value[i].Enable(True)
                self.weight[i].Enable(True)

                self.weight[i].SetSelection(0)
        else:
            for i in range(1, 30):
                self.weight[i].SetSelection(0)

    def calc(self, event):
        if self.borda.GetValue() is True:
            algo = "borda"
        else:
            alg = "topsis"

        target = self.target_choiseChoices[self.target_choise.GetSelection()]
        print((target))

    def reset(self, event):
        self.name2.SetLabelText("reset")

    def rule_select(self, event):
        print(event)


app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()
