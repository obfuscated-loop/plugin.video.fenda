# -*- coding: utf-8 -*-
import time
from datetime import datetime, timedelta
from modules.kodi_utils import get_property, set_property, clear_property, _init_db, metacache_db
# from modules.kodi_utils import logger

all_tables = ('metadata', 'season_metadata', 'function_cache')
id_types = ('tmdb_id', 'imdb_id', 'tvdb_id')
season_prop, media_prop = 'fenda.meta_season_%s', 'fenda.%s_%s_%s'
GET_MOVIE_SHOW = 'SELECT meta, expires FROM metadata WHERE db_type = ? AND %s = ?'
GET_SEASON = 'SELECT meta, expires FROM season_metadata WHERE tmdb_id = ?'
GET_FUNCTION = 'SELECT string_id, data, expires FROM function_cache WHERE string_id = ?'
GET_ALL = 'SELECT db_type, tmdb_id FROM metadata'
GET_ALL_SEASON = 'SELECT tmdb_id FROM season_metadata'
SET_MOVIE_SHOW = 'INSERT OR REPLACE INTO metadata VALUES (?, ?, ?, ?, ?, ?)'
SET_SEASON = 'INSERT INTO season_metadata VALUES (?, ?, ?)'
SET_FUNCTION = 'INSERT INTO function_cache VALUES (?, ?, ?)'
DELETE_MOVIE_SHOW = 'DELETE FROM metadata WHERE db_type = ? AND %s = ?'
DELETE_SEASON = 'DELETE FROM season_metadata WHERE tmdb_id = ?'
DELETE_FUNCTION = 'DELETE FROM function_cache WHERE string_id = ?'
DELETE_ALL = 'DELETE FROM %s'
string = str


