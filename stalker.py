import tweepy

class Stalker():
    
    def __init__(self, api_key, api_key_secret, token, token_secert):
        self.auth = tweepy.OAuthHandler(api_key, api_key_secret)
        self.auth.set_access_token(token, token_secert)

        self.api = tweepy.API(self.auth)
    
    def stalk(self, count, username = None, url = None):
        tweets = []
        if username:
            self.handler = username
        elif url:
            self.handler = url.split('/')[3]
        else:
            return  None
        self.user = self.api.get_user(self.handler)
        for item in tweepy.Cursor(self.api.user_timeline, screen_name=self.handler, include_entities=True).items(count) :
            tweets.append('twitter.com/{}/status/{}'.format(self.handler,item.id))
        
        return tweets
        
        