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
            command=lambda: self.note_name(),
        )
        self.btn.grid(row=0, column=0)

    def note_name(self):
        self.camp = ctk.CTkFrame(
            self,
            width=500,
            height=150,
            fg_color="transparent",
            border_width=2,
            border_color="yellow",
            corner_radius=15,
        )
        self.camp.grid(row=0, column=0)
        self.camp.grid_propagate(False)

        for row in range(1):
            self.camp.grid_rowconfigure(row, weight=1)

        self.camp.grid_columnconfigure(0, weight=1)

        self.name = ctk.CTkEntry(
            self.camp, width=480, height=50, placeholder_text="Nome do Arquivo"
        )
        self.name.grid(row=0, column=0)

        self.cancel = ctk.CTkButton(
            self.camp,
            width=235,
            height=50,
            text="Cancelar",
            fg_color="red",
            font=("Arial", 20, "bold"),
            hover_color="yellow",
            command=lambda: self.camp.grid_remove()
        )
        self.cancel.grid(row=1, column=0, sticky="ws", pady=15, padx=10)

        def check_name():
            global name_of_note
            name_of_note = (self.name.get()).strip()

            if not name_of_note:
                notes = db.view_all_notes()
                q_notes = len(notes)
                name_of_note = f'Nota #{q_notes + 1}'
            
            self.camp.grid_remove()
            self.notepad()

            return name_of_note

        self.proceed = ctk.CTkButton(
            self.camp,
            width=235,
            height=50,
            text="Prosseguir",
            fg_color="orange",
            font=("Arial", 20, "bold"),
            hover_color="yellow",
            command=lambda: check_name(),
        )
        self.proceed.grid(row=1, column=0, sticky="es", pady=15, padx=10)

    def notepad(self):
        self.btn.grid_remove()

        # FRAME RESPONSÁVEL POR ARMAZENAR TODOS OS WIDGETS ABAIXO
        self.editor = ctk.CTkFrame(
            self,
            width=1160,
            height=700,
            corner_radius=15,
            border_width=2,
            border_color="yellow",
            fg_color="transparent",
        )
        self.editor.grid_propagate(False)

        self.editor.grid(row=0, column=0, sticky="nsew")
        self.editor.configure(border_color="white")

        self.editor.grid_columnconfigure(0, weight=1)
        self.editor.grid_rowconfigure(0, weight=1)

        # CAIXA DE TEXTO ONDE O USUÁRIO ESCREVERÁ AS SUAS ANOTAÇÕES
        self.write = ctk.CTkTextbox(
            self.editor,
            width=1140,
            height=600,
            corner_radius=15,
            activate_scrollbars=True,
            scrollbar_button_color="orange",
            scrollbar_button_hover_color="yellow",
            font=("Arial", 14),
        )
        x = self.write.grid(row=0, column=0, padx=(85, 0))

        # BUTTONS : LIMPAR A CAIXA DE TEXTO POR COMPLETO
        self.clear_btn = ctk.CTkButton(
            self.editor,
            width=80,
            height=30,
            text="Clear 🗑️",
            fg_color="red",
            hover_color="orange",
            command=lambda: self.write.delete("1.0", "end"),
        )
        self.clear_btn.grid(row=0, column=0, sticky="ne", pady=(10, 0), padx=(0, 110))

        # BUTTONS : SALVAR A NOTA E VOLTAR PARA A ARÉA ANTERIOR
        self.save = ctk.CTkButton(
            self.editor,
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
                "nome": name_of_note,
                "texto": self.write.get("1.0", "end-1c"),
                "fonte": str(font[0]),
                "tamanho": int(font[1]),
            }
            db.save_note(note)

            self.editor.grid_remove()
            self.btn.grid()

        # BUTTONS : MODIFICAR A FONTE E O TAMANHO
        def change_font_size(value):
            self.write.configure(font=(str(font[0]), int(value)))

        global font
        font = self.write.cget("font")

        self.select_size = ctk.CTkOptionMenu(
            self.editor,
            width=80,
            height=30,
            values=[
                "8",
                "9",
                "10",
                "11",
                "12",
                "14",
                "16",
                "18",
                "20",
                "22",
                "24",
                "26",
                "28",
                "32",
                "36",
                "40",
                "48",
                "56",
                "64",
                "72",
            ],
            fg_color="#3a2f00",
            button_color="#ffb300",
            button_hover_color="#ffc107",
            text_color="white",
            command=change_font_size,
        )
        self.select_size.set("14")
        self.select_size.grid(row=0, column=0, sticky="ne", pady=(10, 0), padx=(0, 200))


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
