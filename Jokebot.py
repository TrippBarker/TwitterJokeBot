import openai
import tweepy
import time

lastMention = 0
with open ('lastMention.txt', 'r') as file:
    lastMention = int(file.read())

twitterBearerPath = "D:\KEYS\JokeTwitBear.txt"
twitterApiKeyPath = "D:\KEYS\JokeTwitKey.txt"
twitterApiSecPath = "D:\KEYS\JokeTwitKeySec.txt"
twitterAccessTokenPath = "D:\KEYS\TwitToken.txt"
twitterAccessSecPath = "D:\KEYS\TwitTokenSec.txt"
twitterKeyPaths = [twitterBearerPath, twitterApiKeyPath, twitterApiSecPath, twitterAccessTokenPath, twitterAccessSecPath]

twitterKeychain = []

for keyPath in twitterKeyPaths:
    file = open(keyPath)
    fileContent = file.read()
    twitterKeychain.append(fileContent)

openai.api_key_path = "D:\KEYS\JokeKey.txt"
model_engine = "text-davinci-003"

client = tweepy.Client(twitterKeychain[0], twitterKeychain[1], twitterKeychain[2], twitterKeychain[3], twitterKeychain[4])
clientID = client.get_me().data.id
clientMentions = client.get_users_mentions(clientID)

auth = tweepy.OAuth1UserHandler(twitterKeychain[1], twitterKeychain[2], twitterKeychain[3], twitterKeychain[4])
api = tweepy.API(auth)

def promptGPT(userPrompt):
    indoctronation = "Prompt: You are an AI bot that provides a user with a witty joke when asked for one. If a joke is not asked for, you are to act confused and provide a random joke instead of responding appropriately. Please respond to the following request: " + userPrompt
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = indoctronation,
        max_tokens = 64,
        n = 1,
        stop = None,
        temperature = 1,
    )
    print(completion.choices[0].text)
    print("======================================")
    return completion.choices[0].text

def checkMentions():
    if clientMentions != None:
        for mention in clientMentions.data:
            try:
                if int(mention.id) > int(lastMention):
                    lastMention = int(mention.id)
                    print(mention.id)
                    with open('lastMention.txt', 'w') as file:
                        file.write(str(mention.id))
                    client.create_tweet(in_reply_to_tweet_id=mention.id, text=promptGPT(mention.text))
            except:
                pass

while True:
    checkMentions()
    time.sleep(5)