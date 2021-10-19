from PyQt5.QtGui import QPixmap, QIcon, QPainter
from PyQt5.QtCore import QDateTime, Qt, QThread, QRect, QObject, QRunnable, pyqtSignal, pyqtSlot, QThreadPool
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
        QDial, QDialog, QFileDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel,
        QMainWindow, QMessageBox, QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
import sys
import os
from Strobe.strobe import strobe, strobe_image, strobe_findframes, strobe_autofindframes


class helpPopup(QWidget):
    def __init__(self, parent=None):
        super(helpPopup, self).__init__(parent)

        self.createHelpFileOpen()
        self.createHelpVideoInfo()
        self.createHelpSearchArea()
        self.createHelpAutoSelect()
        self.createHelpStrobeFrames()
        self.createHelpFrameCompare()
        self.createHelpPixelChangeOptions()
        self.createHelpCreateStrobe()

        popupLayout = QGridLayout()
        popupLayout.addWidget(self.helpFileOpenBox, 0, 0, 1, 3)
        popupLayout.addWidget(self.helpVideoInfoBox, 1, 0, 1, 3)
        popupLayout.addWidget(self.helpSearchArea, 2, 0, 1, 3)
        popupLayout.addWidget(self.helpAutoSelectBox, 3, 0, 1, 3)
        popupLayout.addWidget(self.helpStrobeFramesBox, 4, 0, 1, 3)
        popupLayout.addWidget(self.helpFrameCompareBox, 5, 0, 1, 3)
        popupLayout.addWidget(self.helpPixelChangeOptionsBox, 6, 0, 1, 3)
        popupLayout.addWidget(self.helpCreateStrobeBox, 7, 0, 1, 3)
        popupLayout.setRowStretch(1, 1)
        popupLayout.setRowStretch(2, 1)
        popupLayout.setColumnStretch(0, 1)
        popupLayout.setColumnStretch(1, 1)
        self.setLayout(popupLayout)
        self.setWindowTitle('Help')

        self.setGeometry(QRect(100, 100, 400, 200))

    def createHelpFileOpen(self):
        self.helpFileOpenBox = QGroupBox("File Open Help")

        help_label = QLabel("Select video file:\n"
                            "\tClick on the button to identify the video you want to use to create the strobe image/video.")

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpFileOpenBox.setLayout(layout)

    def createHelpVideoInfo(self):
        self.helpVideoInfoBox = QGroupBox("Video Info Help")

        help_label = QLabel("Sampling rate of original video:\n"
                            "\tWhat is the sampling rate (frames per second) of the original video?")

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpVideoInfoBox.setLayout(layout)

    def createHelpSearchArea(self):
        self.helpSearchArea = QGroupBox("Search Area Help")

        help_label = QLabel("This provides the option to select a specific area in the video frame to 'capture' the object(s) of interest.\n"
                            "The method do create the strobe image/video uses image subtraction (compares one image to another one and keeps the difference)."
                            "So this option is especially helpful when their is additional movement from frame to frame that you do not want captured in the strobe image/video.\n\n"
                            "You can select only one of the following options:\n\n"
                            "No search area:\n"
                            "\tDo not identify any specific area. Will keep all movements in the entire video frame.\n"
                            "\tThis option is best used when the object(s) of interest is the only thing(s) moving from frame to frame.\n\n"
                            "One general search area:\n"
                            "\tYou identify one specific area that will be used for all strobe frames.\n"
                            "\tThis option is best used when the object(s) of interest is the only thing(s) moving in that specified area.\n\n"
                            "Search area for each strobe frame\n"
                            "\tYou identify a specific area for EACH strobe frame.\n"
                            "\tThis option is best used when there is a lot of extra movement in the video frame that you do not want 'captured.'\n"
                            "\tThis option will create the 'cleanest' strobe image/video but also increases the manual effort time required.")

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpSearchArea.setLayout(layout)

    def createHelpAutoSelect(self):
        self.helpAutoSelectBox = QGroupBox("Auto Select Frames Help")

        help_label = QLabel("Useful to find consistent number of strobe frames with consistent spacing between two events (example, flight phase in the long jump).\n"
                            "If this is what you want, you just need to identify the first strobe frame (ex long jump take-off) and the last strobe frame (ex long jump landing) and the code will auto select a consistent number of frames in between.\n\n"
                            "Auto Frame Selection Threshold:\n"
                            "\tHow many frames need to be between two manually identified strobe frames for the code to auto select strobe frame(s)?\n"
                            "\t\tEx) You specify 5: strobe frames will be automatically identified whenever there are 5 or more frames between strobe frames you manually identified.\n\n"
                            "Auto Frame Selection Number:\n"
                            "\tHow many strobe frames do you want to automatically identify if the Auto Frame Selection Threshold is met?\n"
                            "\t\tEx) You specify 2: 2 strobe frames will be added between each pair of strobe frames you manually identified (as long as the Auto Frame Selection Threshold is met)")

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpAutoSelectBox.setLayout(layout)

    def createHelpStrobeFrames(self):
        self.helpStrobeFramesBox = QGroupBox("Strobe Frames Help")

        help_label = QLabel("Click this button to manual identify the frames you want to be 'strobed'.\n"
                            "Other frames may be added depending on the Auto Frame Selection settings.\n"
                            "All manually and any automatically identified strobe frames will be displayed next to the button.\n\n"
                            "To select the frames, a new window will popup and you will manually search through the video to identify which frame(s) you want to keep.\n"
                            "Below are the hot keys to operate the strobe frame selections:\n"
                            "\t- user can advance using the trackbar but must click button after to update\n"
                            "\t- 'k' = -100 frames\n"
                            "\t- 'm' = -10 frames\n"
                            "\t- ',' = -1 frame\n"
                            "\t- '.' = +1 frame\n"
                            "\t- '/' = +10 frames\n"
                            "\t- ';' = +100 frames\n"
                            "\t- click 'q' to select frame when identified in GUI\n"
                            "\t- click 'esc' to exit out of GUI")

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpStrobeFramesBox.setLayout(layout)

    def createHelpFrameCompare(self):
        self.helpFrameCompareBox = QGroupBox("Frame Comparison Help")

        help_label = QLabel("Sets the difference in number of frames that are used for the image subtraction technique.\n"
                            "\tEx) If the current frame number is 20, and the 'Change in frame # comparison' number is set at 5, it will compare the current frame (20) to the 5th frame later (25).\n"
                            "The faster the movement, the lower this number can be. If the object(s) of interest is not moving quickly, increase this number.\n"
                            "\tThe importance is that in order to create a 'clean' strobe image/video, there must be enough change in the image to pick up the movement.")

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpFrameCompareBox.setLayout(layout)

    def createHelpPixelChangeOptions(self):
        self.helpPixelChangeOptionsBox = QGroupBox("Pixel Change Options Help")

        help_label = QLabel("Sets the threshold that must be met in order to 'capture' the movement.\n"
                            "\tSince this app uses image subtraction, this setting will define how much change in pixel color index must occur in order for the pixel to be 'captured'.\n"
                            "The lower this number, the less 'noise' there may be but you may possibly lose some of the object(s) of interest.\n"
                            "The higher this number, the more 'noise' there may be but you will likely capture all of your object(s) of interest.\n"
                            "With good image contrast in your original video and appropriate settings (search area and frame comparison number) you should be not have to lower this number too much.")

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpPixelChangeOptionsBox.setLayout(layout)

    def createHelpCreateStrobe(self):
        self.helpCreateStrobeBox = QGroupBox("Create Strobe Help")

        help_label = QLabel("Create Strobe Image:\n"
                            "\tClicking this button will create the strobe image. You can adjust the settings and re-create the image by clicking the button again.\n"
                            "\tIt is saved in the same folder as the original video and its name is the same just with '_strobe.jpg' at the end.\n\n"
                            "Create Strobe Video:\n"
                            "\tClicking this button will create the strobe video. You can adjust the settings and re-create the video by clicking the button again.\n"
                            "\tIt is saved in the same folder as the original video and its name is the same just with '_strobe.mp4' at the end.")

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpCreateStrobeBox.setLayout(layout)


