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
TODO

Uage
-------

By default, AutoSave is disabled because it is a fairly invasive plugin.
To enable it, you must do the first bind the command to turn the plugin
on or off. Open "Preferences / Key Bindings - User" and add:

```js
{ "keys": ["ctrl+shift+s"], "command": "auto_save" }
```

With this setting, pressing <kbd>Ctrl + Shift + S<kbd> will turn the plugin
on or off. A status message will be displayed in the Sublime Status Bar each
time the plugin is turned on or off.

License
-------

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author
-------

AutoSave was created and maintained by [James Zhang](http://jzhang.io).
Give him a shoutout at [@jamesfzhang](https://twitteri.com/jamesfzhang)
if you have comments or questions.
