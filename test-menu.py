import wx
import os

os.environ["UBUNTU_MENUPROXY"]="0"

class MenuEventFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MenuEventFrame, self).__init__(
            parent, title=title, size=(600, 300))
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuItem = menu1.Append(-1, '&Exit...')
        menuBar.Append(menu1, '&File')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.onCloseMe, menuItem)
        self.text = wx.TextCtrl(self, -1, style=wx.EXPAND | wx.TE_MULTILINE)
        self.Bind(wx.EVT_MENU, self.menuhandler)
        self.SetSize((350, 250))
        self.Centre()

    def onCloseMe(self, event):
        self.Close(True)

    def menuhandler(self, event):
        id = event.GetId()
        if id == wx.ID_NEW:
            self.text.AppendText("new"+"\n")


if __name__ == '__main__':
    app = wx.App()
    panel = MenuEventFrame(None, 'Test MenuBar Event')
    panel.Show()
    app.MainLoop()
