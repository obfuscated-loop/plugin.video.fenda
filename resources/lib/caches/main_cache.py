# -*- coding: utf-8 -*-
from datetime import timedelta
from caches.base_cache import BaseCache
from modules.kodi_utils import maincache_db
# from modules.kodi_utils import logger

like_select = 'SELECT id from maincache where id LIKE %s'
like_delete = 'DELETE FROM maincache WHERE id LIKE %s'
delete = 'DELETE FROM maincache WHERE id=?'
all_list_add = ' OR id LIKE '


class MainCache(BaseCache):
    def __init__(self):
        BaseCache.__init__(self, maincache_db, 'maincache')

    def delete_all_lists(self):
        from modules.meta_lists import media_lists
        media_list = media_lists
        len_media_list = len(media_list)
        for count, item in enumerate(media_list, 1):
            if count == 1:
                command = like_select % item
            else:
                command += '%s%s' % (all_list_add, item)

        try:
            for item in self.dbcon.execute(command):
                try:
                    remove_id = str(item[0])
                    self.dbcon.execute(delete, (remove_id, ))
                    self.delete_memory_cache(remove_id)
                except:
                    pass
            self.dbcon.execute('VACUUM')
        except:
            pass

    def delete_all_folderscrapers(self):
        remove_list = [str(i[0]) for i in self.dbcon.execute(like_select % "'fenda_FOLDERSCRAPER_%'")]

        if not remove_list:
            return

        try:
            self.dbcon.execute(like_delete % "'fenda_FOLDERSCRAPER_%'")
            self.dbcon.execute('VACUUM')

            for item in remove_list:
                self.delete_memory_cache(str(item))
        except:
            pass


main_cache = MainCache()


def cache_object(function, string, args, json=True, expiration=24):
    cache = main_cache.get(string)
    if cache is not None:
        return cache
    if isinstance(args, list):
        args = tuple(args)
    else:
        args = (args,)
    if json:
        result = function(*args).json()
    else:
        result = function(*args)
    main_cache.set(string, result, expiration=timedelta(hours=expiration))
    return result
