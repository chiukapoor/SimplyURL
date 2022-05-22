try:
    from api.resources.helper import URLMapping
    import json
except Exception as e:
    print("Error: {} ".format(e))


def test_get_url_mapping(tmp_path):
    jsonFile = tmp_path / 'temp.json'
    um = URLMapping()
    '''
    Test with empty file
    '''
    data = um.get_url_mapping(jsonFile)
    assert data == {}

    '''
    Test with invalid Dictonary
    '''
    jsonFile.write_text('{"https://www.google.co.in": "XkQJv"')
    data = um.get_url_mapping(jsonFile)
    assert data == {}

    '''
    Test with valid Dictonary
    '''
    jsonFile.write_text('{"https://www.google.co.in": "XkQJv"}')
    data = um.get_url_mapping(jsonFile)
    assert data["https://www.google.co.in"] == "XkQJv"


def test_set_url_mapping(tmp_path):
    jsonFile = tmp_path / 'temp.json'
    um = URLMapping()

    '''
    Test storing Dictonary into a file
    '''
    data = {"https://www.google.co.in": "XkQJv"}
    um.set_url_mapping(jsonFile, data)
    with open(jsonFile, "r") as url_mapping_file:
        umf = json.load(url_mapping_file)

    assert umf == data
