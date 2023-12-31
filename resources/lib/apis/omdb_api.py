# -*- coding: utf-8 -*-
from xml.dom.minidom import parseString as mdParse
# from caches.main_cache import cache_object
from caches.meta_cache import metacache
from modules.metadata import movie_expiry, tvshow_expiry
from modules.utils import get_datetime, get_current_timestamp
from modules.kodi_utils import make_session
# from modules.kodi_utils import logger

class OMDbAPI:
    def __init__(self):
        self.url = 'http://www.omdbapi.com/?apikey=%s&i=%s&tomatoes=True&r=xml'
        self.session = make_session('http://www.omdbapi.com/')

    def fetch_info(self, meta, api_key):
        imdb_id = meta.get('imdb_id')
        if not imdb_id or not api_key:
            return {}
        self.api_key = api_key
        data = self.process_result(imdb_id, meta)
        return data

    def process_result(self, imdb_id, meta):
        data = {}
        self.result = self.get_result(imdb_id)
        if not self.result:
            return {}
        self.result_get = self.result.get
        metascore_rating, tomatometer_rating, tomatousermeter_rating = self.process_rating(
            'metascore'), self.process_rating('tomatoMeter'), self.process_rating('tomatoUserMeter')
        imdb_rating, tomato_image = self.process_rating(
            'imdbRating'), self.process_rating('tomatoImage')
        metascore_icon, imdb_icon, tmdb_icon = 'metacritic.WEBP', 'imdb.WEBP', 'tmdb.WEBP'
        if tomato_image:
            tomatometer_icon = 'rtcertified.WEBP' if tomato_image == 'certified' else 'rtfresh.WEBP' if tomato_image == 'fresh' else 'rtrotten.WEBP'
        elif tomatometer_rating:
            tomatometer_icon = 'rtfresh.WEBP' if int(
                tomatometer_rating) > 59 else 'rtrotten.WEBP'
        else:
            tomatometer_icon = 'rtrotten.WEBP'
        if tomatousermeter_rating:
            tomatousermeter_icon = 'popcorn.WEBP' if int(
                tomatousermeter_rating) > 59 else 'popcorn_spilt.WEBP'
        else:
            tomatousermeter_icon = 'popcorn_spilt.WEBP'
        data = {
            'metascore': {'rating': f'{metascore_rating}%', 'icon': metascore_icon},
            'tomatometer': {'rating': f'{tomatometer_rating}%', 'icon': tomatometer_icon},
            'tomatousermeter': {'rating': f'{tomatousermeter_rating}%', 'icon': tomatousermeter_icon},
            'imdb': {'rating': imdb_rating, 'icon': imdb_icon},
            'tmdb': {'rating': '', 'icon': tmdb_icon},
        }
        media_type = meta.get('mediatype')
        expiry_function = movie_expiry if media_type == 'movie' else tvshow_expiry
        meta['extra_ratings'] = data
        metacache.set(media_type, 'tmdb_id', meta, expiry_function(
            get_datetime(), meta), get_current_timestamp())
        return data

    def get_result(self, imdb_id):
        try:
            result = self.session.get(self.url % (self.api_key, imdb_id)).text
            response_test = dict(mdParse(result).getElementsByTagName('root')[
                                 0].attributes.items())
            if not response_test.get('response', 'False') == 'True':
                return None
        except:
            return None
        return dict(mdParse(result).getElementsByTagName('movie')[0].attributes.items())

    def process_rating(self, rating_name):
        return self.result_get(rating_name, '').replace('N/A', '')


fetch_ratings_info = OMDbAPI().fetch_info