class MetaCache:
    def __init__(self):
        self.dbcon = _init_db(metacache_db)

    def get(self, media_type, id_type, media_id, current_time=None):
        meta, custom_artwork = None, None
        try:
            media_id = string(media_id)

            if not current_time:
                current_time = self._get_timestamp()

            meta = self.get_memory_cache(
                media_type, id_type, media_id, current_time)

            if meta is None:
                cache_data = self.dbcon.execute(GET_MOVIE_SHOW % id_type, (media_type, media_id, ))[0]

                if cache_data:
                    meta, expiry = eval(cache_data[0]), cache_data[1]

                    if expiry < current_time:
                        custom_artwork = self.get_custom_artwork(meta)
                        self.delete(media_type, id_type, media_id,
                                    meta=meta, dbcur=dbcur)
                        meta = None
                    else:
                        self.set_memory_cache(
                            media_type, id_type, meta, expiry, media_id)
        except:
            pass
        return meta, custom_artwork

    def get_season(self, prop_string):
        meta = None
        try:
            current_time = self._get_timestamp()
            meta = self.get_memory_cache_season(prop_string, current_time)

            if meta is None:
                cache_data = self.dbcon.execute(GET_SEASON, (prop_string,))[0]

                if cache_data:
                    meta, expiry = eval(cache_data[0]), cache_data[1]

                    if expiry < current_time:
                        self.delete_season(prop_string, dbcur=dbcur)
                        meta = None
                    else:
                        self.set_memory_cache_season(prop_string, meta, expiry)
        except:
            pass
        return meta

    def set(self, media_type, id_type, meta, expiration=30, current_time=None):
        try:
            meta_get = meta.get
            if current_time:
                expires = current_time + (expiration*86400)
            else:
                expires = self._get_timestamp(expiration)
                
            media_id = string(meta_get(id_type))

            self.dbcon.execute(SET_MOVIE_SHOW, (media_type, string(meta_get('tmdb_id')), meta_get(
                'imdb_id'), string(meta_get('tvdb_id')), repr(meta), expires))
        except:
            return None
        self.set_memory_cache(media_type, id_type, meta, expires, media_id)

    def set_season(self, prop_string, meta, expiration=30):
        try:
            expires = self._get_timestamp(expiration)
            self.dbcon.execute(SET_SEASON, (prop_string, repr(meta), int(expires)))
        except:
            return None
        self.set_memory_cache_season(prop_string, meta, expires)

    def delete(self, media_type, id_type, media_id, meta=None, dbcur=None):
        try:
            self.dbcon.execute(DELETE_MOVIE_SHOW % id_type, (media_type, media_id, ))

            for item in id_types:
                self.delete_memory_cache(media_type, item, meta[item])
            if media_type == 'tvshow':
                self.delete_all_seasons(media_id)
        except:
            return

    def delete_season(self, prop_string, dbcur=None):
        try:
            self.dbcon.execute(DELETE_SEASON, (prop_string, ))
            self.delete_memory_cache_season(prop_string)
        except:
            return

    def get_memory_cache(self, media_type, id_type, media_id, current_time):
        result = None
        try:
            prop_string = media_prop % (media_type, id_type, media_id)
            cachedata = get_property(prop_string)
            if cachedata:
                cachedata = eval(cachedata)
                if cachedata[0] > current_time:
                    result = cachedata[1]
        except:
            pass
        return result

    def get_memory_cache_season(self, prop_string, current_time):
        result = None
        try:
            cachedata = get_property(season_prop % prop_string)
            if cachedata:
                cachedata = eval(cachedata)
                if cachedata[0] > current_time:
                    result = cachedata[1]
        except:
            pass
        return result

    def set_memory_cache(self, media_type, id_type, meta, expires, media_id):
        try:
            cachedata, prop_string = (expires, meta), media_prop % (
                media_type, id_type, media_id)
            set_property(prop_string, repr(cachedata))
        except:
            pass

    def set_memory_cache_season(self, prop_string, meta, expires):
        try:
            cachedata = (expires, meta)
            set_property(season_prop % prop_string, repr(cachedata))
        except:
            pass

    def delete_memory_cache(self, media_type, id_type, media_id):
        try:
            clear_property(media_prop % (media_type, id_type, media_id))
        except:
            pass

    def delete_memory_cache_season(self, prop_string):
        try:
            clear_property(season_prop % prop_string)
        except:
            pass

    def get_function(self, prop_string):
        result = None
        try:
            current_time = self._get_timestamp()
            cache_data = self.dbcon.execute(GET_FUNCTION, (prop_string, ))[0]

            if cache_data:
                if cache_data[2] > current_time:
                    result = eval(cache_data[1])
                else:
                    self.dbcon.execute(DELETE_FUNCTION, (prop_string, ))
        except:
            pass
        return result

    def set_function(self, prop_string, result, expiration=1):
        try:
            expires = self._get_timestamp(expiration)
            self.dbcon.execute(SET_FUNCTION, (prop_string, repr(result), expires))
        except:
            return

    def delete_all_seasons(self, media_id, dbcur=None):
        for item in range(1, 51):
            self.delete_season(f'{media_id}_{string(item)}')

    def delete_all(self):
        try:
            for i in all_tables:
                self.dbcon.execute(DELETE_ALL % i)
                
            self.dbcon.execute('VACUUM')

            for i in self.dbcon.execute(GET_ALL):
                try:
                    self.delete_memory_cache(
                        string(i[0]), 'tmdb_id', string(i[1]))
                except:
                    pass

            for i in self.dbcon.execute(GET_ALL_SEASON):
                try:
                    self.delete_memory_cache_season(string(i[0]))
                except:
                    pass
        except:
            return

    def get_custom_artwork(self, meta):
        return {'custom_poster': meta.get('custom_poster', ''), 'custom_fanart': meta.get('custom_fanart', ''), 'custom_clearlogo': meta.get('custom_clearlogo', ''),
                'custom_banner': meta.get('custom_banner', ''), 'custom_clearart': meta.get('custom_clearart', ''), 'custom_landscape': meta.get('custom_landscape', ''),
                'custom_discart': meta.get('custom_discart', ''), 'custom_keyart': meta.get('custom_keyart', '')}

    def _get_timestamp(self, offset=0):
        # Offset is in DAYS multiply by 86400 to get seconds
        return int(time.time()) + (offset*86400)


metacache = MetaCache()


def cache_function(function, prop_string, url, expiration=30, json=True):
    data = metacache.get_function(prop_string)
    if data:
        return data
    if json:
        result = function(url).json()
    else:
        result = function(url)
    metacache.set_function(prop_string, result, expiration=expiration)
    return result


def delete_meta_cache(silent=False):
    from modules.kodi_utils import confirm_dialog
    try:
        if not silent and not confirm_dialog():
            return False
        metacache.delete_all()
        return True
    except:
        return False
