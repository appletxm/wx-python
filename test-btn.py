import wx

class ButtonClick (wx.Frame):
	def __init__(self, parent, title):
		super(ButtonClick, self).__init__(parent, title = title, size = (800, 400))
		panel = wx.Panel(self, -1)
		button = wx.Button(panel, -1, 'Close', pos = (0, 0), size = (80, 40))
		self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
		self.Bind(wx.EVT_BUTTON, self.onCloseMe, button)
	
	def onCloseWindow(self, event):
		print('===on close window====')
		# self.Close(True)
		self.Destroy()
	
	def onCloseMe(self, event):
		self.Destroy()

if __name__ == "__main__":
	app = wx.PySimpleApp()
	subPanel = ButtonClick(None, 'Button click sample')
	subPanel.Show()
	app.MainLoop()

