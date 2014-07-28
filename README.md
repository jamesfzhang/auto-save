[auto-save](http://jzhang.io/auto-save)
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
**By default, auto-save is disabled** because it is a fairly invasive plugin.
To enable it, you must first bind the command to turn the plugin
on or off. Open "Preferences / Key Bindings - User" and add:

```js
{ "keys": ["ctrl+shift+s"], "command": "auto_save" }
```

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
auto-save was created and maintained by [James Zhang](http://jzhang.io).
Give him a shoutout at [@jamesfzhang](https://twitter.com/jamesfzhang)
if you have comments or questions.
