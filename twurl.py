import urllib.request, urllib.parse, urllib.error
import oauth
# import hidden

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

def augment(url, parameters):
    # secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer("API key",
                                   "API secret key")
    token = oauth.OAuthToken( "Access token",
                              "Access token secret")

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()


def test_me():
    print('* Calling Twitter...')
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
                  {'screen_name': 'drchuck', 'count': '2'})
    print(url)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    print(data)
    headers = dict(connection.getheaders())
    print(headers)

