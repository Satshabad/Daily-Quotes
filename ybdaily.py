import facebook
from auth import facebook_auth_token

quotes = open('ybquotes.txt').readlines()
quotes = filter(lambda s: s != '\n', quotes)
today_index =int(open('ybindex.txt').read())
quote = quotes[today_index]

graph = facebook.GraphAPI(facebook_auth_token)

graph.put_object("me", "feed", message=quote + "- Yogi Bhajan")

open('ybindex.txt', 'w').write(str(today_index +1))

