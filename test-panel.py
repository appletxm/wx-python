import wx
import os
class MyApp(wx.App):
    def __init__(self):
        super(MyApp,self).__init__()

class MyFrame(wx.Frame):
    def __init__(self,title='test',size=wx.DefaultSize):
        super(MyFrame,self).__init__(None,wx.ID_ANY,title=title,size=size,style=wx.DEFAULT_FRAME_STYLE^wx.MINIMIZE_BOX)
        self.Center()
        #self.SetSize(700,700)
        #self.SetTitle('aaa')
        self.InitMenuBar()
        self.InitStatusBar()
        self.panel=wx.Panel(self) #创建panel，大小和Frame是一样大的
        button=wx.Button(self.panel,label=u'Start',size=(50,30),pos=(0,30)) #将button放在panel上

    def InitMenuBar(self):
        #创建一个menubar
        menuBar = wx.MenuBar()

        #创建两个menu
        filemenu = wx.Menu()
        aboutmenu = wx.Menu()

        #filemenu添加一个menuopen，关联的ID为wx.ID_OPEN,名字为Open,如果有状态栏，则状态栏里显示‘打开文件’
        menuopen = filemenu.Append(wx.ID_OPEN,'Open','打开文件')
        #filemenu添加一个menu分隔符
        filemenu.AppendSeparator()
        menusave = filemenu.Append(wx.ID_SAVE,'Save','保存当前设置')
        filemenu.AppendSeparator()
        menuexit = filemenu.Append(wx.ID_EXIT,'Exit','退出程序')
        menuBar.Append(filemenu,'File')

        menuabout = aboutmenu.Append(wx.ID_ABOUT,'Info','Information')
        menuBar.Append(aboutmenu,'Info')

        #将menu与函数绑定
        self.Bind(wx.EVT_MENU,self.Exit,menuexit)
        self.Bind(wx.EVT_MENU,self.Info,menuabout)
        self.Bind(wx.EVT_MENU,self.Open,menuopen)
        self.Bind(wx.EVT_MENU,self.Save,menusave)

        self.SetMenuBar(menuBar)

    def Exit(self,event):
            print('aaaa')
            self.Close()

    def Open(self,event):
        self.dirname=''
        self.filename=''
        dlg = wx.FileDialog(self,'选择文件',self.dirname,'','*.csv*',wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.FilePath = os.path.join(self.dirname,self.filename)
            return self.FilePath

    def Save(self):
        #可以将要保存的东西放入本地磁盘
        pass

    def Info(self,event):
        self.messageinfo='Author:testuser\nDate:2019/5/21\nVersion:0.1'
        message = wx.MessageDialog(self,self.messageinfo,'INFO',wx.OK)
        message.ShowModal()
        message.Destroy()

    def InitStatusBar(self):
        #创建状态栏
        statusbar = self.CreateStatusBar()
        #将状态栏分割为3个部分
        statusbar.SetFieldsCount(3)
        #分割状态栏的比例为3：2：1，用负数表示
        statusbar.SetStatusWidths([-3,-2,-1])
        #每部分状态栏显示的值，当鼠标停在menu上时，0号状态栏会临时显示上面menu里的提示信息
        statusbar.SetStatusText('1111',0)
        statusbar.SetStatusText('2222',1)
        statusbar.SetStatusText('3333',2)


if __name__ == '__main__':
    app = MyApp()
    frame = MyFrame(title='wx-test',size=(400,300))
    frame.Show()
    app.MainLoop()
