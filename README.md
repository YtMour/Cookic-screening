# Cookie信息提取器

这是一个用于从Cookie字符串中提取特定域名Cookie信息的工具，提供命令行和图形界面两种使用方式。

## 功能特点

- 支持JSON格式的Cookie字符串解析
- 支持按域名模式过滤Cookie
- 支持将结果保存为JSON文件
- 提供友好的错误处理机制
- 提供图形化界面操作

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 图形界面版本

运行图形界面版本：

```bash
python cookie_extractor_gui.py
```

图形界面功能：
1. 文件导入
   - 点击"选择文件"按钮导入文件
   - 直接拖放文件到文本区域
   - 直接在文本区域粘贴Cookie文本
2. 域名匹配
   - 在输入框中输入要匹配的域名
   - 点击"提取Cookie"按钮进行匹配
3. 结果查看
   - 在表格中查看匹配结果
   - 点击"保存结果"按钮导出结果

### 命令行版本

```python
from cookie_extractor import CookieExtractor

# 创建提取器实例
extractor = CookieExtractor()

# 解析Cookie字符串
extractor.parse_cookie_string(cookie_str)

# 过滤特定域名的Cookie
twitter_cookies = extractor.filter_by_domain('twitter')

# 保存结果
extractor.save_to_file(twitter_cookies, 'twitter_cookies.json')
```

## 示例

```python
from cookie_extractor import CookieExtractor

# 创建提取器实例
extractor = CookieExtractor()

# 解析Cookie字符串
extractor.parse_cookie_string(cookie_str)

# 过滤特定域名的Cookie
twitter_cookies = extractor.filter_by_domain('twitter')

# 保存结果
extractor.save_to_file(twitter_cookies, 'twitter_cookies.json')
```

## 注意事项

- 输入的Cookie字符串必须是有效的JSON格式
- 域名匹配支持正则表达式
- 输出文件使用UTF-8编码
- 图形界面支持文件拖放操作