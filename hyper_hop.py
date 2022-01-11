import sublime
import sublime_plugin

class HyperHopCommand(sublime_plugin.TextCommand):
    def run(self, edit = None):
        print("Hello")
