'''
AutoSave - Sublime Text Plugin

Provides a convenient way to turn on and turn off
automatically saving the current file after every modification.
'''


import sublime
import sublime_plugin
from threading import Timer


settings_filename = "auto_save.sublime-settings"
on_modified_field = "auto_save_on_modified"
delay_field = "auto_save_delay_in_seconds"


class AutoSaveListener(sublime_plugin.EventListener):

  save_queue = [] # Save queue for on_modified events.

  def on_modified(self, view):
    settings = sublime.load_settings(settings_filename)
    delay = settings.get(delay_field)


    '''
    Must use this callback for ST2 compatibility
    '''
    def callback():
      view.run_command("save")


    '''
    If the queue is longer than 1, pop the last item off,
    Otherwise save and reset the queue.
    '''
    def debounce_save():
      if len(AutoSaveListener.save_queue) > 1:
        AutoSaveListener.save_queue.pop()
      else:
        sublime.set_timeout(callback, 0)
        AutoSaveListener.save_queue = []


    if settings.get(on_modified_field) and view.file_name():
      AutoSaveListener.save_queue.append(0) # Append to queue for every on_modified event.
      Timer(delay, debounce_save).start() # Debounce save by the specified delay.


class AutoSaveCommand(sublime_plugin.TextCommand):

  def run(self, view):
    settings = sublime.load_settings(settings_filename)

    if settings.get(on_modified_field):
      settings.set(on_modified_field, False)
      sublime.status_message("AutoSave Turned Off")
    else:
      settings.set(on_modified_field, True)
      sublime.status_message("AutoSave Turned On")