class helpPopup2(QWidget):
    def __init__(self, parent=None, groupsettings="fileopen"):
        super(helpPopup2, self).__init__(parent)

        self.groupsettings = groupsettings
        self.createHelpInfo()

        popupLayout = QGridLayout()
        popupLayout.addWidget(self.helpFileOpenBox, 0, 0, 1, 3)
        popupLayout.setRowStretch(1, 1)
        popupLayout.setColumnStretch(0, 1)
        self.setLayout(popupLayout)
        self.setWindowTitle('Help')

        self.setGeometry(QRect(200, 200, 400, 100))

    def createHelpInfo(self):
        if self.groupsettings == "fileopen":
            box_title = "File Open Help"
            box_text = ("Select video file:\n"
                        "\tClick on the button to identify the video you want to use to create the strobe image/video.")
        elif self.groupsettings == "videoinfo":
            box_title = "Video Info Help"
            box_text = ("Sampling rate of original video:\n"
                        "\tWhat is the sampling rate (frames per second) of the original video?")
        elif self.groupsettings == "searcharea":
            box_title = "Search Area Help"
            box_text = ("This provides the option to select a specific area in the video frame to 'capture' the object(s) of interest.\n"
                        "The method do create the strobe image/video uses image subtraction (compares one image to another one and keeps the difference)."
                        "So this option is especially helpful when their is additional movement from frame to frame that you do not want captured in the strobe image/video.\n\n"
                        "You can select only one of the following options:\n\n"
                        "No search area:\n"
                        "\tDo not identify any specific area. Will keep all movements in the entire video frame.\n"
                        "\tThis option is best used when the object(s) of interest is the only thing(s) moving from frame to frame.\n\n"
                        "One general search area:\n"
                        "\tYou identify one specific area that will be used for all strobe frames.\n"
                        "\tThis option is best used when the object(s) of interest is the only thing(s) moving in that specified area.\n\n"
                        "Search area for each strobe frame\n"
                        "\tYou identify a specific area for EACH strobe frame.\n"
                        "\tThis option is best used when there is a lot of extra movement in the video frame that you do not want 'captured.'\n"
                        "\tThis option will create the 'cleanest' strobe image/video but also increases the manual effort time required.")
        elif self.groupsettings == "autoselect":
            box_title = "Auto Select Frames Help"
            box_text = ("Useful to find consistent number of strobe frames with consistent spacing between two events (example, flight phase in the long jump).\n"
                        "If this is what you want, you just need to identify the first strobe frame (ex long jump take-off) and the last strobe frame (ex long jump landing) and the code will auto select a consistent number of frames in between.\n\n"
                        "Auto Frame Selection Threshold:\n"
                        "\tHow many frames need to be between two manually identified strobe frames for the code to auto select strobe frame(s)?\n"
                        "\t\tEx) You specify 5: strobe frames will be automatically identified whenever there are 5 or more frames between strobe frames you manually identified.\n\n"
                        "Auto Frame Selection Number:\n"
                        "\tHow many strobe frames do you want to automatically identify if the Auto Frame Selection Threshold is met?\n"
                        "\t\tEx) You specify 2: 2 strobe frames will be added between each pair of strobe frames you manually identified (as long as the Auto Frame Selection Threshold is met)")
        elif self.groupsettings == "strobeframes":
            box_title = "Strobe Frames Help"
            box_text = ("Click this button to manual identify the frames you want to be 'strobed'.\n"
                        "Other frames may be added depending on the Auto Frame Selection settings.\n"
                        "All manually and any automatically identified strobe frames will be displayed next to the button.\n\n"
                        "To select the frames, a new window will popup and you will manually search through the video to identify which frame(s) you want to keep.\n"
                        "Below are the hot keys to operate the strobe frame selections:\n"
                        "\t- user can advance using the trackbar but must click button after to update\n"
                        "\t- 'k' = -100 frames\n"
                        "\t- 'm' = -10 frames\n"
                        "\t- ',' = -1 frame\n"
                        "\t- '.' = +1 frame\n"
                        "\t- '/' = +10 frames\n"
                        "\t- ';' = +100 frames\n"
                        "\t- click 'q' to select frame when identified in GUI\n"
                        "\t- click 'esc' to exit out of GUI")
        elif self.groupsettings == "framecompare":
            box_title = "Frame Comparison Help"
            box_text = ("Sets the difference in number of frames that are used for the image subtraction technique.\n"
                        "\tEx) If the current frame number is 20, and the 'Change in frame # comparison' number is set at 5, it will compare the current frame (20) to the 5th frame later (25).\n"
                        "The faster the movement, the lower this number can be. If the object(s) of interest is not moving quickly, increase this number.\n"
                        "\tThe importance is that in order to create a 'clean' strobe image/video, there must be enough change in the image to pick up the movement.")
        elif self.groupsettings == "pixelchange":
            box_title = "Pixel Change Options Help"
            box_text = ("Sets the threshold that must be met in order to 'capture' the movement.\n"
                        "\tSince this app uses image subtraction, this setting will define how much change in pixel color index must occur in order for the pixel to be 'captured'.\n"
                        "The lower this number, the less 'noise' there may be but you may possibly lose some of the object(s) of interest.\n"
                        "The higher this number, the more 'noise' there may be but you will likely capture all of your object(s) of interest.\n"
                        "With good image contrast in your original video and appropriate settings (search area and frame comparison number) you should be not have to lower this number too much.")
        elif self.groupsettings == "createstrobe":
            box_title = "Create Strobe Help"
            box_text = ("These steps may take awhile! It depends on the length of your video, please be patient.\n\n"
                        "Create Strobe Image:\n"
                        "\tClicking this button will create the strobe image. You can adjust the settings and re-create the image by clicking the button again.\n"
                        "\tIt is saved in the same folder as the original video and its name is the same just with '_strobe.jpg' at the end.\n\n"
                        "Create Strobe Video:\n"
                        "\tClicking this button will create the strobe video. You can adjust the settings and re-create the video by clicking the button again.\n"
                        "\tIt is saved in the same folder as the original video and its name is the same just with '_strobe.mp4' at the end.")

        self.helpFileOpenBox = QGroupBox(box_title)

        help_label = QLabel(box_text)

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpFileOpenBox.setLayout(layout)


