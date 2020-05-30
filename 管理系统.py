import wx
class Myframe(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'然哥出品',size=(600,500))
        panel=wx.Panel(self)
        self.title=wx.StaticText(panel,label="海航技术面试官管理系统")
        self.bmps=wx.Bitmap(r'c:\Users\hasee\Desktop\海航技术新logo-横版_副本.png',wx.BITMAP_TYPE_PNG)
        
        use='海航技术面试官管理系统'
        self.title=wx.StaticText(panel,label=use,pos=(130,40))
        self.name=wx.StaticText(panel,label='用户名',pos=(50,80))
        self.input_name=wx.TextCtrl(panel,pos=(100,76),size=(200,25),style=wx.TE_LEFT)
        self.pw=wx.StaticText(panel,label='密  码',pos=(50,130))
        self.input_pw=wx.TextCtrl(panel,pos=(100,125),size=(200,25),style=wx.TE_PASSWORD)
        
        self.bt_sure=wx.Button(panel,label='确定',pos=(90,170))

        self.bt_cancel=wx.Button(panel,label='取消',pos=(220,170))
      
        
       
     


        self.bt_xinxi=wx.Button(panel,label='面试官信息',pos=(130,100))
        self.bt_jilu=wx.Button(panel,label='面试记录',pos=(350,100))
        self.bt_xinzeng=wx.Button(panel,label='新增面试官',pos=(130,200))
        self.bt_shanchu=wx.Button(panel,label='删除面试官',pos=(350,200))
        self.bt_fuxun=wx.Button(panel,label='复训到期预警',pos=(130,300))
        self.bt_tuichu=wx.Button(panel,label='退出系统',pos=(350,300))
        vsizer=wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTRE,border=20)
   
        panel.SetSizer(vsizer)


    
if __name__ == '__main__':
    app=wx.App()
    frame=Myframe(parent=None,id=-1)
    frame.Show()
    app.MainLoop()


