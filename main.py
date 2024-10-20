import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES


def rename_files_in_folder(folder_path, target_string, replacement_string):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if target_string in filename:
                new_filename = filename.replace(
                    target_string, replacement_string)
                old_file = os.path.join(root, filename)
                new_file = os.path.join(root, new_filename)
                os.rename(old_file, new_file)
                print(f'Renamed: {old_file} -> {new_file}')


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        process_folder(folder_path)


def process_folder(folder_path):
    target_string = simpledialog.askstring("Input", "置換対象の文字列を入力してください:")
    replacement_string = simpledialog.askstring("Input", "置換後の文字列を入力してください:")
    if target_string and replacement_string:
        rename_files_in_folder(folder_path, target_string, replacement_string)
        messagebox.showinfo("完了", "ファイル名の置換が完了しました。")
    else:
        messagebox.showwarning("警告", "文字列が入力されていません。")


def drop(event):
    folder_path = event.data.strip('{}')  # フォルダパスの前後の{}を削除
    if os.path.isdir(folder_path):
        process_folder(folder_path)
    else:
        messagebox.showwarning("警告", "フォルダをドロップしてください。")


# GUIの設定
root = TkinterDnD.Tk()
root.title("ファイル名置換ツール")

frame = tk.Frame(root, width=400, height=200)
frame.pack_propagate(False)
frame.pack()

label = tk.Label(frame, text="ドラッグアンドドロップでフォルダを選択してください")
label.pack(pady=20)

button = tk.Button(frame, text="フォルダを選択", command=select_folder)
button.pack(pady=20)

# ドラッグアンドドロップの設定
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()
