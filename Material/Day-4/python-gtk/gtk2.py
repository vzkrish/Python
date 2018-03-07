import gtk
x=gtk.Window()
x.set_title("My Window")
x.connect("destroy",gtk.main_quit)
x.show_all()
gtk.main()
