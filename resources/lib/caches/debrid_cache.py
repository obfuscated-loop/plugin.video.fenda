# -*- coding: utf-8 -*-
import time
from datetime import datetime, timedelta
from modules.kodi_utils import database, debridcache_db, logger
# from modules.kodi_utils import logger

GET_MANY = 'SELECT * FROM debrid_data WHERE hash in (%s)'
SET_MANY = 'INSERT INTO debrid_data VALUES (?, ?, ?, ?)'
REMOVE_MANY = 'DELETE FROM debrid_data WHERE hash=?'
CLEAR = 'DELETE FROM debrid_data'
CLEAR_DEBRID = 'DELETE FROM debrid_data WHERE debrid=?'


class DebridCache:
    def get_many(self, hash_list):
        result = None

        try:
            current_time = self._get_timestamp(datetime.now())
            dbcon = self._init_db()

            dbcur = dbcon.execute(GET_MANY %
                          (', '.join('?' for _ in hash_list)), hash_list)
            
            cache_data = dbcur.fetchall()
            
            if cache_data:
                if cache_data[0][3] > current_time:
                    result = cache_data
                else:
                    self.remove_many(cache_data)
        except Exception as e:
            logger('debrid_cache.py [get_many]: ', str(e))

        return result

    def set_many(self, hash_list, debrid):
        try:
            expires = self._get_timestamp(datetime.now() + timedelta(days=1))
            insert_list = [(i[0], debrid, i[1], expires) for i in hash_list]
            dbcon = self._init_db()

            dbcon.executemany(SET_MANY, insert_list)
        except Exception as e:
            logger('debrid_cache.py [set_many]: ', str(e))

    def remove_many(self, old_cached_data):
        try:
            old_cached_data = [(str(i[0]),) for i in old_cached_data]
            dbcon = self._init_db()

            dbcon.executemany(REMOVE_MANY, old_cached_data)
        except Exception as e:
            logger('debrid_cache.py [remove_many]: ', str(e))

    def clear_debrid_results(self, debrid):
        try:
            dbcon = self._init_db()

            dbcon.execute(CLEAR_DEBRID, (debrid,))
            dbcon.execute('VACUUM')
            return True
        except Exception as e:
            logger('debrid_cache.py [clear_debrid_results]: ', str(e))
            return False

    def clear_database(self):
        try:
            dbcon = self._init_db()

            dbcon.execute(CLEAR)
            dbcon.execute('VACUUM')
            return 'success'
        except Exception as e:
            logger('debrid_cache.py [clear_database]: ', str(e))
            return 'failure'

    def _init_db(self):
        return self._set_PRAGMAS(
            database.connect(debridcache_db, timeout=40.0, isolation_level=None)
        )

    def _set_PRAGMAS(self, dbcon):
        dbcon.execute('PRAGMA synchronous = OFF')
        dbcon.execute('PRAGMA journal_mode = OFF')
        
        return dbcon

    def _get_timestamp(self, date_time):
        return int(time.mktime(date_time.timetuple()))


debrid_cache = DebridCache()
