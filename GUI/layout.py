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

		options_container.SetMinSize( wx.Size( -1,700 ) )
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

		self.name_col = wx.StaticText( self.cols_panel, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_col.Wrap( -1 )

		self.name_col.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		cols.Add( self.name_col, 0, wx.ALL, 5 )

		self.rule_col = wx.StaticText( self.cols_panel, wx.ID_ANY, u"Rule", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rule_col.Wrap( -1 )

		self.rule_col.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		cols.Add( self.rule_col, 0, wx.ALL, 5 )

		self.value_col = wx.StaticText( self.cols_panel, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.DefaultSize, 0 )
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

		self.specs_scroll = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.VSCROLL )
		self.specs_scroll.SetScrollRate( 5, 5 )
		self.specs_scroll.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		specs = wx.FlexGridSizer( 30, 5, 0, 0 )
		specs.SetFlexibleDirection( wx.BOTH )
		specs.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.n1 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.n1.Wrap( -1 )

		specs.Add( self.n1, 0, wx.ALL, 5 )

		self.name1 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name1.Wrap( -1 )

		specs.Add( self.name1, 0, wx.ALL, 5 )

		self.rule1 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rule1.Wrap( -1 )

		specs.Add( self.rule1, 0, wx.ALL, 5 )

		self.value1 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.value1, 0, wx.ALL, 5 )

		self.weight1 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.weight1, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		specs.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		specs.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		specs.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		specs.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		specs.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		specs.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		specs.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		specs.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		specs.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		specs.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		specs.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		specs.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		specs.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		specs.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		specs.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		specs.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		specs.Add( self.m_staticText38, 0, wx.ALL, 5 )

		self.m_staticText39 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		specs.Add( self.m_staticText39, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_staticText40 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		specs.Add( self.m_staticText40, 0, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		specs.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		specs.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

		self.m_staticText43 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		specs.Add( self.m_staticText43, 0, wx.ALL, 5 )

		self.m_staticText44 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		specs.Add( self.m_staticText44, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		specs.Add( self.m_staticText45, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		specs.Add( self.m_staticText46, 0, wx.ALL, 5 )

		self.m_staticText47 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		specs.Add( self.m_staticText47, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		specs.Add( self.m_staticText48, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		specs.Add( self.m_staticText49, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		specs.Add( self.m_staticText50, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		specs.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		specs.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.m_staticText53 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		specs.Add( self.m_staticText53, 0, wx.ALL, 5 )

		self.m_staticText54 = wx.StaticText( self.specs_scroll, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		specs.Add( self.m_staticText54, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self.specs_scroll, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		specs.Add( self.m_textCtrl24, 0, wx.ALL, 5 )


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


