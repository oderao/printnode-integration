# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "printnode_integration"
app_title = "Printnode Integration"
app_publisher = "MaxMorais"
app_description = "Integration with Printnode API"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "max.morais.dmm@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/printnode_integration/css/printnode_integration.css"
app_include_js = "/assets/printnode_integration/js/printnode_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/printnode_integration/css/printnode_integration.css"
# web_include_js = "/assets/printnode_integration/js/printnode_integration.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "printnode_integration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "printnode_integration.install.before_install"
# after_install = "printnode_integration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "printnode_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"CTC Lab Test": {
		"after_insert": "printnode_integration.events.after_insert",
		"on_update": "printnode_integration.events.on_update",
		"on_submit": "printnode_integration.events.on_submit",
		"on_trash": "printnode_integration.events.on_trash"
	}
}

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"printnode_integration.tasks.all"
# 	],
# 	"daily": [
# 		"printnode_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"printnode_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"printnode_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"printnode_integration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "printnode_integration.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "printnode_integration.event.get_events"
# }

