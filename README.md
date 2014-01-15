Trailing Spaces
===============
A [Sublime Text 2](http://www.sublimetext.com/2) and
[3](http://www.sublimetext.com/3) plugin that allows you to **automatically save your current file after every modification.**

- [Synopsis](#synopsis)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Author](#author)

Synopsis
-------
In the rare occasion where you'd want your Sublime Text file to save after
each keystroke, you can now use this plugin. I wrote this plugin because
I wanted to make a screencast that shows live editing of HTML along with
the changes showing live in the browser. It's easy to use Javascript to
reload the browers every second, but I did not want to manually save the
file after every keystroke. That's why this plugin was created.

Installation
-------

### From Package Control
TODO.

### From Github
Go to the `Packages` directory under Sublime Text's data directory:

OS X: `cd ~/Library/Application Support/Sublime Text 3/Packages`

Then clone this repository: `git clone https://github.com/jamesfzhang/AutoSave.git`

Uage
-------
By default, AutoSave is disabled because it is a fairly invasive plugin.
To enable it, you must do the first bind the command to turn the plugin
on or off. Open "Preferences / Key Bindings - User" and add:

```js
{ "keys": ["ctrl+shift+s"], "command": "auto_save" }
```

With this setting, pressing <kbd>Ctrl + Shift + S</kbd> will turn the plugin
on or off. A status message will be displayed in the Sublime Status Bar each
time the plugin is turned on or off.

License
-------
[MIT-License](https://raw.github.com/jamesfzhang/AutoSave/master/MIT-License).

Author
-------
AutoSave was created and maintained by [James Zhang](http://jzhang.io).
Give him a shoutout at [@jamesfzhang](https://twitteri.com/jamesfzhang)
if you have comments or questions.
