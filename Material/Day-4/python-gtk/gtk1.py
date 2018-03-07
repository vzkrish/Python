# import gtk library
import gtk

# create a window object
x=gtk.Window()

# set the title for the window
x.set_title("Test Window")

# define the close button action
x.connect("destroy",gtk.main_quit)

# display all the above
x.show_all()

# show it permanently
gtk.main()


"""

  window = gtk.Window()
  window.set_title("PyGTK Test Window")
  window.connect("destroy", gtk.main_quit)
  window.show_all()

  gtk.main()
"""
