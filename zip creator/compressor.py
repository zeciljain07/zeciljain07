import PySimpleGUI as psg
from zip_creator import make_archive

label1 = psg.Text("Select files to compress:")
input1 = psg.Input()
choose_button1 = psg.FilesBrowse("Choose", key="files")

label2 = psg.Text("Select destination folder:")
input2 = psg.Input()
choose_button2 = psg.FolderBrowse("Choose", key="folder")

compress_button = psg.Button("Compress")
output_label = psg.Text(key="output", text_color="orange")

window = psg.Window("File Compressor",
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Successful!")

window.close()
