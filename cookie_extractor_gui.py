import sys
import json
from pathlib import Path
from typing import List, Dict, Any
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLineEdit, QLabel, 
                             QTableWidget, QTableWidgetItem, QFileDialog, 
                             QMessageBox, QTextEdit, QHeaderView, QFrame,
                             QSizePolicy)
from PySide6.QtCore import Qt, QMimeData, QSize
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QFont, QPalette, QColor

class StyledButton(QPushButton):
    """自定义样式按钮"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(40)
        self.setFont(QFont('Microsoft YaHei', 10))
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: #3F51B5;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #303F9F;
            }
            QPushButton:pressed {
                background-color: #1A237E;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
            }
        """)

class StyledLineEdit(QLineEdit):
    """自定义样式输入框"""
    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setMinimumHeight(40)
        self.setFont(QFont('Microsoft YaHei', 10))
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid #E0E0E0;
                border-radius: 4px;
                padding: 8px 12px;
                background-color: white;
                color: #333333;
            }
            QLineEdit:focus {
                border: 2px solid #3F51B5;
            }
            QLineEdit::placeholder {
                color: #9E9E9E;
            }
        """)

class StyledTextEdit(QTextEdit):
    """自定义样式文本编辑框"""
    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setFont(QFont('Microsoft YaHei', 10))
        self.setStyleSheet("""
            QTextEdit {
                border: 2px solid #E0E0E0;
                border-radius: 4px;
                padding: 8px;
                background-color: white;
                color: #333333;
            }
            QTextEdit:focus {
                border: 2px solid #3F51B5;
            }
            QTextEdit::placeholder {
                color: #9E9E9E;
            }
        """)

class StyledTable(QTableWidget):
    """自定义样式表格"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont('Microsoft YaHei', 10))
        self.setStyleSheet("""
            QTableWidget {
                border: 2px solid #E0E0E0;
                border-radius: 4px;
                background-color: white;
                gridline-color: #F5F5F5;
                color: #333333;
            }
            QHeaderView::section {
                background-color: #F5F5F5;
                padding: 8px;
                border: none;
                font-weight: bold;
                color: #333333;
                border-bottom: 1px solid #E0E0E0;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #F5F5F5;
            }
            QTableWidget::item:selected {
                background-color: #E8EAF6;
                color: #3F51B5;
            }
        """)
        self.setShowGrid(True)
        self.setGridStyle(Qt.SolidLine)
        self.setAlternatingRowColors(True)
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.horizontalHeader().setStretchLastSection(True)
        self.setEditTriggers(QTableWidget.NoEditTriggers)

class CookieExtractorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cookies: List[Dict[str, Any]] = []
        self.initUI()
        
    def initUI(self):
        """初始化UI界面"""
        self.setWindowTitle('Cookie信息提取器')
        self.setMinimumSize(1000, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F5F5;
            }
            QLabel {
                color: #333333;
                font-weight: 500;
            }
            QFrame {
                background-color: white;
                border-radius: 8px;
                border: 1px solid #E0E0E0;
            }
        """)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)
        
        # 标题
        title_label = QLabel('Cookie信息提取器')
        title_label.setFont(QFont('Microsoft YaHei', 20, QFont.Bold))
        title_label.setStyleSheet('color: #3F51B5; margin-bottom: 16px;')
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 文件导入区域
        import_frame = QFrame()
        import_layout = QHBoxLayout(import_frame)
        import_layout.setContentsMargins(16, 16, 16, 16)
        import_layout.setSpacing(12)
        
        import_label = QLabel('文件导入：')
        import_label.setFont(QFont('Microsoft YaHei', 10, QFont.Bold))
        import_label.setStyleSheet('color: #333333;')
        
        self.file_path_label = QLabel('未选择文件')
        self.file_path_label.setFont(QFont('Microsoft YaHei', 10))
        self.file_path_label.setStyleSheet('color: #666666;')
        self.file_path_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        
        import_btn = StyledButton('选择文件')
        import_btn.setFixedWidth(120)
        import_btn.clicked.connect(self.import_file)
        
        import_layout.addWidget(import_label)
        import_layout.addWidget(self.file_path_label)
        import_layout.addWidget(import_btn)
        
        # Cookie文本输入区域
        text_frame = QFrame()
        text_layout = QVBoxLayout(text_frame)
        text_layout.setContentsMargins(16, 16, 16, 16)
        text_layout.setSpacing(8)
        
        text_label = QLabel('Cookie文本')
        text_label.setFont(QFont('Microsoft YaHei', 10, QFont.Bold))
        text_label.setStyleSheet('color: #333333;')
        
        self.cookie_text = StyledTextEdit('在此粘贴Cookie文本或拖放文件...')
        self.cookie_text.setAcceptDrops(True)
        self.cookie_text.dragEnterEvent = self.dragEnterEvent
        self.cookie_text.dropEvent = self.dropEvent
        self.cookie_text.setMinimumHeight(120)
        
        text_layout.addWidget(text_label)
        text_layout.addWidget(self.cookie_text)
        
        # 域名匹配区域
        match_frame = QFrame()
        match_layout = QHBoxLayout(match_frame)
        match_layout.setContentsMargins(16, 16, 16, 16)
        match_layout.setSpacing(12)
        
        domain_label = QLabel('域名匹配：')
        domain_label.setFont(QFont('Microsoft YaHei', 10, QFont.Bold))
        domain_label.setStyleSheet('color: #333333;')
        
        self.domain_input = StyledLineEdit('输入要匹配的域名（例如：twitter）')
        match_btn = StyledButton('提取Cookie')
        match_btn.setFixedWidth(120)
        match_btn.clicked.connect(self.extract_cookies)
        
        match_layout.addWidget(domain_label)
        match_layout.addWidget(self.domain_input)
        match_layout.addWidget(match_btn)
        
        # 结果显示区域
        result_frame = QFrame()
        result_layout = QVBoxLayout(result_frame)
        result_layout.setContentsMargins(16, 16, 16, 16)
        result_layout.setSpacing(8)
        
        result_label = QLabel('匹配结果')
        result_label.setFont(QFont('Microsoft YaHei', 10, QFont.Bold))
        result_label.setStyleSheet('color: #333333;')
        
        self.result_table = StyledTable()
        self.result_table.setColumnCount(9)
        self.result_table.setHorizontalHeaderLabels([
            '域名', '名称', '值', '过期时间', 'HttpOnly', 
            'Path', 'SameSite', 'Secure', 'ID'
        ])
        
        # 设置表格列宽自适应
        header = self.result_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        result_layout.addWidget(result_label)
        result_layout.addWidget(self.result_table)
        
        # 保存按钮
        save_btn = StyledButton('保存结果')
        save_btn.setFixedWidth(200)
        save_btn.clicked.connect(self.save_results)
        
        # 保存按钮容器（用于居中显示）
        save_container = QWidget()
        save_layout = QHBoxLayout(save_container)
        save_layout.addStretch()
        save_layout.addWidget(save_btn)
        save_layout.addStretch()
        
        # 添加所有组件到主布局
        layout.addWidget(import_frame)
        layout.addWidget(text_frame)
        layout.addWidget(match_frame)
        layout.addWidget(result_frame)
        layout.addWidget(save_container)
        
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
        
        for row, cookie in enumerate(cookies):
            self.result_table.setItem(row, 0, QTableWidgetItem(str(cookie.get('domain', ''))))
            self.result_table.setItem(row, 1, QTableWidgetItem(str(cookie.get('name', ''))))
            self.result_table.setItem(row, 2, QTableWidgetItem(str(cookie.get('value', ''))))
            self.result_table.setItem(row, 3, QTableWidgetItem(str(cookie.get('expirationDate', ''))))
            self.result_table.setItem(row, 4, QTableWidgetItem(str(cookie.get('httpOnly', ''))))
            self.result_table.setItem(row, 5, QTableWidgetItem(str(cookie.get('path', ''))))
            self.result_table.setItem(row, 6, QTableWidgetItem(str(cookie.get('sameSite', ''))))
            self.result_table.setItem(row, 7, QTableWidgetItem(str(cookie.get('secure', ''))))
            self.result_table.setItem(row, 8, QTableWidgetItem(str(cookie.get('id', ''))))
        
        self.result_table.resizeColumnsToContents()
    
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
                # 从表格中获取数据
                cookies = []
                for row in range(self.result_table.rowCount()):
                    cookie = {
                        'domain': self.result_table.item(row, 0).text(),
                        'name': self.result_table.item(row, 1).text(),
                        'value': self.result_table.item(row, 2).text(),
                        'expirationDate': float(self.result_table.item(row, 3).text() or 0),
                        'httpOnly': self.result_table.item(row, 4).text().lower() == 'true',
                        'path': self.result_table.item(row, 5).text(),
                        'sameSite': self.result_table.item(row, 6).text(),
                        'secure': self.result_table.item(row, 7).text().lower() == 'true',
                        'id': int(self.result_table.item(row, 8).text() or 0)
                    }
                    cookies.append(cookie)
                
                # 保存到文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(cookies, f, indent=2, ensure_ascii=False)
                
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