import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="选择包含.m4s文件的文件夹")
    return folder_path

def find_files(folder_path):
    files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('30280.m4s'):
            files.append(os.path.join(folder_path, file_name))
    return files

def process_file(file_path):
    temp_file = file_path + '.tmp'
    
    with open(file_path, 'rb') as f:
        content = f.read()
    
    content = content.replace(b'000000000', b'')
    
    with open(temp_file, 'wb') as f:
        f.write(content)
    
    os.replace(temp_file, file_path)
    
    mp3_path = file_path[:-4] + '.mp3'
    os.rename(file_path, mp3_path)
    return mp3_path

def main():
    folder_path = select_folder()
    if not folder_path:
        print("未选择文件夹，程序退出")
        return
    
    files = find_files(folder_path)
    if not files:
        print("未找到以'30280'结尾的.m4s文件")
        return
    
    print(f"找到 {len(files)} 个文件")
    
    for file_path in files:
        print(f"处理文件: {file_path}")
        try:
            mp3_path = process_file(file_path)
            print(f"完成: {mp3_path}")
        except Exception as e:
            print(f"处理失败: {e}")
    
    print("全部处理完成")

if __name__ == "__main__":
    main()
