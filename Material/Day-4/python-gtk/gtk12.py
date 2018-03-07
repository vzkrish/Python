# check button

import gtk
x=gtk.Window()
x.set_position(gtk.WIN_POS_CENTER)
x.set_border_width(8)
x.set_title('Check Button')
x.connect('destroy',gtk.main_quit)
x.set_default_size(250, 200)


fixed=gtk.Fixed()
button = gtk.CheckButton("Show title")
button.set_active(True)
button.unset_flags(gtk.CAN_FOCUS)
#button.connect("clicked", on_clicked)
fixed.put(button, 50, 50)
x.connect("destroy", gtk.main_quit)
x.add(fixed)
x.show_all()
gtk.main()


"""
class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()
        self.set_title("Check Button")
        self.set_position(gtk.WIN_POS_CENTER)
        

        fixed = gtk.Fixed()
        button = gtk.CheckButton("Show title")
        button.set_active(True)
        button.unset_flags(gtk.CAN_FOCUS)
        button.connect("clicked", self.on_clicked)

        fixed.put(button, 50, 50)

        self.connect("destroy", gtk.main_quit)
        self.add(fixed)
        self.show_all()

    def on_clicked(self, widget):
        if widget.get_active():
            self.set_title("Check Button")
        else:
           self.set_title("")
        
PyApp()
gtk.main()
"""
