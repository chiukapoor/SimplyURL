import json

class URLMapping:
    def get_url_mapping(self, filePath):
        with open(filePath, "r") as url_mapping_file:
            return json.load(url_mapping_file)

    def set_url_mapping(self, filePath, data):
        with open(filePath, "w") as url_mapping_file:
            json.dump(data, url_mapping_file)