import PySimpleGUI as psg
from extractor import extract_archive

psg.theme("Black")

label1 = psg.Text("Select Archive:")
input1 = psg.Input()
choose_button1 = psg.FileBrowse("Choose", key="archive")

label2 = psg.Text("Select Dest Dir:")
input2 = psg.Input()
choose_button2 = psg.FolderBrowse("Choose", key="folder")

extract_button = psg.Button("Extract")
output_label = psg.Text(key="output", text_color="green")

window = psg.Window("Archive Extractor",
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Successful!")

window.close()
