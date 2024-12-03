import os
import tkinter as tk
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image

# ---------------------------------
# 初期処理
# ---------------------------------

# ファイルディレクトリを取得
scriptDIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()

# 出力ディレクトリを定義
OUTPUT_DIR = f"{scriptDIR}/img"

# ドラッグされたファイルのリストを保持
dropped_file_list = []

# ---------------------------------
# 関数定義
# ---------------------------------

def ensure_output_dir():
    """出力フォルダを確認し、存在しない場合は作成する"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def on_drop(event):
    """ファイルがドラッグ＆ドロップされた際の処理"""
    global dropped_file_list
    file_paths = event.data.split()  # 複数ファイルを分割してリストに格納
    for file_path in file_paths:
        if file_path not in dropped_file_list:
            dropped_file_list.append(file_path)
    
    # リストウィジェットを更新
    file_listbox.delete(0, tk.END)  # リストをクリア
    for file in dropped_file_list:
        file_listbox.insert(tk.END, file)

    label.configure(text=f"{len(dropped_file_list)} file(s) ready for conversion")

def convert_to_webp():
    """変換ボタンが押されたときに実行される処理"""
    if not dropped_file_list:
        label.configure(text="No files selected")
        return

    ensure_output_dir()
    success_count = 0
    for file_path in dropped_file_list:
        try:
            # 入力ファイルの情報を取得
            file_name = os.path.basename(file_path)
            file_stem, _ = os.path.splitext(file_name)

            # 出力ファイルパス
            output_file_path = os.path.join(OUTPUT_DIR, f"{file_stem}.webp")

            # 画像を開いてWebP形式に変換
            img = Image.open(file_path)
            img.save(output_file_path, format='WEBP')

            success_count += 1
        except Exception as e:
            label.configure(text=f"Error processing: {file_path}")
            continue

    label.configure(text=f"Converted {success_count}/{len(dropped_file_list)} files")
    file_listbox.delete(0, tk.END)  # リストをリセット
    dropped_file_list.clear()

# フォントの指定
font = ('メイリオ', 10)

# 出力ディレクトリを確認
ensure_output_dir()

# メインウィンドウの作成
root = TkinterDnD.Tk()

# GUI全体のダークテーマ設定
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ウィンドウのタイトルとサイズ
root.title("Image File Drag and Drop")
root.geometry("420x400")
root.resizable(False, False)

# メインフレーム
main_frame = ctk.CTkFrame(root, corner_radius=10)
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)

# ドラッグ＆ドロップエリア
drop_area = ctk.CTkFrame(main_frame, width=400, height=100, corner_radius=10)
drop_area.grid(row=0, column=0, padx=10, pady=10)

drop_label = ctk.CTkLabel(drop_area, text="Drag and Drop Images")
drop_label.place(relx=0.5, rely=0.5, anchor="center")

# ファイルリスト表示
file_listbox = tk.Listbox(main_frame, bg="darkgray", fg="white", height=8, selectmode=tk.BROWSE)
file_listbox.grid(row=1, column=0, padx=10, pady=8, sticky="nsew")

# ステータスラベル
label = ctk.CTkLabel(main_frame, text="No files selected", width=200, height=40, corner_radius=8)
label.grid(row=2, column=0, padx=10, pady=4)

# 変換ボタン
convert_button = ctk.CTkButton(main_frame, text="Convert to WebP", command=convert_to_webp)
convert_button.grid(row=3, column=0, padx=10, pady=30)

# ドラッグ＆ドロップイベントのバインド
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', on_drop)

# メインループの開始
root.mainloop()
