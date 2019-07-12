import tweepy

class Stalker():
    
    def __init__(self, api_key, api_key_secret, token, token_secert):
        self.auth = tweepy.OAuthHandler(api_key, api_key_secret)
        self.auth.set_access_token(token, token_secert)

        self.api = tweepy.API(self.auth)
    
    def stalk(self, count, username = None, url = None, typ = 'all' ):
        all_tweets       = []
        personal_tweets  = []
        retweeted_tweets = []
        if username:
            self.set_target(username)
        elif url:
            self.set_target(url.split('/')[3])
        
        if self.handler is None:
            return  None
        
        self.user = self.api.get_user(self.handler)
        for item in tweepy.Cursor(self.api.user_timeline, screen_name=self.handler, include_entities=True).items(count) :
            all_tweets.append('twitter.com/{}/status/{}'.format(self.handler,item.id))   
            
            if item.retweeted:
                retweeted_tweets.append('twitter.com/{}/status/{}'.format(self.handler,item.id))
            
            else:
                personal_tweets.append('twitter.com/{}/status/{}'.format(self.handler,item.id))
        
        if typ == 'all':
            tweets = all_tweets
        elif typ == 'personal':
            tweets = personal_tweets
        elif typ == 'retweeted':
            tweets = retweeted_tweets
        else:
            return  []
        return tweets
    
    def set_target(self, target):
        self.handler = target
        
    @property
    def get_target(self):
        return  self.handler
