import customtkinter as ctk
from utils.db import *
from datetime import datetime


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


class MyTasks(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            width=580,
            height=650,
            corner_radius=15,
            border_width=2,
            border_color="yellow",
            fg_color="transparent",
        )
        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.configure(border_color="white")

        name_text = ctk.CTkLabel(
            self,
            width=540,
            height=60,
            text="Tarefas",
            font=("Arial", 35, "bold"),
        )
        name_text.grid(row=0, column=0, sticky="n", pady=(7, 0))

        Sfr_tasks = ctk.CTkScrollableFrame(
            self,
            width=510,
            height=535,
            corner_radius=15,
            scrollbar_fg_color="transparent",
            fg_color="#373737",
            scrollbar_button_color="orange",
            scrollbar_button_hover_color="yellow",
        )
        Sfr_tasks.grid(row=0, column=0, pady=(122, 0), sticky="s")
        Sfr_tasks.grid_columnconfigure(0, weight=1)

        search_bar = ctk.CTkEntry(
            self,
            width=490,
            height=40,
            placeholder_text="Pesquisar",
            corner_radius=15,
        )
        search_bar.grid(row=0, column=0, sticky="n", pady=70, padx=(45, 0))

        search_symbol = ctk.CTkLabel(
            self,
            width=40,
            height=40,
            text="🔍️",
            font=("Arial", 25),
            fg_color="orange",
            corner_radius=5,
        )
        search_symbol.grid(row=0, column=0, sticky="nw", pady=70, padx=(20, 0))


