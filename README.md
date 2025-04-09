# Cookie信息提取器

一个简洁美观的Cookie信息提取和管理工具，基于Python和PySide6开发。

## 功能特点

- 🎯 精准的Cookie提取：支持域名匹配，快速筛选目标Cookie
- 📝 灵活的数据导入：支持文件拖放和文本粘贴两种方式
- 🎨 美观的界面设计：现代化UI，支持自定义主题
- 📊 清晰的数据展示：表格化展示Cookie信息，支持排序
- 💾 便捷的数据导出：支持导出为标准JSON格式
- 🔍 强大的搜索功能：支持模糊匹配和精确匹配
- 🖥️ 跨平台支持：Windows、macOS、Linux全平台支持

## 安装说明

### 使用可执行文件（推荐）

1. 从 [Releases](https://github.com/YtMour/Cookic-screening/releases/tag/cookie) 页面下载最新版本
2. 解压下载的文件
3. 双击运行 `Cookie信息提取器.exe`

### 从源码安装

1. 克隆仓库：
```bash
git clone https://github.com/YtMour/Cookic-screening.git
cd cookie-extractor
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行程序：
```bash
python cookie_extractor_gui.py
```

## 使用方法

1. **导入Cookie数据**
   - 拖放JSON文件到程序窗口
   - 或点击"选择文件"按钮导入
   - 或直接粘贴Cookie文本到输入框

2. **匹配Cookie**
   - 在域名输入框中输入要匹配的域名
   - 支持模糊匹配，如输入"twitter"可匹配".twitter.com"
   - 点击"提取Cookie"按钮开始匹配

3. **查看结果**
   - 匹配结果将在表格中显示
   - 可以点击表头进行排序
   - 鼠标悬停可查看完整内容

4. **导出数据**
   - 点击"保存结果"按钮
   - 选择保存位置
   - 自动保存为标准JSON格式

## 技术栈

- Python 3.10+
- PySide6
- PyInstaller（用于打包）

## 开发说明

### 环境配置

```bash
# 安装开发依赖
pip install -r requirements-dev.txt

# 运行测试
python -m pytest tests/

# 构建可执行文件
python build_exe.py
```

### 项目结构

```
cookie-extractor/
├── cookie_extractor_gui.py  # 主程序
├── build_exe.py            # 打包脚本
├── requirements.txt        # 依赖文件
├── icons.ico              # 程序图标
└── README.md              # 说明文档
```

## 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情


## 更新日志

### v1.0.0 (2024-03-xx)
- 🎉 首次发布
- ✨ 实现基本的Cookie提取功能
- 🎨 优化UI界面
- 🐛 修复已知问题