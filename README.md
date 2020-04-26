RabbitVCS Context Integration
===============================

**A RabbitVCS Plugin for Sublime Text**
*...because who has time to `Open Containing Folder...`
and THEN use RabbitVCS?*

A simple plugin to expose the best of the RabbitVCS GUI to the
Sublime Text 2 or Sublime Text 3 context menu.

Adds the following to the context menu for an active file:

* Diff
* Show log
* Check for modifications
* Blame
* Commit...
* Commit (repo)...
* Sync (repo)...

Adds the following to the context menu in the side bar:

* Diff
* Show log
* Check for modifications
* Blame
* Commit...
* Sync...

If there is no active file, it tries to guess the "relevant" repository
by looking at the project file or the first open folder. In the side bar,
it runs the command for the selected directory or file.

## Installation

Please be sure you have installed the prerequisites before expecting this to work:

* Sublime Text 2/3
* RabbitVCS

You can install using [Package Control](https://packagecontrol.io/packages/RabbitVCS%20Context%20Integration),
or manually install it.  Instructions for both follow.

### Using Package Control

In Sublime Text's menu, choose: `Preferences > Package Control: Install Package`

Then just type in `RabbitVCS Context Integration`, click it, and away you go!

### Manually Install

If you don't use Package Control, you can do the following:

1. Go to folder `Packages`:
   It can be found at `%APPDATA%\Sublime Text 3\Packages`.  Also, clicking
   `Preferences/Browse Packages...` in Sublime Text will open the right directory.
2. In that directory, run `git clone git@github.com:sjp27/rabbitvcs-st3.git`.

## Thanks

Thanks to the authors and contributors of the following repositories,
from whom I got useful direction:

* https://github.com/fyneworks/sublime-TortoiseGIT
* https://github.com/kemayo/sublime-text-git
* https://github.com:ses4j/tgit-st3.git

