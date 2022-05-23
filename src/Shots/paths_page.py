from PySide2.QtWidgets import QWidget


class PathPage(QWidget):
    def __init__(self, instance):
        super(PathPage, self).__init__()
        self.instance = instance
        self.main_window = instance.main_window
        try:
            self.main_window.ui.team_tableWid.cellClicked.disconnect()
        except:
            pass
        self.shot_details = instance.shot_details
        self.employee_details = instance.main_window.employee_details
        self.main_window.ui.input_path_tb.clear()
        self.main_window.ui.retake_path_tb.clear()
        self.main_window.ui.output_path_tb.clear()
        self.main_window.ui.input_path_tb.append(self.shot_details['input_path'])
        self.main_window.ui.retake_path_tb.append(self.shot_details['retake_path'])
        self.main_window.ui.output_path_tb.append(self.shot_details['output_path'])