'''
AutoSave - Sublime Text Plugin

Provides a convenient way to turn on and turn off
automatically saving the current file after every modification.
'''

import os
import sublime
import sublime_plugin
from threading import Timer


settings_filename = "auto_save.sublime-settings"

on_modified_field = "auto_save_on_modified"
delay_field = "auto_save_delay_in_seconds"
all_files_field = "auto_save_all_files"
current_file_field = "auto_save_current_file"
backup_field = "auto_save_backup"
backup_suffix_field = "auto_save_backup_suffix"



class AutoSaveListener(sublime_plugin.EventListener):

  save_queue = [] # Save queue for on_modified events.

  @staticmethod
  def generate_backup_filename(filename, backup_suffix):
    dirname, basename = [os.path.dirname(filename),
      os.path.basename(filename).split('.')]
    if len(basename) > 1:
      basename.insert(-1, backup_suffix)
    else:
      basename.append(backup_suffix)
    return dirname + '/' + '.'.join(basename)


  def on_modified(self, view):
    settings = sublime.load_settings(settings_filename)
    if not (settings.get(on_modified_field) and view.file_name() and view.is_dirty()):
      return

    delay = settings.get(delay_field)
    all_files = settings.get(all_files_field)
    current_file = settings.get(current_file_field)
    backup = settings.get(backup_field)
    backup_suffix = settings.get(backup_suffix_field)

    if not all_files and current_file != view.file_name():
      return


    def callback():
      '''
      Must use this callback for ST2 compatibility
      '''
      if view.is_dirty() and not view.is_loading():
        if not backup: # Save file
          view.run_command("save")
        else: # Save backup file
          content = view.substr(sublime.Region(0, view.size()))
          try:
            with open(AutoSaveListener.generate_backup_filename(
              view.file_name(), backup_suffix), 'w', encoding='utf-8') as f:
              f.write(content)
          except Exception as e:
            sublime.status_message(e)
            raise e

      else:
        print("Auto-save callback invoked, but view is",
              "currently loading." if view.is_loading() else "unchanged from disk.")


    def debounce_save():
      '''
      If the queue is longer than 1, pop the last item off,
      Otherwise save and reset the queue.
      '''
      if len(AutoSaveListener.save_queue) > 1:
        AutoSaveListener.save_queue.pop()
      else:
        sublime.set_timeout(callback, 0)
        AutoSaveListener.save_queue = []


    AutoSaveListener.save_queue.append(0) # Append to queue for every on_modified event.
    Timer(delay, debounce_save).start() # Debounce save by the specified delay.




class AutoSaveCommand(sublime_plugin.ApplicationCommand):

  def run(self, **kwargs):
    '''
    Toggle auto-save on and off. Can be bound to a keystroke, e.g. ctrl+alt+s.
    If enable argument is given, auto save will be enabled (if True) or disabled (if False).
    If enable is not provided, auto save will be toggled (on if currently off and vice versa).
    '''
    enable = kwargs.get('enable', None)
    all_files = kwargs.get('all_files', True)
    backup = kwargs.get('backup', False)

    settings = sublime.load_settings(settings_filename)
    if enable is None: # toggle
      enable = not settings.get(on_modified_field)

    if not enable:
      message = "AutoSave Turned Off"
      filename = settings.get(current_file_field)
      if settings.get(backup_field) and filename: # Delete backup file
        try:
          os.remove(AutoSaveListener.generate_backup_filename(
            filename, settings.get(backup_suffix_field)))
        except:
          pass

    settings.set(on_modified_field, enable)
    settings.set(all_files_field, all_files)
    filename = sublime.Window.active_view(sublime.active_window()).file_name()
    settings.set(current_file_field, filename)
    settings.set(backup_field, backup)

    if enable:
      message = "AutoSave %sTurned On" % ("Backup " if backup else "")
      if not all_files:
        message += " for: " + os.path.basename(filename)
    sublime.status_message(message)
