import PyInstaller.__main__
import os
from pathlib import Path

# 获取当前目录
current_dir = Path(__file__).parent

# 定义图标文件
icon_file = 'icons.ico' if Path('icons.ico').exists() else 'icons.png'

# 确保图标文件存在
if not Path(icon_file).exists():
    print(f"警告: 图标文件 {icon_file} 不存在!")

# PyInstaller参数
params = [
    'cookie_extractor_gui.py',  # 主程序文件
    '--name=Cookie信息提取器',  # 生成的exe名称
    '--noconsole',  # 不显示控制台窗口
    '--onefile',    # 打包成单个exe文件
    '--clean',      # 清理临时文件
    f'--distpath={current_dir / "dist"}',  # 输出目录
    f'--workpath={current_dir / "build"}',  # 工作目录
    '--noconfirm',  # 覆盖现有文件不确认
]

# 添加图标
if Path(icon_file).exists():
    params.extend(['--icon', icon_file])

# 添加数据文件
datas = []
if Path('icons.ico').exists():
    datas.append(('icons.ico', '.'))
if Path('icons.png').exists():
    datas.append(('icons.png', '.'))

# 如果有数据文件，添加到参数中
if datas:
    for src, dst in datas:
        params.extend(['--add-data', f'{src};{dst}'])

print("打包参数:", params)

# 运行PyInstaller
PyInstaller.__main__.run(params) 