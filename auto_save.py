'''
Provides a convenient way to turn on and turn off
automatically saving your files after every modification.

See README.md for details

@author: James Zhang (https://twitter.com/jamesfzhang)
@license: MIT (http://www.opensource.org/licenses/mit-license)
@since: 2014-01-14
'''

import sublime
import sublime_plugin

auto_save_settings_filename = "auto_save.sublime-settings"
settings = sublime.load_settings(auto_save_settings_filename)

class AutoSaveListener(sublime_plugin.EventListener):
  def on_modified(self, view):
    settings = sublime.load_settings(auto_save_settings_filename)
    if settings.get("auto_save_on_modified"):
      view.run_command("save")

class AutoSaveCommand(sublime_plugin.TextCommand):
  def run(self, view):
    if settings.get("auto_save_on_modified"):
      settings.set("auto_save_on_modified", False)
      sublime.status_message("Auto Save Turned Off")
    else:
      settings.set("auto_save_on_modified", True)
      sublime.status_message("Auto Save Turned On")
