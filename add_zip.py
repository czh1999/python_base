#一个脚本,点击后修改其他文件的后缀，如果没有后缀增加.zip后缀
from pathlib import Path
import sys
def main():
    #获取当前目录
    current_dir = Path(__file__).parent
    #获取当前文件的文件名
    current_file_name = Path(__file__).name
    #遍历当前目录下的所有文件
    for file in current_dir.iterdir():
        #如果是文件且不是当前文件
        if file.is_file() and file.name != current_file_name and not file.name.endswith(".bat"):
            #获取文件的后缀
            suffix = file.suffix
            new_file = file.with_suffix('.zip')
            file.rename(new_file)
            print(f"已将文件 {file.name} 修改为 {new_file.name}")  
            