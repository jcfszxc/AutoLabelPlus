from PyQt5 import QtWidgets, QtCore
from ui_main import Ui_autoLabel  # 导入UI类
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # 创建UI对象
        self.ui = Ui_autoLabel()
        # 设置UI
        self.ui.setupUi(self)

        # 方法1：获取屏幕尺寸并设置窗口大小为屏幕的一定比例
        screen = QtWidgets.QApplication.primaryScreen().size()
        # 设置窗口大小为屏幕的80%
        self.resize(int(screen.width() * 0.8), int(screen.height() * 0.8))

        # 方法2：将窗口居中显示
        self.center_window()
        
        # 方法3：设置最小尺寸，防止窗口被缩放得太小
        self.setMinimumSize(400, 300)

        # 连接按钮点击信号到槽函数
        self.ui.pushButtonOpenDir.clicked.connect(self.open_directory)
        self.ui.pushButtonNextImage.clicked.connect(self.next_image)
        self.ui.pushButtonPrevImage.clicked.connect(self.previous_image)
        
        # 存储当前选择的目录路径
        self.current_directory = None
        self.current_image_index = -1
        
        # 在这里可以添加其他初始化代码

    def center_window(self):
        """将窗口移动到屏幕中央"""
        # 获取屏幕几何信息
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        # 获取窗口几何信息
        size = self.geometry()
        # 计算居中位置
        new_left = (screen.width() - size.width()) // 2
        new_top = (screen.height() - size.height()) // 2
        # 移动窗口
        self.move(new_left, new_top)


    def open_directory(self):
        """打开文件夹选择对话框并显示第一张图片"""
        # 打开文件夹对话框，如果已经有选择过的目录，就从那个目录开始，否则从当前目录开始
        start_dir = self.current_directory if self.current_directory else "./"
        directory = QFileDialog.getExistingDirectory(
            self,
            "选择文件夹",
            start_dir,
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )

        # 如果用户选择了文件夹（没有点击取消）
        if directory:
            self.current_directory = directory
            print(f"选择的文件夹路径: {directory}")
            
            # 定义支持的图片格式
            image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
            
            # 递归获取目录下所有图片文件
            def find_images(folder):
                image_files = []
                for item in os.listdir(folder):
                    item_path = os.path.join(folder, item)
                    if os.path.isfile(item_path):
                        if item.lower().endswith(image_extensions):
                            image_files.append(item_path)
                    elif os.path.isdir(item_path):
                        # 递归搜索子文件夹
                        image_files.extend(find_images(item_path))
                return sorted(image_files)  # 对文件列表进行排序
            
            # 调用递归函数获取所有图片
            self.image_files = find_images(directory)
                    
            # 如果找到了图片文件
            if self.image_files:
                # 设置当前索引为0并显示第一张图片
                self.current_image_index = 0
                self.display_current_image()
                # 更新按钮状态
                self.update_navigation_buttons()
            else:
                print("未在选择的目录中找到图片文件")

    def display_current_image(self):
        """显示当前索引对应的图片"""
        if 0 <= self.current_image_index < len(self.image_files):
            current_image = self.image_files[self.current_image_index]
            print(f"显示图片: {current_image}")
            
            # 创建QGraphicsScene
            scene = QGraphicsScene()
            
            # 加载图片
            pixmap = QPixmap(current_image)
            
            # 根据GraphicsView的大小调整图片大小
            view_size = self.ui.graphicsView.size()
            scaled_pixmap = pixmap.scaled(
                view_size,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            
            # 将图片添加到场景中
            scene.addPixmap(scaled_pixmap)
            
            # 设置场景到GraphicsView
            self.ui.graphicsView.setScene(scene)
            
            # 调整视图以显示整个场景
            self.ui.graphicsView.fitInView(
                scene.sceneRect(),
                Qt.KeepAspectRatio
            )

    def next_image(self):
        """切换到下一张图片"""
        if self.current_image_index < len(self.image_files) - 1:
            self.current_image_index += 1
            self.display_current_image()
            self.update_navigation_buttons()

    def previous_image(self):
        """切换到上一张图片"""
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.display_current_image()
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        """更新导航按钮的启用状态"""
        # 当没有上一张图片时禁用上一张按钮
        self.ui.pushButtonPrevImage.setEnabled(self.current_image_index > 0)
        # 当没有下一张图片时禁用下一张按钮
        self.ui.pushButtonNextImage.setEnabled(
            self.current_image_index < len(self.image_files) - 1
        )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # 获取屏幕的DPI信息并设置
    screen = app.primaryScreen()
    dpi = screen.physicalDotsPerInch()
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 启用高DPI缩放
    app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)    # 使用高DPI图标
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())