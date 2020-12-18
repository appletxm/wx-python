import wx
from test2 import TestFrame

class MyWin(wx.Frame):
    def __init__(self, parent, title):
        super(MyWin, self).__init__(parent, title=title, size=(800, 450))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.btn = wx.Button(panel, -1, "click Me")
        vbox.Add(self.btn, 0, wx.ALIGN_CENTER)
        self.btn.Bind(wx.EVT_BUTTON, self.OnClicked)

        self.tbtn = wx.ToggleButton(panel, -1, "click to on")
        vbox.Add(self.tbtn, 0, wx.EXPAND)
        self.tbtn.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        bmp = wx.Bitmap("res/new.png", wx.BITMAP_TYPE_ANY)
        self.bmpbtn = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp,
                                      size=(bmp.GetWidth()+10, bmp.GetHeight()+10))

        hbox.Add(self.bmpbtn, 0, wx.ALIGN_CENTER)
        self.bmpbtn.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.bmpbtn.SetLabel("NEW")

        bmp1 = wx.Bitmap("res/open.png", wx.BITMAP_TYPE_ANY)
        self.bmpbtn1 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp1, size=(
            bmp.GetWidth()+10, bmp.GetHeight()+10))

        hbox.Add(self.bmpbtn1, 0, wx.ALIGN_CENTER)
        self.bmpbtn1.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.bmpbtn1.SetLabel("OPEN")

        bmp2 = wx.Bitmap("res/save.png", wx.BITMAP_TYPE_BMP)
        self.bmpbtn2 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp2, size=(
            bmp.GetWidth()+10, bmp.GetHeight()+10))

        hbox.Add(self.bmpbtn2, 0, wx.ALIGN_CENTER)
        self.bmpbtn2.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.bmpbtn2.SetLabel("SAVE")

        vbox.Add(hbox, 1, wx.ALIGN_CENTER)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()
        self.Fit()

    def OnClicked(self, event):
        btn = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", btn)
        testFrame = TestFrame(None)
        # print(String(testFrame))
        TestFrame.openPanel(testFrame)

    def OnToggle(self, event):
        state = event.GetEventObject().GetValue()

        if state == True:
            print("Toggle button state off")
            event.GetEventObject().SetLabel("click to off")
        else:
            print(" Toggle button state on")
            event.GetEventObject().SetLabel("click to on")


if __name__ == '__main__':
    app = wx.App()
    MyWin(None,  'Button demo')
    testFrame = TestFrame(None)
    app.MainLoop()
