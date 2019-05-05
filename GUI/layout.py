# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 17 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv


###########################################################################
## Class main_dialog
###########################################################################

class main_dialog(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Game Of Phones", pos=wx.DefaultPosition,
                          size=wx.Size(1010, 795), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetIcon(wx.Icon("GUI/icon.png"))

        main_dialog = wx.FlexGridSizer(2, 1, 0, 0)
        main_dialog.SetFlexibleDirection(wx.VERTICAL)
        main_dialog.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)

        options = wx.BoxSizer(wx.HORIZONTAL)

        self.topBullet = wx.Image("GUI/topBullet.jpg").ConvertToBitmap()
        self.m_bitmap6 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(self.topBullet), wx.DefaultPosition, wx.DefaultSize,
                                         0)
        options.Add(self.m_bitmap6, 0, wx.ALL, 5)

        algorithms = wx.BoxSizer(wx.VERTICAL)

        self.algo_label = wx.StaticText(self, wx.ID_ANY, u"Algorithm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.algo_label.Wrap(-1)

        self.algo_label.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial"))

        algorithms.Add(self.algo_label, 0, wx.ALL, 5)

        self.borda = wx.RadioButton(self, wx.ID_ANY, u"Borda", wx.DefaultPosition, wx.DefaultSize, 0)
        self.borda.SetValue(True)
        algorithms.Add(self.borda, 0, wx.ALL, 5)

        self.topsis = wx.RadioButton(self, wx.ID_ANY, u"TOPSIS", wx.DefaultPosition, wx.DefaultSize, 0)
        algorithms.Add(self.topsis, 0, wx.ALL, 5)

        options.Add(algorithms, 1, wx.LEFT, 20)

        targets = wx.BoxSizer(wx.VERTICAL)

        self.target_label = wx.StaticText(self, wx.ID_ANY, u"Target:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.target_label.Wrap(-1)

        self.target_label.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial"))

        targets.Add(self.target_label, 0, wx.ALL, 5)

        self.target_choiseChoices = ["Children", "Hi-Tech Employee", "Pensioners", "Custom"]
        self.target_choise = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.target_choiseChoices,
                                       0)
        self.target_choise.SetSelection(0)
        targets.Add(self.target_choise, 0, wx.ALL, 5)

        options.Add(targets, 1, 0, 5)

        buttons = wx.BoxSizer(wx.VERTICAL)

        self.calc_btn = wx.Button(self, wx.ID_ANY, u"Claculate", wx.DefaultPosition, wx.DefaultSize, 0)
        buttons.Add(self.calc_btn, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.rst_btn = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        buttons.Add(self.rst_btn, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        options.Add(buttons, 1, 0, 5)

        main_dialog.Add(options, 1, wx.ALIGN_CENTER | wx.ALIGN_TOP | wx.ALL, 5)

        options_container = wx.BoxSizer(wx.HORIZONTAL)

        options_container.SetMinSize(wx.Size(-1, 1000))
        specificatios = wx.BoxSizer(wx.VERTICAL)

        self.specifications_label = wx.StaticText(self, wx.ID_ANY, u"Specifications", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.specifications_label.Wrap(-1)

        self.specifications_label.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial"))

        specificatios.Add(self.specifications_label, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cols_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 15), wx.TAB_TRAVERSAL)
        self.cols_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.cols_panel.SetMaxSize(wx.Size(-1, 25))

        cols = wx.FlexGridSizer(1, 5, 0, 0)
        cols.SetFlexibleDirection(wx.BOTH)
        cols.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.spacer_col = wx.StaticText(self.cols_panel, wx.ID_ANY, u"    ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.spacer_col.Wrap(-1)

        self.spacer_col.SetFont(
            wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        cols.Add(self.spacer_col, 0, wx.ALL, 5)

        self.name_col = wx.StaticText(self.cols_panel, wx.ID_ANY, u"Name                                    ",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.name_col.Wrap(-1)

        self.name_col.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        cols.Add(self.name_col, 0, wx.ALL, 5)

        self.rule_col = wx.StaticText(self.cols_panel, wx.ID_ANY, u"Rule                           ",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.rule_col.Wrap(-1)

        self.rule_col.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        cols.Add(self.rule_col, 0, wx.ALL, 5)

        self.value_col = wx.StaticText(self.cols_panel, wx.ID_ANY, u"Value                         ",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.value_col.Wrap(-1)

        self.value_col.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        cols.Add(self.value_col, 0, wx.ALL, 5)

        self.weight_col = wx.StaticText(self.cols_panel, wx.ID_ANY, u"Weight", wx.DefaultPosition, wx.DefaultSize, 0)
        self.weight_col.Wrap(-1)

        self.weight_col.SetFont(
            wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        cols.Add(self.weight_col, 0, wx.ALL, 5)

        self.cols_panel.SetSizer(cols)
        self.cols_panel.Layout()
        specificatios.Add(self.cols_panel, 1, wx.ALL | wx.EXPAND, 5)

        self.specs_scroll = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1), wx.VSCROLL)
        self.specs_scroll.SetScrollRate(5, 5)
        self.specs_scroll.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        specs = wx.FlexGridSizer(30, 5, 0, 0)
        specs.SetFlexibleDirection(wx.BOTH)
        specs.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.num = [0]
        self.name = [0]
        self.rule = [0]
        self.value = [0]
        self.weight = [0]

        self.specs_name = [
            0,
            ["Battery Capacity", ""],
            ["Year", ""],
            ["Height", ""],
            ["Width", ""],
            ["Weight", ""],
            ["No. of SIM Cards", ""],
            ["SIM Card Type", "constant"],
            ["Screen Size", ""],
            ["Screen Resolution", ""],
            ["Operating System", "constant"],
            ["No. of CPU Cores", ""],
            ["SD Card Option", "boolean"],
            ["Max SD Card Size", ""],
            ["RAM", ""],
            ["Main Camera Quality", ""],
            ["Main Camera Video", ""],
            ["Secondary Camera Quality", ""],
            ["Secondary Camera Video", ""],
            ["IR Transmitter", "boolean"],
            ["Radio", "boolean"],
            ["Charging Cable Type", "constant"],
            ["NFC", "boolean"],
            ["Finger Print", "boolean"],
            ["Price", ""],
            ["BaseMark Test", ""],
            ["Load Speaker", ""],
            ["Audio Quality", ""],
            ["Battery Endurance", ""],
            ["Water Resistant", "boolean"]
        ]
        self.common_rule_choice = ["Highest Better", "Lowest Better", "Optimal Value", "Not Important"]
        self.boolean_rule_choice = ["Boolean", "Not Important"]
        self.constant_rule_choice = ["Constant Scale", "Not Important"]
        self.spec_weight_choice = ["1", "2", "3", "4", "5"]

        sim_container = wx.FlexGridSizer(4, 2, 0, 0)
        sim_container.SetFlexibleDirection(wx.BOTH)
        sim_container.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.nano_sim = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Nano", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.nano_sim.Wrap(-1)

        sim_container.Add(self.nano_sim, 0, wx.ALL, 5)

        sim_choice = ["1", "2", "3", "4"]
        self.nano_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sim_choice, 0)
        self.nano_choice.SetSelection(0)
        self.nano_choice.Enable(False)
        sim_container.Add(self.nano_choice, 0, wx.ALL, 5)

        self.micro_sim = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Micro", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.micro_sim.Wrap(-1)

        sim_container.Add(self.micro_sim, 0, wx.ALL, 5)

        self.micro_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sim_choice,
                                      0)
        self.micro_choice.SetSelection(0)
        self.micro_choice.Enable(False)
        sim_container.Add(self.micro_choice, 0, wx.ALL, 5)

        self.mini_sim = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Mini", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.mini_sim.Wrap(-1)

        sim_container.Add(self.mini_sim, 0, wx.ALL, 5)

        self.mini_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sim_choice,
                                     0)
        self.mini_choice.SetSelection(0)
        self.mini_choice.Enable(False)
        sim_container.Add(self.mini_choice, 0, wx.ALL, 5)

        self.full_sim = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Full", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.full_sim.Wrap(-1)

        sim_container.Add(self.full_sim, 0, wx.ALL, 5)

        self.full_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sim_choice,
                                     0)
        self.full_choice.SetSelection(0)
        self.full_choice.Enable(False)
        sim_container.Add(self.full_choice, 0, wx.ALL, 5)

        # specs.Add(sim_container, 1, wx.EXPAND, 5)

        op_container = wx.FlexGridSizer(6, 2, 0, 0)
        op_container.SetFlexibleDirection(wx.BOTH)
        op_container.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.android_op = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Android", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.android_op.Wrap(-1)

        op_container.Add(self.android_op, 0, wx.ALL, 5)

        op_choice = ["1", "2", "3", "4", "5", "6"]
        self.android_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, op_choice, 0)
        self.android_choice.SetSelection(5)
        self.android_choice.Enable(False)
        op_container.Add(self.android_choice, 0, wx.ALL, 5)

        self.apple_op = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Apple", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.apple_op.Wrap(-1)

        op_container.Add(self.apple_op, 0, wx.ALL, 5)

        self.apple_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, op_choice,
                                      0)
        self.apple_choice.SetSelection(4)
        self.apple_choice.Enable(False)
        op_container.Add(self.apple_choice, 0, wx.ALL, 5)

        self.microsoft_op = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Microsoft", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.microsoft_op.Wrap(-1)

        op_container.Add(self.microsoft_op, 0, wx.ALL, 5)

        self.microsoft_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, op_choice,
                                          0)
        self.microsoft_choice.SetSelection(3)
        self.microsoft_choice.Enable(False)
        op_container.Add(self.microsoft_choice, 0, wx.ALL, 5)

        self.blackberry_op = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Blackberry", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.blackberry_op.Wrap(-1)

        op_container.Add(self.blackberry_op, 0, wx.ALL, 5)

        self.blackberry_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, op_choice,
                                           0)
        self.blackberry_choice.SetSelection(2)
        self.blackberry_choice.Enable(False)
        op_container.Add(self.blackberry_choice, 0, wx.ALL, 5)

        self.firefox_op = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Firefox", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.firefox_op.Wrap(-1)

        op_container.Add(self.firefox_op, 0, wx.ALL, 5)

        self.firefox_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, op_choice,
                                        0)
        self.firefox_choice.SetSelection(0)
        self.firefox_choice.Enable(False)
        op_container.Add(self.firefox_choice, 0, wx.ALL, 5)

        self.symbian_op = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Symbian", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.symbian_op.Wrap(-1)

        op_container.Add(self.symbian_op, 0, wx.ALL, 5)

        self.symbian_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, op_choice,
                                        0)
        self.symbian_choice.SetSelection(1)
        self.symbian_choice.Enable(False)
        op_container.Add(self.symbian_choice, 0, wx.ALL, 5)

        # specs.Add(op_container, 1, wx.EXPAND, 5)

        usb_container = wx.FlexGridSizer(3, 2, 0, 0)
        usb_container.SetFlexibleDirection(wx.BOTH)
        usb_container.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.type_c_usb = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Type C / iPhone", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.type_c_usb.Wrap(-1)

        usb_container.Add(self.type_c_usb, 0, wx.ALL, 5)

        usb_choice = ["1", "2", "3"]
        self.type_c_choice = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, usb_choice, 0)
        self.type_c_choice.SetSelection(2)
        self.type_c_choice.Enable(False)
        usb_container.Add(self.type_c_choice, 0, wx.ALL, 5)

        self.mini_usb = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Mini USB", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.mini_usb.Wrap(-1)

        usb_container.Add(self.mini_usb, 0, wx.ALL, 5)

        self.mini_choice_usb = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, usb_choice,
                                         0)
        self.mini_choice_usb.SetSelection(0)
        self.mini_choice_usb.Enable(False)
        usb_container.Add(self.mini_choice_usb, 0, wx.ALL, 5)

        self.micro_usb = wx.StaticText(self.specs_scroll, wx.ID_ANY, u"Micro USB", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.micro_usb.Wrap(-1)

        usb_container.Add(self.micro_usb, 0, wx.ALL, 5)

        self.micro_choice_usb = wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, usb_choice,
                                          0)
        self.micro_choice_usb.SetSelection(1)
        self.micro_choice_usb.Enable(False)
        usb_container.Add(self.micro_choice_usb, 0, wx.ALL, 5)

        # specs.Add(usb_container, 1, wx.EXPAND, 5)

        for i in range(1, 30):
            self.num.append(
                wx.StaticText(self.specs_scroll, wx.ID_ANY, str(i) + "  ", wx.DefaultPosition, wx.DefaultSize, 0))
            self.num[i].Wrap(-1)

            specs.Add(self.num[i], 0, wx.ALIGN_CENTER_VERTICAL, wx.ALL, 5)

            self.name.append(
                wx.StaticText(self.specs_scroll, wx.ID_ANY, self.specs_name[i][0], wx.DefaultPosition, wx.DefaultSize,
                              0))
            self.name[i].Wrap(-1)

            specs.Add(self.name[i], 0, wx.ALIGN_CENTER_VERTICAL, wx.ALL, 5)

            if self.specs_name[i][1] == "boolean":
                self.rule_choice = self.boolean_rule_choice
                self.rule.append(
                    wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.rule_choice, 0))
                self.rule[i].SetSelection(0)
                self.rule[i].Enable(False)

                specs.Add(self.rule[i], 0, wx.ALIGN_CENTER_VERTICAL, wx.ALL, 5)

                boolean_chice = ["Good", "Bad"]
                self.value.append(
                    wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, boolean_chice, 0))
                self.value[i].SetSelection(0)
                self.value[i].Enable(False)

                specs.Add(self.value[i], 0, wx.ALL, 5)
            elif self.specs_name[i][1] == "constant":
                self.rule_choice = self.constant_rule_choice
                self.rule.append(
                    wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.rule_choice, 0))
                self.rule[i].SetSelection(0)
                self.rule[i].Enable(False)

                specs.Add(self.rule[i], 0, wx.ALIGN_CENTER_VERTICAL, wx.ALL, 5)

                if self.specs_name[i][0] == "SIM Card Type":
                    self.value.append(sim_container)
                elif self.specs_name[i][0] == "Operating System":
                    self.value.append(op_container)
                elif self.specs_name[i][0] == "Charging Cable Type":
                    self.value.append(usb_container)

                specs.Add(self.value[i], 0, wx.ALL, 5)
            else:
                self.rule_choice = self.common_rule_choice
                self.rule.append(
                    wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.rule_choice, 0))
                self.rule[i].SetSelection(0)
                self.rule[i].Enable(False)

                specs.Add(self.rule[i], 0, wx.ALIGN_CENTER_VERTICAL, wx.ALL, 5)

                self.value.append(
                    wx.TextCtrl(self.specs_scroll, wx.ID_ANY, "N/A", wx.DefaultPosition, wx.DefaultSize, 0))
                self.value[i].SetMaxLength(10)
                self.value[i].Enable(False)

                specs.Add(self.value[i], 0, wx.ALL, 5)

            self.weight.append(
                wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.spec_weight_choice, 0))
            self.weight[i].SetSelection(0)
            self.weight[i].Enable(False)

            specs.Add(self.weight[i], 0, wx.ALIGN_CENTER_VERTICAL, wx.ALL, 5)

        self.specs_scroll.SetSizer(specs)
        self.specs_scroll.Layout()
        specificatios.Add(self.specs_scroll, 1, wx.ALL | wx.EXPAND, 5)

        options_container.Add(specificatios, 1, wx.EXPAND, 5)

        result = wx.BoxSizer(wx.VERTICAL)

        self.result_headline = wx.BoxSizer(wx.HORIZONTAL)

        self.result_label = wx.StaticText(self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0)
        self.result_label.Wrap(-1)

        self.result_label.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial"))

        self.result_headline.Add(self.result_label, 0, wx.ALL, 5)

        self.result_time = wx.StaticText(self, wx.ID_ANY, u"After mS", wx.DefaultPosition, wx.DefaultSize, 0)
        self.result_time.Wrap(-1)

        self.result_headline.Add(self.result_time, 0, wx.ALL, 5)

        result.Add(self.result_headline, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.res_scroll = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, -1), wx.VSCROLL)
        self.res_scroll.SetScrollRate(5, 5)
        self.res_scroll.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        top_5 = wx.FlexGridSizer(5, 3, 0, 0)
        top_5.SetFlexibleDirection(wx.HORIZONTAL)
        top_5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.res_num = [0]
        self.res_phone = [0]
        self.res_img = [0]

        for i in range(1, 6):
            self.res_num.append(
                wx.StaticText(self.res_scroll, wx.ID_ANY, str(i) + ".", wx.DefaultPosition, wx.DefaultSize, 0))
            self.res_num[i].Wrap(-1)

            top_5.Add(self.res_num[i], 0, wx.ALL, 5)

            self.res_phone.append(
                wx.adv.HyperlinkCtrl(self.res_scroll, wx.ID_ANY, u"Phone Name", "", wx.DefaultPosition, wx.DefaultSize,
                                     wx.adv.HL_DEFAULT_STYLE))

            top_5.Add(self.res_phone[i], 0, wx.ALL, 5)

            self.res_img.append(
                wx.StaticBitmap(self.res_scroll, wx.ID_ANY, wx.Bitmap("GUI/defPhone.png"), wx.DefaultPosition, wx.DefaultSize, 0))

            top_5.Add(self.res_img[i], 0, wx.ALL, 5)

        self.res_scroll.SetSizer(top_5)
        self.res_scroll.Layout()
        result.Add(self.res_scroll, 1, wx.EXPAND | wx.ALL, 5)

        options_container.Add(result, 1, wx.EXPAND, 5)

        main_dialog.Add(options_container, 1, wx.ALIGN_CENTER | wx.ALIGN_TOP | wx.ALL | wx.EXPAND, 5)

        self.SetSizer(main_dialog)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.borda.Bind(wx.EVT_RADIOBUTTON, self.borda_click)
        self.topsis.Bind(wx.EVT_RADIOBUTTON, self.topsis_click)
        self.target_choise.Bind(wx.EVT_CHOICE, self.target_select)
        self.calc_btn.Bind(wx.EVT_BUTTON, self.calc)
        self.rst_btn.Bind(wx.EVT_BUTTON, self.reset)
        for i in range(1, 30):
            self.rule[i].Bind(wx.EVT_CHOICE, self.rule_select)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def borda_click(self, event):
        event.Skip()

    def topsis_click(self, event):
        event.Skip()

    def target_select(self, event):
        event.Skip()

    def calc(self, event):
        event.Skip()

    def reset(self, event):
        event.Skip()

    def rule_select(self, event):
        event.Skip()
