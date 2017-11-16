from io_export import CSVExporter, JSONExporter
import os

class FileWriter(object):

    def __init__(self, exporter):
        self.exporter = exporter

    def write(self, path, filename):
        try:
            with open(os.path.join(path, filename)) as file:
                file.write(self.exporter.build_string())
                
        except IOError as e:
            print(e)