class MyNotes(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            width=580,
            height=650,
            corner_radius=15,
            border_width=2,
            border_color="yellow",
            fg_color="transparent",
        )
        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.configure(border_color="white")

        name_text = ctk.CTkLabel(
            self,
            width=550,
            height=60,
            text="Notas",
            font=("Arial", 35, "bold"),
        )
        name_text.grid(row=0, column=0, sticky="n", pady=(7, 0))

        Sfr_notes = ctk.CTkScrollableFrame(
            self,
            width=510,
            height=535,
            corner_radius=15,
            scrollbar_fg_color="transparent",
            fg_color="#373737",
            scrollbar_button_color="orange",
            scrollbar_button_hover_color="yellow",
        )
        Sfr_notes.grid(row=0, column=0, pady=(122, 0), sticky="s")
        Sfr_notes.grid_columnconfigure(0, weight=1)
        Sfr_notes.grid_rowconfigure(0, weight=1)

        search_bar = ctk.CTkEntry(
            self,
            width=490,
            height=40,
            placeholder_text="Pesquisar",
            corner_radius=15,
        )
        search_bar.grid(row=0, column=0, sticky="n", pady=70, padx=(45, 0))

        search_symbol = ctk.CTkLabel(
            self,
            width=40,
            height=40,
            text="🔍️",
            font=("Arial", 25),
            fg_color="orange",
            corner_radius=5,
        )
        search_symbol.grid(row=0, column=0, sticky="nw", pady=70, padx=(20, 0))

        # PUXA TODAS AS NOTAS JÁ REGISTRADAS NO BANCO DE DADOS EM FORMA DE LISTA (CADA INDEX É UMA NOTA, E CADA NOTA ESTÁ DENTRO DE UMA TUPLA)
        notes = db.notes()
        row = 0

        self.viewer = ctk.CTkFrame(
                master,
                width=600,
                height=700,
                corner_radius=15,
                border_width=2,
                border_color="white",
                fg_color="transparent",
            )
        self.viewer.grid_propagate(False)
        self.viewer.grid_columnconfigure(0, weight=1)
        self.viewer.grid_rowconfigure(0, weight=1)

        self.x_btn = ctk.CTkButton(
            self.viewer,
            width=40,
            height=40,
            fg_color="red",
            text="X",
            font=("Arial", 17, "bold"),
            hover_color="#9C0000",
            command=lambda: self.viewer.grid_remove(),
        )
        self.x_btn.grid(row=0, column=0, sticky="ne", pady=10, padx=10)

        self.note_n = ctk.CTkLabel(
            self.viewer,
            width=100,
            height=30,
            font=("Arial", 20, "bold"),
        )
        self.note_n.grid(row=0, column=0, sticky="nw", pady=20, padx=20)

        self.content = ctk.CTkTextbox(
            self.viewer,
            width=560,
            height=630,
            state="normal",
            corner_radius=15,
        )
        self.content.grid(row=0, column=0, pady=(43, 0))

        for note in notes:
            name = (note[1]).lower()
            data, time = (note[5]).split(" ")
            fonte = note[3]
            ID = note[0]

            row += 1

            note_fr = ctk.CTkFrame(
                Sfr_notes,
                width=500,
                height=130,
                fg_color="transparent",
                corner_radius=15,
                border_width=2,
                border_color="orange",
            )
            note_fr.grid(row=row, column=0, pady=5, padx=(0, 10))

            note_fr.grid_propagate(False)
            note_fr.grid_columnconfigure(0, weight=1)
            note_fr.grid_rowconfigure(0, weight=1)

            def view(nota):
                name = (nota[1]).lower()

                self.content.configure(state="normal")
                self.note_n.configure(text=f"NOME: {(name[0:35]).title()}",)
                self.content.delete("1.0", "end")
                self.content.insert("1.0", nota[2])
                self.content.configure(state="disabled", font=(nota[3], nota[4]),)
                self.viewer.grid(row=0, column=0, sticky="nsew", padx=(107, 4), pady=10)

            note_name = ctk.CTkLabel(
                note_fr,
                width=100,
                height=30,
                text=f"NOME: {(name[0:35]).title()}",
                font=("Arial", 20, "bold"),
            )
            note_name.grid(row=0, column=0, sticky="nw", pady=10, padx=10)

            info = ctk.CTkLabel(
                note_fr,
                width=100,
                height=30,
                text=f'ID: {ID} | FONTE: "{fonte}" | DATA DA CRIAÇÃO: {data} ás {time}',
                font=("Arial", 14, "bold"),
            )
            info.grid(row=0, column=0, sticky="w", padx=10, pady=(0, 25))

            view_btn = ctk.CTkButton(
                note_fr,
                width=215,
                height=45,
                text="Visualizar",
                fg_color="blue",
                font=("Arial", 20, "bold"),
                hover_color="yellow",
                command=lambda n=note: view(n),
            )
            view_btn.grid(row=0, column=0, sticky="sw", pady=10, padx=7)

            edit_btn = ctk.CTkButton(
                note_fr,
                width=215,
                height=45,
                text="Editar",
                fg_color="orange",
                font=("Arial", 20, "bold"),
                hover_color="yellow",
            )
            edit_btn.grid(row=0, column=0, sticky="se", pady=10, padx=57)

            delete_btn = ctk.CTkButton(
                note_fr,
                width=45,
                height=45,
                text="🗑️",
                fg_color="red",
                font=("Arial", 20, "bold"),
                hover_color="#9C0000",
            )
            delete_btn.grid(row=0, column=0, sticky="se", pady=10, padx=7)


