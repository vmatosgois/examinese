import tkinter
import tkinter.messagebox
import customtkinter
import os
import main as soft
import kdigo
from PIL import Image

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
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
        self.home = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Home_preta.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "Home_branca.png")), size=(25, 25))
        self.lab = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Lab_preta.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "Lab_branca.png")), size=(25, 25))
        self.espiro = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "lung_preta.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "lung_branca.png")), size=(25, 25))
        self.calc = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Calc_preta.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "Calc_branca.png")), size=(25, 25))
        self.config = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Config_preta.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "Config_branca.png")), size=(25, 25))
        self.help = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Ajuda_preta.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "Ajuda_branca.png")), size=(25, 25))
                        
        
        # Barra lateral

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Examine-SE", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.home_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Início',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.home, anchor='w', command=self.sidebar_button_event)
        self.home_button.grid(row=1, column=0, padx=5, pady=2, sticky= 'ew')
        
        self.lab_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Laboratoriais',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.lab, anchor='w', command=self.sidebar_button_event)
        self.lab_button.grid(row=2, column=0, padx=5, pady=2, sticky= 'ew')
        
        self.espiro_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Espirometria',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.espiro, anchor='w', command=self.sidebar_button_event)
        self.espiro_button.grid(row=3, column=0, padx=5, pady=2, sticky= 'ew')
        
        self.calc_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Calculadoras',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.calc, anchor='w', command=self.sidebar_button_event)
        self.calc_button.grid(row=4, column=0, padx=5, pady=2, sticky= 'ew')
                
        self.help_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Ajuda',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.help, anchor='w', command=self.sidebar_button_event)
        self.help_button.grid(row=6, column=0, padx=5, pady=2, sticky= 'ew')

        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Claro", "Escuro", "Sistema"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Proporção:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))
        
        # Home
        
        self.homeframe = customtkinter.CTkFrame(self, corner_radius= 0, fg_color='transparent')
        self.homeframe.grid(row=0, column= 1, rowspan=5, columnspan= 5 ,sticky= 'nsew')
        self.homeframe.grid_columnconfigure(1, weight=1)
        self.homeframe.grid_rowconfigure((0, 1), weight=1)

        # Tela inicial
        

        self.apresentacao = customtkinter.CTkLabel(self.homeframe, text= 'Bem-vindos ao Examine-se', font=customtkinter.CTkFont(size=30, weight="bold"))
        self.apresentacao.grid(row= 0, column= 1, padx= 20, pady= (50, 20))
        self.subtitulo = customtkinter.CTkLabel(self.homeframe, text= "Este é um projeto desenvolvido\n como parte do Trabalho de Conclusão de Curso \ndo Curso de Medicina de Victor Matos Gois. \n\n Para começar, por favor escolha uma das opções no menu à esquerda.", font=customtkinter.CTkFont(size=20))
        self.subtitulo.grid(row= 1, column=1, padx= 20, pady= 20)
        self.logo = customtkinter.CTkImage(light_image=Image.open("ufs_horizontal_positiva.png"),
                                  dark_image=Image.open("ufs_horizontal_negativa.png"))
        
        # # create main entry and button
        # self.main_button_1 = customtkinter.CTkButton(master=self, text='Enviar', fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column= 1, padx=(20, 20), pady=(20, 20), sticky="ns")
        
        # self.titulo = customtkinter.CTkLabel(self, text= 'Formatação de exames \n Para começar, certifique-se de que os exames estão precedidos de data no formato 00/00/00 ou 00/00/0000.', font=customtkinter.CTkFont(size=16))
        # self.titulo.grid(row= 0, column= 1, padx = 20, pady = (20,0), sticky='nsew')
        # self.textbox = customtkinter.CTkEntry(self,
        #                        placeholder_text="Insira seus exames aqui",
        #                        width=120,
        #                        height=25,
        #                        border_width=2,
        #                        corner_radius=10)
        # self.textbox.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew") 


        # # create checkbox and switch frame
        # self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        # self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        self.espiro_button.configure(state="disabled")
        # self.checkbox_3.configure(state="disabled")
        # self.checkbox_1.select()
        self.appearance_mode_optionemenu.set("Escuro")
        self.scaling_optionemenu.set("100%")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        if new_appearance_mode == 'Claro':
            new_appearance_mode = 'Light'
        elif new_appearance_mode == 'Escuro':
            new_appearance_mode = 'Dark'
        else:
            new_appearance_mode = 'System'
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()