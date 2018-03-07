# import gtk library
import gtk

# create a window object
x=gtk.Window()
x.set_title("New Buttons")
x.set_size_request(450,250)
x.set_position(gtk.WIN_POS_CENTER)
x.set_tooltip_text("Window Widget")


# creating buttons

x1=gtk.Button("Add")
x2=gtk.Button("Del")
x3=gtk.Button("Modify")

# create an invisible container
y=gtk.Fixed()

# place the buttons inside the container
y.put(x1,20,30)
x1.set_tooltip_text("Add the employees")
y.put(x2,100,150)
x2.set_tooltip_text("deleting the employees")

y.put(x3,200,150)
x3.set_tooltip_text("modifying the employees")
# add the container to the window object
x.add(y)

# adding close action to the  main window
x.connect("destroy",gtk.main_quit)
# display all
x.show_all()

#activate
gtk.main()

"""
self.set_tooltip_text("Window widget")
        button.set_tooltip_text("Button widget")
"""


