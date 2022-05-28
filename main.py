################################################################################
##
## BY: NARENDAR REDDY G
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

# GUI FILE
import ctypes
import json
import logging.config
import logging
import logging.handlers
from logging.handlers import SysLogHandler
import shutil
import sys
import datetime

import getpass
from os.path import exists

import requests
import yaml
from PySide2 import QtWidgets, QtGui, QtWebSockets, QtCharts, QtCore
from PySide2.QtCore import QTimer, QSize, Qt, QUrl, Slot, QCoreApplication
from PySide2.QtGui import QIcon, QPen, QPainter, QBrush
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QMessageBox, QApplication, QMainWindow
from win10toast import ToastNotifier

import api
from _globals import *
from app_modules import *
from src.Notifications.system_tray import SystemTrayIcon
from src.Shots.Shots_Ingestion import Shots_Ingestion
from src.Shots.task_help_main_table import TaskHelp_Main
from src.Stats.employee_stats import Employee_Stats
from src.Users.user_table import All_Users
from src.change_pwd import ChangePassword
from src.custom_checkbox import CustomComboBox
from src.filters_panel import Filters_Panel_Modal
from src.reports.studio_report import Studio_Reports
from uipy.change_password import Ui_CP_MainWindow
from uipy.change_password_modal import Ui_CP_Dialog
from uipy.login_window import Ui_Form
from uipy.main_window import Ui_MainWindow
from src.Clients.clients import Clients
from src.Projects.projects import Projects
from src.MyTask.my_task import My_Task
from src.Notifications.notifications import popup
from src.Shots.all_shots_table import All_Shots

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.login_ui = Ui_Form()
        self.login_ui.setupUi(self)
        # TODO: Change version before production build
        # self.login_ui.ver_lbl.setText("V15.5267")
        self.login_ui.password_le.returnPressed.connect(lambda: self.LoginClicked())
        # self.login_ui.password_le.installEventFilter(self)
        self.login_ui.login_btn.clicked.connect(lambda: self.LoginClicked())

        #TODO: Enable this code block before deploying to production to display login window
        self.show()

        # #  ##TODO: Comment this code block before deploying to production
        url = "{}{}/api/auth/".format(api.config['API']['hostname'], api.config['API']['port'])
        supervisor = {
            'username': 'supervisor',
            'password': 'ofx@12345'
        }
        teamlead = {
            'username': 'teamlead1',
            'password': 'ofx@12345'
        }
        qc = {
            'username': 'qc1',
            'password': 'ofx@12345'
        }
        manager = {
            'username': 'manager',
            'password': 'ofx@12345'
        }
        artist = {
            'username': 'artist1',
            'password': 'ofx@12345'
        }
        dataio = {
            'username': 'dataio',
            'password': 'ofx@12345'
        }
        user_data = {
            'username': 'ganeshbabu.g',
            'password': 'Ofx@1234'
        }
        my_data = {
            'username': 'admin',
            'password': 'Tomato@123'
        }
        response = requests.post(url, data=supervisor, verify=False)
        # MainWindow(response.json())

    @Slot()
    def LoginClicked(self):
        userName = self.login_ui.username_le.text()
        ##TODO: Enable below before deploying to Production
        # userName = getpass.getuser()
        passWord = self.login_ui.password_le.text()
        url = "{}{}/api/auth/".format(api.config['API']['hostname'], api.config['API']['port'])
        data = {
            'username': userName,
            'password': passWord
        }
        response = requests.post(url, data=data, verify=False)
        if response.status_code == 400:
            msg = QMessageBox()
            msg.setText("Wrong Password \n Please try Again ")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            msg.close()
        elif response.status_code == 200:
            self.login_data = response.json()
            self.employee_details = api.get_employee_data(self.login_data['id'])
            print(self.employee_details)
            if self.employee_details['employement_status'] != "Active":
                msg = QMessageBox()
                msg.setText("Authorization not Allowed \n Please contact Pipeline Administrator ")
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                msg.close()
            else:
                self.hide()
                MainWindow(self.employee_details)

    def get_display_name(self):
        GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
        NameDisplay = 3

        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameEx(NameDisplay, None, size)

        nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameEx(NameDisplay, nameBuffer, size)
        return nameBuffer.value


