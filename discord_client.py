import discord


class MyClient(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run('OTE0MTY3NzEwODE0OTkwNDE3.YaJHBg.FU3Qbv1uTNcZL59D-EqZkRTWUW8')
