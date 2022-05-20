import json

class URLMapping:
    def get_url_mapping(self, filePath):
        try:
            with open(filePath, "r") as url_mapping_file:
                try:
                    data = json.load(url_mapping_file)
                except Exception as e:
                    print(f"While loading the json to Dict: \n{e}")
                finally:
                    data={}
        except Exception as e:
            print(f"File {filePath}: \n{e}")
            data={}
        finally:
            return data

    def set_url_mapping(self, filePath, data):
        try:
            with open(filePath, "w") as url_mapping_file:
                json.dump(data, url_mapping_file)
        except Exception as e:
            print(f"While unloading the json to Dict: \n {e}")