#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Fri May  3 16:58:40 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.button_1 = wx.Button(self, wx.ID_ANY, "button_1")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("Phone Picker")
        self.button_1.SetMinSize((100, 100))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        grid_sizer_1 = wx.GridSizer(2, 9, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        grid_sizer_1.SetSizeHints(self)
        self.Layout()
        self.Centre()
        # end wxGlade

# end of class MyDialog

class MyApp(wx.App):
    def OnInit(self):
        self.main_dialog = MyDialog(None, wx.ID_ANY, "")
        self.SetTopWindow(self.main_dialog)
        self.main_dialog.ShowModal()
        self.main_dialog.Destroy()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()