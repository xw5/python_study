import itchat

itchat.auto_login(hotReload=False)

userfinfo = itchat.search_friends("沅江酱")

print('userfinfo:', userfinfo)

userid = userfinfo[0]['UserName']

itchat.send("么么哒！", userid)