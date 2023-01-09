#https://www.pythontutorial.net/tkinter/tkinter-example/
import PySimpleGUI as sg
import os
from pytube import YouTube
from datetime import datetime

now = datetime.now()


def rename_file(out_file, file_ext):
    current_time = now.strftime("%Y%d%m_%H%M%S")
    base, ext = os.path.splitext(out_file)
    new_file = base + current_time + '.' + file_ext
    os.rename(out_file, new_file)

def download_360p_mp4_videos(url: str, file_format: str,outpath: str = "./"):
    yt = YouTube(url)
    if file_format == "music":
        out_file = yt.streams.filter(only_audio=True).first().download(outpath)
        rename_file(out_file, "mp3")
    else:
        out_file = yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)
        rename_file(out_file, "mp4")
    return yt.title



label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a youtube url...", key = 'url')
file_format_combo = sg.Combo(['music','video'],default_value='music',key='file_format')
add_button = sg.Button("Download")
list_box = sg.Text(key='titles',size=[70,10],background_color="grey")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                layout=[[label],[input_box],[add_button,file_format_combo],[list_box],[exit_button]],
                font=('Helvetica',14))

while True:
    event, value = window.read()
    match event:
        case "Download":
            url = value['url'].strip()
            file_format = value['file_format'].strip()
            title = download_360p_mp4_videos(url,file_format)
            window['titles'].update(window['titles'].get() + '\n' + file_format + ":" +  title + " downloaded")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()