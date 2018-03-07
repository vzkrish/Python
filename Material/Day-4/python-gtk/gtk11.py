# label
import gtk

s="""unix is a multiprogramming operating system which
    has a wide range of features ranging from security,
    networking to data management"""

x=gtk.Window()
x.set_position(gtk.WIN_POS_CENTER)
x.set_border_width(8)
x.set_title('My Label')
x.connect('destroy',gtk.main_quit)
t=gtk.Label(s)
x.add(t)
x.show_all()
gtk.main()



