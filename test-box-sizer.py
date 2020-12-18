# coding:utf-8
import wx
import os


class MyApp(wx.App):
    def __init__(self):
        super(MyApp, self).__init__()


class MyFrame(wx.Frame):
    def __init__(self, title='test', size=wx.DefaultSize):
        super(MyFrame, self).__init__(None, wx.ID_ANY, title=title,
                                      size=size, style=wx.DEFAULT_FRAME_STYLE ^ wx.MINIMIZE_BOX)
        self.Center()
        # self.SetSize(700,700)
        # self.SetTitle('aaa')
        self.InitMenuBar()
        self.InitStatusBar()
        self.splitwindow()
        # self.Bind(wx.EVT_ERASE_BACKGROUND,self.EraseBack)
        self.InitLpanel()
        self.InitRpanel()

    def EraseBack(self, event):
        self.ParentWindow.SetSashPosition(0)

    def splitwindow(self):
        self.ParentWindow = wx.SplitterWindow(self)  # 创建分割窗口
        self.lpanel = wx.Panel(self.ParentWindow)  # 创建左面板
        self.rpanel = wx.Panel(self.ParentWindow)  # 创建右面板
        self.lpanel.SetBackgroundColour('#949449')
        self.rpanel.SetBackgroundColour(colour='RED')
        self.ParentWindow.SplitVertically(self.lpanel, self.rpanel, 100)
        self.ParentWindow.SetMinimumPaneSize(50)  # 设定最小的窗口不能小于50

    def InitMenuBar(self):
        # 创建一个menubar
        menuBar = wx.MenuBar()

        # 创建两个menu
        filemenu = wx.Menu()
        aboutmenu = wx.Menu()

        # filemenu添加一个menuopen，关联的ID为wx.ID_OPEN,名字为Open,如果有状态栏，则状态栏里显示‘打开文件’
        menuopen = filemenu.Append(wx.ID_OPEN, 'Open', '打开文件')
        # filemenu添加一个menu分隔符
        filemenu.AppendSeparator()
        menusave = filemenu.Append(wx.ID_SAVE, 'Save', '保存当前设置')
        filemenu.AppendSeparator()
        menuexit = filemenu.Append(wx.ID_EXIT, 'Exit', '退出程序')
        menuBar.Append(filemenu, 'File')

        menuabout = aboutmenu.Append(wx.ID_ABOUT, 'Info', 'Information')
        menuBar.Append(aboutmenu, 'Info')

        # 将menu与函数绑定
        self.Bind(wx.EVT_MENU, self.Exit, menuexit)
        self.Bind(wx.EVT_MENU, self.Info, menuabout)
        self.Bind(wx.EVT_MENU, self.Open, menuopen)
        self.Bind(wx.EVT_MENU, self.Save, menusave)

        self.SetMenuBar(menuBar)

    def Exit(self, event):
        print('aaaa')
        self.Close()

    def Open(self, event):
        self.dirname = ''
        self.filename = ''
        dlg = wx.FileDialog(self, '选择文件', self.dirname,
                            '', '*.csv*', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.FilePath = os.path.join(self.dirname, self.filename)
            return self.FilePath

    def Save(self):
        # 可以将要保存的东西放入本地磁盘
        pass

    def Info(self, event):
        self.messageinfo = 'Author:testuser\nDate:2019/5/21\nVersion:0.1'
        message = wx.MessageDialog(self, self.messageinfo, 'INFO', wx.OK)
        message.ShowModal()
        message.Destroy()

    def InitStatusBar(self):
        # 创建状态栏
        statusbar = self.CreateStatusBar()
        # 将状态栏分割为3个部分
        statusbar.SetFieldsCount(3)
        # 分割状态栏的比例为3：2：1，用负数表示
        statusbar.SetStatusWidths([-3, -2, -1])
        # 每部分状态栏显示的值，当鼠标停在menu上时，0号状态栏会临时显示上面menu里的提示信息
        statusbar.SetStatusText('1111', 0)
        statusbar.SetStatusText('2222', 1)
        statusbar.SetStatusText('3333', 2)

    def InitLpanel(self):
        self.lpanel.SetBackgroundColour('#AABBCC')
        LBox = wx.BoxSizer(wx.VERTICAL)  # 创建左面板的整体布局管理器，为竖直方向

        nm_staticbox = wx.StaticBox(
            self.lpanel, -1, 'Account:')  # 创建Account staticbox
        # 为Account staticbox创建竖直的布局管理器
        nm_sizer = wx.StaticBoxSizer(nm_staticbox, wx.VERTICAL)

        nm_box = wx.BoxSizer(wx.HORIZONTAL)  # 创建文本框的布局管理器
        nm_input_box = wx.BoxSizer(wx.HORIZONTAL)

        username = wx.StaticText(self.lpanel, -1, "UserName")  # 创建静态文本框
        passwd = wx.StaticText(self.lpanel, -1, label="Passwd")
        # 创建文本输入框，self.username.GetValue()可以获取文本输入框的value
        self.username_input = wx.TextCtrl(
            self.lpanel, -1, style=wx.TE_LEFT, value='username', size=(50, 20))
        self.passwd_input = wx.TextCtrl(
            self.lpanel, -1, style=wx.TE_LEFT | wx.TE_PASSWORD, value='12345678', size=(50, 20))  # size为文本框的大小

        nm_box.Add(username, proportion=0, flag=wx.LEFT, border=1)
        # proportion=0时，表示控件大小不变，为正数时，按照值的大小进行缩放
        # flag有三类，wx.LEFT,wx.TOP,wx.RIGHT,wx.ALL等表示声明边界；wx.ALIGN_LEFT,wx.CENTER,wx.ALIGN_CENTER_HORIZONTAL,wx.ALIGEN_TOP,wx.ALIGN_BOTTOM等表示声明对齐方式;wx.EXPAND为填充
        # border为边界间隔
        nm_box.Add(passwd, 0, wx.LEFT, 15)
        nm_input_box.Add(self.username_input, 0, wx.LEFT, 10)
        nm_input_box.Add(self.passwd_input, 0, wx.LEFT, 20)
        LBox.Add(nm_sizer, 0, wx.ALL | wx.LEFT | wx.RIGHT, 10)

        nm_sizer.Add(nm_box, 0, wx.ALL | wx.CENTER, 1)
        nm_sizer.Add(nm_input_box, 0, wx.ALL | wx.CENTER, 1)

        self.lpanel.SetSizer(LBox)  # boxsizer生效

    def InitRpanel(self):
        self.rpanel.SetBackgroundColour('#4F9D9D')
        self.logtext = wx.TextCtrl(
            self.rpanel, style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_READONLY)
        # wx.TE_CENTER 文本居中；
        # wx.TE_LEFT左对齐；
        # wx.TE_PASSWORD 文本用*号代替；
        # wx.TE_READONLY，只读，用户不能修改
        # wx.TE_MULTILINE 多行显示
        # wx.TE_HSCROLL 长的行将不换行，显示水平滚动条
        # wx.TE_RICH2 把最新版本的丰富文本控件用作基本的窗口部件
        self.logtext.SetMaxLength(0)  # 取消默认文本长度限制，当其它数字时，可以限制文本的输入长度

        self.points = self.logtext.GetFont().GetPointSize()  # 当前字体大小
        self.font = wx.Font(self.points+3, wx.DEFAULT,
                            wx.NORMAL, wx.BOLD, False)
        # self.font=wx.Font(self.points+3,wx.ROMAN,wx.ITALIC,wx.BOLD,True)
        # wx.Font(pointSize,family,style,weight,underline)
        # pointSize:wx.DEFAULT,wx.MODERN,wxROMAN,wx.SCRIPT,wx.SWISS
        # sytle:wx.MORMAL,wx.SLANT,wx.ITALIC
        # weight:wx.NORMAL,wx.LIGHT,wx.BOLD
        # True :underline or not

        statictext = wx.StaticText(self.rpanel, -1, label='Log Area')
        statictext.SetForegroundColour(wx.BLACK)
        # statictext.SetBackgroundColour(wx.WHITE)
        RBox = wx.BoxSizer(wx.VERTICAL)
        RBox.Add(statictext, 0, flag=wx.ALL | wx.CENTER, border=2)
        RBox.Add(self.logtext, 1, flag=wx.ALL | wx.EXPAND, border=2)
        self.rpanel.SetSizer(RBox)

        def LogMessage(self, message, colour='BLACK'):
            self.logtext.SetDefaultStyle(
                wx.TextAttr(colour, wx.WHITE, self.font))
            self.logtext.AppendText("[{0}]:{1}\n".format(
                time.strftime('%H:%M:%S'), message))


if __name__ == '__main__':
    app = MyApp()
    frame = MyFrame(title='wx-test', size=(400, 300))
    frame.Show()
    app.MainLoop()
