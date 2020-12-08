# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class testFrame
###########################################################################


class TestFrame (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer4 = wx.BoxSizer(wx.VERTICAL)

		m_radioBox1Choices = [u"Radio Button"]
		self.m_radioBox1 = wx.RadioBox(self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS)
		self.m_radioBox1.SetSelection(0)
		bSizer4.Add(self.m_radioBox1, 0, wx.ALL, 5)

		self.m_bpButton1 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW | 0)
		self.m_bpButton1.SetBitmap(wx.Bitmap("res/save.png", wx.BITMAP_TYPE_ANY))
		bSizer4.Add(self.m_bpButton1, 1, wx.ALL | wx.EXPAND, 5)

		self.SetSizer(bSizer4)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_radioBox1.Bind(wx.EVT_MIDDLE_DOWN, self.mouseDown)
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.buttonClick)

		# self.Show()

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def mouseDown( self, event ):
		print('---mouse down--')
		event.Skip()

	def buttonClick(self, event):
		print('---button click--')
		event.Skip()

	def openPanel(self):
		self.Show()

	def testFn(self):
		print("我正在学 Python")

if __name__ == '__main__':
  app = wx.App()
  TestFrame(None)
  app.MainLoop()



