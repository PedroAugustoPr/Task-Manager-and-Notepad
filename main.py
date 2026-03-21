import customtkinter as ctk
from utils.db import *


ctk.set_appearance_mode("dark")


class BaseFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            width=1160,
            height=700,
            corner_radius=15,
            border_width=2,
            border_color="yellow",
            fg_color="transparent",
        )
        self.grid_propagate(False)


class MyNotes(BaseFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.configure(border_color="white")

        Sfr_notas = ctk.CTkScrollableFrame(
            self,
            width=630,
            height=650,
            corner_radius=15,
            scrollbar_fg_color="transparent",
            fg_color="transparent",
            border_width=2,
            border_color="yellow",
        )
        Sfr_notas.grid(row=0, column=0, pady=(8, 0), padx=(0, 7), sticky="ens")
        Sfr_notas.grid_columnconfigure(0, weight=1)

        search_bar = ctk.CTkEntry(
            Sfr_notas,
            width=580,
            height=40,
            placeholder_text="Pesquisar",
            corner_radius=15,
        )
        search_bar.grid(row=0, column=0, pady=(0, 280), padx=(30, 0))

        s_search = ctk.CTkLabel(
            Sfr_notas, width=30, height=30, text="🔍️", font=("Arial", 30)
        )
        s_search.grid(row=0, column=0, pady=(0, 278), padx=(0, 600))


class SideBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            width=100,
            height=685,
            corner_radius=15,
            border_width=2,
            border_color="yellow",
        )
        for row in range(0, 4):
            self.grid_rowconfigure(row, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

    def create_button(self, text, row, font_size=30, command=None):
        btn = ctk.CTkButton(
            self,
            width=80,
            height=80,
            corner_radius=15,
            text=text,
            fg_color="transparent",
            font=("Arial", font_size),
            command=command,
            hover_color="orange",
        )
        btn.grid(row=row, column=0)
        return btn


class HomePage(BaseFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.mynotes = MyNotes(self)
        self.mynotes.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)


class CreateNotes(BaseFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
        self.configure(border_color="white")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.btn = ctk.CTkButton(
            self,
            width=100,
            height=50,
            text="Criar Nota",
            fg_color="orange",
            hover_color="yellow",
            command=lambda: self.notepad(),
        )
        self.btn.grid(row=0, column=0)

    def notepad(self):
        self.btn.destroy()

        self.write = ctk.CTkTextbox(
            self,
            width=1140,
            height=600,
            corner_radius=15,
            activate_scrollbars=True,
            scrollbar_button_color="orange",
            scrollbar_button_hover_color="yellow",
            font=("Arial", 15),
        )
        x = self.write.grid(row=0, column=0, padx=(85, 0))

        self.clear_btn = ctk.CTkButton(
            self,
            width=80,
            height=30,
            text="Clear 🗑️",
            fg_color="red",
            hover_color="orange",
            command=lambda: self.write.delete("1.0", "end"),
        )
        self.clear_btn.grid(row=0, column=0, sticky="ne", pady=(10, 0), padx=(0, 110))

        self.save = ctk.CTkButton(
            self,
            width=80,
            height=30,
            text="Salvar 📃",
            fg_color="blue",
            hover_color="orange",
            command=lambda: save(),
        )
        self.save.grid(row=0, column=0, sticky="ne", pady=(10, 0), padx=(0, 20))

        def save():
            font = self.write.cget("font")
            note = {
                "texto": self.write.get("1.0", "end-1c"),
                "fonte": str(font[0]),
                "tamanho": int(font[1])
            }
            db.save_note(note)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("")

        largura = 1280
        altura = 720

        l_tela = self.winfo_screenwidth()
        a_tela = self.winfo_screenheight()

        x = (l_tela - largura) // 2
        y = (a_tela - altura) // 2

        self.geometry(f"{largura}x{altura}+{x}+{y}")

        self.minsize(width=1280, height=720)
        self.maxsize(width=1280, height=720)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.pages = {
            "home": HomePage(self.container),
            "notes": CreateNotes(self.container),
        }

        for page in self.pages:
            self.pages[page].grid(row=0, column=0, sticky="nsew")

        self.sidebar = SideBar(self)
        self.sidebar.grid(row=0, column=0, sticky="nsw")

        self.buttons = {
            "home_button": self.sidebar.create_button(
                "🏠︎", 0, 33, command=lambda: self.change_page("home")
            ),
            "notes_button": self.sidebar.create_button(
                "📝", 1, command=lambda: self.change_page("notes")
            ),
            "tasks_button": self.sidebar.create_button("📋", 2, 33),
            "settings_button": self.sidebar.create_button("⚙️", 3, 40),
        }

        self.change_page("notes")

    def change_page(self, page_name):
        self.pages[page_name].tkraise()

        for button in self.buttons.values():
            button.configure(fg_color="transparent")

        self.buttons[f"{page_name}_button"].configure(fg_color="orange")


app = App()
app.mainloop()
