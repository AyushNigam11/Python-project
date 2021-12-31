#mac-ayushs-air%
from instabot import Bot
bot = Bot()
bot.login(username="yoour username", password="your password")

######  upload a picture #######
bot.upload_photo("sc.jpg", caption="BOT-TESTING")

######  follow someone #######
bot.follow("elonrmuskk")

######  send a message #######
bot.send_message("Hello", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("your usrname")
for follower in my_followers:
    print(follower)
