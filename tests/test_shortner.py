try:
    from flask import url_for
except Exception as e:
    print("Error: {} ".format(e))


def test_link_shortner(client):
    user_url = url_for('api.linkshortner')

    '''
    Test with invalid URL
    Expected Reponse Code: 400
    '''
    data = {"url": "htp://www.google.co.in"}
    rep = client.post(user_url, json=data)
    assert rep.status_code == 400

    '''
    Test with no json data
    Expected Reponse Code: 400
    '''

    rep = client.post(user_url)
    assert rep.status_code == 400

    '''
    Test with correct URL
    Expected Reponse Code: 200
    '''
    url = "https://www.google.co.in"
    data = {"url": url}
    rep = client.post(user_url, json=data)
    results = rep.get_json()
    assert results["url"] == url
    assert results["short_url"] != None
    assert rep.status_code == 201


def test_redirector(client):
    '''
    Test with invalid shortened URL
    Expected Reponse Code: 400
    '''
    user_url = url_for('api.redirector', shortenedId="asd")
    rep = client.get(user_url)
    assert rep.status_code == 400

    '''
    Test with correct shortened URL
    Expected Reponse Code: 200
    '''
    user_url = url_for('api.redirector', shortenedId="XkQJv")
    rep = client.get(user_url)
    assert rep.status_code == 302
