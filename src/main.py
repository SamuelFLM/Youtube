import PySimpleGUI as sg
import webbrowser
import re
from pytube import YouTube
import pyautogui as bot
def main():
    sg.theme_background_color("white")
    cabecalho = [sg.Image(filename="img\Group 15 (2).png", background_color="white", pad=(0,(0,80)))]
    link = [
        [sg.Image(filename="img\Link.png", background_color="white", pad=(0,(0,20)))],
        [sg.Input("", background_color="white",border_width=0,k="link", pad=(20,(0,10)), font="Arial 9 bold", focus=True)],
        [sg.Image(filename="img\Line 1.png", background_color="white", pad=(20,(0,50)))],
        ]
    titulo = [
        [sg.Image(filename="img\Titulo.png", background_color="white", pad=(0,(0,20)))],
        [sg.Input("", background_color="white",border_width=0,k="titulo", font="Arial 9 bold", disabled=True,disabled_readonly_background_color="white",pad=(20,(0,10)))],
        [sg.Image(filename="img\Line 1.png", background_color="white", pad=(20,(0,20)))],
        [sg.Image(filename="img\Baixando.....png", background_color="white", pad=(20,(0,60)), k="baixando")],
    ]
    rodape =[
        [sg.Image(filename="img\Group 13 (1).png", background_color="white", pad=(0,(0,0)), enable_events=True, k="baixar")],
        [sg.Image(filename="img\Group 14.png", background_color="white", pad=(0,(0,0)), enable_events=True, k="ajuda")],
    ]
    layout = [cabecalho,link,titulo,rodape]
    window = sg.Window("Youtube Bot", layout=layout,size=(317,565),margins=(0,0), element_justification='c', icon="img\hd-youtube-logo-png-transparent-background-20.ico")
    
    while True:
        event, values = window.read(timeout=10)
        
        if event == sg.WIN_CLOSED:
            break
        
        try:
            if bool(values["link"]):
                url = str(values["link"])
                validacao = re.search("^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+",url)
                if validacao:
                    yt = YouTube(url=url)
                    window["baixar"].update(filename="img\Group 13.png")
                    window["titulo"].update(f"{yt.title}")
                    if event == "baixar":
                        bot.confirm(title="Iniciando", text="Iniciar Download.", buttons=["OK"])
                        ys = yt.streams.get_highest_resolution()
                        ys.download()
                        bot.confirm(title="Concluido", text="Download Concluido.", buttons=["OK"])
            else:
                if bool(values["link"]) == False:
                    window["baixar"].update(filename="img\Group 13 (1).png")
                    window["titulo"].update("")
                if event == "baixar":
                    bot.confirm(title="Erro", text="Insira o link do video", buttons=["OK"])
            if event == "ajuda":
                webbrowser.open_new_tab("https://github.com/SamuelFLM/Youtube-Bot-Download")
        except:
            pass
if __name__ == "__main__":
    main() 
