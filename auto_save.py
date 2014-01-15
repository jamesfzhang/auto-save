'''
AutoSave - Sublime Text Plugin

Provides a convenient way to turn on and turn off
automatically saving the current file after every modification.
'''


import sublime
import sublime_plugin


auto_save_settings_filename = "auto_save.sublime-settings"


class AutoSaveListener(sublime_plugin.EventListener):

  def on_modified(self, view):
    settings = sublime.load_settings(auto_save_settings_filename)

    if settings.get("auto_save_on_modified"):
      view.run_command("save")


class AutoSaveCommand(sublime_plugin.TextCommand):

  def run(self, view):
    settings = sublime.load_settings(auto_save_settings_filename)

    if settings.get("auto_save_on_modified"):
      settings.set("auto_save_on_modified", False)
      sublime.status_message("AutoSave Turned Off")
    else:
      settings.set("auto_save_on_modified", True)
      sublime.status_message("AutoSave Turned On")