class MainWindow(QMainWindow):
    def __init__(self, login_data):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.login_data = login_data
        self.employee_details = api.get_employee_data(login_data['id'])
        # self.logger.debug("LoggedIn Succesfully: {}".format(self.employee_details['fullName']))
        # self.permissions = api.rolePermissions(str(16))
        self.main_timer = QTimer()
        # self.client = QtWebSockets.QWebSocket("", QtWebSockets.QWebSocketProtocol.Version13, None)
        # self.sockets_host = "{}{}/ws/emp/".format(api.config['SOCKETS']['host'], api.config['SOCKETS']['port'])
        # ws_Url = QUrl(self.sockets_host + str(self.employee_details['id'])+"/")
        # # self.client.error.connect(self.error)
        # # self.client.open(ws_Url)
        # # self.client.textMessageReceived.connect(self.processTextMessage)
        self.team_lead = False
        self.team_lead_id =None
        # my_logger = logging.getLogger('ShotBuzz')
        # my_logger.setLevel(logging.INFO)
        # handler = SysLogHandler(address=('192.168.10.15', 514))
        # formatter = logging.Formatter(
        #     'SB_Login: { "%(message)s", "%(lineno)d", "%(msecs)d ms" }')
        #
        # handler.formatter = formatter
        # my_logger.addHandler(handler)
        # my_logger.info("LoggedIn Succesfully: {}".format(self.employee_details['fullName']))
        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.start_time = 1
        # self.setWindowTitle(' TENDRILL')
        # UIFunctions.labelTitle(self, 'TENDRILL')
        UIFunctions.labelDescription(self, 'Welcome ' + self.employee_details['fullName'])
        # UIFunctions.labelPage(self, "Clients")
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################
        ## ==> END ##

    ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        _file = exists(FILTERS_FILE)

        if _file:
            # Read YAML file
            with open(FILTERS_FILE, 'r') as stream:
                self.filters_loaded = yaml.safe_load(stream)
            # for _cid in self.filters_loaded['clients']:
            #     G_CLIENTS_ID_LIST.append(_cid['id'])
            #     G_CLIENTS_LIST.append(_cid)
            for _pid in self.filters_loaded['projects']:
                G_PROJECTS_ID_LIST.append(_pid['id'])
                G_PROJECTS_LIST.append(_pid)
            for _sid in self.filters_loaded['status']:
                G_STATUS_ID_LIST.append(_sid['id'])
                G_STATUS_LIST.append(_sid)
        else:
            # Write YAML file
            d = {'projects': G_PROJECTS_LIST, 'status': G_STATUS_LIST}
            with open(FILTERS_FILE, 'w') as yaml_file:
                yaml.dump(d, yaml_file, default_flow_style=False)

        # TODO: Change version before production build
        self.ui.label_version.setText("V01.5262")
        self.ui.projects_pb.hide()
        self.ui.all_shots_pb.hide()
        self.ui.shots_ingest_pb.hide()
        self.ui.my_task_pb.hide()
        role = self.employee_details['role']
        if role == "DATA I/O":
            self.ui.projects_pb.show()
            self.ui.all_shots_pb.show()
            self.ui.shots_ingest_pb.show()
            self.ui.stackedWidget.setCurrentWidget(self.ui.projects_page)
            Projects(self)


        elif role == "TEAM LEAD" or role == "AST TEAM LEAD" or role == "QC" or role == "AST QC" or role == "SUPERVISOR" or role == "AST SUPERVISOR" or role == "PRODUCTION MANAGER" or role == "AST PRODUCTION MANAGER":
            self.ui.all_shots_pb.show()
            self.ui.my_task_pb.show()
            self.ui.stackedWidget.setCurrentWidget(self.ui.all_shots_page)
            All_Shots(self)

        elif role == "VFX ARTIST":
            self.ui.my_task_pb.show()
            self.ui.stackedWidget.setCurrentWidget(self.ui.my_task_page)
            My_Task(self)
        # UIFunctions.addNewMenu(self, "Reports", "reports",
        #                        "url(:/16x16/icons/16x16/cil-chart-line.png)", True)
        # UIFunctions.addNewMenu(self, "Change Password", "chng_pwd",
        #                        "url(:/16x16/icons/16x16/password_change.png)", True)
        # UIFunctions.addNewMenu(self, "Mail", "mail",
        #                        "url(:/16x16/icons/16x16/cil-envelope-closed.png)", True)
        # UIFunctions.addNewMenu(self, "Settings", "settings", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        # UIFunctions.selectStandardMenu(self, "clients")
        ## ==> END ##

        ## ==> START PAGE
        # self.ui.stackedWidget.setCurrentWidget(self.ui.clients_page)
        # Clients(self)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        user = getpass.getuser()
        UIFunctions.userIcon(self, user.split(".")[-1].upper() + user[0], "", True)

        self.ui.projects_pb.clicked.connect(self.client_btn)
        self.ui.all_shots_pb.clicked.connect(self.all_shots_btn)
        self.ui.shots_ingest_pb.clicked.connect(self.shots_ingest_btn)
        self.ui.my_task_pb.clicked.connect(self.my_task_btn)
        self.ui.chng_pwd_pb.clicked.connect(self.change_password_btn)
        self.ui.log_out_btn.clicked.connect(lambda: self.logOut())

        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################

        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.cli_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.pro_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.shot_import_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.team_tableWid.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

        ##TODO: UnComment below line before deploying to production
        # self.get_storage_space()
        # mp3_play()
        ## ==> END ##

    def convert_bytes(self,bytes_number):
        tags = ["Byte", "KB", "MB", "GB", "TB"]

        i = 0
        double_bytes = bytes_number

        while (i < len(tags) and bytes_number >= 1024):
            double_bytes = bytes_number / 1024.0
            i = i + 1
            bytes_number = bytes_number / 1024

        return round(double_bytes, 2), tags[i]

    def get_storage_space(self):
        stats = shutil.disk_usage(r'\\172.168.1.250\ofxstorage')
        total = self.convert_bytes(stats.total)
        used = self.convert_bytes(stats.used)
        free = self.convert_bytes(stats.free)
        self.ui.storage_bar.setMaximum(total[0])
        self.ui.storage_bar.setMinimum(0)
        self.ui.storage_bar.setValue(used[0])

        if self.ui.storage_bar.text() < "50%":
            self.ui.storage_bar.setStyleSheet("""QProgressBar {background-color:white;color:black;border: 1px solid white;border-bottom-right-radius:5px;border-bottom-left-radius:5px}
                QProgressBar::chunk {background-color: green;border-bottom-right-radius:5px;border-bottom-left-radius:5px}""")
        if self.ui.storage_bar.text() >= "80%":
            self.ui.storage_bar.setStyleSheet("""QProgressBar {background-color:white;color:white;border: 1px solid white;border-bottom-right-radius:5px;border-bottom-left-radius:5px}
        QProgressBar::chunk {background-color: red;border-bottom-right-radius:5px;border-bottom-left-radius:5px}""")

        self.ui.storage_bar.setToolTip(QCoreApplication.translate("MainWindow", u"Total: {} {}\n"
                                                                             "Used: {} {}\n"
                                                                             "Free: {} {}", None).format(total[0],total[1],used[0],used[1],free[0],free[1]))

    def processTextMessage(self, message):
        message_json = json.loads(message)
        value = self.ui.notification_btn.text()
        final_val = int(value)+1
        self.ui.notification_btn.setText(str(final_val))
        # create an object to ToastNotifier class
        n = ToastNotifier()

        n.show_toast("ShotBuzz", message_json['message'], duration=10,
                     icon_path="D:/Native Design/Shot-Buzz/icons/oscarfx/icon.ico", threaded=True)
        # self.tray_notify(message_json['message'])

    def tray_notify(self, message):
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()
        w = QtWidgets.QWidget()
        w.setWindowTitle(" TENDRILL -  A Complete Pipeline Application")
        tray_icon = SystemTrayIcon(QtGui.QIcon("D:/Native Design/Shot-Buzz/icons/oscarfx/png.png"), w)
        tray_icon.show()
        tray_icon.showMessage('Tendrill', message)
        app.exec_()

    def error(self, error_code):
        print("error code: {}".format(error_code))
        print(self.client.errorString())

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################

    def emmitted(self):
        print("emitted")
    @Slot()
    def notifications(self):
        self.popup = popup(self, self.ui.notification_btn)
        self.popup.show()

    def Button(self, button):
        # GET BT CLICKED
        btnWidget = button
        self.browser = QWebEngineView()
        if btnWidget.objectName() == "projects":
            self.ui.stackedWidget.setCurrentWidget(self.ui.projects_page)
            UIFunctions.resetStyle(self, "projects")
            UIFunctions.labelPage(self, "Projects")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            Projects(self)

        # PAGE NEW USER
        elif btnWidget.objectName() == "shots":
            self.ui.stackedWidget.setCurrentWidget(self.ui.all_shots_page)
            UIFunctions.resetStyle(self, "shots")
            UIFunctions.labelPage(self, "Shots")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            All_Shots(self)

        # PAGE NEW MY TASK
        elif btnWidget.objectName() == "my_task":
            self.ui.stackedWidget.setCurrentWidget(self.ui.my_task_page)
            UIFunctions.resetStyle(self, "my_task_page")
            UIFunctions.labelPage(self, "MY TASK")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            My_Task(self)

            # PAGE NEW MY TASK
        elif btnWidget.objectName() == "task_help":
            self.ui.stackedWidget.setCurrentWidget(self.ui.taskHelp_Main_page)
            UIFunctions.resetStyle(self, "taskHelp_Main_page")
            UIFunctions.labelPage(self, "TASK HELP")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            TaskHelp_Main(self)

        # PAGE NEW SHOTS IMPORT
        elif btnWidget.objectName() == "shots_import":
            self.ui.stackedWidget.setCurrentWidget(self.ui.shot_upload_page)
            UIFunctions.resetStyle(self, "shot_upload_page")
            UIFunctions.labelPage(self, "Shots Import")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            Shots_Ingestion(self)

        # PAGE NEW Studio Reports
        elif btnWidget.objectName() == "reports":
            self.ui.stackedWidget.setCurrentWidget(self.ui.reports_page)
            UIFunctions.resetStyle(self, "reports_page")
            UIFunctions.labelPage(self, "Studio Reports")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            Studio_Reports(self)

        # PAGE NEW Studio Reports
        elif btnWidget.objectName() == "chng_pwd":
            self.ui.stackedWidget.setCurrentWidget(self.ui.change_password_page)
            UIFunctions.resetStyle(self, "change_password_page")
            UIFunctions.labelPage(self, "Change Password")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            ChangePassword(self)

        # PAGE NEW SHOTS IMPORT
        elif btnWidget.objectName() == "tickets":
            self.browser.setWindowTitle("OSCARFX TICKETING PORTAL")
            ofx_icon = QIcon()
            ofx_icon.addFile(u":/oscarfx/icons/oscarfx/icon.png", QSize(), QIcon.Normal, QIcon.Off)
            self.browser.setWindowIcon(ofx_icon)
            self.browser.setUrl(QUrl('https://assetmanager:99/login.aspx'))
            self.main_timer.timeout.connect(self.browser.show())

        elif btnWidget.objectName() == "mail":
            self.browser.setWindowTitle("OSCARFX MAILING PORTAL")
            ofx_icon = QIcon()
            ofx_icon.addFile(u":/oscarfx/icons/oscarfx/icon.png", QSize(), QIcon.Normal, QIcon.Off)
            self.browser.setWindowIcon(ofx_icon)
            self.browser.setUrl(QUrl('https://mail.oscarfx.com/'))
            self.main_timer.timeout.connect(self.browser.show())

            # PAGE NEW USER
        elif btnWidget.objectName() == "users":
            self.ui.stackedWidget.setCurrentWidget(self.ui.users_page)
            UIFunctions.resetStyle(self, "users")
            UIFunctions.labelPage(self, "Users")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            All_Users(self)

            # PAGE NEW USER
        elif btnWidget.objectName() == "stats":
            self.ui.stackedWidget.setCurrentWidget(self.ui.users_page)
            UIFunctions.resetStyle(self, "stats")
            UIFunctions.labelPage(self, "Stats")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            All_Users(self)

        # PAGE WIDGETS
        elif btnWidget.objectName() == "settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "settings")
            UIFunctions.labelPage(self, "Settings")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    # def eventFilter(self, watched, event):
    #     if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
    #         print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        # if event.buttons() == Qt.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')
        # if event.buttons() == Qt.MidButton:
        #     print('Mouse click: MIDDLE BUTTON')

    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    # def keyPressEvent(self, event):
    #     print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)
    #
    def resizeFunction(self):
        pass
        # print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

    def client_btn(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.projects_page)
        Projects(self)

    def all_shots_btn(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.all_shots_page)
        All_Shots(self)

    def shots_ingest_btn(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.shot_upload_page)
        Shots_Ingestion(self)

    def my_task_btn(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.my_task_page)
        My_Task(self)

    def change_password_btn(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.change_password_page)
        ChangePassword(self)

    def logOut(self):
        qm = QMessageBox()
        result = qm.question(self, 'Shot Buzz Application', "Logout Confirmation!", qm.Yes | qm.No)
        if result == qm.Yes:
            del self.login_data
            self.hide()
            window.show()




def date_difference(date1, date2):
    val = 0
    if not date1 == '-' and not date1 == '-':
        tokens1 = date1.split('-')
        tokens2 = date2.split('-')
        tokens1[2] = tokens1[2].split(' ')[0]
        if len(tokens1) == 3 and len(tokens2) == 3:
            d0 = datetime.date(int(tokens1[2]), int(tokens1[1]), int(tokens1[0]))
            d1 = datetime.date(int(tokens2[2]), int(tokens2[1]), int(tokens2[0]))
            delta = d0 - d1
        val = delta.days
    return val

if __name__ == '__main__':
    status_today = str(datetime.date.today().day) + '-' + str(datetime.date.today().month) + '-' + str(datetime.date.today().year)
    ex_date = '30-06-2022'
    status_days_left = int(date_difference(ex_date, status_today))
    print ('Tendril Demo will be Expired on ',ex_date)
    print (status_days_left)
    if status_days_left>=0:
        app = QApplication(sys.argv)
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
        window = LoginWindow()
        sys.exit(app.exec_())
    else:
        print ('Tendril Demo version is expired')
        v = input()
        #w = QWidget()
        #QMessageBox.information(w, "Message", "Oops ...  Stark Demo version is expired ..!!!")
        sys.exit()