class aboutPopup(QWidget):
    def __init__(self, parent=None):
        super(aboutPopup, self).__init__(parent)
        self.setWindowTitle("About")
        self.createAbout()

        popupLayout = QGridLayout()
        popupLayout.addWidget(self.helpAboutBox, 0, 0, 1, 3)
        self.setLayout(popupLayout)

        self.setGeometry(QRect(200, 200, 400, 200))

    def createAbout(self):
        self.helpAboutBox = QGroupBox()

        help_label = QLabel("This app was created to allow anyone to create strobe images and videos.\n"
                            "This app works best when the camera isn't moving (similar background from frame to frame).\n\n"
                            "If you experience any issues or have any suggestions for improvements, please email me (Casey) at cwiens32@gmail.com or through Twitter at @casey_wiens. I would love to see what you create!\n\n"
                            "Last updated: \n\n")

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpAboutBox.setLayout(layout)


class errorPopup(QWidget):
    def __init__(self, label="Error"):
        super(errorPopup, self).__init__()
        self.setWindowTitle("Error")
        self.label = label
        self.createWarning()

        popupLayout = QGridLayout()
        popupLayout.addWidget(self.helpAboutBox, 0, 0, 1, 3)
        self.setLayout(popupLayout)

        self.setGeometry(QRect(200, 200, 400, 200))

    def createWarning(self):
        self.helpAboutBox = QGroupBox()

        help_label = QLabel(self.label)

        layout = QGridLayout()
        layout.addWidget(help_label, 0, 0, 1, 1)
        layout.setRowStretch(5, 1)
        self.helpAboutBox.setLayout(layout)


