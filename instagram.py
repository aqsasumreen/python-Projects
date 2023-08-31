from instabot import Bot
bot =Bot()
# bot.login(username = "username", password="pass")
# bot.follow("aqsa_ghd")
# bot.upload_photo("sec_qr.py" , caption ="so beautifull")
# bot.unfollow("aqsa_ghd")
bot.send_messages("bdcsjhsiioqu",["amber_2","aqsa_ghd"])
#To fetch the info of Folloers
# followers = bot.get_user_followers("username")
# for follower in followers:
#     print(bot.get_user_info(follower))
# To fetch the info of followings
followings = bot.get_user_following("username")
for following in followings:
    print(bot.get_user_info(following))