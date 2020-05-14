import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

#userid = input('user = ')
#pw = input('password = ')

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
print('Test finished.')
loop.close()