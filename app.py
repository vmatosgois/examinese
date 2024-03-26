import tkinter
import tkinter.messagebox
import customtkinter as ctk
import os
import main as soft
import kdigo
import webbrowser
import time
import pyperclip
import log
import espiro as es
import images as img
from loguru import logger
from PIL import Image

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
version = 'Piloto (beta v0.7)'
user = 'Victor Matos'

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Variáveis:
        
        entry = ''
        
        # janela
        self.title("Examine-SE")
        self.geometry(f"{1024}x{576}") # Feito em 1100x580

        # Grid
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0), weight=1)

        # Imagens
        
        self.home = ctk.CTkImage(light_image=img.home_p_final, dark_image=img.home_b_final, size=(25, 25))
        self.lab = ctk.CTkImage(light_image=img.lab_p_final, dark_image=img.lab_b_final, size=(25, 25))
        self.espiro = ctk.CTkImage(light_image=img.lung_p_final, dark_image=img.lung_b_final, size=(25, 25))
        self.calc = ctk.CTkImage(light_image=img.calc_p_final, dark_image=img.calc_b_final, size=(25, 25))
        self.config = ctk.CTkImage(light_image=img.config_p_final, dark_image=img.config_b_final, size=(25, 25))
        self.help = ctk.CTkImage(light_image=img.ajuda_p_final, dark_image=img.ajuda_b_final, size=(25, 25))                  
        
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
        
        self.calc_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='CKD-EPI',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.calc, anchor='w', command=self.calc_button_action)
        self.calc_button.grid(row=4, column=0, padx=5, pady=2, sticky= 'ew')
                
        self.help_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height= 30, border_spacing= 10, text='Ajuda',
                                                   fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                   image=self.help, anchor='w', command=self.help_button_action)
        self.help_button.grid(row=6, column=0, padx=5, pady=2, sticky= 'ew')

        
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(0, 0))
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Claro", "Escuro", "Sistema"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="Zoom:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(0, 0))
        self.scaling_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionmenu.grid(row=10, column=0, padx=20, pady=(10, 20))
        
        
        # Rodapé
        
        self.footer_frame = ctk.CTkFrame(self, height= 20, corner_radius=0)
        self.footer_frame.grid(row= 5, column= 1, sticky= 'nsew')
        self.footer_frame.columnconfigure(1, weight=1)
        
        self.footer_version_label = ctk.CTkLabel(self.footer_frame, text=f'Versão: {version}')
        self.footer_version_label.grid(row=0, column= 2, sticky= 'e', padx= 10)
        
        self.footer_user_label = ctk.CTkLabel(self.footer_frame, text=f'Usuário: {user}')
        self.footer_user_label.grid(row=0, column= 0, sticky= 'w', padx= 10)
        
        self.footer_message_label = ctk.CTkLabel(self.footer_frame, text='', text_color='green', font=ctk.CTkFont(weight="bold"))
        self.footer_message_label.grid(row=0, column= 1, sticky= 'n', padx= 10)
        
        # Home
        
        self.home_frame = ctk.CTkFrame(self, corner_radius= 0, fg_color='transparent')
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_rowconfigure((0, 1, 2), weight=1)

        self.apresentacao = ctk.CTkLabel(self.home_frame, text= 'Bem-vindos ao Examine-se', font=ctk.CTkFont(size=30, weight="bold"))
        self.apresentacao.grid(row= 0, column= 1, padx= 20, pady= (50, 20))
      
        self.subtitulo = ctk.CTkLabel(self.home_frame, text= "Este é um projeto desenvolvido\n como parte do Trabalho de Conclusão de Curso \ndo Curso de Medicina de Victor Matos Gois. \n\n Para começar, por favor escolha uma das opções no menu à esquerda.", font=ctk.CTkFont(size=20))
        self.subtitulo.grid(row= 1, column=1, padx= 20, pady= 20)
       
        self.ufslogo = ctk.CTkImage(light_image=img.ufs_p_final, dark_image=img.ufs_b_final, size= (275, 112))
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
                               font=ctk.CTkFont(family='Consolas', size=13))
        self.textbox.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew") 

        self.svcopia_lab = ctk.CTkCheckBox(self.lab_frame, text='Salvar uma cópia dos resultados')
        self.svcopia_lab.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="s")

        self.lab_concluir = ctk.CTkButton(self.lab_frame, text='Concluir', fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), hover_color=('gray70', 'gray30'), command=self.lab_button_concluir)
        self.lab_concluir.grid(row=4, column= 0, padx=(20, 20), pady=(20, 20), sticky="ns")
        
        self.lab_undo_button = ctk.CTkButton(self.lab_frame, text='Desfazer', fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), hover_color=('gray70', 'gray30'), command=self.lab_button_undo)

        # Espiro
        
        self.espiro_frame = ctk.CTkFrame(self, corner_radius= 0, fg_color='transparent')
        self.espiro_frame.columnconfigure(0, weight=1)
        
        self.espiro_subframe0= ctk.CTkFrame(self.espiro_frame, corner_radius= 0, fg_color= 'transparent')
        self.espiro_subframe0.grid(row= 0, column= 0, sticky= 'nsew')
        self.espiro_subframe0.columnconfigure(3, weight=1)
    
        self.espiro_label = ctk.CTkLabel(self.espiro_subframe0, text= 'Formatação de Espirometrias', font=ctk.CTkFont(size=20, weight='bold'))
        self.espiro_label.grid(row= 0, column = 3, padx= 20, pady= 20, sticky='n')
        self.espiro_sublabel = ctk.CTkLabel(self.espiro_subframe0,
                                            text= 'Para começar, preencha todos os campos exibidos abaixo.\nInsira apenas números.\nNos campos "Previsto >", informe o valor do Limite Inferior da Normalidade.\nNI = Não Informado',
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
        
        self.previsto_fef2575_label = ctk.CTkLabel(self.espiro_subframe4, text='Previsto >', font=ctk.CTkFont(size=14))
        self.previsto_fef2575_label.grid(row= 4, column= 2, padx= 10, pady= 5, sticky= 'ne')
        self.previsto_fef2575_entry = ctk.CTkEntry(self.espiro_subframe4, width=70, corner_radius= 15)
        self.previsto_fef2575_entry.grid(row= 4, column= 3, pady= 5, sticky='nw')
                
        self.pos_fef2575_label = ctk.CTkLabel(self.espiro_subframe4, text='Pós BD - FEF 25-75%:', font=ctk.CTkFont(size=14))
        self.pos_fef2575_label.grid(row= 4, column= 4, padx= 10, pady= 5, sticky= 'ne')
        self.pos_fef2575_entry = ctk.CTkEntry(self.espiro_subframe4, width=70, corner_radius= 15)
        self.pos_fef2575_entry.grid(row= 4, column= 5, pady= 5, sticky='nw')
        
        self.espiro_subframe5 = ctk.CTkFrame(self.espiro_frame, corner_radius= 0, fg_color= 'transparent')
        self.espiro_subframe5.grid(row=5, column= 0, sticky= 'nsew')
        self.espiro_subframe5.columnconfigure((0, 6), weight=1)
        
        self.svcopia_espiro = ctk.CTkCheckBox(self.espiro_subframe5, text='Salvar uma cópia dos resultados')
        self.svcopia_espiro.grid(row=0, column=1, pady=(20, 0), padx=20, sticky="s")
        
        self.espiro_concluir = ctk.CTkButton(self.espiro_subframe5, text='Concluir', fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), hover_color=('gray70', 'gray30'), command=self.espiro_button_concluir)
        self.espiro_concluir.grid(row=1, column= 1, padx=(20, 20), pady=(20, 20), sticky="ns")
        
        # Calculadoras, que vai ser só o ckdepi
        
        self.calc_frame = ctk.CTkFrame(self, corner_radius= 0, fg_color='transparent')
        self.calc_frame.grid_columnconfigure((0,1,2), weight=1)
        
        self.calc_label = ctk.CTkLabel(self.calc_frame, text= 'Cálculo de função renal', font=ctk.CTkFont(size=20, weight='bold'))
        self.calc_label.grid(row= 0, column= 1, padx = 20, pady = 20, sticky='nsew')
        self.calc_sublabel = ctk.CTkLabel(self.calc_frame, font=ctk.CTkFont(size=16),
                                                  text= 'Preencha os campos correspondentes e clique em "Concluir".')
        self.calc_sublabel.grid(row=1, column=1, padx=20, pady=(0,10), sticky= 'nsew')
        
        self.calc_subframe = ctk.CTkFrame(self.calc_frame, corner_radius=10)
        self.calc_subframe.grid(row= 2, column= 1, padx= 20, pady= 10)
        
        self.idade_label = ctk.CTkLabel(self.calc_subframe, text='Idade:', font=ctk.CTkFont(size=14))
        self.idade_label.grid(row= 2, column=1, padx= 12, sticky='nws')
        self.idade_entry = ctk.CTkEntry(self.calc_subframe, width=170, corner_radius= 10)
        self.idade_entry.grid(row= 3, column= 1, padx= 10, pady= (0,5), sticky='nw')
        
        self.sex_label = ctk.CTkLabel(self.calc_subframe, text='Sexo:', font=ctk.CTkFont(size=14))
        self.sex_label.grid(row= 4, column=1, padx= 12, sticky='nws')
        self.radio_var = tkinter.StringVar(value=None)
        self.radiobutton_frame = ctk.CTkFrame(self.calc_subframe, fg_color='transparent')
        self.radiobutton_frame.grid(row=5, column=1, sticky="nsew")
        self.sex_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame, radiobutton_height= 20, radiobutton_width= 20, border_width_checked= 10, text= 'Masculino', variable=self.radio_var, value='H', font=ctk.CTkFont(size=14))
        self.sex_button_1.grid(row=1, column=1, pady=10, padx=10, sticky="n")
        self.sex_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame, radiobutton_height= 20, radiobutton_width= 20, border_width_checked= 10, text= 'Feminino', variable=self.radio_var, value='M', font=ctk.CTkFont(size=14))
        self.sex_button_2.grid(row=2, column=1, pady=10, padx=10, sticky="n")
        self.sex_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame, radiobutton_height= 20, radiobutton_width= 20, border_width_checked= 10, text= 'None', variable=self.radio_var, value=None, font=ctk.CTkFont(size=14))
        
        self.creat_label = ctk.CTkLabel(self.calc_subframe, text='Creatinina Sérica (mg/dL):', font=ctk.CTkFont(size=14))
        self.creat_label.grid(row= 6, column=1, padx= 12, sticky='nws')
        self.creat_entry = ctk.CTkEntry(self.calc_subframe, width=170, corner_radius= 10)
        self.creat_entry.grid(row= 7, column= 1, padx= 10, pady= (0,5), sticky='nw')
        
        self.calc_concluir = ctk.CTkButton(self.calc_frame, text='Concluir', fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), hover_color=('gray70', 'gray30'), command=self.ckdepi_button_concluir)
        self.calc_concluir.grid(row=3, column= 1, padx=(20, 20), pady=(10, 20), sticky="ns")
        
        self.ckdepi_result = ctk.CTkTextbox(self.calc_frame, fg_color='transparent', width= 400, state= 'normal',border_width=0, corner_radius= 0,font=ctk.CTkFont(size=16))
        
        # Ajuda
        
        self.help_frame = ctk.CTkFrame(self, corner_radius= 0, fg_color='transparent')
        self.help_frame.columnconfigure(3, weight= 1)
        
        self.help_label = ctk.CTkLabel(self.help_frame, text= 'Dúvidas, sugestões e reclamações', font=ctk.CTkFont(size=20, weight='bold'))
        self.help_label.grid(row= 0, column = 3, padx= 20, pady= 20, sticky='n')
        self.help_sublabel = ctk.CTkLabel(self.help_frame,
                                            text= 'Caso deseje relatar erros, sugerir melhorias e/ou entrar em contato\ncom o desenvolvedor responsável, utilize uma das opções abaixo.',
                                            font=ctk.CTkFont(size=16))
        self.help_sublabel.grid(row=1, column= 3, padx=20, pady= (0,20), sticky='n')
        
        self.info_text = ctk.CTkTextbox(self.help_frame, height= 200, fg_color='transparent', state= 'normal',border_width=0, corner_radius= 0,font=ctk.CTkFont(size=16))
        self.info_text.insert(0.0,
                              text='Informações para contato:\n\nVictor Matos:\n\nTelefone (Whatsapp): (79) 99808-0327\nEmail: vmatosgois@academico.ufs.br\n\nCaso esteja conectado à internet, pode ser utilizado o formulário abaixo:')
        self.info_text.configure(state='disabled')
        self.info_text.grid(row= 2, column=3, padx=20, sticky='nsew')
        
        self.button_forms = ctk.CTkButton(self.help_frame, text= 'Clique aqui para entrar em contato via Google Forms',fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), hover_color=('gray70', 'gray30'), font=ctk.CTkFont(size=16), command=self.abrir_link)
        self.button_forms.grid(row= 3, column= 3, sticky= 'n')        

        # Valores padrão
        self.svcopia_lab.select()
        self.svcopia_espiro.select()
        self.appearance_mode_optionmenu.set("Escuro")
        self.scaling_optionmenu.set("100%")

        # Tela inicial padrão
        self.select_frame("home")

    def select_frame(self, frame):
        # Cor do botão
        self.home_button.configure(fg_color=("gray75", "gray25") if frame == "home" else "transparent")
        self.lab_button.configure(fg_color=("gray75", "gray25") if frame == "lab" else "transparent")
        self.espiro_button.configure(fg_color=("gray75", "gray25") if frame == "espiro" else "transparent")
        self.calc_button.configure(fg_color=("gray75", "gray25") if frame == "calc" else "transparent")
        self.help_button.configure(fg_color=("gray75", "gray25") if frame == "help" else "transparent")

        logger.info(f'Alterado para página {frame}')
        
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

    # Botões dos frames
    
    def home_button_action(self):
        self.select_frame("home")
        self.remove_message()

    def lab_button_action(self):
        self.select_frame("lab")
        self.remove_message()

    def espiro_button_action(self):
        self.select_frame("espiro")
        self.remove_message()

    def calc_button_action(self):
        self.select_frame("calc")
        self.remove_message()
        
    def help_button_action(self):
        self.select_frame("help")
        self.remove_message()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        if new_appearance_mode == 'Claro':
            new_appearance_mode = 'Light'
        elif new_appearance_mode == 'Escuro':
            new_appearance_mode = 'Dark'
        else:
            new_appearance_mode = 'System'
        ctk.set_appearance_mode(new_appearance_mode)
        
        logger.info(f'Tema alterado para {new_appearance_mode}')

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        logger.info(f'Escala alterada para: {new_scaling_float}')
    
    def abrir_link(self):
        webbrowser.open('https://forms.gle/YEPhf3DAVcMSvS7W9')
        logger.info('Utilizado formulário')
        
    # Botões de finalizar
    @logger.catch
    def lab_button_concluir(self):
        # Entradas
        global entry
            
        entry = self.textbox.get("0.0", 'end-1c')
        if entry != '':
            output = soft.main(entry)
            self.textbox.delete("0.0", "end")
            self.textbox.insert("0.0", output)
            
            pyperclip.copy(output)
            
            if self.svcopia_lab.get() == 1:
                self.create_copy(entry, output)
            
            self.textbox.configure(state='disabled')
            
            self.lab_concluir.configure(text= 'Novo texto', command= self.lab_button_new)
            
            self.lab_undo_button.grid(row= 4, column= 0, padx=(20, 20), pady=(20, 20), sticky="w")
            
            self.message()
            
            logger.success('Exames processados com sucesso')
            
            logger.info(f'Texto inicial:\n\n{entry}\n\nSaída:\n\n{output}')
            
            return entry
        else:
            tkinter.messagebox.showwarning('Erro', 'Por favor, insira o texto.')
            
            logger.erro('Nenhum texto inserido')
            
    @logger.catch    
    def lab_button_new(self):
        self.lab_undo_button.grid_forget()
        
        self.textbox.configure(state='normal')
        self.textbox.delete("0.0", "end")
        
        self.lab_concluir.configure(text= 'Concluir', command= self.lab_button_concluir)
        
        self.remove_message()
        
        logger.info('Novo texto')
   
    @logger.catch    
    def lab_button_undo(self):
        global entry
        
        self.lab_undo_button.grid_forget()
        
        self.lab_concluir.configure(text= 'Concluir', command= self.lab_button_concluir)
        
        self.textbox.configure(state='normal')
        self.textbox.delete("0.0", "end")
        self.textbox.insert('0.0', entry)
        
        self.remove_message()
        
        logger.info('Retornado ao texto original')
    
    @logger.catch    
    def espiro_button_concluir(self):
        
        es.valores['DATA'] = self.data_entry.get()
        es.valores['PRE_CVF'] = self.pre_cvf_entry.get()
        es.valores['CVF_PREVISTO'] = self.previsto_cvf_entry.get()
        es.valores['POS_CVF'] = self.pos_cvf_entry.get()
        es.valores['PRE_FEV1'] = self.pre_fev_entry.get()
        es.valores['FEV1_PREVISTO'] = self.previsto_fev_entry.get()
        es.valores['POS_FEV1'] = self.pos_fev_entry.get()
        es.valores['FEV1/CVF_PREVISTO'] = self.previsto_fev_cvf_entry.get()
        es.valores['PRE_FEF2575'] = self.pre_fef2575_entry.get()
        es.valores['FEF2575_PREVISTO'] = self.previsto_fef2575_entry.get()
        es.valores['POS_FEF2575'] = self.pos_fef2575_entry.get()

        output = es.main(valores=es.valores)
        
        pyperclip.copy(output)
            
        if self.svcopia_espiro.get() == 1:
                self.create_copy(es.valores, output)
                
        self.message()
        
        logger.success('Espirometria formatada com sucesso')
        logger.info(f'Variáveis e resultados:\n\n{es.valores}\n\n{output}')
    
    @logger.catch    
    def ckdepi_button_concluir(self):
        
        self.ckdepi_result.configure(state='normal')
        self.ckdepi_result.delete("0.0", "end")
        
        idade = self.idade_entry.get()
        sexo = self.radio_var.get() if self.radio_var.get() != None else ''
        creat = self.creat_entry.get()

        if '' not in (idade, sexo, creat):
            tfg = kdigo.ckdepi(creat, idade, sexo)
            score = kdigo.scoreKdigo(tfg)
            
            self.ckdepi_result.insert(0.0, text=f'Resultado:\n{tfg} {kdigo.unidade}\nEstágio: {score}')
            self.ckdepi_result.configure(state='disabled')
            self.ckdepi_result.grid(row= 4, column=1, padx=20, sticky='n')
            
            pyperclip.copy(self.ckdepi_result.get('0.0', 'end-1c'))
            
            self.message()
            
            logger.success(f'TFG calculado com sucesso\n{self.ckdepi_result.get()}')
        else: 
            tkinter.messagebox.showwarning('Erro', 'Por favor, preencha todos os campos.')
            
            logger.warning('Campos não preenchidos encontrados')
            logger.info(f'Variáveis atuais: Idade: {idade}, Sexo: {sexo}, Creat: {creat} ')

    # Outras funções:
    
    def message(self):
        
        self.footer_message_label.configure(text='Copiado para a área de transferência!')
        
    def remove_message(self):
        
        self.footer_message_label.configure(text='')
    
    @logger.catch    
    def create_copy(self, text1, text2):
        
        t = time.localtime()
        name = time.strftime("%d-%m-%Y %H-%M-%S", t)
        with open(f'copias/{name}.txt', 'x', encoding='utf-8') as history:
            history.write(f'Entrada:\n{text1}\n\nSaída:\n{text2}')
        
        logger.success('Cópia criada com sucesso')

@logger.catch        
def start():
    due_date = time.localtime()    
    if due_date[1] < 7:
        history_path= "copias"
        if not os.path.exists(history_path): os.makedirs(history_path)
        logger.success(f'Inicializado com sucesso. Usuário: {user}')
        app = App()
        app.mainloop()
    else:
        tkinter.messagebox.showinfo(title= 'Fim de período de testes', message='O período de testes foi encerrado.\nObrigado pela sua participação na pesquisa.\nCaso acredite que isto seja um erro, entre em contato com Victor Matos.\nTelefone para contato: (79)99808-0327\nEmail: vmatosgois@gmail.com')
        logger.critical(f'Tentativa de inicializar após fim de fase de testes. Usuário: {user}')
                
if __name__ == "__main__":
    log.create_log()
    start()
    