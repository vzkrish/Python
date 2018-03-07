# window level
def display(*p):
    print 'welcome'
    return
def output(*q):
    print 'good bye'
    return
import gtk
x=gtk.Window()
x.set_title("My Menu")
x.set_size_request(250,150)
x.set_position(gtk.WIN_POS_CENTER)
x.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))

# create the menu bar object
m=gtk.MenuBar()

# add items to the menu bar by creating item objects
m1=gtk.MenuItem("File")
n1=gtk.Menu()
m1.set_submenu(n1)
add=gtk.MenuItem("Add")
add.connect('activate',display)
n1.append(add)
dele=gtk.MenuItem("Del")
dele.connect('activate',output)
n1.append(dele)
exit=gtk.MenuItem("Exit")
exit.connect('activate',gtk.main_quit)
n1.append(exit)

m2=gtk.MenuItem("Edit")
m3=gtk.MenuItem("Print")


# append the menu items to the menu bar
m.append(m1)
m.append(m2)
m.append(m3)

# layout management
vbox=gtk.VBox(False,2)
vbox.pack_start(m,False,False,0)
x.add(vbox)
x.connect("destroy",gtk.main_quit)
x.show_all()
gtk.main()



