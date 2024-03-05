import tkinter
import tkinter.messagebox
import customtkinter as ctk
import os
import main as soft
import kdigo
from PIL import Image

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # janela
        self.title("Examine-SE")
        self.geometry(f"{1100}x{580}")

        # Grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0), weight=1)

        # Imagens
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.home = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "Home_preta.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "Home_branca.png")), size=(25, 25))
        self.lab = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "Lab_preta.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "Lab_branca.png")), size=(25, 25))
        self.espiro = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "lung_preta.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "lung_branca.png")), size=(25, 25))
        self.calc = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "Calc_preta.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "Calc_branca.png")), size=(25, 25))
        self.config = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "Config_preta.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "Config_branca.png")), size=(25, 25))
        self.help = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "Ajuda_preta.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "Ajuda_branca.png")), size=(25, 25))
                        
        
        # Barra lateral

        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Examine-SE", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.home_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Início',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.home, anchor='w', command=self.home_button_action)
        self.home_button.grid(row=1, column=0, padx=5, pady=2, sticky= 'ew')
        
        self.lab_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Laboratoriais',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.lab, anchor='w', command=self.lab_button_action)
        self.lab_button.grid(row=2, column=0, padx=5, pady=2, sticky= 'ew')
        
        self.espiro_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Espirometria',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.espiro, anchor='w', command=self.espiro_button_action)
        self.espiro_button.grid(row=3, column=0, padx=5, pady=2, sticky= 'ew')
        
        self.calc_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Calculadoras',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.calc, anchor='w', command=self.calc_button_action)
        self.calc_button.grid(row=4, column=0, padx=5, pady=2, sticky= 'ew')
                
        self.help_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Ajuda',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.help, anchor='w', command=self.help_button_action)
        self.help_button.grid(row=6, column=0, padx=5, pady=2, sticky= 'ew')

        
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Claro", "Escuro", "Sistema"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="Proporção:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionmenu.grid(row=10, column=0, padx=20, pady=(10, 20))
        
        # Home
        
        self.home_frame = ctk.CTkFrame(self, corner_radius= 0, fg_color='transparent')
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_rowconfigure((0, 1, 2), weight=1)

        self.apresentacao = ctk.CTkLabel(self.home_frame, text= 'Bem-vindos ao Examine-se', font=ctk.CTkFont(size=30, weight="bold"))
        self.apresentacao.grid(row= 0, column= 1, padx= 20, pady= (50, 20))
      
        self.subtitulo = ctk.CTkLabel(self.home_frame, text= "Este é um projeto desenvolvido\n como parte do Trabalho de Conclusão de Curso \ndo Curso de Medicina de Victor Matos Gois. \n\n Para começar, por favor escolha uma das opções no menu à esquerda.", font=ctk.CTkFont(size=20))
        self.subtitulo.grid(row= 1, column=1, padx= 20, pady= 20)
       
        self.ufslogo = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "ufs_horizontal_preta.png")),
                                  dark_image=Image.open(os.path.join(image_path, "ufs_horizontal_branca.png")), size= (275, 112))
        self.ufs = ctk.CTkLabel(self.home_frame, text='', image=self.ufslogo ,anchor='s')
        self.ufs.grid(row= 3, column= 1, padx=20, pady= 20)
        
        # Lab
        
        self.lab_frame = ctk.CTkFrame(self, corner_radius= 0, fg_color='transparent')
        self.lab_frame.grid_columnconfigure(0, weight=1)
        self.lab_frame.grid_rowconfigure((2), weight=1)
        
        self.titulo = ctk.CTkLabel(self.lab_frame, text= 'Formatação de exames', font=ctk.CTkFont(size=20, weight='bold'))
        self.titulo.grid(row= 0, column= 0, padx = 20, pady = 20, sticky='nsew')
        
        self.description = ctk.CTkLabel(self.lab_frame, font=ctk.CTkFont(size=16),
                                                  text= 'Para começar, certifique-se de que os exames estão precedidos \
de data no formato "dia/mês/ano"\nPor exemplo: 01/01/01 ou 01/01/2001.\n\
Insira seus exames no campo abaixo')
        self.description.grid(row=1, column=0, padx=20, sticky= 'nsew')
        
        self.textbox = ctk.CTkTextbox(self.lab_frame,
                               border_width=2,
                               corner_radius=10,
                               font=ctk.CTkFont(size=14))
        self.textbox.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew") 

        self.svcopia_lab = ctk.CTkCheckBox(self.lab_frame, text='Salvar uma cópia dos resultados')
        self.svcopia_lab.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="s")

        self.lab_concluir = ctk.CTkButton(self.lab_frame, text='Concluir', fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.lab_concluir.grid(row=4, column= 0, padx=(20, 20), pady=(20, 20), sticky="ns")

        # Espiro
        
        self.espiro_frame = ctk.CTkFrame(self, corner_radius= 0, fg_color='transparent')
        self.espiro_frame.columnconfigure(0, weight=1)
        
        self.espiro_subframe0= ctk.CTkFrame(self.espiro_frame, corner_radius= 0, fg_color= 'transparent')
        self.espiro_subframe0.grid(row= 0, column= 0, sticky= 'nsew')
        self.espiro_subframe0.columnconfigure(3, weight=1)
    
        self.espiro_label = ctk.CTkLabel(self.espiro_subframe0, text= 'Formatação de Espirometrias', font=ctk.CTkFont(size=20, weight='bold'))
        self.espiro_label.grid(row= 0, column = 3, padx= 20, pady= 20, sticky='n')
        self.espiro_sublabel = ctk.CTkLabel(self.espiro_subframe0,
                                            text= 'Para começar, preencha todos os campos exibidos abaixo.\nInsira apenas números.\nNos campos "Previsto >", informe o valor do Limite Inferior da Normalidade.',
                                            font=ctk.CTkFont(size=16))
        self.espiro_sublabel.grid(row=1, column= 3, padx=20, pady= (0,20), sticky='n')
        
        self.espiro_subframe1 = ctk.CTkFrame(self.espiro_frame, corner_radius= 0, fg_color= 'transparent')
        self.espiro_subframe1.grid(row=1, column= 0, sticky= 'nsew')
        self.espiro_subframe1.columnconfigure((0, 6), weight=1)
        
        self.data_label = ctk.CTkLabel(self.espiro_subframe1, text='Data:', font=ctk.CTkFont(size=14))
        self.data_label.grid(row= 0, column= 2, padx= 10, pady= 5, sticky= 'ne')
        self.data_entry = ctk.CTkEntry(self.espiro_subframe1, width=100, corner_radius= 15)
        self.data_entry.grid(row= 0, column= 3, pady= 5, sticky='nw')
        
        self.espiro_subframe2 = ctk.CTkFrame(self.espiro_frame, corner_radius= 0, fg_color= 'transparent')
        self.espiro_subframe2.grid(row=2, column= 0, sticky= 'nsew')
        self.espiro_subframe2.columnconfigure((0, 6), weight=1)
        
        self.pre_cvf_label = ctk.CTkLabel(self.espiro_subframe2, text='Pré BD - CVF:', font=ctk.CTkFont(size=14))
        self.pre_cvf_label.grid(row= 1, column= 0, padx= 10, pady= 5, sticky= 'ne')
        self.pre_cvf_entry = ctk.CTkEntry(self.espiro_subframe2, width=70, corner_radius= 15)
        self.pre_cvf_entry.grid(row= 1, column= 1, pady= 5, sticky='nw')
        
        self.previsto_cvf_label = ctk.CTkLabel(self.espiro_subframe2, text='Previsto >', font=ctk.CTkFont(size=14))
        self.previsto_cvf_label.grid(row= 1, column= 2, padx= 10, pady= 5, sticky= 'ne')
        self.previsto_cvf_entry = ctk.CTkEntry(self.espiro_subframe2, width=70, corner_radius= 15)
        self.previsto_cvf_entry.grid(row= 1, column= 3, pady= 5, sticky='nw')
        
        self.pos_cvf_label = ctk.CTkLabel(self.espiro_subframe2, text='Pós BD - CVF:', font=ctk.CTkFont(size=14))
        self.pos_cvf_label.grid(row= 1, column= 4, padx= 10, pady= 5, sticky= 'ne')
        self.pos_cvf_entry = ctk.CTkEntry(self.espiro_subframe2, width=70, corner_radius= 15)
        self.pos_cvf_entry.grid(row= 1, column= 5, pady= 5, sticky='nw')
        
        self.pre_fev_label = ctk.CTkLabel(self.espiro_subframe2, text='Pré BD - FEV1:', font=ctk.CTkFont(size=14))
        self.pre_fev_label.grid(row= 2, column= 0, padx= 10, pady= 5, sticky= 'ne')
        self.pre_fev_entry = ctk.CTkEntry(self.espiro_subframe2, width=70, corner_radius= 15)
        self.pre_fev_entry.grid(row= 2, column= 1, pady= 5, sticky='nw')
        
        self.previsto_fev_label = ctk.CTkLabel(self.espiro_subframe2, text='Previsto >', font=ctk.CTkFont(size=14))
        self.previsto_fev_label.grid(row= 2, column= 2, padx= 10, pady= 5, sticky= 'ne')
        self.previsto_fev_entry = ctk.CTkEntry(self.espiro_subframe2, width=70, corner_radius= 15)
        self.previsto_fev_entry.grid(row= 2, column= 3, pady= 5, sticky='nw')
        
        self.pos_fev_label = ctk.CTkLabel(self.espiro_subframe2, text='Pós BD - FEV1:', font=ctk.CTkFont(size=14))
        self.pos_fev_label.grid(row= 2, column= 4, padx= 10, pady= 5, sticky= 'ne')
        self.pos_fev_entry = ctk.CTkEntry(self.espiro_subframe2, width=70, corner_radius= 15)
        self.pos_fev_entry.grid(row= 2, column= 5, pady= 5, sticky='nw')
        
        self.espiro_subframe3 = ctk.CTkFrame(self.espiro_frame, corner_radius= 0, fg_color= 'transparent')
        self.espiro_subframe3.grid(row=3, column= 0, sticky= 'nsew')
        self.espiro_subframe3.columnconfigure((0, 6), weight=1)
        
        self.previsto_fev_cvf_label = ctk.CTkLabel(self.espiro_subframe3, text='Previsto FEV1/CVF >', font=ctk.CTkFont(size=14))
        self.previsto_fev_cvf_label.grid(row= 3, column= 2, padx= 10, pady= 5, sticky= 'ne')
        self.previsto_fev_cvf_entry = ctk.CTkEntry(self.espiro_subframe3, width=70, corner_radius= 15)
        self.previsto_fev_cvf_entry.grid(row= 3, column= 3, pady= 5, sticky='nw')
        
        self.espiro_subframe4 = ctk.CTkFrame(self.espiro_frame, corner_radius= 0, fg_color= 'transparent')
        self.espiro_subframe4.grid(row=4, column= 0, sticky= 'nsew')
        self.espiro_subframe4.columnconfigure((0, 6), weight=1)
        
        self.pre_fef2575_label = ctk.CTkLabel(self.espiro_subframe4, text='Pré BD - FEF 25-75%:', font=ctk.CTkFont(size=14))
        self.pre_fef2575_label.grid(row= 4, column= 0, padx= 10, pady= 5, sticky= 'ne')
        self.pre_fef2575_entry = ctk.CTkEntry(self.espiro_subframe4, width=70, corner_radius= 15)
        self.pre_fef2575_entry.grid(row= 4, column= 1, pady= 5, sticky='nw')
                
        self.pos_fef2575_label = ctk.CTkLabel(self.espiro_subframe4, text='Pós BD - FEF 25-75%:', font=ctk.CTkFont(size=14))
        self.pos_fef2575_label.grid(row= 4, column= 4, padx= 10, pady= 5, sticky= 'ne')
        self.pos_fef2575_entry = ctk.CTkEntry(self.espiro_subframe4, width=70, corner_radius= 15)
        self.pos_fef2575_entry.grid(row= 4, column= 5, pady= 5, sticky='nw')
        
        self.espiro_subframe5 = ctk.CTkFrame(self.espiro_frame, corner_radius= 0, fg_color= 'transparent')
        self.espiro_subframe5.grid(row=5, column= 0, sticky= 'nsew')
        self.espiro_subframe5.columnconfigure((0, 6), weight=1)
        
        self.svcopia_espiro = ctk.CTkCheckBox(self.espiro_subframe5, text='Salvar uma cópia dos resultados')
        self.svcopia_espiro.grid(row=0, column=1, pady=(20, 0), padx=20, sticky="s")
        
        self.espiro_concluir = ctk.CTkButton(self.espiro_subframe5, text='Concluir', fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.espiro_concluir.grid(row=1, column= 1, padx=(20, 20), pady=(20, 20), sticky="ns")
        
        # Calculadoras
        
        self.calc_frame = ctk.CTkFrame(self, corner_radius= 0, fg_color='transparent')
        
        # Ajuda
        
        self.help_frame = ctk.CTkFrame(self, corner_radius= 0, fg_color='transparent')

        # Valores padrão
        self.espiro_button.configure(state="enabled")
        self.svcopia_lab.select()
        self.svcopia_espiro.select()
        self.appearance_mode_optionmenu.set("Escuro")
        self.scaling_optionmenu.set("100%")

        # Tela inicial padrão
        self.select_frame("espiro")

    def select_frame(self, frame):
        # Cor do botão
        self.home_button.configure(fg_color=("gray75", "gray25") if frame == "home" else "transparent")
        self.lab_button.configure(fg_color=("gray75", "gray25") if frame == "lab" else "transparent")
        self.espiro_button.configure(fg_color=("gray75", "gray25") if frame == "espiro" else "transparent")
        self.calc_button.configure(fg_color=("gray75", "gray25") if frame == "calc" else "transparent")
        self.help_button.configure(fg_color=("gray75", "gray25") if frame == "help" else "transparent")

        # Exibir
        if frame == "home":
            self.home_frame.grid(row=0, column= 1, rowspan=5, columnspan= 5 ,sticky= 'nsew')
        else:
            self.home_frame.grid_forget()
        if frame == "lab":
            self.lab_frame.grid(row=0, column= 1, rowspan=5, columnspan= 5 ,sticky= 'nsew')
        else:
            self.lab_frame.grid_forget()
        if frame == "espiro":
            self.espiro_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.espiro_frame.grid_forget()
        if frame == "calc":
            self.calc_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.calc_frame.grid_forget()
        if frame == "help":
            self.help_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.help_frame.grid_forget()

    def home_button_action(self):
        self.select_frame("home")

    def lab_button_action(self):
        self.select_frame("lab")

    def espiro_button_action(self):
        self.select_frame("espiro")

    def calc_button_action(self):
        self.select_frame("calc")
        
    def help_button_action(self):
        self.select_frame("help")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        if new_appearance_mode == 'Claro':
            new_appearance_mode = 'Light'
        elif new_appearance_mode == 'Escuro':
            new_appearance_mode = 'Dark'
        else:
            new_appearance_mode = 'System'
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app = App()
    app.mainloop()