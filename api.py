import  stalker

def write_list(lst, filepath):
    with open(filepath, 'w') as f:
        for item in lst:
            f.write("%s\n" % item)

if __name__ == "__main__":
    API_KEY = 'enter yours'
    API_KEY_SECRET = 'enter yours'
    ACCESS_TOKEN = 'enter yours'
    ACCESS_TOKEN_SECRET = 'enter yours'
    
    stalk = stalker.Stalker(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    lst = stalk.stalk('count', username='enter username', url= 'enter url') #enter count and (username or url of the account you wannna stalk)
    
    write_list(lst, 'path to file')