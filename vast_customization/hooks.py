from . import __version__ as app_version

app_name = "vast_customization"
app_title = "Vast Customization"
app_publisher = "Commquest Technologies (Pty) Ltd."
app_description = "Custom Apps for VAST Group"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@commquest.co.za"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vast_customization/css/vast_customization.css"
# app_include_js = "/assets/vast_customization/js/vast_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/vast_customization/css/vast_customization.css"
# web_include_js = "/assets/vast_customization/js/vast_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "vast_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "vast_customization.install.before_install"
# after_install = "vast_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "vast_customization.uninstall.before_uninstall"
# after_uninstall = "vast_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vast_customization.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

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
# 		"vast_customization.tasks.all"
# 	],
# 	"daily": [
# 		"vast_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"vast_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vast_customization.tasks.weekly"
# 	]
# 	"monthly": [
# 		"vast_customization.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "vast_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vast_customization.event.get_events"
# }
#
# Each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "vast_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"vast_customization.auth.validate"
# ]

fixtures = [
    {
        "dt": "Letter Head",
        "filters": [
            ["name", "in", [
                "Blank Letterhead",
                "Bonram Letterhead",
                "Bonram No Banking Letterhead",
                "Vast Protection No Banking",
                "Vast Protection Solutions FNB",
                "Vast Protection Solutions",
                "Capitec Vast",
                "Dzimelela Letterhead",
                "Dzimelela No Banking Details",
                "Mzila Energies Letterhead"
            ]]
        ]
    },
    {
        "dt": "Print Format",
        "filters": [
            ["name", "in", [
                "Ngaa Purchase Order",
                "Ngaa Issue",
                "Ngaa Quotation",
                "Ngaa Sales Invoice",
                "Custom Delivery Note",
                "Custom Quotation",
                "Custom Sales Invoice",
                "Custom Payment Entry",
                "CITY OF JOBURG",
                "D note Dzi",
                "Dn",
                "d note",
                "tshwane",
                "Quote 1",
                "quote",
                "IMPERIAL",
                "Dzimelela Material Request",
                "Custom Material Request",
                "Dzimelela Purchase Order",
                "Custom Purchase Order",
                "Dzimelela Supplier Invoice",
                "Custom Supplier Invoice",
                "Dzimelela Supplier Quotation",
                "Custom Supplier Quotation",
                "Dzimelela Sales Invoice",
                "Dzimelela Sales Order",
                "Custom Sales Order",
                "Ngaa Delivery Note",
                "Ngaa Sales Order",
                "Ngaa Request For Quotation",
                "Ngaa Payment Request",
                "Ngaa Purchase Receipt",
                "Ngaa Purchase Invoice",
                "Ngaa Supplier Quotation",
                "Ngaa Material Request",
                "Pastel Quotation",
                "Quest Supplier Quotation",
                "Quest Request For Quotation",
                "Quest Material Request",
                "Quest Sales Order",
                "Quest Sales Invoice",
                "Quest Quotation"
            ]]
        ]
    }
]



