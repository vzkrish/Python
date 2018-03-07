import gtk
x=gtk.Window()
x.set_title("Simple menu")
x.set_size_request(250, 200)
x.set_position(gtk.WIN_POS_CENTER)

# create a menu bar object
mb = gtk.MenuBar()

# create menu item objects
x1= gtk.MenuItem("File")
x2=gtk.MenuItem("Print")
x3=gtk.MenuItem("Backup")
x4=gtk.MenuItem("Exit")

# append menu item objects to menu bar object
mb.append(x1)
mb.append(x2)
mb.append(x3)
mb.append(x4)

# layout
vbox = gtk.VBox(False, 2)
vbox.pack_start(mb, False, False, 0)

x.add(vbox)
x.connect("destroy", gtk.main_quit)
x.show_all()
gtk.main()
