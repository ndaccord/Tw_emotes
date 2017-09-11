import aiohttp, logging, json, os, random, urllib.request

import hangups

import plugins


logger = logging.getLogger(__name__)


_externals = { "running": False }


def _initialise(bot):
    plugins.register_user_command(["t"])



def get_emote(image_uri, bot):
    logger.info("getting {}".format(image_uri))
    filename = os.path.basename(image_uri)


    r = yield from aiohttp.request('get', image_uri)
    raw = yield from r.read()
    image_data = io.BytesIO(raw)
    image_id = yield from bot._client.upload_image(image_data, filename=filename)
    return image_id


def t(bot, event, em_str):


    em_id = map_str_to_id(em_str)


    instanceImageUrl = "https://static-cdn.jtvnw.net/emoticons/v1/" + em_id + "/2.0"

    image_id = yield from bot.call_shared('image_upload_single', instanceImageUrl)


    yield from bot.coro_send_message(event.conv.id_, None, image_id=image_id)
	

import json
#import urllib
from random import randint

def map_str_to_id(em_str):

	with urllib.request.urlopen("https://twitchemotes.com/api_cache/v3/global.json") as url:
		s = url.read()
	data = json.loads(s)

	
	try:
		if em_str not in data:

			with urllib.request.urlopen("https://twitchemotes.com/api_cache/v3/images.json") as url:
				s = url.read()
			data = json.loads(s)
			em_id = [data[b]['id'] for b in data if data[b]['code']==em_str][0]

			return(str(em_id))

		else:
			return str(data[em_str]["id"])
	
	except:

		omegalol = randint(0, 212000)
		return(str(omegalol))
		


#import sys
#machintruc(sys.argv[1], sys.argv[2], sys.argv[3])



















	



	
