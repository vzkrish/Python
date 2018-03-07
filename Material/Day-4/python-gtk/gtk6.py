import gtk
x=gtk.Window()
x.set_title("Simple menu")
x.set_size_request(250, 200)
x.set_position(gtk.WIN_POS_CENTER)

mb = gtk.MenuBar()

#filemenu = gtk.Menu()
filem = gtk.MenuItem("File")
"""
filem.set_submenu(filemenu)
       
exit = gtk.MenuItem("Exit")
exit.connect("destroy", gtk.main_quit)
filemenu.append(exit)
"""
mb.append(filem)

vbox = gtk.VBox(False, 2)
vbox.pack_start(mb, False, False, 0)

x.add(vbox)

x.connect("destroy", gtk.main_quit)
x.show_all()
        
        

gtk.main()
