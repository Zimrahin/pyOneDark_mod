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

import json
import os

class Settings(object):
	# APP PATH
	# json_file = "settings.json"
	# app_path = os.path.abspath(os.getcwd())
	# settings_path = os.path.normpath(os.path.join(app_path, json_file))
	# if not os.path.isfile(settings_path):
	# 	print(f"WARNING: \"settings.json\" not found! check in the folder {settings_path}")

	def __init__(self):
		super(Settings, self).__init__()
		self.items = {
						"app_name": "Stepper Motor Controller",
						"version" : "v1.11.11",
						"copyright" : "",
						"year" : 2022,
						"theme_name" : "default",
						"custom_title_bar": False,
						"startup_size": [
							1400,
							720
						],
						"minimum_size": [
							960,
							540
						],
						"left_menu_size" : {
							"minimum" : 50,
							"maximum" : 160
						},
						"left_menu_content_margins" : 3,
						"left_column_size" : {
							"minimum" : 0,
							"maximum" : 240
						},
						"right_column_size" : {
							"minimum" : 0,
							"maximum" : 240
						},
						"time_animation" : 200,
						"font" : {
							"family" : "Segoe UI",
							"title_size" : 11,
							"text_size" : 10
						}
					}

		# DESERIALIZE
		# self.deserialize()

	# SERIALIZE JSON
	def serialize(self):
		# WRITE JSON FILE
		with open(self.settings_path, "w", encoding='utf-8') as write:
			json.dump(self.items, write, indent=4)

	# DESERIALIZE JSON
	def deserialize(self):
		# READ JSON FILE
		with open(self.settings_path, "r", encoding='utf-8') as reader:
			settings = json.loads(reader.read())
			self.items = settings