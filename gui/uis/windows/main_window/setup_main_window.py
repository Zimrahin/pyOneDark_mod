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

from . functions_main_window import *
import sys
import os
from qt_core import *
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets import *
from . ui_main import UI_MainWindow
from . functions_main_window import *

class SetupMainWindow:
	def __init__(self):
		super().__init__()
		# SETUP MAIN WINDOw
		# Load widgets from "gui\uis\main_window\ui_main.py"
		self.ui = UI_MainWindow()
		self.ui.setup_ui(self)

	# ADD LEFT MENUS
	add_left_menus = [
		{
			"btn_icon" : "icon_home.svg",
			"btn_id" : "btn_home",
			"btn_text" : "Home",
			"btn_tooltip" : "Home Page",
			"show_top" : True,
			"is_active" : True
		},
		{
			"btn_icon" : "icon_file.svg",
			"btn_id" : "btn_new_file",
			"btn_text" : "New File",
			"btn_tooltip" : "Create New File",
			"show_top" : True,
			"is_active" : False
		},
		{
			"btn_icon" : "icon_folder_open.svg",
			"btn_id" : "btn_open_file",
			"btn_text" : "Open File",
			"btn_tooltip" : "Open File",
			"show_top" : True,
			"is_active" : False
		},
		# {
		#     "btn_icon" : "icon_save.svg",
		#     "btn_id" : "btn_save",
		#     "btn_text" : "Save File",
		#     "btn_tooltip" : "Save file",
		#     "show_top" : True,
		#     "is_active" : False
		# },
		{
			"btn_icon" : "icon_info.svg",
			"btn_id" : "btn_info",
			"btn_text" : "Information",
			"btn_tooltip" : "Open Information",
			"show_top" : False,
			"is_active" : False
		},
		{
			"btn_icon" : "icon_settings.svg",
			"btn_id" : "btn_settings",
			"btn_text" : "Settings",
			"btn_tooltip" : "Open Settings",
			"show_top" : False,
			"is_active" : False
		}
	]

	# SETUP CUSTOM BTNs OF CUSTOM WIDGETS
	# Get sender() function when btn is clicked
	def setup_btns(self):
		if self.ui.left_menu.sender() != None:
			return self.ui.left_menu.sender()
		elif self.ui.left_column.sender() != None:
			return self.ui.left_column.sender()

	# SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
	def setup_gui(self):
		# APP TITLE
		self.setWindowTitle(self.settings["app_name"])
		
		# LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
		# ADD MENUS
		self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

		# SET SIGNALS
		self.ui.left_menu.clicked.connect(self.btn_clicked)
		self.ui.left_menu.released.connect(self.btn_released)

		# LEFT COLUMN SET SIGNALS
		self.ui.left_column.clicked.connect(self.btn_clicked)
		self.ui.left_column.released.connect(self.btn_released)

		# SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
		MainFunctions.set_page(self, self.ui.load_pages.page_1)
		MainFunctions.set_left_column_menu(
			self,
			menu = self.ui.left_column.menus.menu_1,
			title = "Settings",
			icon_path = Functions.set_svg_icon("icon_settings.svg")
		)
	 

		# EXAMPLE CUSTOM WIDGETS
		# Here are added the custom widgets to pages and columns that
		# were created using Qt Designer.
		# This is just an example and should be deleted when creating
		# your application.
		#
		# OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
		# You can access objects inside Qt Designer projects using
		# the objects below:
		#
		# <OBJECTS>
		# LEFT COLUMN: self.ui.left_column.menus
		# RIGHT COLUMN: self.ui.right_column
		# LOAD PAGES: self.ui.load_pages
		# </OBJECTS>

		# LOAD SETTINGS
		settings = Settings()
		self.settings = settings.items

		# LOAD THEME COLOR
		themes = Themes()
		self.themes = themes.items

		#------------------------------------------------------------
		# LEFT COLUMN
		# BTN 1
		self.left_btn_1 = PyPushButton(
			text="Btn 1",
			radius=8,
			color=self.themes["app_color"]["text_foreground"],
			bg_color=self.themes["app_color"]["dark_one"],
			bg_color_hover=self.themes["app_color"]["dark_three"],
			bg_color_pressed=self.themes["app_color"]["dark_four"]
		)
		self.left_btn_1.setMaximumHeight(40)
		self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

		# BTN 2
		self.left_btn_2 = PyPushButton(
			text="Btn With Icon",
			radius=8,
			color=self.themes["app_color"]["text_foreground"],
			bg_color=self.themes["app_color"]["dark_one"],
			bg_color_hover=self.themes["app_color"]["dark_three"],
			bg_color_pressed=self.themes["app_color"]["dark_four"]
		)
		self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
		self.left_btn_2.setIcon(self.icon)
		self.left_btn_2.setMaximumHeight(40)
		self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

		# BTN 3 - Default QPushButton
		self.left_btn_3 = QPushButton("Default QPushButton")
		self.left_btn_3.setMaximumHeight(40)
		self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

		#------------------------------------------------------------
		# PAGES
		# PAGE 1

		# PAGE 2
		# PUSH BUTTON 1
		self.push_button_1 = PyPushButton(
			text = "Button Without Icon",
			radius  =8,
			color = self.themes["app_color"]["text_foreground"],
			bg_color = self.themes["app_color"]["dark_one"],
			bg_color_hover = self.themes["app_color"]["dark_three"],
			bg_color_pressed = self.themes["app_color"]["dark_four"]
		)
		self.push_button_1.setMinimumHeight(40)

		# PUSH BUTTON 2
		self.push_button_2 = PyPushButton(
			text = "Button With Icon",
			radius = 8,
			color = self.themes["app_color"]["text_foreground"],
			bg_color = self.themes["app_color"]["dark_one"],
			bg_color_hover = self.themes["app_color"]["dark_three"],
			bg_color_pressed = self.themes["app_color"]["dark_four"]
		)
		self.icon_2 = QIcon(Functions.set_svg_icon("icon_settings.svg"))
		self.push_button_2.setMinimumHeight(40)
		self.push_button_2.setIcon(self.icon_2)

		# PY LINE EDIT
		self.line_edit = PyLineEdit(
			text = "",
			place_holder_text = "Place holder text",
			radius = 8,
			border_size = 2,
			color = self.themes["app_color"]["text_foreground"],
			selection_color = self.themes["app_color"]["white"],
			bg_color = self.themes["app_color"]["dark_one"],
			bg_color_active = self.themes["app_color"]["dark_three"],
			context_color = self.themes["app_color"]["context_color"]
		)
		self.line_edit.setMinimumHeight(30)

		# TOGGLE BUTTON
		self.toggle_button = PyToggle(
			width = 50,
			bg_color = self.themes["app_color"]["dark_two"],
			circle_color = self.themes["app_color"]["icon_color"],
			active_color = self.themes["app_color"]["context_color"]
		)


		# ADD WIDGETS
		self.ui.load_pages.row_3_layout.addWidget(self.push_button_1)
		self.ui.load_pages.row_3_layout.addWidget(self.push_button_2)
		self.ui.load_pages.row_3_layout.addWidget(self.toggle_button)
		self.ui.load_pages.row_4_layout.addWidget(self.line_edit)
		# pages est?? descrito con QForm probablemente, deber??a cambiarlo a un layout H y V

		#------------------------------------------------------------
