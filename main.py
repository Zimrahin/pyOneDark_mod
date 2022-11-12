# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////


from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

from qt_core import *
from gui.core.json_settings import Settings

from gui.uis.windows.main_window import *
from gui.widgets import *

os.environ['QT_FONT_DPI'] = '96'

# https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
import ctypes
myappid = 'StepperMotorController' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		# SETUP MAIN WINDOw
		# Load widgets from "gui\uis\main_window\ui_main.py"
		self.ui = UI_MainWindow()
		self.ui.setup_ui(self)

		# LOAD SETTINGS
		settings = Settings()
		self.settings = settings.items

		# SETUP MAIN WINDOW
		self.hide_grips = True # Show/Hide resize grips
		SetupMainWindow.setup_gui(self)

		# SHOW MAIN WINDOW
		self.show()

	# Check function by object name / btn_id
	def btn_clicked(self):
		# GET BUTTON CLICKED
		btn = SetupMainWindow.setup_btns(self)

		# Remove Selection If Clicked By "btn_close_left_column"
		if btn.objectName() != "btn_settings":
			self.ui.left_menu.deselect_all_tab()

		# LEFT MENU
		
		# HOME BTN
		if btn.objectName() == "btn_home":
			# Select Menu
			self.ui.left_menu.select_only_one(btn.objectName())

			# Load Page 1
			MainFunctions.set_page(self, self.ui.load_pages.page_1)

		# WIDGETS BTN
		if btn.objectName() == "btn_open_file":
			# Select Menu
			self.ui.left_menu.select_only_one(btn.objectName())

			# Load Page 2
			MainFunctions.set_page(self, self.ui.load_pages.page_2)


		if btn.objectName() == 'btn_info':
			# Select Menu
			self.ui.left_menu.select_only_one(btn.objectName())

			# Load Page 3 
			MainFunctions.set_page(self, self.ui.load_pages.page_3)

		# SETTINGS LEFT
		if btn.objectName() == "btn_close_left_column" or btn.objectName() == "btn_settings" or btn.objectName() == "btn_home" or btn.objectName() == "btn_open_file" or btn.objectName() == "btn_new_file" or btn.objectName() == 'btn_info':
			if not MainFunctions.left_column_is_visible(self):
				if btn.objectName() == "btn_settings" :
				# CHECK IF LEFT COLUMN IS VISIBLE
					# Show 
					MainFunctions.toggle_left_column(self)
					self.ui.left_menu.select_only_one_tab(btn.objectName())
			else:
				if btn.objectName() == "btn_close_left_column" or btn.objectName() == "btn_settings" or btn.objectName() == "btn_home" or btn.objectName() == "btn_open_file" or btn.objectName() == "btn_new_file" or btn.objectName() == 'btn_info':
					self.ui.left_menu.deselect_all_tab()
					# Hide
					MainFunctions.toggle_left_column(self)
					if btn.objectName() != "btn_settings":
						self.ui.left_menu.select_only_one_tab(btn.objectName())

		# DEBUG
		print(f"Button {btn.objectName()}, clicked!")


	# Check function by object name / btn_id
	def btn_released(self):
		# GET BUTTON CLICKED
		btn = SetupMainWindow.setup_btns(self)

		# DEBUG
		print(f"Button {btn.objectName()}, released!")

	def mousePressEvent(self, event):
		# SET DRAG POS WINDOW
		self.dragPos = event.globalPos()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("icon.ico"))
	window = MainWindow()

	sys.exit(app.exec_())