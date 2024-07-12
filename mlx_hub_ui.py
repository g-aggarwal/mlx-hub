import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QTabWidget, QLabel, QStackedWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from mlx_hub import suggest, scan, download, delete

class WorkerThread(QThread):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    repo_id = None
    operation = None

    def run(self):
        try:
            if self.operation == 'download':
                if download(self.repo_id):
                    self.finished.emit()
                else:
                    self.error.emit(f"Failed to download {self.repo_id}")
            elif self.operation == 'delete':
                if delete(self.repo_id):
                    self.finished.emit()
                else:
                    self.error.emit(f"Failed to delete {self.repo_id}")
        except Exception as e:
            self.error.emit(str(e))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MLX Manager')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.suggestedTab = QWidget()
        self.installedTab = QWidget()

        self.tabs.addTab(self.suggestedTab, "Suggested")
        self.tabs.addTab(self.installedTab, "Installed")

        self.initSuggestedTab()
        self.initInstalledTab()

        layout.addWidget(self.tabs)

        self.setLayout(layout)

        self.workerThread = WorkerThread()
        self.workerThread.finished.connect(self.onOperationFinished)
        self.workerThread.error.connect(self.onOperationError)

    def initSuggestedTab(self):
        layout = QVBoxLayout()

        self.suggestedList = QListWidget()
        self.suggestedList.itemClicked.connect(self.download_model)
        layout.addWidget(self.suggestedList)

        self.suggestedTab.setLayout(layout)
        self.loadSuggestedModels()

    def initInstalledTab(self):
        layout = QVBoxLayout()

        self.installedList = QListWidget()
        self.installedList.itemClicked.connect(self.delete_model)
        layout.addWidget(self.installedList)

        self.installedTab.setLayout(layout)
        self.loadInstalledModels()

    def loadSuggestedModels(self):
        self.suggestedList.clear()
        suggested_models = suggest()
        installed_models = [repo.repo_id for repo in scan()]
        for model in suggested_models:
            if model not in installed_models:
                self.suggestedList.addItem(model)

    def loadInstalledModels(self):
        self.installedList.clear()
        installed_models = [repo.repo_id for repo in scan()]
        for model in installed_models:
            self.installedList.addItem(model)

    def download_model(self, item):
        self.setLoadingView(self.suggestedTab)
        self.workerThread.repo_id = item.text()
        self.workerThread.operation = 'download'
        self.workerThread.start()

    def delete_model(self, item):
        self.setLoadingView(self.installedTab)
        self.workerThread.repo_id = item.text()
        self.workerThread.operation = 'delete'
        self.workerThread.start()

    def onOperationFinished(self):
        self.loadSuggestedModels()
        self.loadInstalledModels()
        self.unsetLoadingView()

    def onOperationError(self, message):
        self.unsetLoadingView()
        print(message)  # You can replace this with a message box to show the error to the user

    def setLoadingView(self, tab):
        layout = tab.layout()
        self.stackedWidget = QStackedWidget()
        self.loadingLabel = QLabel("Loading...", alignment=Qt.AlignCenter)
        self.stackedWidget.addWidget(self.loadingLabel)
        self.stackedWidget.addWidget(layout.itemAt(0).widget())
        layout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)

    def unsetLoadingView(self):
        self.stackedWidget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())