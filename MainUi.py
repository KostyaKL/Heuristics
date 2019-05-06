import random
import urllib.request

import wx
import wx.xrc

from GUI import layout as lay
from time import strftime, gmtime


class MainFrame(lay.main_dialog):

    pre_config = {}

    def __init__(self, parent):
        lay.main_dialog.__init__(self, parent)
        if self.borda.GetValue() is True:
            self.borda_click(0)
        else:
            self.topsis_click(0)

        from DataBase import preConfig
        self.pre_config = preConfig.pre_config
        self.target_refresh()

        self.result_time.Hide()

        self.get_config()

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

        if target == "Custom":
            self.rule_select(0)
            return

        for i in range(1, 30):
            if self.specs_name[i][1] == "boolean":
                self.rule[i].SetSelection(self.boolean_rule_choice.index(self.pre_config[target][i]["Rule"]))
            elif self.specs_name[i][1] == "constant":
                self.rule[i].SetSelection(self.constant_rule_choice.index(self.pre_config[target][i]["Rule"]))
            else:
                self.rule[i].SetSelection(self.common_rule_choice.index(self.pre_config[target][i]["Rule"]))

            if self.pre_config[target][i]["Name"] == "SIM Card Type":
                self.nano_choice.SetSelection(self.sim_choice.index(str(self.pre_config[target][i]["Value"][0])))
                self.micro_choice.SetSelection(self.sim_choice.index(str(self.pre_config[target][i]["Value"][1])))
                self.mini_choice.SetSelection(self.sim_choice.index(str(self.pre_config[target][i]["Value"][2])))
                self.full_choice.SetSelection(self.sim_choice.index(str(self.pre_config[target][i]["Value"][3])))
            elif self.pre_config[target][i]["Name"] == "Operating System":
                self.android_choice.SetSelection(self.op_choice.index(str(self.pre_config[target][i]["Value"][0])))
                self.apple_choice.SetSelection(self.op_choice.index(str(self.pre_config[target][i]["Value"][1])))
                self.microsoft_choice.SetSelection(self.op_choice.index(str(self.pre_config[target][i]["Value"][2])))
                self.blackberry_choice.SetSelection(self.op_choice.index(str(self.pre_config[target][i]["Value"][3])))
                self.firefox_choice.SetSelection(self.op_choice.index(str(self.pre_config[target][i]["Value"][4])))
                self.symbian_choice.SetSelection(self.op_choice.index(str(self.pre_config[target][i]["Value"][5])))
            elif self.pre_config[target][i]["Name"] == "Charging Cable Type":
                self.type_c_choice.SetSelection(self.usb_choice.index(str(self.pre_config[target][i]["Value"][0])))
                self.mini_choice_usb.SetSelection(self.usb_choice.index(str(self.pre_config[target][i]["Value"][1])))
                self.micro_choice_usb.SetSelection(self.usb_choice.index(str(self.pre_config[target][i]["Value"][2])))
            elif self.pre_config[target][i]["Rule"] == "Boolean":
                self.value[i].SetSelection(self.boolean_choice.index(str(self.pre_config[target][i]["Value"])))
                self.value[i].Enable(False)
            elif self.pre_config[target][i]["Rule"] == "Not Important":
                self.name[i].Enable(False)
            else:
                self.value[i].SetValue(self.pre_config[target][i]["Value"])
                self.value[i].Enable(False)

            self.weight[i].SetSelection(self.spec_weight_choice.index(str(self.pre_config[target][i]["Weight"])))
            self.rule[i].Enable(False)
            self.weight[i].Enable(False)

            self.nano_choice.Enable(False)
            self.micro_choice.Enable(False)
            self.mini_choice.Enable(False)
            self.full_choice.Enable(False)

            self.android_choice.Enable(False)
            self.apple_choice.Enable(False)
            self.microsoft_choice.Enable(False)
            self.blackberry_choice.Enable(False)
            self.firefox_choice.Enable(False)
            self.symbian_choice.Enable(False)

            self.type_c_choice.Enable(False)
            self.micro_choice_usb.Enable(False)
            self.mini_choice_usb.Enable(False)

    def calc(self, event):
        config = self.get_config()

        fields_error = False
        for item in config:
            if config[item]["Value"] == "":
                fields_error = True
                break
            if config[item]["Rule"] == "Constant Scale":
                if config[item]["Name"] == "SIM Card Type":
                    tmp_val = []
                    for i in range(0, 4):
                        tmp_val.append(config[item]["Value"][i])
                    while len(tmp_val) > 0:
                        tmp = tmp_val.pop()
                        if tmp in tmp_val:
                            fields_error = True
                            break
                elif config[item]["Name"] == "Operating System":
                    tmp_val = []
                    for i in range(0, 6):
                        tmp_val.append(config[item]["Value"][i])
                    while len(tmp_val) > 0:
                        tmp = tmp_val.pop()
                        if tmp in tmp_val:
                            fields_error = True
                            break
                elif config[item]["Name"] == "Charging Cable Type":
                    tmp_val = []
                    for i in range(0, 3):
                        tmp_val.append(config[item]["Value"][i])
                    while len(tmp_val) > 0:
                        tmp = tmp_val.pop()
                        if tmp in tmp_val:
                            fields_error = True
                            break
        if fields_error:
            wx.MessageBox("Please Fill All Fields", "Error!")
            return

        self.res_scroll.Hide()
        self.result_time.Hide()
        progg = wx.ProgressDialog("Please Wait", "Loading Data Base", maximum=100, parent=None, style=wx.PD_AUTO_HIDE | wx.PD_APP_MODAL)
        progg.Pulse()

        if self.borda.GetValue() is True:
            algo = "Borda"
        else:
            algo = "TOPSIS"

        from DataBase import TableOfPhones, dbScarper
        db = dbScarper.load_obj("DataBase/db")
        table = TableOfPhones.TableOfPhonesClass()
        table.build_me(db, config)

        progg.Update(2, "Calculating")
        progg.Pulse()
        if algo == "Borda":
            from Algorithms import BordaAlgo
            result = BordaAlgo.Borda.borda(table.table, table.num_of_phones-1, table.num_of_specs)
        elif algo == "TOPSIS":
            from Algorithms import TopsisAlgo
            result = TopsisAlgo.Topsis.topsis(table.table, table.num_of_phones, table.num_of_specs, table.criteria_weight)

        top_candidate = []
        for i in range(0, table.num_of_phones):
            table.candidate_dict[i]["rank"] = result["result"][i-1]
            top_candidate.append(table.candidate_dict[i])

        top_candidate = sorted(top_candidate, key=lambda k: k["rank"], reverse=True)

        progg.Update(2, "Loading Result")
        progg.Pulse()
        no_internet = False

        # print("\nalgorithm:", algo, "target:", self.target_choiseChoices[self.target_choise.GetSelection()])
        for i in range(1, 6):
            self.res_phone[i].SetLabelText(top_candidate[i-1]["brand"] + " " + top_candidate[i-1]["model"])
            self.res_phone[i].SetURL(db[top_candidate[i-1]["brand"]]["models"][top_candidate[i-1]["model"]]["url"])

            img_url = db[top_candidate[i-1]["brand"]]["models"][top_candidate[i-1]["model"]]["img"]

            if not no_internet:
                try:
                    with urllib.request.urlopen(img_url) as url:
                        with open('temp.jpg', 'wb') as f:
                            f.write(url.read())

                    img = wx.Image('temp.jpg').ConvertToBitmap()

                    self.res_img[i].SetBitmap(wx.Bitmap(img))
                except:
                    no_internet = True
                    progg.Update(100, "WARNING! No Internet Connection, Can't Load Images")
                    progg.Pulse()

            # print(top_candidate[i-1]["brand"], top_candidate[i-1]["model"], "|- Rank:", top_candidate[i-1]["rank"])

        if no_internet:
            wx.MessageBox("Can't Load Images", "No Internet Connection")

        # for debugging
        with open(self.target_choiseChoices[self.target_choise.GetSelection()] + '_table.csv', 'w') as f:
            printout = "spec"
            for i in range(0, table.num_of_specs):
                printout = printout + "," + table.specs_dict[i]
            printout = printout + "," + strftime("%d-%m-%Y %H:%M:%S", gmtime())
            f.write(printout + "\n")
            for j in range(0, table.num_of_phones):
                printout = table.candidate_dict[j]["brand"] + " " + table.candidate_dict[j]["model"]
                for i in range(0, table.num_of_specs):
                    tmp = str(table.table[i][j])
                    if tmp.find(",") >= 0:
                        tmp = "\"" + tmp + "\""
                    printout = printout + "," + tmp
                f.write(printout + "\n")
        # for debugging

        algo_time = strftime("{}".format(result["time"] % 1000), gmtime(result["time"]/1000.0))
        self.result_time.SetLabelText(algo + " Algorithm Finished After " + algo_time + " ms")
        self.result_time.Show()
        self.res_scroll.Show()
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
        config = self.get_config()
        for i in range(1, 30):
            self.rule[i].Enable(True)
            self.weight[i].Enable(True)

            if config[i]["Name"] == "SIM Card Type":
                if self.constant_rule_choice[self.rule[i].GetSelection()] == "Not Important":
                    self.nano_choice.Enable(False)
                    self.micro_choice.Enable(False)
                    self.mini_choice.Enable(False)
                    self.full_choice.Enable(False)
                    self.name[i].Enable(False)
                    self.weight[i].Enable(False)
                    self.weight[i].SetSelection(0)
                else:
                    self.nano_choice.Enable(True)
                    self.micro_choice.Enable(True)
                    self.mini_choice.Enable(True)
                    self.full_choice.Enable(True)
                    self.name[i].Enable(True)
                    self.weight[i].Enable(True)

            elif config[i]["Name"] == "Operating System":
                if self.constant_rule_choice[self.rule[i].GetSelection()] == "Not Important":
                    self.android_choice.Enable(False)
                    self.apple_choice.Enable(False)
                    self.microsoft_choice.Enable(False)
                    self.blackberry_choice.Enable(False)
                    self.firefox_choice.Enable(False)
                    self.symbian_choice.Enable(False)
                    self.name[i].Enable(False)
                    self.weight[i].Enable(False)
                    self.weight[i].SetSelection(0)
                else:
                    self.android_choice.Enable(True)
                    self.apple_choice.Enable(True)
                    self.microsoft_choice.Enable(True)
                    self.blackberry_choice.Enable(True)
                    self.firefox_choice.Enable(True)
                    self.symbian_choice.Enable(True)
                    self.name[i].Enable(True)
                    self.weight[i].Enable(True)

            elif config[i]["Name"] == "Charging Cable Type":
                if self.constant_rule_choice[self.rule[i].GetSelection()] == "Not Important":
                    self.type_c_choice.Enable(False)
                    self.micro_choice_usb.Enable(False)
                    self.mini_choice_usb.Enable(False)
                    self.name[i].Enable(False)
                    self.weight[i].Enable(False)
                    self.weight[i].SetSelection(0)
                else:
                    self.type_c_choice.Enable(True)
                    self.micro_choice_usb.Enable(True)
                    self.mini_choice_usb.Enable(True)
                    self.name[i].Enable(True)
                    self.weight[i].Enable(True)

            elif config[i]["Rule"] == "Boolean":
                if self.constant_rule_choice[self.rule[i].GetSelection()] == "Not Important":
                    self.value[i].Enable(False)
                    self.name[i].Enable(False)
                    self.weight[i].Enable(False)
                    self.weight[i].SetSelection(0)
                else:
                    self.value[i].Enable(True)
                    self.name[i].Enable(True)
                    self.weight[i].Enable(True)
            elif config[i]["Rule"] == "Not Important":
                self.value[i].Enable(False)
                if self.specs_name[i][1] != "boolean":
                    self.value[i].SetValue("N/A")
                self.name[i].Enable(False)
                self.weight[i].Enable(False)
                self.weight[i].SetSelection(0)
            elif config[i]["Rule"] != "Optimal Value":
                self.value[i].Enable(False)
                if self.specs_name[i][1] != "boolean":
                    self.value[i].SetValue("N/A")
                self.name[i].Enable(True)
                self.weight[i].Enable(True)
            else:
                self.value[i].Enable(True)
                if self.value[i].GetValue() == "N/A" and self.specs_name[i][1] != "boolean":
                    self.value[i].SetValue("")
                self.name[i].Enable(True)
                self.weight[i].Enable(True)

    def get_config(self):
        config = {}
        for i in range(1, 30):
            config[i] = {}
            config[i]["Name"] = self.name[i].GetLabelText()

            if self.specs_name[i][1] == "boolean":
                config[i]["Rule"] = self.boolean_rule_choice[self.rule[i].GetSelection()]
            elif self.specs_name[i][1] == "constant":
                config[i]["Rule"] = self.constant_rule_choice[self.rule[i].GetSelection()]
            else:
                config[i]["Rule"] = self.common_rule_choice[self.rule[i].GetSelection()]

            if config[i]["Name"] == "SIM Card Type":
                config[i]["Value"] = []
                config[i]["Value"].append(int(self.sim_choice[self.nano_choice.GetSelection()]))
                config[i]["Value"].append(int(self.sim_choice[self.micro_choice.GetSelection()]))
                config[i]["Value"].append(int(self.sim_choice[self.mini_choice.GetSelection()]))
                config[i]["Value"].append(int(self.sim_choice[self.full_choice.GetSelection()]))
            elif config[i]["Name"] == "Operating System":
                config[i]["Value"] = []
                config[i]["Value"].append(int(self.op_choice[self.android_choice.GetSelection()]))
                config[i]["Value"].append(int(self.op_choice[self.apple_choice.GetSelection()]))
                config[i]["Value"].append(int(self.op_choice[self.microsoft_choice.GetSelection()]))
                config[i]["Value"].append(int(self.op_choice[self.blackberry_choice.GetSelection()]))
                config[i]["Value"].append(int(self.op_choice[self.firefox_choice.GetSelection()]))
                config[i]["Value"].append(int(self.op_choice[self.symbian_choice.GetSelection()]))
            elif config[i]["Name"] == "Charging Cable Type":
                config[i]["Value"] = []
                config[i]["Value"].append(int(self.usb_choice[self.type_c_choice.GetSelection()]))
                config[i]["Value"].append(int(self.usb_choice[self.mini_choice_usb.GetSelection()]))
                config[i]["Value"].append(int(self.usb_choice[self.micro_choice_usb.GetSelection()]))
            elif config[i]["Rule"] == "Boolean":
                config[i]["Value"] = self.boolean_choice[self.value[i].GetSelection()]
            elif config[i]["Rule"] == "Not Important":
                config[i]["Value"] = 1
            else:
                config[i]["Value"] = self.value[i].GetValue()
            config[i]["Weight"] = int(self.spec_weight_choice[self.weight[i].GetSelection()])
        return config




app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()
