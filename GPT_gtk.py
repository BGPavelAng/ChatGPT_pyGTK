import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import openai
import #importar la clave

openai.api_key = #clave

messages = [{'role': 'system', 'content': 'eres un asistente de lenguaje de programación'}]

class Ventana(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="AppChatGPT personal (Pavel Anguiano)")

        # Define las dimensiones y la posición de la ventana
        self.set_default_size(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(6)

        self.menubar = Gtk.MenuBar()

        filemenu = Gtk.Menu()
        filemenu_item = Gtk.MenuItem("Archivo")
        filemenu_role = Gtk.MenuItem("Tipo de rol")
        filemenu_role.set_submenu(filemenu)
        self.menubar.append(filemenu_item)
        self.menubar.append(filemenu_role)

        open_item = Gtk.MenuItem("assistant")
        filemenu.append(open_item)

        open_user = Gtk.MenuItem("user")
        filemenu.append(open_user)

        self.input = Gtk.Entry()

        # Crea un label
        self.label = Gtk.Label()
        self.label.set_line_wrap(True)
        self.label.set_text("Mostar respuesta de ChatGPT!")

        # Crea una caja de texto con scroll vertical
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_hexpand(True)
        self.scroll.set_vexpand(True)

        # Crea dos botones
        self.boton1 = Gtk.Button.new_with_label("Enviar")
        self.boton1.connect("clicked", self.on_boton1_clicked)
        self.boton2 = Gtk.Button.new_with_label("Salir")
        self.boton2.connect("clicked", Gtk.main_quit)

        # Añade los widgets a la ventana
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.pack_start(self.menubar, True, True, 0)
        vbox.pack_start(self.input, True, True, 0)
        vbox.pack_start(self.label, True, True, 0)
        vbox.pack_start(self.scroll, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        hbox.pack_start(self.boton1, True, True, 0)
        hbox.pack_end(self.boton2, True, True, 0)

        vbox.pack_end(hbox, False, False, 0)

        self.add(vbox)

        #modificar para automatizar esto


    # Función del botón 1
    def on_boton1_clicked(self, widget):

        texto = self.input.get_text()

        messages.append({'role': 'user', 'content': texto})

        respuesta = openai.ChatCompletion.create(model = #escribe el modelo,
                                                 messages = messages)

        ChatGPT = (respuesta.choices[0].message.content)

        messages.append({'role': 'assistant', 'content': ChatGPT})

        self.label.set_text(ChatGPT)


win = Ventana()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
