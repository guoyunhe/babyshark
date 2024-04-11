import asyncio
from ffmpeg.asyncio import FFmpeg
from ffmpeg import Progress
import os
from PySide6.QtCore import QStandardPaths, Signal, Slot
from PySide6.QtGui import Qt, QIcon, QPixmap, QTransform
from PySide6.QtWidgets import (
    QMessageBox,
    QFileDialog,
    QLabel,
    QMainWindow,
    QProgressBar,
    QToolBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
from gettext import gettext as _
import traceback
from app.thumbnail import generate_thumbnail


class MainWindow(QMainWindow):
    start_signal = Signal()
    video_filter = _('Video Files (*.avi *.mkv *.mp4 *.webm)')

    def __init__(self,  parent: QWidget = None):
        super().__init__(parent)

        self.setWindowTitle(_('Rotate Video'))

        toolbar = QToolBar(self)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        open_video_button = QToolButton(self)
        open_video_button.setText(_('&Open video...'))
        open_video_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        open_video_button.setIcon(QIcon.fromTheme('document-open'))
        open_video_button.clicked.connect(self.open_file)
        toolbar.addWidget(open_video_button)

        toolbar.addSeparator()

        rotate_left_button = QToolButton(self)
        rotate_left_button.setText(_('Rotate &left'))
        rotate_left_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        rotate_left_button.setIcon(QIcon.fromTheme('object-rotate-left'))
        rotate_left_button.clicked.connect(self.rotate_left)
        toolbar.addWidget(rotate_left_button)

        rotate_right_button = QToolButton(self)
        rotate_right_button.setText(_('Rotate &right'))
        rotate_right_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        rotate_right_button.setIcon(QIcon.fromTheme('object-rotate-right'))
        rotate_right_button.clicked.connect(self.rotate_right)
        toolbar.addWidget(rotate_right_button)

        toolbar.addSeparator()

        save_button = QToolButton(self)
        save_button.setText(_('&Save'))
        save_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        save_button.setIcon(QIcon.fromTheme('document-save'))
        save_button.clicked.connect(self.save)
        toolbar.addWidget(save_button)

        saveas_button = QToolButton(self)
        saveas_button.setText(_('Save &as...'))
        saveas_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        saveas_button.setIcon(QIcon.fromTheme('document-save-as'))
        saveas_button.clicked.connect(self.saveas)
        toolbar.addWidget(saveas_button)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        self.thumbnail_viewer = QLabel(self)
        self.thumbnail_viewer.setMinimumHeight(300)
        self.thumbnail_pixmap = QPixmap()
        main_layout.addWidget(self.thumbnail_viewer)

        progress_bar = QProgressBar(self)
        progress_bar.setValue(20)
        main_layout.addWidget(progress_bar)

        self.rotate_degree = 0

    @Slot()
    def open_file(self):
        video, pattern = QFileDialog.getOpenFileName(
            self,
            _('Open video'),
            QStandardPaths.standardLocations(QStandardPaths.HomeLocation)[0],
            self.video_filter
        )
        if (not video):
            return
        self.input_filename = video
        try:
            thumbnail_filename = generate_thumbnail(video)
            self.thumbnail_pixmap.load(thumbnail_filename)
            self.rotate_degree = 0
            self.render_thumbnail()
        except:
            QMessageBox.critical(
                self,
                _('Failed to open video file'),
                _('Please make sure the video file is playable and accessible.')
            )

    @Slot()
    def rotate_left(self):
        self.rotate_degree -= 90
        if (self.rotate_degree < 0):
            self.rotate_degree += 360
        self.render_thumbnail()

    @Slot()
    def rotate_right(self):
        self.rotate_degree += 90
        if (self.rotate_degree >= 360):
            self.rotate_degree -= 360
        self.render_thumbnail()

    def render_thumbnail(self):
        trans = QTransform()
        trans.rotate(self.rotate_degree)
        transformed = self.thumbnail_pixmap.transformed(trans)
        transformed = transformed.scaled(
            self.thumbnail_viewer.size(),
            Qt.AspectRatioMode.KeepAspectRatio
        )
        self.thumbnail_viewer.setPixmap(
            transformed
        )

    @Slot()
    def save(self):
        self.output_filename = self.input_filename + '~'
        self.async_start()

    @Slot()
    def saveas(self):
        video, pattern = QFileDialog.getSaveFileName(
            self,
            _('Save video as...'),
            os.path.dirname(self.input_filename),
            self.video_filter
        )
        self.output_filename = video
        self.async_start()

    @Slot()
    def async_start(self):
        self.start_signal.emit()

    async def convert(self):
        print('convert')
        print(self.input_filename)
        print(self.output_filename)
        vf = ''
        if self.rotate_degree == 90:
            vf = 'transpose=1'
        elif self.rotate_degree == 180:
            vf = 'transpose=1,transpose=1'
        elif self.rotate_degree == 270:
            vf = 'transpose=2'

        ffmpeg = (
            FFmpeg()
            .option('y')
            .input(self.input_filename)
            .output(
                self.output_filename
            )
        )

        @ffmpeg.on("progress")
        def on_progress(progress: Progress):
            print(progress)

        try:
            print('start')
            await ffmpeg.execute()
            print('done')
        except Exception:
            print(traceback.format_exc())