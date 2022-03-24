import sublime
import sublime_plugin

class HyperHopCommand(sublime_plugin.TextCommand):
    def run(self, edit = None):
        print("Hello")
        self.view.insert(edit, 0, "#import ole\n")
        for region in self.view.sel():
            str = self.view.substr(region)
            str = str+str
            self.view.replace(edit, region, str)
