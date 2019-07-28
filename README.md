auto-save
===============
A [Sublime Text](http://www.sublimetext.com/) plugin that **automatically saves the current file after every modification**.

- [Synopsis](#synopsis)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Author](#author)

Synopsis
-------
In the occasion where you'd want Sublime Text to save the current file after
each change, you can use this plugin.

Demo
-------
![Image](https://github.com/jamesfzhang/auto-save/blob/master/demo.gif?raw=true)

Installation
-------
#### From Package Control
auto-save is available through [Sublime Package Control](https://sublime.wbond.net/packages/auto-save)
and is the recommended way to install.

#### From Github
Alternatively, you may install via GitHub by cloning this repository into the `Packages`
directory under Sublime Text's data directory:

On Mac:

```
cd ~/Library/Application Support/Sublime Text 3/Packages
git clone https://github.com/jamesfzhang/auto-save.git
```

Usage
-------
**By default, auto-save is disabled** because it is a fairly invasive plugin. To make it less invasive, you can instruct it to only auto-save changes to the file that is active when you turn on auto-save. In this mode, it will ignore changes to all other files.

To run auto-save whenever a file is modified, set `"auto_save_on_modified": true` in your user settings. To ignore certain files, set `auto_save_ignore_files` to a list of file suffices like `[".yml", "package.json"]`.

You can also instruct it to auto-backup the file instead of auto-saving it. The backup gets created in the same directory as its source file. The backup file takes the same name as its source file, with the string `.autosave` inserted directly before the file extension. When auto-save is disabled, the backup file is deleted.

There are two ways to enable it. You can press <kbd>Command + Shift + P</kbd> to bring up the Command Palette, and search for **AutoSave**. Here, there are 3 options:

- Toggle AutoSave: all files
- Toggle AutoSave: current file only
- Toggle AutoSave Backup: current file only

Alternatively, you can bind commands to turn the plugin on or off. For example, to toggle auto-save for all files, open "Preferences / Key Bindings - User" and add:

```js
{ "keys": ["ctrl+shift+s"], "command": "auto_save" }
```

To toggle it for only the current file, and instruct to make a backup of the file instead of saving the file itself, you could add:

```js
{ "keys": ["ctrl+shift+s"], "command": "auto_save", "args": {"all_files": false, "backup": true} }
```

This key bindings file takes an array of key bindings so please ensure that this key binding, along with any existing ones, are properly wrapped in `[]`.

With this setting, pressing <kbd>Ctrl + Shift + S</kbd> will turn the plugin
on or off. A status message will be displayed in the Sublime Status Bar each
time the plugin is turned on or off.

By default, auto-save debounces "save" events by 1 second. For fast typers, this improves
performance dramatically such that "save" events are not called constantly, just when it matters.

License
-------
[MIT-License](https://raw.github.com/jamesfzhang/auto-save/master/MIT-License).

Author
-------
auto-save was created and maintained by James Zhang. Give him a shoutout at [@jamesfzhang](https://twitter.com/jamesfzhang)
if you have comments or questions.