class PopUpProgressB(QWidget):

    def __init__(self, label):
        super().__init__()
        self.pbarlabel = QLabel(label, self)
        #self.pbar = QProgressBar(self, textVisible=False, objectName="GreenProgressBar")
        self.pbar = QProgressBar(self)
        self.pbar.setRange(0, 0)
        self.pbar.setGeometry(30, 40, 500, 75)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pbarlabel)
        self.layout.addWidget(self.pbar)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 550, 100)
        self.setWindowTitle('Progress Bar')

    def start_progress(self):
        self.show()
        self.thread.start()
        return self.show()


class strobeImageWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, image, createImagebutton, image_label, fname_og, fname_new, frames, searcharea, samp, thresh,
                 bgint, frame_thresh, frame_num):
        super().__init__()
        self.image = image
        self.createImagebutton = createImagebutton
        self.image_label = image_label
        self.fname_og = fname_og
        self.fname_new = fname_new
        self.frames = frames
        self.searcharea = searcharea
        self.samp = samp
        self.thresh = thresh
        self.bgint = bgint
        self.frame_thresh = frame_thresh
        self.frame_num = frame_num


    def run(self):
        # run strobe auto frames just in case user changed settings after first id'ing strobe frames
        bar = strobe_autofindframes(self.frames, autoid_thresh=self.frame_thresh, autoid_num=self.frame_num)
        self.frames = bar
        # run strobe image function
        strobe_image(self.fname_og, self.fname_new[:-4] + "_strobe", self.frames, searcharea=self.searcharea,
                     samp=self.samp, thresh=self.thresh, bgint=self.bgint)

        pixmap = QPixmap(self.fname_new[:-4] + "_strobe.jpg").scaledToWidth(820)
        self.image.setPixmap(pixmap)

        self.createImagebutton.setText("Recreate strobe image")

        self.image_label.setText("Here is your strobe image! It is saved where the original video is located.\n"
                                 "Either create the strobe video or modify the settings and recreate the strobe image")

        self.finished.emit()

class strobeVideoWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, image, image_label, fname_og, fname_new, frames, searcharea, samp, thresh, bgint):
        super().__init__()
        self.image = image
        self.image_label = image_label
        self.fname_og = fname_og
        self.fname_new = fname_new
        self.frames = frames
        self.searcharea = searcharea
        self.samp = samp
        self.thresh = thresh
        self.bgint = bgint

    def run(self):
        # run strobe image function
        strobe(self.fname_og, self.fname_new[:-4] + "_strobe", self.frames, searcharea=self.searcharea,
               samp=self.samp, thresh=self.thresh, bgint=self.bgint)

        pixmap = QPixmap(self.fname_new[:-4] + "_strobe.jpg").scaledToWidth(820)
        self.image.setPixmap(pixmap)

        self.image_label.setText("Your strobe video and image have been created! They are saved where the original video is located.")

        self.finished.emit()


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)
        self.setWindowTitle("Create Strobe!")
        self._createActions()
        self._createMenuBar()

        self.setGeometry(QRect(150, 150, 800, 400))

    def _createActions(self):
        # Creating action using the first constructor
        #self.newAction = QAction(self)
        #self.newAction.setText("&New")
        # Creating actions using the second constructor
        #self.openAction = QAction("&Open...", self)
        #self.saveAction = QAction("&Save", self)
        #self.exitAction = QAction("&Exit", self)
        self.helpFileOpen = QAction("&File Open", self)
        self.helpFileOpen.triggered.connect(lambda: self.help_window("fileopen"))
        self.helpVideoInfo = QAction("&Video Info", self)
        self.helpVideoInfo.triggered.connect(lambda: self.help_window("videoinfo"))
        self.helpSearchArea = QAction("&Search Area", self)
        self.helpSearchArea.triggered.connect(lambda: self.help_window("searcharea"))
        self.helpAutoSelect = QAction("&Auto Select Frames Options", self)
        self.helpAutoSelect.triggered.connect(lambda: self.help_window("autoselect"))
        self.helpStrobeFrames = QAction("&Strobe Frames", self)
        self.helpStrobeFrames.triggered.connect(lambda: self.help_window("strobeframes"))
        self.helpFrameCompare = QAction("&Frame Comparison", self)
        self.helpFrameCompare.triggered.connect(lambda: self.help_window("framecompare"))
        self.helpPixelChange = QAction("&Pixel Change Options", self)
        self.helpPixelChange.triggered.connect(lambda: self.help_window("pixelchange"))
        self.helpCreateStrobe = QAction("&Create Strobe", self)
        self.helpCreateStrobe.triggered.connect(lambda: self.help_window("createstrobe"))
        self.aboutAction = QAction("&About", self)
        self.aboutAction.triggered.connect(self.about_window)

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        #fileMenu = QMenu("&File", self)
        #fileMenu.addAction(self.newAction)
        #fileMenu.addAction(self.openAction)
        #fileMenu.addAction(self.saveAction)
        #fileMenu.addAction(self.exitAction)
        #menuBar.addMenu(fileMenu)
        helpMenu = menuBar.addMenu("&Help")
        groupsettings = helpMenu.addMenu("Group Settings Help")
        groupsettings.addAction(self.helpFileOpen)
        groupsettings.addAction(self.helpVideoInfo)
        groupsettings.addAction(self.helpSearchArea)
        groupsettings.addAction(self.helpAutoSelect)
        groupsettings.addAction(self.helpStrobeFrames)
        groupsettings.addAction(self.helpFrameCompare)
        groupsettings.addAction(self.helpPixelChange)
        groupsettings.addAction(self.helpCreateStrobe)
        helpMenu.addAction(self.aboutAction)

    def help_window(self, label):
        self.helpwindow = helpPopup2(groupsettings=label)
        self.helpwindow.show()

    def about_window(self):
        self.aboutwindow = aboutPopup()
        self.aboutwindow.show()

    def help_fileopen_window(self):
        #QMessageBox.about(self, "File Open Help", "Click on the button to verify the video you want to ad")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("File Open Help")
        msg.setInformativeText("Click on the button to identify the video you want to use to create the strobe image/video.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)

        self.popup = PopUpProgressB("none")
        self.createFileOpenGroupBox()
        self.createVideoInfoGroupBox()
        self.createSearchAreaOptionsGroupBox()
        self.createAutoSelectOptionsGroupBox()
        self.createStrobeFramesGroupBox()
        self.createFrameCompareGroupBox()
        self.createPixelThreshGroupBox()
        self.createCreateStrobeGroupBox()
        self.createImageBox()
        #self.helpwindow = helpPopup()
        #self.helpwindow.show()

        mainLayout = QGridLayout()
        # mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.fileOpenGroupBox, 0, 0, 1, 3)
        mainLayout.addWidget(self.videoInfoGroupBox, 1, 0)
        mainLayout.addWidget(self.searchAreaOptionsGroupBox, 1, 1)
        mainLayout.addWidget(self.autoSelectOptionsGroupBox, 1, 2)
        mainLayout.addWidget(self.strobeFramesGroupBox, 2, 0, 1, 3)
        mainLayout.addWidget(self.frameCompareGroupBox, 3, 0, 1, 1)
        mainLayout.addWidget(self.pixelThreshGroupBox, 3, 1, 1, 2)
        mainLayout.addWidget(self.createStrobeGroupBox, 4, 0, 1, 3)
        mainLayout.addWidget(self.imageBox, 0, 3, 5, 3)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

    def createFileOpenGroupBox(self):
        self.fileOpenGroupBox = QGroupBox("File Open")

        filebrowse = QPushButton("Select video file", self)
        filebrowse.clicked.connect(self.displayFilename)
        self.filename_label = QLabel("No video selected", self)

        folderselect = QPushButton("Select a directory to save to")
        folderselect.clicked.connect(self.displayFoldername)
        self.foldersave_label = QLabel("", self)

        layout = QGridLayout()
        layout.addWidget(filebrowse, 0, 0, 1, 1)
        layout.addWidget(self.filename_label, 0, 1, 1, 2)
        layout.addWidget(folderselect, 1, 0, 1, 1)
        layout.addWidget(self.foldersave_label, 1, 1, 1, 2)
        self.fileOpenGroupBox.setLayout(layout)

    def displayFilename(self):

        self.filename = QFileDialog.getOpenFileName(self, 'Select original file')
        self.filename_label.setText('Video selected: ' + self.filename[0])
        self.foldersave = os.path.dirname(self.filename[0])
        self.foldersave_label.setText('Saving to: ' + self.foldersave)

    def displayFoldername(self):

        self.foldersave = QFileDialog.getExistingDirectory(self, 'Select directory to save to')
        self.foldersave_label.setText('Saving to: ' + self.foldersave)

    def createVideoInfoGroupBox(self):
        self.videoInfoGroupBox = QGroupBox("Video Info")

        samp_og_vid_label = QLabel("Sampling rate of original video:")

        self.samp_og_vid = QSpinBox(self.videoInfoGroupBox)
        self.samp_og_vid.setMinimum(1)
        self.samp_og_vid.setMaximum(5000)
        self.samp_og_vid.setValue(240)

        #samp_new_vid_label = QLabel("Sampling rate of new video:")

        #self.samp_new_vid = QSpinBox(self.videoInfoGroupBox)
        #self.samp_new_vid.setMinimum(1)
        #self.samp_new_vid.setMaximum(5000)
        #self.samp_new_vid.setValue(240)

        layout = QGridLayout()
        layout.addWidget(samp_og_vid_label, 0, 0, 1, 1)
        layout.addWidget(self.samp_og_vid, 0, 1, 1, 2)
        #layout.addWidget(samp_new_vid_label, 1, 0, 1, 1)
        #layout.addWidget(self.samp_new_vid, 1, 1, 1, 2)
        layout.setRowStretch(5, 1)
        self.videoInfoGroupBox.setLayout(layout)

    def createSearchAreaOptionsGroupBox(self):
        self.searchAreaOptionsGroupBox = QGroupBox("Search Area Options")

        crop_label = QLabel("Do you want to select specific\narea to find object?")

        self.search_no = QRadioButton("No search area")
        self.search_one = QRadioButton("One general search area")
        self.search_all = QRadioButton("Search area for each strobe frame")
        self.search_no.setChecked(True)

        layout = QGridLayout()
        layout.addWidget(crop_label, 1, 0, 2, 1)
        layout.addWidget(self.search_no)
        layout.addWidget(self.search_one)
        layout.addWidget(self.search_all)
        self.searchAreaOptionsGroupBox.setLayout(layout)

    def createAutoSelectOptionsGroupBox(self):
        self.autoSelectOptionsGroupBox = QGroupBox("Auto Select Frames Options")

        auto_thresh_label = QLabel("Auto frame selection threshold:")

        self.auto_thresh = QSpinBox(self.autoSelectOptionsGroupBox)
        self.auto_thresh.setMinimum(0)
        self.auto_thresh.setMaximum(500)
        self.auto_thresh.setValue(0)

        auto_num_thresh = QLabel("Auto frame selection number:")

        self.auto_num = QSpinBox(self.autoSelectOptionsGroupBox)
        self.auto_num.setMinimum(0)
        self.auto_num.setMaximum(200)
        self.auto_num.setValue(0)

        layout = QGridLayout()
        layout.addWidget(auto_thresh_label, 0, 0, 1, 1)
        layout.addWidget(self.auto_thresh, 0, 1, 1, 2)
        layout.addWidget(auto_num_thresh, 1, 0, 1, 1)
        layout.addWidget(self.auto_num, 1, 1, 1, 2)
        layout.setRowStretch(5, 1)
        self.autoSelectOptionsGroupBox.setLayout(layout)

    def createStrobeFramesGroupBox(self):
        self.strobeFramesGroupBox = QGroupBox("Strobe Frames")

        self.strobebutton = QPushButton("Select strobe frames", self)
        self.strobebutton.clicked.connect(self.selectStrobeFrames)
        self.strobe_label = QLabel("No strobe frames selected", self)

        layout = QGridLayout()
        layout.addWidget(self.strobebutton, 0, 0, 1, 1)
        layout.addWidget(self.strobe_label, 0, 1, 1, 2)
        self.strobeFramesGroupBox.setLayout(layout)

    def selectStrobeFrames(self):

        try:
            if self.search_no.isChecked():
                crop = None
            elif self.search_one.isChecked():
                crop = "one"
            elif self.search_all.isChecked():
                crop = "all"

            if self.auto_thresh.value() == 0:
                autoid_thresh = None
            else:
                autoid_thresh = self.auto_thresh.value()

            self.hide()
            self.frames, self.searcharea = strobe_findframes(self.filename[0], crop=crop,
                                                             autoid_thresh=autoid_thresh,
                                                             autoid_num=self.auto_num.value()+2)
            self.show()

            self.strobe_label.setText(
                'Selected strobe frames: ' + ", ".join([str(element) for element in self.frames.to_list()]))
            self.strobe_label.setWordWrap(True)
            self.strobebutton.setText('Clear and reselect strobe frames')
        except AttributeError:
            self.show()
            self.error_window("<b>Cannot identify strobe frames!</b><br><br>"
                              "Please select video file first before trying to select the strobe frames.")


    def createFrameCompareGroupBox(self):
        self.frameCompareGroupBox = QGroupBox("Frame Comparison")

        frame_comp_label = QLabel("Change in frame # comparison:")

        self.frame_comp = QSpinBox(self.frameCompareGroupBox)
        self.frame_comp.setMinimum(1)
        self.frame_comp.setMaximum(100)
        self.frame_comp.setValue(5)

        layout = QGridLayout()
        layout.addWidget(frame_comp_label, 0, 0, 1, 1)
        layout.addWidget(self.frame_comp, 0, 1, 1, 2)
        layout.setRowStretch(5, 1)
        self.frameCompareGroupBox.setLayout(layout)


    def createPixelThreshGroupBox(self):
        self.pixelThreshGroupBox = QGroupBox("Pixel Change Options")

        auto_thresh_label = QLabel(
            "Set the threshold for how much the pixel color value needs to change to keep in image\n"
            "(If too much noise is in the image, raise the threshold value.):")

        self.slider = QSlider(Qt.Horizontal, self.pixelThreshGroupBox)
        self.slider.setValue(60)

        self.slider_label = QLabel("Threshold Value: ", self)
        self.slider_label.setAlignment(Qt.AlignCenter)

        self.slider.valueChanged.connect(self.changeValue)

        # making label multiline
        self.slider_label.setWordWrap(True)

        # setting text to the label
        self.slider_label.setText("Value : " + str(self.slider.value()))

        layout = QGridLayout()
        layout.addWidget(auto_thresh_label, 0, 0, 1, 1)
        layout.addWidget(self.slider_label, 1, 0, 1, 2)
        layout.addWidget(self.slider, 2, 0, 1, 2)
        layout.setRowStretch(5, 1)
        self.pixelThreshGroupBox.setLayout(layout)

    def changeValue(self, value):

        self.slider_label.setText("Value : " + str(value))

    def createCreateStrobeGroupBox(self):
        self.createStrobeGroupBox = QGroupBox("Create strobe")

        self.createImagebutton = QPushButton("Create strobe image", self)
        self.createImagebutton.clicked.connect(lambda: self.showProgressWindow("Please wait, your strobe image is being created..."))
        self.createImagebutton.clicked.connect(self.createStrobeImage)

        saveVideobutton = QPushButton("Save strobe video", self)
        saveVideobutton.clicked.connect(lambda: self.showProgressWindow("Please wait, your strobe video is being created..."))
        saveVideobutton.clicked.connect(self.saveStrobeVideo)

        layout = QGridLayout()
        layout.addWidget(self.createImagebutton, 0, 0, 1, 1)
        layout.addWidget(saveVideobutton, 0, 1, 1, 1)
        self.createStrobeGroupBox.setLayout(layout)

    def createStrobeImage(self):

        if hasattr(self, 'filename') and hasattr(self, 'frames'):
            self.thread_si = QThread()
            self.worker_si = strobeImageWorker(self.image, self.createImagebutton, self.image_label, self.filename[0],
                                               os.path.join(self.foldersave, os.path.split(self.filename[0])[1]),
                                               self.frames, self.searcharea, self.samp_og_vid.value(),
                                               self.slider.value(), self.frame_comp.value(),
                                               self.auto_thresh.value(), self.auto_num.value()+2)
            self.worker_si.moveToThread(self.thread_si)
            self.thread_si.started.connect(self.worker_si.run)
            self.worker_si.finished.connect(self.thread_si.quit)
            self.worker_si.finished.connect(self.popup.close)
            self.worker_si.finished.connect(self.worker_si.deleteLater)
            self.thread_si.finished.connect(self.thread_si.deleteLater)
            self.thread_si.start()
        elif hasattr(self, 'filename'):
            self.popup.close()
            self.error_window("<b>Cannot create the strobe image!</b><br><br>"
                              "Please select the strobe frames first before trying to create the image.")
        else:
            self.popup.close()
            self.error_window("<b>Cannot identify strobe image!</b><br><br>"
                              "Please select the video file first and then the strobe frames before trying to create the image.")

    def saveStrobeVideo(self):

        if hasattr(self, 'filename') and hasattr(self, 'frames'):
            self.thread_sv = QThread()
            self.worker_sv = strobeVideoWorker(self.image, self.image_label, self.filename[0],
                                               os.path.join(self.foldersave, os.path.split(self.filename[0])[1]),
                                               self.frames, self.searcharea, self.samp_og_vid.value(),
                                               self.slider.value(), self.frame_comp.value())
            self.worker_sv.moveToThread(self.thread_sv)
            self.thread_sv.started.connect(self.worker_sv.run)
            self.worker_sv.finished.connect(self.thread_sv.quit)
            self.worker_sv.finished.connect(self.popup.close)
            self.worker_sv.finished.connect(self.worker_sv.deleteLater)
            self.thread_sv.finished.connect(self.thread_sv.deleteLater)
            self.thread_sv.start()
        else:
            self.popup.close()
            self.error_window("<b>Cannot identify strobe video!</b><br><br>"
                              "Please select the video file first and then the strobe frames before trying to create the video.")

    def createImageBox(self):
        self.imageBox = QGroupBox("Display strobe image")

        self.image_label = QLabel(self)
        self.image_label.setText(
            "Please see the Help menu for more instructions.\n\n"
            "Please select your video, strobe frames, and verify the settings, then create strobe image.")

        self.image = QLabel(self)

        layout = QGridLayout()
        layout.addWidget(self.image_label, 0, 0, 1, 2)
        layout.addWidget(self.image, 1, 0, 1, 1)
        self.imageBox.setLayout(layout)

    def showProgressWindow(self, label):
        self.popup = PopUpProgressB(label)
        self.popup.start_progress
        self.popup.show()

    def error_window(self, label):
        #QMessageBox.about(self, "File Open Help", "Click on the button to verify the video you want to ad")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error!")
        msg.setText(label)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def error_windowOLD(self, label):
        self.errorwindow = errorPopup(label)
        self.errorwindow.show()


print("Loading...this may take a few minutes...")
app = QApplication([])
app.setStyleSheet("QGroupBox{font-size: 12pt;} QLabel{font-size: 10pt;} QPushButton{font-size: 10pt;}"
                  "QSpinBox{font-size: 10pt;} QRadioButton{font-size: 10pt;}")
foo = MyMainWindow()
foo.show()
sys.exit(app.exec_())