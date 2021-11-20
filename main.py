import requests,json,math,time
token=""
gid=""
id=""
msgslst=[]
offset=0
msgamount = requests.get(f'https://discord.com/api/v9/guilds/{gid}/messages/search?author_id={id}&offset={offset}',headers={'authorization':token}).json()['total_results']
for i in range(0,msgamount,25):
    time.sleep(3) #you might need to go higher to prevent rate limiting
    c = requests.get(f'https://discord.com/api/v9/guilds/{gid}/messages/search?author_id={id}&offset={i}',headers={'authorization':token})
    jsn=c.json()
    try:
        msgs=jsn['messages']
    except:
        print(jsn)
    for x in msgs:
        msgslst.append(x)
        print(x[0]['content'])
