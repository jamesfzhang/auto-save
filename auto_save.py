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
      if view.is_dirty() and not view.is_loading():
        view.run_command("save")
      else:
        print("Auto-save callback invoked, but view is",
              "currently loading." if view.is_loading() else "unchanged from disk.")


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


    if settings.get(on_modified_field) and view.file_name() and view.is_dirty():
      AutoSaveListener.save_queue.append(0) # Append to queue for every on_modified event.
      Timer(delay, debounce_save).start() # Debounce save by the specified delay.


class AutoSaveCommand(sublime_plugin.TextCommand):

  def run(self, view, enable=None):
    '''
    Toggle auto-save on and off. Can be bound to a keystroke, e.g. ctrl+alt+s.
    If enable argument is given, auto save will be enabled (if True) or disabled (if False).
    If enable is not provided, auto save will be toggled (on if currently off and vice versa).
    '''
    settings = sublime.load_settings(settings_filename)
    if enable is None: # toggle
      enable = not settings.get(on_modified_field)
    settings.set(on_modified_field, enable)
    sublime.status_message("AutoSave Turned %s" % ("On" if enable else "Off"))
