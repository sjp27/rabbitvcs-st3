"""
Invoke useful RabbitVCS GUI windows from Sublime Text

By Scott Stafford, https://github.com/ses4j
"""

import os
import time
import sublime, sublime_plugin

try:
    from .rabbitvcs_utils import *
except ValueError:
    # We get `ValueError: Attempted relative import in non-package` in ST2.
    from rabbitvcs_utils import *


class RabbitvcsCommandBase(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return is_git_controlled(self._relevant_path())

    def _active_line_number(self):

        view = self.window.active_view()
        if view:
            (row,col) = view.rowcol(view.sel()[0].begin())
            return row
        else:
            return None

    def _active_file_path(self):
        view = self.window.active_view()
        if view and view.file_name() and len(view.file_name()) > 0:
            return view.file_name()

    def _active_repo_path(self):
        path = self._active_file_path()
        if not path:
            path = self.window.project_file_name()
        if not path:
            path = self.window.folders()[0]
        if path is None:
            return

        root = git_root(path)

        if root is False:
            return
        else:
            return root

    def _active_file_or_repo_path(self):
        path = self._active_file_path()
        if path is not None:
            return path

        # If no active file, then guess the repo.
        return self._active_repo_path()

    def _selected_dir(self, dirs):
        if len(dirs):
            return dirs[0]
        else:
            return

    def _execute_command(self, command, path=None, args="null"):
        if path is None:
            run_rabbitvcs_command(command, args, self._relevant_path())
        else:
            run_rabbitvcs_command(command, args, path)


class RabbitvcsLogCommand(RabbitvcsCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('log', self._selected_dir(dirs))
    
    def _relevant_path(self):
        return self._active_file_or_repo_path()


class RabbitvcsDiffCommand(RabbitvcsCommandBase):
    
    def run(self, edit=None, dirs=[]):
        settings = sublime.load_settings('RabbitVCS Context Integration.sublime-settings')
        rabbitvcs_diff = settings.get('rabbitvcs_diff')
        self._execute_command(rabbitvcs_diff, self._selected_dir(dirs))

    def _relevant_path(self):
        return self._active_file_or_repo_path()


class RabbitvcsCommitCommand(RabbitvcsCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('commit', self._selected_dir(dirs))

    def _relevant_path(self):
        return self._active_file_or_repo_path()


class RabbitvcsCommitRepoCommand(RabbitvcsCommandBase):
    def run(self, edit=None):
        self._execute_command('commit')

    def _relevant_path(self):
        return self._active_repo_path()


class RabbitvcsStatusCommand(RabbitvcsCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('repostatus', self._selected_dir(dirs))

    def _relevant_path(self):
        return self._active_file_or_repo_path()

class RabbitvcsBlameCommand(RabbitvcsCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('blame', self._selected_dir(dirs), str(self._active_line_number()))

    def _relevant_path(self):
        return self._active_file_path()

class RabbitvcsAddCommand(RabbitvcsCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('add', self._selected_dir(dirs))

    def _relevant_path(self):
        return self._active_file_or_repo_path()
		
class RabbitvcsRevertCommand(RabbitvcsCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('revert', self._selected_dir(dirs))
    def _relevant_path(self):
        return self._active_file_or_repo_path()
