from src.MyTask.completed_task import Completed_Task
from src.MyTask.pending_task import Pending_Task
from src.MyTask.task_help import Task_Help


class My_Task(object):
    def __init__(self, obj):
        super(My_Task, self).__init__()
        self.main_window = obj
        try:
            self.main_window.ui.add_taskPer_btn.clicked.disconnect()
            self.main_window.ui.add_per_btn.clicked.disconnect()
            self.main_window.ui.task_tabWid.currentChanged.disconnect()
            self.main_window.ui.send_btn.clicked.disconnect()
            self.main_window.ui.dep_tabWidget.currentChanged.disconnect()
            self.main_window.ui.shot_details_tabWidget.currentChanged.disconnect()
            self.main_window.ui.assign_btn.clicked.disconnect()
            self.main_window.ui.start_btn.clicked.disconnect()
            self.main_window.ui.qc_btn.clicked.disconnect()
            self.main_window.ui.comp_btn.clicked.disconnect()
            self.main_window.ui.retake_btn.clicked.disconnect()
            self.main_window.ui.nuke_btn.clicked.disconnect()
            self.main_window.ui.nukeX_btn.clicked.disconnect()
            self.main_window.ui.sfx_btn.clicked.disconnect()
            self.main_window.ui.psd_btn.clicked.disconnect()
            self.main_window.ui.mocha_btn.clicked.disconnect()
            self.main_window.ui.approved_btn.clicked.disconnect()
            self.main_window.ui.hold_btn.clicked.disconnect()
            self.main_window.ui.client_retake_btn.clicked.disconnect()

            ### Folders Disconnect
            self.main_window.ui.input_TreeWid.itemClicked.disconnect()
            self.main_window.ui.Pscripts_treeWid.itemClicked.disconnect()
            self.main_window.ui.Rscripts_treeWid.itemClicked.disconnect()
            self.main_window.ui.Mscripts_treeWid.itemClicked.disconnect()
            self.main_window.ui.Ppre_ren_treeWid.itemClicked.disconnect()
            self.main_window.ui.Rpre_ren_treeWid.itemClicked.disconnect()
            self.main_window.ui.Mpre_ren_treeWid.itemClicked.disconnect()
            self.main_window.ui.Poutput_treeWid.itemClicked.disconnect()
            self.main_window.ui.Routput_treeWid.itemClicked.disconnect()
            self.main_window.ui.Moutput_treeWid.itemClicked.disconnect()
            self.main_window.ui.Pqc_treeWid.itemClicked.disconnect()
            self.main_window.ui.Rqc_treeWid.itemClicked.disconnect()
            self.main_window.ui.Mqc_treeWid.itemClicked.disconnect()

            self.main_window.ui.t_cli_sel_cb.activated.disconnect()
            self.main_window.ui.t_pro_sel_cb.activated.disconnect()
            self.main_window.ui.t_status_sel_cb.activated.disconnect()
            self.main_window.ui.task_search_btn.clicked.disconnect()
            self.main_window.ui.task_search_btn.clicked.disconnect()
            self.main_window.ui.task_pending_tableWid.cellDoubleClicked.disconnect()
            self.main_window.ui.task_completed_tableWid.cellDoubleClicked.disconnect()
        except:
            pass
        # self.main_window.ui.approved_btn.hide()
        # self.main_window.ui.retake_btn.hide()
        # self.main_window.ui.hold_btn.hide()
        # self.main_window.ui.client_retake_btn.hide()
        # self.main_window.ui.assign_btn.hide()
        self.main_window.ui.task_tabWid.currentChanged.connect(lambda : self.taskTabClicked())
        if self.main_window.ui.task_tabWid.currentIndex() == 0:
            Pending_Task(self)
        elif self.main_window.ui.task_tabWid.currentIndex() == 1:
            Completed_Task(self)

    def taskTabClicked(self):
        currentIndex = self.main_window.ui.task_tabWid.currentIndex()
        if currentIndex == 0:
            self.main_window.ui.task_tabWid.setCurrentIndex(0)
            Pending_Task(self)
        elif currentIndex == 1:
            self.main_window.ui.task_tabWid.setCurrentIndex(1)
            Completed_Task(self)
        elif currentIndex == 2:
            self.main_window.ui.task_tabWid.setCurrentIndex(2)
            Task_Help(self)