class HomePage(BaseFrame):
    def __init__(self, master):
        super().__init__(master)

        for column in range(1):
            self.grid_columnconfigure(column, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.mytasks = MyTasks(self)
        self.mytasks.grid(row=0, column=0, sticky="nsw", padx=(107, 0), pady=10)

        self.mynotes = MyNotes(self)
        self.mynotes.grid(row=0, column=1, sticky="ens", padx=(0, 8), pady=10)


class CreateNotes(BaseFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
        self.configure(border_color="white")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # BUTTONS : BOTÃO RESPONSÁVEL POR INICIALIZAR O PROCESSO DE CRIAÇÃO DE UMA NOVA NOTA
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
        # FRAMES : FRAME ONDE SERÁ PERGUNTADO O NOME DA NOTA
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

        # ENTRADA DE TEXTO ONDE O USUÁRIO DEVE INSERIR O NOME DA NOVA NOTA
        self.name = ctk.CTkEntry(
            self.camp, width=480, height=50, placeholder_text="Nome do Arquivo"
        )
        self.name.grid(row=0, column=0)

        # BUTTONS : CANCELA A CRIAÇÃO DE UMA NOVA NOTA E VOLTA PARA A "TELA" ANTERIOR
        self.cancel = ctk.CTkButton(
            self.camp,
            width=235,
            height=50,
            text="Cancelar",
            fg_color="red",
            font=("Arial", 20, "bold"),
            hover_color="yellow",
            command=lambda: self.camp.grid_remove(),
        )
        self.cancel.grid(row=1, column=0, sticky="ws", pady=15, padx=10)

        # FUNCTIONS : VERIFICA SE O USUÁRIO DIGITOU O NOME DA NOTA OU NÃO
        def check_name():
            global name_of_note
            name_of_note = (self.name.get()).strip()

            # SE A CONDIÇÃO FOR VERDADEIRA, RETORNA UM NOME ENUMERADO SEQUENCIALMENTE DE ACORDO COM A QUANTIDADE DE NOTAS JÁ CRIADAS PELO USUÁRIO
            if not name_of_note:
                notes = db.notes()
                q_notes = len(notes)
                name_of_note = f"Nota #{q_notes + 1}"

            self.camp.grid_remove()
            self.notepad()

            return name_of_note

        # BUTTONS : PROSSEGUIR PARA A FUNÇÃO NOTEPAD?
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

        # FRAMES : FRAME RESPONSÁVEL POR ARMAZENAR TODOS OS WIDGETS ABAIXO
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
        self.write.grid(row=0, column=0, padx=(85, 0))

        # BUTTONS : LIMPAR A CAIXA DE TEXTO POR COMPLETO
        self.clear_btn = ctk.CTkButton(
            self.editor,
            width=80,
            height=30,
            text="Clear 🗑️",
            fg_color="red",
            hover_color="#9C0000",
            command=lambda: self.write.delete("1.0", "end"),
        )
        self.clear_btn.grid(row=0, column=0, sticky="ne", pady=(10, 0), padx=(0, 110))

        # BUTTONS : SALVAR A NOTA E VOLTAR PARA A ARÉA ANTERIOR
        self.save_btn = ctk.CTkButton(
            self.editor,
            width=80,
            height=30,
            text="Salvar 📃",
            fg_color="blue",
            hover_color="orange",
            command=lambda: save(),
        )
        self.save_btn.grid(row=0, column=0, sticky="ne", pady=(10, 0), padx=(0, 20))

        # FUNCTIONS : SALVAR A NOTA CRIADA PELO USUÁRIO NO BANCO DE DADOS
        def save():
            # PEGA A DATA E O HORÁRIO ATUAL E ARMAZENA COMO STRING
            now = datetime.now()
            data_time = now.strftime("%d/%m/%Y %H:%M")

            font = self.write.cget("font")

            note = {
                "nome": name_of_note,
                "texto": self.write.get("1.0", "end-1c"),
                "fonte": str(font[0]),
                "tamanho": int(font[1]),
                "data": data_time,
            }
            db.save_note(note)

            self.editor.grid_remove()
            self.btn.grid()

        # BUTTONS : MODIFICAR A FONTE E O TAMANHO
        def change_font_size(value):
            self.write.configure(font=(str(font[0]), int(value)))

        global font
        font = self.write.cget("font")

        # MENU RESPONSÁVEL POR PROVER A SELEÇÃO DO TAMANHO DA FONTE
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

        self.change_page("home")

    def change_page(self, page_name):
        self.pages[page_name].tkraise()

        for button in self.buttons.values():
            button.configure(fg_color="transparent")

        self.buttons[f"{page_name}_button"].configure(fg_color="orange")


app = App()
app.mainloop()
