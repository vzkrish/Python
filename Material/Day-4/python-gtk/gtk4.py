import gtk
x=gtk.Window()
x.set_title("Buttons")
x.set_size_request(250, 200)
x.set_position(gtk.WIN_POS_CENTER)

# buttons or child widgets
        
x1=gtk.Button("Button")
x1.set_sensitive(False)

x2 = gtk.Button("Button")

x3 =  gtk.Button(stock=gtk.STOCK_CLOSE)

x4 = gtk.Button("Button")
x4.set_size_request(80, 40)

# this is an invisible container
y = gtk.Fixed()

y.put(x1, 20, 30)
y.put(x2, 100, 30)
y.put(x3, 20, 80)
y.put(x4, 100, 80)
        
x.connect("destroy", gtk.main_quit)
        
x.add(y)
x.show_all()
gtk.main()
