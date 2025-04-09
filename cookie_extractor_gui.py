import sys
import os
import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLineEdit, QLabel, 
                             QTableWidget, QTableWidgetItem, QFileDialog, 
                             QMessageBox, QTextEdit, QHeaderView, QFrame,
                             QSizePolicy)
from PySide6.QtCore import Qt, QMimeData, QSize, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QFont, QPalette, QColor, QIcon

def resource_path(relative_path):
    """获取资源绝对路径"""
    try:
        # PyInstaller创建临时文件夹，将路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class SimpleButton(QPushButton):
    """简约风格按钮"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(32)
        self.setFont(QFont('Microsoft YaHei', 9))
        self.setCursor(Qt.PointingHandCursor)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #4A90E2;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 16px;
                font-weight: normal;
            }
            QPushButton:hover {
                background-color: #357ABD;
            }
            QPushButton:pressed {
                background-color: #2D6DA3;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
            }
        """)

class SimpleLineEdit(QLineEdit):
    """简约风格输入框"""
    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setMinimumHeight(32)
        self.setFont(QFont('Microsoft YaHei', 9))
        self.setStyleSheet("""
            QLineEdit {
                border: 1px solid #E0E0E0;
                border-radius: 4px;
                padding: 6px 12px;
                background-color: white;
                color: #333333;
            }
            QLineEdit:focus {
                border: 1px solid #4A90E2;
            }
            QLineEdit::placeholder {
                color: #999999;
            }
        """)

