import urllib.request

import wx
import wx.xrc

from GUI import layout as lay
from time import strftime, gmtime


class MainFrame(lay.main_dialog):
    def __init__(self, parent):
        lay.main_dialog.__init__(self, parent)
        if self.borda.GetValue() is True:
            self.borda_click(0)
        else:
            self.topsis_click(0)
        self.target_refresh()

        self.result_time.Hide()

    def borda_click(self, event):
        self.weight_col.Hide()
        for i in range(1, 30):
            self.weight[i].Hide()

    def topsis_click(self, event):
        self.weight_col.Show()
        for i in range(1, 30):
            self.weight[i].Show()

    def target_select(self, event):
        self.target_refresh()

    def target_refresh(self):
        target = self.target_choiseChoices[self.target_choise.GetSelection()]
        if target == "Children":
            criteria_weight = [5, 4, 3, 3, 4, 1, 1, 5, 5, 5, 4, 2, 4, 4, 4, 4, 4, 4, 2, 1, 1, 1, 2, 5, 3, 5, 5, 5, 4]

            # 0 highest better/boollean/constant, 1 lowest/not important, 2 optimal, 3 not important
            criteria_rule = [0, 0, 2, 2, 1, 3, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
            for i in range(1, 30):
                self.rule[i].Enable(False)
                self.weight[i].Enable(False)
                self.rule[i].SetSelection(criteria_rule[i-1])

                if self.rule[i].GetString(criteria_rule[i - 1]) == "Highest Better" or self.rule[i].GetString(criteria_rule[i - 1]) == "Lowest Better":
                    self.value[i].SetValue("N/A")
                    self.value[i].Enable(False)
                if self.rule[i].GetString(criteria_rule[i - 1]) == "Not Important":
                    self.name[i].Enable(False)
                    #self.value[i].Enable(False)
                    self.weight[i].Enable(False)
                else:
                    self.name[i].Enable(True)
                if self.name[i].GetLabel() == "Height":
                    self.value[i].SetValue("145")
                if self.name[i].GetLabel() == "Width":
                    self.value[i].SetValue("65")
                if self.name[i].GetLabel() == "Screen Size":
                    self.value[i].SetValue("4.75")

                self.weight[i].SetSelection(criteria_weight[i - 1] - 1)

            self.nano_choice.SetSelection(0)
            self.micro_choice.SetSelection(0)
            self.mini_choice.SetSelection(0)
            self.full_choice.SetSelection(0)

            self.android_choice.SetSelection(5)
            self.apple_choice.SetSelection(4)
            self.microsoft_choice.SetSelection(3)
            self.blackberry_choice.SetSelection(2)
            self.firefox_choice.SetSelection(0)
            self.symbian_choice.SetSelection(1)

            self.type_c_choice.SetSelection(2)
            self.micro_choice_usb.SetSelection(1)
            self.mini_choice_usb.SetSelection(0)
        elif target == "Hi-Tech Employee":
            criteria_weight = [5, 5, 3, 3, 4, 4, 3, 4, 5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 2, 1, 3, 3, 4, 5, 4, 1, 2, 5, 4]

            # 0 highest better/boollean/constant, 1 lowest/not important, 2 optimal, 3 not important
            criteria_rule = [0, 0, 2, 2, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 3, 0, 0, 0]
            for i in range(1, 30):
                self.rule[i].Enable(False)
                self.weight[i].Enable(False)
                self.rule[i].SetSelection(criteria_rule[i - 1])

                if self.rule[i].GetString(criteria_rule[i - 1]) == "Highest Better" or self.rule[i].GetString(criteria_rule[i - 1]) == "Lowest Better":
                    self.value[i].SetValue("N/A")
                    self.value[i].Enable(False)
                if self.rule[i].GetString(criteria_rule[i - 1]) == "Not Important":
                    self.name[i].Enable(False)
                    #self.value[i].Enable(False)
                    self.weight[i].Enable(False)
                else:
                    self.name[i].Enable(True)
                if self.name[i].GetLabel() == "Height":
                    self.value[i].SetValue("150")
                if self.name[i].GetLabel() == "Width":
                    self.value[i].SetValue("70")
                if self.name[i].GetLabel() == "Screen Size":
                    self.value[i].SetValue("5.25")

                self.weight[i].SetSelection(criteria_weight[i - 1] - 1)

                self.nano_choice.SetSelection(3)
                self.micro_choice.SetSelection(2)
                self.mini_choice.SetSelection(1)
                self.full_choice.SetSelection(0)

                self.android_choice.SetSelection(5)
                self.apple_choice.SetSelection(4)
                self.microsoft_choice.SetSelection(2)
                self.blackberry_choice.SetSelection(3)
                self.firefox_choice.SetSelection(0)
                self.symbian_choice.SetSelection(1)

                self.type_c_choice.SetSelection(2)
                self.micro_choice_usb.SetSelection(1)
                self.mini_choice_usb.SetSelection(0)
        elif target == "Pensioners":
            criteria_weight = [5, 2, 4, 4, 4, 1, 1, 5, 3, 1, 1, 5, 5, 1, 4, 4, 4, 4, 4, 5, 4, 2, 1, 5, 1, 5, 5, 5, 3]

            # 0 highest better/boollean/constant, 1 lowest/not important, 2 optimal, 3 not important
            criteria_rule = [0, 0, 2, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 3, 0, 0, 0, 0]
            for i in range(1, 30):
                self.rule[i].Enable(False)
                self.weight[i].Enable(False)
                self.rule[i].SetSelection(criteria_rule[i - 1])

                if self.rule[i].GetString(criteria_rule[i - 1]) == "Highest Better" or self.rule[i].GetString(criteria_rule[i - 1]) == "Lowest Better":
                    self.value[i].SetValue("N/A")
                    self.value[i].Enable(False)
                if self.rule[i].GetString(criteria_rule[i - 1]) == "Not Important":
                    self.name[i].Enable(False)
                    #self.value[i].Enable(False)
                    self.weight[i].Enable(False)
                else:
                    self.name[i].Enable(True)
                if self.name[i].GetLabel() == "Height":
                    self.value[i].SetValue("175")
                if self.name[i].GetLabel() == "Width":
                    self.value[i].SetValue("85")

                self.weight[i].SetSelection(criteria_weight[i - 1] - 1)

                self.nano_choice.SetSelection(0)
                self.micro_choice.SetSelection(1)
                self.mini_choice.SetSelection(2)
                self.full_choice.SetSelection(3)

                self.android_choice.SetSelection(4)
                self.apple_choice.SetSelection(5)
                self.microsoft_choice.SetSelection(2)
                self.blackberry_choice.SetSelection(3)
                self.firefox_choice.SetSelection(0)
                self.symbian_choice.SetSelection(1)

                self.type_c_choice.SetSelection(2)
                self.micro_choice_usb.SetSelection(1)
                self.mini_choice_usb.SetSelection(0)
        elif target == "Custom":
            # for i in range(1, 30):
            #     self.rule[i].Enable(True)
            #     self.weight[i].Enable(True)
            #
            #     if self.specs_name[i][1] == "":
            #         self.value[i].SetValue("N/A")
            #         self.value[i].Enable(False)
            #
            #     self.weight[i].SetSelection(0)
            print("todo")
        else:
            for i in range(1, 30):
                self.weight[i].SetSelection(0)

    def calc(self, event):
        progg = wx.ProgressDialog("Please Wait", "Calculating", maximum=100, parent=None, style=wx.PD_AUTO_HIDE | wx.PD_APP_MODAL)
        progg.Pulse()

        if self.borda.GetValue() is True:
            algo = "Borda"
        else:
            algo = "TOPSIS"

        target = self.target_choiseChoices[self.target_choise.GetSelection()]

        from DataBase import TableOfPhones, dbScarper
        db = dbScarper.load_obj("DataBase/db")
        table = TableOfPhones.TableOfPhones(db, target)

        if algo == "Borda":
            from Algorithms import BordaAlgo
            result = BordaAlgo.Borda.borda(table.table, table.num_of_phones, table.num_of_specs)
        elif algo == "TOPSIS":
            from Algorithms import TopsisAlgo
            result = TopsisAlgo.Topsis.topsis(table.table, table.num_of_phones, table.num_of_specs, table.criteria_weight)

        top_candidate = []
        for i in range(0, table.num_of_phones):
            table.candidate_dict[i]["rank"] = result["result"][i]
            top_candidate.append(table.candidate_dict[i])

        top_candidate = sorted(top_candidate, key=lambda k: k["rank"], reverse=True)

        for i in range(1,6):
            self.res_phone[i].SetLabelText(top_candidate[i-1]["brand"] + " " + top_candidate[i-1]["model"])
            self.res_phone[i].SetURL(db[top_candidate[i-1]["brand"]]["models"][top_candidate[i-1]["model"]]["url"])

            img_url = db[top_candidate[i-1]["brand"]]["models"][top_candidate[i-1]["model"]]["img"]

            with urllib.request.urlopen(img_url) as url:
                with open('temp.jpg', 'wb') as f:
                    f.write(url.read())

            img = wx.Image('temp.jpg').ConvertToBitmap()

            self.res_img[i].SetBitmap(wx.Bitmap(img))

            print(top_candidate[i-1]["brand"], top_candidate[i-1]["model"], "|- Rank:", top_candidate[i-1]["rank"])

        algo_time = strftime("%H:%M:%S:{}".format(result["time"] % 1000), gmtime(result["time"]/1000.0))
        self.result_time.SetLabelText(algo + " Finished After " + algo_time)
        self.result_time.Show()
        self.Layout()

        progg.Destroy()

    def reset(self, event):
        self.target_choise.SetSelection(0)
        self.borda.SetValue(True)
        self.borda_click(0)
        self.target_refresh()

        for i in range(1,6):
            self.res_phone[i].SetLabelText("Phone Name")
            self.res_phone[i].SetURL("")
            self.res_img[i].SetBitmap(wx.NullBitmap)
            self.res_img[i].SetBitmap(wx.Bitmap("GUI/defPhone.png"))

        self.result_time.Hide()
        self.Layout()

    def rule_select(self, event):
        print(self.Id)
        print(event)


app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()
