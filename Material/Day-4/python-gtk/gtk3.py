import gtk
x=gtk.Window()
x.set_title("New Window")
x.set_size_request(450,250)
x.set_position(gtk.WIN_POS_CENTER)
x.connect("destroy",gtk.main_quit)
x.show_all()
gtk.main()