class SimpleTextEdit(QTextEdit):
    """简约风格文本编辑框"""
    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setFont(QFont('Microsoft YaHei', 9))
        self.setStyleSheet("""
            QTextEdit {
                border: 1px solid #E0E0E0;
                border-radius: 4px;
                padding: 8px;
                background-color: white;
                color: #333333;
            }
            QTextEdit:focus {
                border: 1px solid #4A90E2;
            }
            QTextEdit::placeholder {
                color: #999999;
            }
            /* 滚动条样式 */
            QScrollBar:vertical {
                border: none;
                background: #F5F5F5;
                width: 8px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #BDBDBD;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background: #9E9E9E;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        # 启用拖放功能
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.setText(content)
            except Exception as e:
                QMessageBox.warning(self, "错误", f"读取文件时出错：{str(e)}")

class SimpleTable(QTableWidget):
    """简约风格表格"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont('Microsoft YaHei', 9))
        self.setStyleSheet("""
            QTableWidget {
                border: 1px solid #E0E0E0;
                border-radius: 4px;
                background-color: white;
                gridline-color: #EEEEEE;
                color: #333333;
            }
            QHeaderView::section {
                background-color: #F5F5F5;
                padding: 8px 12px;
                border: none;
                font-weight: bold;
                color: #333333;
                border-bottom: 1px solid #E0E0E0;
            }
            QTableWidget::item {
                padding: 8px 12px;
                border-bottom: 1px solid #EEEEEE;
            }
            QTableWidget::item:selected {
                background-color: #F5F5F5;
                color: #333333;
            }
            QTableWidget::item:hover {
                background-color: #F8F9FA;
            }
            /* 设置交替行颜色 */
            QTableWidget::item:alternate {
                background-color: #FAFAFA;
            }
            /* 滚动条样式 */
            QScrollBar:vertical {
                border: none;
                background: #F5F5F5;
                width: 8px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #BDBDBD;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background: #9E9E9E;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar:horizontal {
                border: none;
                background: #F5F5F5;
                height: 8px;
                margin: 0px;
            }
            QScrollBar::handle:horizontal {
                background: #BDBDBD;
                min-width: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:horizontal:hover {
                background: #9E9E9E;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }
        """)
        self.setShowGrid(True)
        self.setGridStyle(Qt.SolidLine)
        self.setAlternatingRowColors(True)
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.horizontalHeader().setStretchLastSection(True)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # 设置表格列宽
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setDefaultSectionSize(120)
        
        # 设置水平滚动条
        self.setHorizontalScrollMode(QTableWidget.ScrollPerPixel)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

class CookieExtractorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cookies: List[Dict[str, Any]] = []
        self.initUI()
        
    def initUI(self):
        """初始化UI界面"""
        self.setWindowTitle('Cookie信息提取器')
        self.setMinimumSize(900, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: white;
            }
            QLabel {
                color: #333333;
                font-weight: normal;
                font-size: 13px;
            }
        """)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # 标题
        title_label = QLabel('Cookie信息提取器')
        title_label.setStyleSheet("""
            QLabel {
                color: #333333;
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 16px;
            }
        """)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # 上半部分布局（文件导入和域名匹配）
        top_layout = QVBoxLayout()
        top_layout.setSpacing(16)
        
        # 文件导入区域
        file_frame = QFrame()
        file_layout = QVBoxLayout(file_frame)
        file_layout.setSpacing(8)
        file_layout.setContentsMargins(0, 0, 0, 0)
        
        file_label = QLabel('文件导入')
        file_label.setStyleSheet('font-size: 14px; color: #333333;')
        file_layout.addWidget(file_label)
        
        # 文件路径和按钮布局
        path_layout = QHBoxLayout()
        path_layout.setSpacing(8)
        
        self.file_path_label = QLabel('未选择文件')
        self.file_path_label.setStyleSheet("""
            QLabel {
                color: #666666;
                padding: 6px 12px;
                background-color: #F8F9FA;
                border: 1px solid #E0E0E0;
                border-radius: 4px;
            }
        """)
        self.file_path_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        
        import_btn = SimpleButton('选择文件')
        import_btn.setFixedWidth(90)
        import_btn.clicked.connect(self.import_file)
        
        path_layout.addWidget(self.file_path_label)
        path_layout.addWidget(import_btn)
        file_layout.addLayout(path_layout)
        
        # Cookie文本输入区域
        self.cookie_text = SimpleTextEdit('请在此粘贴Cookie文本或拖放文件')
        self.cookie_text.setFixedHeight(100)
        file_layout.addWidget(self.cookie_text)
        
        top_layout.addWidget(file_frame)
        
        # 域名匹配区域
        domain_frame = QFrame()
        domain_layout = QVBoxLayout(domain_frame)
        domain_layout.setSpacing(8)
        domain_layout.setContentsMargins(0, 0, 0, 0)
        
        domain_label = QLabel('域名匹配')
        domain_label.setStyleSheet('font-size: 14px; color: #333333;')
        domain_layout.addWidget(domain_label)
        
        # 域名输入和匹配按钮布局
        input_layout = QHBoxLayout()
        input_layout.setSpacing(8)
        
        self.domain_input = SimpleLineEdit('输入要匹配的域名（例如：twitter）')
        match_btn = SimpleButton('提取Cookie')
        match_btn.setFixedWidth(90)
        match_btn.clicked.connect(self.extract_cookies)
        
        input_layout.addWidget(self.domain_input)
        input_layout.addWidget(match_btn)
        domain_layout.addLayout(input_layout)
        
        top_layout.addWidget(domain_frame)
        main_layout.addLayout(top_layout)
        
        # 匹配结果区域
        result_frame = QFrame()
        result_layout = QVBoxLayout(result_frame)
        result_layout.setSpacing(8)
        result_layout.setContentsMargins(0, 0, 0, 0)
        
        result_header = QHBoxLayout()
        result_label = QLabel('匹配结果')
        result_label.setStyleSheet('font-size: 14px; color: #333333;')
        
        # 添加匹配结果数量显示
        self.result_count_label = QLabel('0 个结果')
        self.result_count_label.setStyleSheet("""
            QLabel {
                color: #666666;
                padding: 4px 8px;
                background-color: #F5F5F5;
                border-radius: 4px;
                font-size: 12px;
            }
        """)
        
        save_btn = SimpleButton('保存结果')
        save_btn.setFixedWidth(90)
        save_btn.clicked.connect(self.save_results)
        
        result_header.addWidget(result_label)
        result_header.addWidget(self.result_count_label)
        result_header.addStretch()
        result_header.addWidget(save_btn)
        result_layout.addLayout(result_header)
        
        # 添加表格说明标签
        table_info = QLabel('提示：表格显示了所有匹配的 Cookie 信息，包括域名、名称、值、过期时间等属性。可以通过点击列标题进行排序。')
        table_info.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 12px;
                padding: 4px 0;
            }
        """)
        result_layout.addWidget(table_info)
        
        # 结果表格
        self.result_table = SimpleTable()
        self.result_table.setColumnCount(9)
        self.result_table.setHorizontalHeaderLabels([
            '域名', 'Cookie名称', 'Cookie值', '过期时间', 'HttpOnly',
            '路径', 'SameSite', 'Secure', 'ID'
        ])
        result_layout.addWidget(self.result_table)
        
        # 设置表格列宽
        header = self.result_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Interactive)  # 域名
        header.setSectionResizeMode(1, QHeaderView.Interactive)  # 名称
        header.setSectionResizeMode(2, QHeaderView.Interactive)  # 值 - 改为Interactive以确保显示
        header.setSectionResizeMode(3, QHeaderView.Interactive)  # 过期时间
        header.setSectionResizeMode(4, QHeaderView.Interactive)  # HttpOnly
        header.setSectionResizeMode(5, QHeaderView.Interactive)  # 路径
        header.setSectionResizeMode(6, QHeaderView.Interactive)  # SameSite
        header.setSectionResizeMode(7, QHeaderView.Interactive)  # Secure
        header.setSectionResizeMode(8, QHeaderView.Interactive)  # ID
        
        # 设置默认列宽
        self.result_table.setColumnWidth(0, 150)  # 域名
        self.result_table.setColumnWidth(1, 150)  # 名称
        self.result_table.setColumnWidth(2, 250)  # 值 - 设置更大的默认宽度
        self.result_table.setColumnWidth(3, 150)  # 过期时间
        self.result_table.setColumnWidth(4, 80)   # HttpOnly
        self.result_table.setColumnWidth(5, 80)   # 路径
        self.result_table.setColumnWidth(6, 100)  # SameSite
        self.result_table.setColumnWidth(7, 80)   # Secure
        self.result_table.setColumnWidth(8, 60)   # ID
        
        main_layout.addWidget(result_frame, stretch=1)
        
        # 设置窗口图标
        for icon_name in ['icons.ico', 'icons.png']:
            icon_path = resource_path(icon_name)
            if os.path.exists(icon_path):
                self.setWindowIcon(QIcon(icon_path))
                break
        
    def import_file(self):
        """导入文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择Cookie文件",
            "",
            "JSON文件 (*.json);;文本文件 (*.txt);;所有文件 (*.*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.file_path_label.setText(Path(file_path).name)
                self.cookie_text.setText(content)
            except Exception as e:
                QMessageBox.warning(self, "错误", f"读取文件时出错：{str(e)}")
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """处理拖入事件"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        """处理文件拖放"""
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.file_path_label.setText(Path(file_path).name)
                self.cookie_text.setText(content)
            except Exception as e:
                QMessageBox.warning(self, "错误", f"读取文件时出错：{str(e)}")
    
    def extract_cookies(self):
        """提取Cookie"""
        try:
            # 获取输入的Cookie文本
            cookie_str = self.cookie_text.toPlainText().strip()
            if not cookie_str:
                QMessageBox.warning(self, "警告", "请输入Cookie文本")
                return
            
            # 解析Cookie
            self.cookies = json.loads(cookie_str)
            
            # 获取域名匹配模式
            domain_pattern = self.domain_input.text().strip()
            if not domain_pattern:
                QMessageBox.warning(self, "警告", "请输入要匹配的域名")
                return
            
            # 过滤Cookie
            import re
            pattern = re.compile(domain_pattern, re.IGNORECASE)
            filtered_cookies = [
                cookie for cookie in self.cookies 
                if pattern.search(cookie.get('domain', ''))
            ]
            
            # 显示结果
            self.display_results(filtered_cookies)
            
        except json.JSONDecodeError:
            QMessageBox.warning(self, "错误", "Cookie文本格式错误")
        except Exception as e:
            QMessageBox.warning(self, "错误", f"处理过程中出错：{str(e)}")
    
    def display_results(self, cookies: List[Dict[str, Any]]):
        """显示结果到表格"""
        self.result_table.setRowCount(len(cookies))
        
        # 更新匹配结果数量
        self.result_count_label.setText(f'共 {len(cookies)} 个结果')
        
        for row, cookie in enumerate(cookies):
            # 保存原始时间戳到表格的userData中
            expiration = cookie.get('expirationDate', 0)
            
            # 设置域名和名称
            self.result_table.setItem(row, 0, QTableWidgetItem(str(cookie.get('domain', ''))))
            self.result_table.setItem(row, 1, QTableWidgetItem(str(cookie.get('name', ''))))
            
            # 设置value值，确保正确显示
            value = str(cookie.get('value', ''))
            value_item = QTableWidgetItem(value)
            value_item.setToolTip(value)  # 添加工具提示，方便查看完整内容
            self.result_table.setItem(row, 2, value_item)
            
            # 创建时间显示项
            time_item = QTableWidgetItem()
            time_item.setData(Qt.UserRole, float(expiration) if expiration else 0)
            
            # 格式化显示时间
            if expiration:
                try:
                    expiration_date = datetime.fromtimestamp(float(expiration)).strftime('%Y-%m-%d %H:%M:%S')
                    time_item.setText(expiration_date)
                except:
                    time_item.setText(str(expiration))
            else:
                time_item.setText('')
            
            self.result_table.setItem(row, 3, time_item)
            
            # 设置其他属性
            self.result_table.setItem(row, 4, QTableWidgetItem(str(cookie.get('httpOnly', False))))
            self.result_table.setItem(row, 5, QTableWidgetItem(str(cookie.get('path', '/'))))
            self.result_table.setItem(row, 6, QTableWidgetItem(str(cookie.get('sameSite', ''))))
            self.result_table.setItem(row, 7, QTableWidgetItem(str(cookie.get('secure', False))))
            self.result_table.setItem(row, 8, QTableWidgetItem(str(cookie.get('id', ''))))
            
            # 设置单元格对齐方式和工具提示
            for col in range(self.result_table.columnCount()):
                item = self.result_table.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    if not item.toolTip():
                        item.setToolTip(item.text())
                    # 确保单元格内容可见
                    item.setFlags(item.flags() | Qt.ItemIsEnabled)
    
    def save_results(self):
        """保存结果到文件"""
        if not self.result_table.rowCount():
            QMessageBox.warning(self, "警告", "没有可保存的结果")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "保存结果",
            "",
            "JSON文件 (*.json)"
        )
        
        if file_path:
            try:
                # 从表格中获取完整的Cookie数据
                cookies = []
                for row in range(self.result_table.rowCount()):
                    # 获取存储在UserRole中的原始时间戳
                    time_item = self.result_table.item(row, 3)
                    expiration_timestamp = time_item.data(Qt.UserRole) if time_item else 0

                    cookie = {
                        'domain': self.result_table.item(row, 0).text(),
                        'name': self.result_table.item(row, 1).text(),
                        'value': self.result_table.item(row, 2).text(),
                        'expirationDate': float(expiration_timestamp),
                        'httpOnly': self.result_table.item(row, 4).text().lower() == 'true',
                        'path': self.result_table.item(row, 5).text(),
                        'sameSite': self.result_table.item(row, 6).text(),
                        'secure': self.result_table.item(row, 7).text().lower() == 'true',
                        'id': int(self.result_table.item(row, 8).text().strip() or 0)
                    }
                    cookies.append(cookie)
                
                # 保存到文件，使用单行格式（不缩进，不换行）
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(cookies, f, indent=None, separators=(',', ':'), ensure_ascii=False)
                
                QMessageBox.information(self, "成功", "结果已保存")
                
            except Exception as e:
                QMessageBox.warning(self, "错误", f"保存文件时出错：{str(e)}")

def main():
    app = QApplication(sys.argv)
    
    # 设置应用程序样式
    app.setStyle('Fusion')
    
    # 设置全局字体
    font = QFont('Microsoft YaHei', 10)
    app.setFont(font)
    
    window = CookieExtractorGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 