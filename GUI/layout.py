# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 17 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class main_dialog
###########################################################################

class main_dialog ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Phone Picker", pos = wx.DefaultPosition, size = wx.Size( 1010,795 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		main_dialog = wx.FlexGridSizer( 2, 1, 0, 0 )
		main_dialog.SetFlexibleDirection( wx.VERTICAL )
		main_dialog.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )

		options = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap6 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		options.Add( self.m_bitmap6, 0, wx.ALL, 5 )

		algorithms = wx.BoxSizer( wx.VERTICAL )

		self.algo_label = wx.StaticText( self, wx.ID_ANY, u"Algorithm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.algo_label.Wrap( -1 )

		self.algo_label.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		algorithms.Add( self.algo_label, 0, wx.ALL, 5 )

		self.borda = wx.RadioButton( self, wx.ID_ANY, u"Borda", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.borda.SetValue( True )
		algorithms.Add( self.borda, 0, wx.ALL, 5 )

		self.topsis = wx.RadioButton( self, wx.ID_ANY, u"TOPSIS", wx.DefaultPosition, wx.DefaultSize, 0 )
		algorithms.Add( self.topsis, 0, wx.ALL, 5 )


		options.Add( algorithms, 1, wx.LEFT, 20 )

		targets = wx.BoxSizer( wx.VERTICAL )

		self.target_label = wx.StaticText( self, wx.ID_ANY, u"Target:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.target_label.Wrap( -1 )

		self.target_label.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		targets.Add( self.target_label, 0, wx.ALL, 5 )

		target_choiseChoices = [ u"Children", u"Hi-Tech Employee", u"Pensioners", u"Custom" ]
		self.target_choise = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, target_choiseChoices, 0 )
		self.target_choise.SetSelection( 0 )
		targets.Add( self.target_choise, 0, wx.ALL, 5 )


		options.Add( targets, 1, 0, 5 )

		buttons = wx.BoxSizer( wx.VERTICAL )

		self.calc_btn = wx.Button( self, wx.ID_ANY, u"Claculate", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttons.Add( self.calc_btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.rst_btn = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttons.Add( self.rst_btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		options.Add( buttons, 1, 0, 5 )


		main_dialog.Add( options, 1, wx.ALIGN_CENTER|wx.ALIGN_TOP|wx.ALL, 5 )

		options_container = wx.BoxSizer( wx.HORIZONTAL )

		options_container.SetMinSize( wx.Size( -1,1000 ) )
		specificatios = wx.BoxSizer( wx.VERTICAL )

		self.specifications_label = wx.StaticText( self, wx.ID_ANY, u"Specifications", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.specifications_label.Wrap( -1 )

		self.specifications_label.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		specificatios.Add( self.specifications_label, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.cols_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,15 ), wx.TAB_TRAVERSAL )
		self.cols_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		self.cols_panel.SetMaxSize( wx.Size( -1,25 ) )

		cols = wx.FlexGridSizer( 1, 5, 0, 0 )
		cols.SetFlexibleDirection( wx.BOTH )
		cols.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.spacer_col = wx.StaticText( self.cols_panel, wx.ID_ANY, u"    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacer_col.Wrap( -1 )

		self.spacer_col.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		cols.Add( self.spacer_col, 0, wx.ALL, 5 )

		self.name_col = wx.StaticText( self.cols_panel, wx.ID_ANY, u"Name                                    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_col.Wrap( -1 )

		self.name_col.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		cols.Add( self.name_col, 0, wx.ALL, 5 )

		self.rule_col = wx.StaticText( self.cols_panel, wx.ID_ANY, u"Rule                           ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rule_col.Wrap( -1 )

		self.rule_col.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		cols.Add( self.rule_col, 0, wx.ALL, 5 )

		self.value_col = wx.StaticText( self.cols_panel, wx.ID_ANY, u"Value                         ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.value_col.Wrap( -1 )

		self.value_col.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		cols.Add( self.value_col, 0, wx.ALL, 5 )

		self.weight_col = wx.StaticText( self.cols_panel, wx.ID_ANY, u"Weight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weight_col.Wrap( -1 )

		self.weight_col.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		cols.Add( self.weight_col, 0, wx.ALL, 5 )


		self.cols_panel.SetSizer( cols )
		self.cols_panel.Layout()
		specificatios.Add( self.cols_panel, 1, wx.ALL|wx.EXPAND, 5 )

		self.specs_scroll = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,-1 ), wx.VSCROLL )
		self.specs_scroll.SetScrollRate( 5, 5 )
		self.specs_scroll.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		specs = wx.FlexGridSizer( 30, 5, 0, 0 )
		specs.SetFlexibleDirection( wx.BOTH )
		specs.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

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
						["No. of CPU Cores", "constant"],
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
		self.boolean_rule_choice = ["Yes/No", "Not Important"]
		self.constant_rule_choice = ["Constant Scale", "Not Important"]
		self.spec_weight_choice = ["1", "2", "3", "4", "5"]

		for i in range(1, 30):
			self.num.append(wx.StaticText(self.specs_scroll, wx.ID_ANY, str(i), wx.DefaultPosition, wx.DefaultSize, 0))
			self.num[i].Wrap(-1)

			specs.Add(self.num[i], 0, wx.ALL, 5)

			self.name.append(wx.StaticText(self.specs_scroll, wx.ID_ANY, self.specs_name[i][0], wx.DefaultPosition, wx.DefaultSize, 0))
			self.name[i].Wrap(-1)

			specs.Add(self.name[i], 0, wx.ALL, 5)

			if self.specs_name[i][1] == "boolean":
				self.rule_choice = self.boolean_rule_choice
			elif self.specs_name[i][1] == "constant":
				self.rule_choice = self.constant_rule_choice
			else:
				self.rule_choice = self.common_rule_choice

			self.rule.append(wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.rule_choice, 0))
			self.rule[i].SetSelection(0)
			self.rule[i].Enable(False)

			specs.Add(self.rule[i], 0, wx.ALL, 5)

			self.value.append(wx.TextCtrl(self.specs_scroll, wx.ID_ANY, "no value", wx.DefaultPosition, wx.DefaultSize, 0))
			self.value[i].SetMaxLength(10)
			self.value[i].Enable(False)

			specs.Add(self.value[i], 0, wx.ALL, 5)

			self.weight.append(wx.Choice(self.specs_scroll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.spec_weight_choice, 0))
			self.weight[i].SetSelection(0)
			self.weight[i].Enable(False)

			specs.Add(self.weight[i], 0, wx.ALL, 5)

		self.specs_scroll.SetSizer( specs )
		self.specs_scroll.Layout()
		specificatios.Add( self.specs_scroll, 1, wx.ALL|wx.EXPAND, 5 )


		options_container.Add( specificatios, 1, wx.EXPAND, 5 )

		result = wx.BoxSizer( wx.VERTICAL )

		self.result_label = wx.StaticText( self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.result_label.Wrap( -1 )

		self.result_label.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		result.Add( self.result_label, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.res_scroll = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.VSCROLL )
		self.res_scroll.SetScrollRate( 5, 5 )
		self.res_scroll.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		top_5 = wx.FlexGridSizer( 5, 3, 0, 0 )
		top_5.SetFlexibleDirection( wx.HORIZONTAL )
		top_5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.label1 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"1.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )

		top_5.Add( self.label1, 0, wx.ALL, 5 )

		self.name1 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"phone name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name1.Wrap( -1 )

		top_5.Add( self.name1, 0, wx.ALL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self.res_scroll, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		top_5.Add( self.m_bitmap1, 0, wx.ALL, 5 )

		self.label2 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"2.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label2.Wrap( -1 )

		top_5.Add( self.label2, 0, wx.ALL, 5 )

		self.name2 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"phone name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name2.Wrap( -1 )

		top_5.Add( self.name2, 0, wx.ALL, 5 )

		self.m_bitmap2 = wx.StaticBitmap( self.res_scroll, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		top_5.Add( self.m_bitmap2, 0, wx.ALL, 5 )

		self.label3 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"3.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label3.Wrap( -1 )

		top_5.Add( self.label3, 0, wx.ALL, 5 )

		self.name3 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"phone name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name3.Wrap( -1 )

		top_5.Add( self.name3, 0, wx.ALL, 5 )

		self.m_bitmap3 = wx.StaticBitmap( self.res_scroll, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		top_5.Add( self.m_bitmap3, 0, wx.ALL, 5 )

		self.label4 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"4.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label4.Wrap( -1 )

		top_5.Add( self.label4, 0, wx.ALL, 5 )

		self.name4 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"phone name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name4.Wrap( -1 )

		top_5.Add( self.name4, 0, wx.ALL, 5 )

		self.m_bitmap4 = wx.StaticBitmap( self.res_scroll, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		top_5.Add( self.m_bitmap4, 0, wx.ALL, 5 )

		self.label5 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"5.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label5.Wrap( -1 )

		top_5.Add( self.label5, 0, wx.ALL, 5 )

		self.name5 = wx.StaticText( self.res_scroll, wx.ID_ANY, u"phone name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name5.Wrap( -1 )

		top_5.Add( self.name5, 0, wx.ALL, 5 )

		self.m_bitmap5 = wx.StaticBitmap( self.res_scroll, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		top_5.Add( self.m_bitmap5, 0, wx.ALL, 5 )


		self.res_scroll.SetSizer( top_5 )
		self.res_scroll.Layout()
		result.Add( self.res_scroll, 1, wx.EXPAND |wx.ALL, 5 )


		options_container.Add( result, 1, wx.EXPAND, 5 )


		main_dialog.Add( options_container, 1, wx.ALIGN_CENTER|wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( main_dialog )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


