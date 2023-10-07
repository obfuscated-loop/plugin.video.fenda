# -*- coding: utf-8 -*-
from modules.kodi_utils import local_string as ls

years_movies = [
    2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995,
    1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966,
    1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943, 1942, 1941, 1940, 1939, 1938, 1937,
    1936, 1935, 1934, 1933, 1932, 1931, 1930, 1929, 1928, 1927, 1926, 1925, 1924, 1923, 1922, 1921, 1920, 1919, 1918, 1917, 1916, 1915, 1914, 1913, 1912, 1911, 1910, 1909, 1908,
    1907, 1906, 1905, 1904, 1903, 1902, 1901, 1900
]

years_tvshows = [
    2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995,
    1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966,
    1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943, 1942
]

decades_movies = [
    2020, 2010, 2000, 1990, 1980, 1970, 1960, 1950, 1940, 1930, 1920, 1910, 1900
]

decades_tvshows = [
    2020, 2010, 2000, 1990, 1980, 1970, 1960, 1950, 1940
]

oscar_winners = (
    (545611, 776503, 581734, 496243, 490132, 399055, 376867, 314365, 194662,
     76203, 68734, 74643, 45269, 12162, 12405, 6977, 1422, 1640, 70, 122),
    (1574, 453, 98, 14, 1934, 597, 409, 197, 13, 424,
     33, 274, 581, 403, 380, 746, 792, 606, 279, 11050),
    (783, 9443, 16619, 12102, 11778, 703, 1366, 510, 240, 9277,
     238, 1051, 11202, 3116, 17917, 10633, 874, 15121, 11113, 5769),
    (947, 1725, 284, 665, 17281, 826, 2897, 15919, 654, 11426, 27191,
     2769, 705, 25430, 23383, 33667, 887, 28580, 17661, 27367),
    (289, 43266, 223, 770, 34106, 43278, 43277, 12311,
     3078, 56164, 33680, 42861, 143, 65203, 28966, 631)
)

movie_certifications = [
    'G',
    'PG',
    'PG-13',
    'R',
    'NC-17',
    'NR'
]

tvshow_certifications = [
    'tv-y',
    'tv-y7',
    'tv-g',
    'tv-pg',
    'tv-14',
    'tv-ma'
]

languages = [
    (ls(32861), 'ar'), (ls(32862), 'bs'),   (ls(32863), 'bg'),   (ls(32864),
                                                                  'zh'),   (ls(32865), 'hr'),   (ls(32866), 'nl'),   (ls(32867), 'en'),
    (ls(32868), 'fi'), (ls(32869), 'fr'),   (ls(32870), 'de'),   (ls(32871),
                                                                  'el'),   (ls(32872), 'he'),   (ls(32873), 'hi'),   (ls(32874), 'hu'),
    (ls(32875), 'is'), (ls(32876), 'it'),   (ls(32877), 'ja'),   (ls(32878),
                                                                  'ko'),   (ls(32879), 'mk'),   (ls(32880), 'no'),   (ls(32881), 'fa'),
    (ls(32882), 'pl'), (ls(32883), 'pt'),   (ls(32884), 'pa'),   (ls(32885),
                                                                  'ro'),   (ls(32886), 'ru'),   (ls(32887), 'sr'),   (ls(32888), 'sl'),
    (ls(32889), 'es'), (ls(32890), 'sv'),   (ls(32891), 'tr'),   (ls(32892), 'uk')
]

meta_languages = [
    {'iso': 'zh', 'name': 'Chinese'},          {
        'iso': 'hr', 'name': 'Croatian'},
    {'iso': 'cs', 'name': 'Czech'},            {'iso': 'da', 'name': 'Danish'},
    {'iso': 'nl', 'name': 'Dutch'},            {'iso': 'en', 'name': 'English'},
    {'iso': 'fi', 'name': 'Finnish'},          {'iso': 'fr', 'name': 'French'},
    {'iso': 'de', 'name': 'German'},           {'iso': 'el', 'name': 'Greek'},
    {'iso': 'he', 'name': 'Hebrew'},           {
        'iso': 'hu', 'name': 'Hungarian'},
    {'iso': 'it', 'name': 'Italian'},          {
        'iso': 'ja', 'name': 'Japanese'},
    {'iso': 'ko', 'name': 'Korean'},           {
        'iso': 'no', 'name': 'Norwegian'},
    {'iso': 'pl', 'name': 'Polish'},           {
        'iso': 'pt', 'name': 'Portuguese'},
    {'iso': 'ru', 'name': 'Russian'},          {
        'iso': 'sl', 'name': 'Slovenian'},
    {'iso': 'es', 'name': 'Spanish'},          {'iso': 'sv', 'name': 'Swedish'},
    {'iso': 'tr', 'name': 'Turkish'},          {
        'iso': 'ar-SA', 'name': 'Arabic Saudi Arabia'}
]

language_choices = {
    'None': 'None',              'Afrikaans': 'afr',            'Albanian': 'alb',             'Arabic': 'ara',
    'Armenian': 'arm',           'Basque': 'baq',               'Bengali': 'ben',              'Bosnian': 'bos',
    'Breton': 'bre',             'Bulgarian': 'bul',            'Burmese': 'bur',              'Catalan': 'cat',
    'Chinese': 'chi',            'Croatian': 'hrv',             'Czech': 'cze',                'Danish': 'dan',
    'Dutch': 'dut',              'English': 'eng',              'Esperanto': 'epo',            'Estonian': 'est',
    'Finnish': 'fin',            'French': 'fre',               'Galician': 'glg',             'Georgian': 'geo',
    'German': 'ger',             'Greek': 'ell',                'Hebrew': 'heb',               'Hindi': 'hin',
    'Hungarian': 'hun',          'Icelandic': 'ice',            'Indonesian': 'ind',           'Italian': 'ita',
    'Japanese': 'jpn',           'Kazakh': 'kaz',               'Khmer': 'khm',                'Korean': 'kor',
    'Latvian': 'lav',            'Lithuanian': 'lit',           'Luxembourgish': 'ltz',        'Macedonian': 'mac',
    'Malay': 'may',              'Malayalam': 'mal',            'Manipuri': 'mni',             'Mongolian': 'mon',
    'Montenegrin': 'mne',        'Norwegian': 'nor',            'Occitan': 'oci',              'Persian': 'per',
    'Polish': 'pol',             'Portuguese': 'por',           'Portuguese(Brazil)': 'pob',   'Romanian': 'rum',
    'Russian': 'rus',            'Serbian': 'scc',              'Sinhalese': 'sin',            'Slovak': 'slo',
    'Slovenian': 'slv',          'Spanish': 'spa',              'Swahili': 'swa',              'Swedish': 'swe',
    'Syriac': 'syr',             'Tagalog': 'tgl',              'Tamil': 'tam',                'Telugu': 'tel',
    'Thai': 'tha',               'Turkish': 'tur',              'Ukrainian': 'ukr',            'Urdu': 'urd',
    'Vietnamese': 'vie'
}

regions = [
    {'code': 'AF', 'name': ls(32893)},   {'code': 'AL', 'name': ls(32894)},   {
        'code': 'DZ', 'name': ls(32895)},   {'code': 'AQ', 'name': ls(32896)},
    {'code': 'AR', 'name': ls(32897)},   {'code': 'AM', 'name': ls(32898)},   {
        'code': 'AU', 'name': ls(32899)},   {'code': 'AT', 'name': ls(32900)},
    {'code': 'BD', 'name': ls(32901)},   {'code': 'BY', 'name': ls(32902)},   {
        'code': 'BE', 'name': ls(32903)},   {'code': 'BR', 'name': ls(32904)},
    {'code': 'BG', 'name': ls(32905)},   {'code': 'KH', 'name': ls(32906)},   {
        'code': 'CA', 'name': ls(32907)},   {'code': 'CL', 'name': ls(32908)},
    {'code': 'CN', 'name': ls(32909)},   {'code': 'HR', 'name': ls(32910)},   {
        'code': 'CZ', 'name': ls(32911)},   {'code': 'DK', 'name': ls(32912)},
    {'code': 'EG', 'name': ls(32913)},   {'code': 'FI', 'name': ls(32914)},   {
        'code': 'FR', 'name': ls(32915)},   {'code': 'DE', 'name': ls(32916)},
    {'code': 'GR', 'name': ls(32917)},   {'code': 'HK', 'name': ls(32918)},   {
        'code': 'HU', 'name': ls(32919)},   {'code': 'IS', 'name': ls(32920)},
    {'code': 'IN', 'name': ls(32921)},   {'code': 'ID', 'name': ls(32922)},   {
        'code': 'IR', 'name': ls(32923)},   {'code': 'IQ', 'name': ls(32924)},
    {'code': 'IE', 'name': ls(32925)},   {'code': 'IL', 'name': ls(32926)},   {
        'code': 'IT', 'name': ls(32927)},   {'code': 'JP', 'name': ls(32928)},
    {'code': 'MY', 'name': ls(32929)},   {'code': 'NP', 'name': ls(32930)},   {
        'code': 'NL', 'name': ls(32931)},   {'code': 'NZ', 'name': ls(32932)},
    {'code': 'NO', 'name': ls(32933)},   {'code': 'PK', 'name': ls(32934)},   {
        'code': 'PY', 'name': ls(32935)},   {'code': 'PE', 'name': ls(32936)},
    {'code': 'PH', 'name': ls(32937)},   {'code': 'PL', 'name': ls(32938)},   {
        'code': 'PT', 'name': ls(32939)},   {'code': 'PR', 'name': ls(32940)},
    {'code': 'RO', 'name': ls(32941)},   {'code': 'RU', 'name': ls(32942)},   {
        'code': 'SA', 'name': ls(32943)},   {'code': 'RS', 'name': ls(32944)},
    {'code': 'SG', 'name': ls(32945)},   {'code': 'SK', 'name': ls(32946)},   {
        'code': 'SI', 'name': ls(32947)},   {'code': 'ZA', 'name': ls(32948)},
    {'code': 'ES', 'name': ls(32949)},   {'code': 'LK', 'name': ls(32950)},   {
        'code': 'SE', 'name': ls(32951)},   {'code': 'CH', 'name': ls(32952)},
    {'code': 'TH', 'name': ls(32953)},   {'code': 'TR', 'name': ls(32954)},   {
        'code': 'UA', 'name': ls(32955)},   {'code': 'AE', 'name': ls(32956)},
    {'code': 'GB', 'name': ls(32957)},   {'code': 'US', 'name': ls(32958)},   {
        'code': 'UY', 'name': ls(32959)},   {'code': 'VE', 'name': ls(32960)},
    {'code': 'VN', 'name': ls(32961)},   {'code': 'YE', 'name': ls(32962)},   {
        'code': 'ZW', 'name': ls(32963)}
]

movie_genres = {
    ls(32548): ['28', 'genre_action'],                ls(32549): ['12', 'genre_adventure'],
    ls(32550): ['16', 'genre_animation'],             ls(32551): ['35', 'genre_comedy'],
    ls(32552): ['80', 'genre_crime'],                 ls(32553): ['99', 'genre_documentary'],
    ls(32554): ['18', 'genre_drama'],                 ls(32555): ['10751', 'genre_family'],
    ls(32558): ['14', 'genre_fantasy'],               ls(32559): ['36', 'genre_history'],
    ls(32560): ['27', 'genre_horror'],                ls(32561): ['10402', 'genre_music'],
    ls(32557): ['9648', 'genre_mystery'],             ls(32562): ['10749', 'genre_romance'],
    ls(32563): ['878', 'genre_scifi'],                ls(32564): ['10770', 'genre_soap'],
    ls(32565): ['53', 'genre_thriller'],              ls(32566): ['10752', 'genre_war'],
    ls(32567): ['37', 'genre_western']
}

tvshow_genres = {
    '%s & %s' % (ls(32548), ls(32549)): ['10759', 'genre_action'],         ls(32550): ['16', 'genre_animation'],
    ls(32551): ['35', 'genre_comedy'],                                     ls(32552): ['80', 'genre_crime'],
    ls(32553): ['99', 'genre_documentary'],                                ls(32554): ['18', 'genre_drama'],
    ls(32555): ['10751', 'genre_family'],                                  ls(32556): ['10762', 'genre_kids'],
    ls(32557): ['9648', 'genre_mystery'],                                  ls(32568): ['10763', 'genre_news'],
    ls(32569): ['10764', 'genre_reality'],                                 ls(33057): ['10765', 'genre_scifi'],
    ls(32570): ['10766', 'genre_soap'],                                    ls(32570): ['10767', 'genre_talk'],
    ls(32572): ['10768', 'genre_war'],                                     ls(32567): ['37', 'genre_western']
}

networks = [
    {'id': 54, 'name': 'Disney Channel', 'logo': 'network_disney'},                   {
        'id': 44, 'name': 'Disney XD', 'logo': 'network_disneyxd'},
    {'id': 2, 'name': 'ABC', 'logo': 'network_abc'},                                  {
        'id': 493, 'name': 'BBC America', 'logo': 'network_bbcamerica'},
    {'id': 6, 'name': 'NBC', 'logo': 'network_nbc'},                                  {
        'id': 13, 'name': 'Nickelodeon', 'logo': 'network_nickelodeon'},
    {'id': 14, 'name': 'PBS', 'logo': 'network_pbs'},                                 {
        'id': 16, 'name': 'CBS', 'logo': 'network_cbs'},
    {'id': 19, 'name': 'FOX', 'logo': 'network_fox'},                                 {
        'id': 21, 'name': 'The WB', 'logo': 'network_thewb'},
    {'id': 24, 'name': 'BET', 'logo': 'network_bet'},                                 {
        'id': 30, 'name': 'USA Network', 'logo': 'network_usanetwork'},
    {'id': 23, 'name': 'CBC', 'logo': 'network_cbc'},                                 {
        'id': 88, 'name': 'FX', 'logo': 'network_fx'},
    {'id': 33, 'name': 'MTV', 'logo': 'network_mtv'},                                 {
        'id': 34, 'name': 'Lifetime', 'logo': 'network_lifetime'},
    {'id': 35, 'name': 'Nick Junior', 'logo': 'network_nickjr'},                      {
        'id': 41, 'name': 'TNT', 'logo': 'network_tnt'},
    {'id': 43, 'name': 'National Geographic', 'logo': 'network_natgeo'},              {
        'id': 47, 'name': 'Comedy Central', 'logo': 'network_comedycentral'},
    {'id': 49, 'name': 'HBO', 'logo': 'network_hbo'},                                 {
        'id': 55, 'name': 'Spike', 'logo': 'network_spike'},
    {'id': 67, 'name': 'Showtime', 'logo': 'network_showtime'},                       {
        'id': 56, 'name': 'Cartoon Network', 'logo': 'network_cartoonnetwork'},
    {'id': 65, 'name': 'History Channel', 'logo': 'network_history'},                 {
        'id': 84, 'name': 'TLC', 'logo': 'network_tlc'},
    {'id': 68, 'name': 'TBS', 'logo': 'network_tbs'},                                 {
        'id': 71, 'name': 'The CW', 'logo': 'network_thecw'},
    {'id': 74, 'name': 'Bravo', 'logo': 'network_bravo'},                             {
        'id': 76, 'name': 'E!', 'logo': 'network_e'},
    {'id': 77, 'name': 'Syfy', 'logo': 'network_syfy'},                               {
        'id': 80, 'name': 'Adult Swim', 'logo': 'network_adultswim'},
    {'id': 91, 'name': 'Animal Planet', 'logo': 'network_animalplanet'},              {
        'id': 110, 'name': 'CTV', 'logo': 'network_ctv'},
    {'id': 129, 'name': 'A&E', 'logo': 'network_ane'},                                {
        'id': 158, 'name': 'VH1', 'logo': 'network_vh1'},
    {'id': 174, 'name': 'AMC', 'logo': 'network_amc'},                                {
        'id': 928, 'name': 'Crackle', 'logo': 'network_crackle'},
    {'id': 202, 'name': 'WGN America', 'logo': 'network_wgnamerica'},                 {
        'id': 209, 'name': 'Travel Channel', 'logo': 'network_travel'},
    {'id': 213, 'name': 'Netflix', 'logo': 'network_netflix'},                       {
        'id': 251, 'name': 'Audience', 'logo': 'network_audience'},
    {'id': 270, 'name': 'SundanceTV', 'logo': 'network_sundancetv'},                  {
        'id': 318, 'name': 'Starz', 'logo': 'network_starz'},
    {'id': 359, 'name': 'Cinemax', 'logo': 'network_cinemax'},                        {
        'id': 364, 'name': 'truTV', 'logo': 'network_trutv'},
    {'id': 384, 'name': 'Hallmark Channel', 'logo': 'network_hallmark'},              {
        'id': 397, 'name': 'TV Land', 'logo': 'network_tvland'},
    {'id': 1024, 'name': 'Amazon', 'logo': 'network_amazon'},                         {
        'id': 1267, 'name': 'Freeform', 'logo': 'network_freeform'},
    {'id': 4, 'name': 'BBC 1', 'logo': 'network_bbc1'},                               {
        'id': 332, 'name': 'BBC 2', 'logo': 'network_bbc2'},
    {'id': 3, 'name': 'BBC 3', 'logo': 'network_bbc3'},                               {
        'id': 100, 'name': 'BBC 4', 'logo': 'network_bbc4'},
    {'id': 214, 'name': 'Sky 1', 'logo': 'network_sky1'},                             {
        'id': 9, 'name': 'ITV', 'logo': 'network_itv'},
    {'id': 26, 'name': 'Channel 4', 'logo': 'network_channel4'},                      {
        'id': 99, 'name': 'Channel 5', 'logo': 'network_channel5'},
    {'id': 136, 'name': 'E4', 'logo': 'network_e4'},                                  {
        'id': 210, 'name': 'HGTV', 'logo': 'network_hgtv'},
    {'id': 453, 'name': 'Hulu', 'logo': 'network_hulu'},                              {
        'id': 1436, 'name': 'YouTube Red', 'logo': 'network_youtubered'},
    {'id': 64, 'name': 'Discovery Channel', 'logo': 'network_discovery'},             {
        'id': 2739, 'name': 'Disney+', 'logo': 'network_disneyplus'},
    {'id': 2552, 'name': 'Apple TV +', 'logo': 'network_appletvplus'},                {
        'id': 2697, 'name': 'Acorn TV', 'logo': 'network_acorntv'},
    {'id': 1709, 'name': 'CBS All Access', 'logo': 'network_cbsallaccess'},           {
        'id': 3186, 'name': 'HBO Max', 'logo': 'network_hbomax'},
    {'id': 2243, 'name': 'DC Universe', 'logo': 'network_dcuniverse'},                {
        'id': 2076, 'name': 'Paramount Network', 'logo': 'network_paramount'},
    {'id': 4330, 'name': 'Paramount+', 'logo': 'network_paramountplus'},              {
        'id': 3353, 'name': 'Peacock', 'logo': 'network_peacock'},
    {'id': 4353, 'name': 'Discovery+', 'logo': 'network_discoveryplus'},              {
        'id': 132, 'name': 'Oxygen', 'logo': 'network_oxygen'},
    {'id': 244, 'name': 'Discovery ID', 'logo': 'network_discoveryid'}
]

watch_providers = [
    {'name': 'Netflix', 'id': 8, 'logo': 't2yyOv40HZeVlLjYsCsPHnWLk4W.jpg'},                     {
        'name': 'Amazon Prime Video', 'id': 9, 'logo': 'emthp39XA2YScoYL1p0sdbAH2WA.jpg'},
    {'name': 'Disney Plus', 'id': 337, 'logo': '7rwgEs15tFwyR9NPQ5vpzxTj19Q.jpg'},               {
        'name': 'Google Play Movies', 'id': 3, 'logo': 'tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg'},
    {'name': 'Sun Nxt', 'id': 309, 'logo': 'uW4dPCcbXaaFTyfL5HwhuDt5akK.jpg'},                   {
        'name': 'Apple TV', 'id': 2, 'logo': 'peURlLlr8jggOwK53fJ5wdQl05y.jpg'},
    {'name': 'MUBI', 'id': 11, 'logo': 'bVR4Z1LCHY7gidXAJF5pMa4QrDS.jpg'},                       {
        'name': 'Apple TV Plus', 'id': 350, 'logo': '6uhKBfmtzFqOcLousHwZuzcrScK.jpg'},
    {'name': 'fuboTV', 'id': 257, 'logo': 'jPXksae158ukMLFhhlNvzsvaEyt.jpg'},                    {
        'name': 'Classix', 'id': 445, 'logo': 'iaMw6nOyxUzXSacrLQ0Au6CfZkc.jpg'},
    {'name': 'Hulu', 'id': 15, 'logo': 'zxrVdFjIjLqkfnwyghnfywTn3Lh.jpg'},                       {
        'name': 'Curiosity Stream', 'id': 190, 'logo': '67Ee4E6qOkQGHeUTArdJ1qRxzR2.jpg'},
    {'name': 'Paramount Plus', 'id': 531, 'logo': 'xbhHHa1YgtpwhC8lb1NQ3ACVcLd.jpg'},            {
        'name': 'GuideDoc', 'id': 100, 'logo': 'iX0pvJ2GFATbVIH5IHMwG0ffIdV.jpg'},
    {'name': 'Public Domain Movies', 'id': 638, 'logo': 'liEIj6CkvojVDiMWeexGvflSPZT.jpg'},      {
        'name': 'HBO Max', 'id': 384, 'logo': 'Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg'},
    {'name': 'Netflix Kids', 'id': 175, 'logo': 'j2OLGxyy0gKbPVI0DYFI2hJxP6y.jpg'},              {
        'name': 'Eventive', 'id': 677, 'logo': 'fadQYOyKL0tqfyj012nYJxm3N2I.jpg'},
    {'name': 'Spamflix', 'id': 521, 'logo': 'xN97FFkFAdY1JvHhS4zyPD4URgD.jpg'},                  {
        'name': 'AMC+', 'id': 526, 'logo': 'xlonQMSmhtA2HHwK3JKF9ghx7M8.jpg'},
    {'name': 'Cultpix', 'id': 692, 'logo': '59azlQKUgFdYq6QI5QEAxIeecyL.jpg'},                   {
        'name': 'DOCSVILLE', 'id': 475, 'logo': 'bvcdVO7SDHKEa6D40g1jntXKNj.jpg'},
    {'name': 'Peacock', 'id': 386, 'logo': '8VCV78prwd9QzZnEm0ReO6bERDa.jpg'},                   {
        'name': 'VIX ', 'id': 457, 'logo': '58aUMVWJRolhWpi4aJCkGHwfKdg.jpg'},
    {'name': 'FilmBox+', 'id': 701, 'logo': '4FqTBYsUSZgS9z9UGKgxSDBbtc8.jpg'},                  {
        'name': 'Peacock Premium', 'id': 387, 'logo': 'xTHltMrZPAJFLQ6qyCBjAnXSmZt.jpg'},
    {'name': 'aha', 'id': 532, 'logo': 'm3NWxxR23l1w1e156fyTuw931gx.jpg'},                       {
        'name': 'Amazon Video', 'id': 10, 'logo': '5NyLm42TmCqCMOZFvH4fcoSNKEW.jpg'},
    {'name': 'Kocowa', 'id': 464, 'logo': 'xfAAOAERZCnPB5jW5lhboAcXk8L.jpg'},                    {
        'name': 'WOW Presents Plus', 'id': 546, 'logo': 'mgD0T960hnYU4gBxbPPBrcDfgWg.jpg'},
    {'name': 'Takflix', 'id': 1771, 'logo': 'cnIHBy3uLWhHRR7VeWQhK3ZsYP0.jpg'},                  {
        'name': 'Crunchyroll', 'id': 283, 'logo': '8Gt1iClBlzTeQs8WQm8UrCoIxnQ.jpg'},
    {'name': 'YouTube', 'id': 192, 'logo': 'oIkQkEkwfmcG7IGpRR1NB8frZZM.jpg'},                   {
        'name': 'Magellan TV', 'id': 551, 'logo': 'gekkP93StjYdiMAInViVmrnldNY.jpg'},
    {'name': 'BroadwayHD', 'id': 554, 'logo': 'xLu1rkZNOKuNnRNr70wySosfTBf.jpg'},                {
        'name': 'KoreaOnDemand', 'id': 575, 'logo': 'uHv6Y4YSsr4cj7q4cBbAg7WXKEI.jpg'},
    {'name': 'Dekkoo', 'id': 444, 'logo': 'u2H29LCxRzjZVUoZUQAHKm5P8Zc.jpg'},                    {
        'name': 'Starz Apple TV', 'id': 1855, 'logo': 'hB24bAA8Y2ei6pbEGuCNdKUOjxI.jpg'},
    {'name': 'Filmzie', 'id': 559, 'logo': 'olmH7t5tEng8Yuq33KmvpvaaVIg.jpg'},                   {
        'name': 'Showtime Apple TV', 'id': 675, 'logo': 'xVN3LKkOtCrlFT9mavhkx8SzMwV.jpg'},
    {'name': 'True Story', 'id': 567, 'logo': 'osREemsc9uUB2J8VTkQeAVk2fu9.jpg'},                {
        'name': 'AMC Plus Apple TV ', 'id': 1854, 'logo': 'yFgm7vxwKZ4jfXIlPizlgoba2yi.jpg'},
    {'name': 'DocAlliance Films', 'id': 569, 'logo': 'aQ1ritN00jXc7RAFfUoQKGAAfp7.jpg'},         {
        'name': 'Britbox Apple TV ', 'id': 1852, 'logo': 'cN85Wjk0FIFr3z6rbiimz10uWVo.jpg'},
    {'name': 'Hoichoi', 'id': 315, 'logo': 'd4vHcXY9rwnr763wQns2XJThclt.jpg'},                   {
        'name': 'BritBox', 'id': 151, 'logo': 'aGIS8maihUm60A3moKYD9gfYHYT.jpg'},
    {'name': 'Pluto TV', 'id': 300, 'logo': 't6N57S17sdXRXmZDAkaGP0NHNG0.jpg'},                  {
        'name': 'Starz', 'id': 43, 'logo': 'eWp5LdR4p4uKL0wACBBXapDV2lB.jpg'},
    {'name': 'Rakuten Viki', 'id': 344, 'logo': 'qjtOUIUnk4kRpcZmaddjqDHM0dR.jpg'},              {
        'name': 'Discovery Plus Amazon', 'id': 584, 'logo': 'a2OcajC4bM5ItniQdjyOV7tgthW.jpg'},
    {'name': 'iQIYI', 'id': 581, 'logo': '8MXYXzZGoPAEQU13GWk1GVvKNUS.jpg'},                     {
        'name': 'Showtime Amazon', 'id': 203, 'logo': 'zoL69abPHiVC1Qzd4kM6hwLSo0j.jpg'},
    {'name': 'AMC+ Amazon', 'id': 528, 'logo': '9edKQczyuMmQM1yS520hgmJbcaC.jpg'},               {
        'name': 'Funimation Now', 'id': 269, 'logo': 'fWq61Fy4onav0wZJTA3c2fs0G66.jpg'},
    {'name': 'The Roku Channel', 'id': 207, 'logo': 'z0h7mBHwm5KfMB2MKeoQDD2ngEZ.jpg'},          {
        'name': 'Showtime Roku Premium', 'id': 632, 'logo': 'qMf2zirM2w0sO0mdAIIoP5XnQn8.jpg'},
    {'name': 'Runtime', 'id': 1875, 'logo': 'nvCfpn94VKJN4ZpkDgoupJWlXqq.jpg'},                  {
        'name': 'AMC+ Roku Premium', 'id': 635, 'logo': 'ni2NgPmIqqJRXeiA8Zdj4UhBZnU.jpg'},
    {'name': 'YouTube Premium', 'id': 188, 'logo': '6IPjvnYl6WWkIwN158qBFXCr2Ne.jpg'},           {
        'name': 'YouTube Free', 'id': 235, 'logo': '4SCmZgf7AeJLKKRPcbf5VFkGpBj.jpg'},
    {'name': 'Hoopla', 'id': 212, 'logo': 'aJ0b9BLU1Cvv5hIz9fEhKKc1x1D.jpg'},                    {
        'name': 'The CW', 'id': 83, 'logo': '6Y6w3F5mYoRHCcNAG0ZD2AndLJ2.jpg'},
    {'name': 'Vudu', 'id': 7, 'logo': '21dEscfO8n1tL35k4DANixhffsR.jpg'},                        {
        'name': 'Starz Roku Premium', 'id': 634, 'logo': '5OAb2w7D9C2VHa0k5PaoAYeFYFE.jpg'},
    {'name': 'VUDU Free', 'id': 332, 'logo': 'xzfVRl1CgJPYa9dOoyVI3TDSQo2.jpg'},                 {
        'name': 'Criterion Channel', 'id': 258, 'logo': '4TJTNWd2TT1kYj6ocUEsQc8WRgr.jpg'},
    {'name': 'Showtime', 'id': 37, 'logo': '4kL33LoKd99YFIaSOoOPMQOSw1A.jpg'},                   {
        'name': 'PBS', 'id': 209, 'logo': 'bbxgdl6B5T75wJE713BiTCIBXyS.jpg'},
    {'name': 'FXNow', 'id': 123, 'logo': 'twV9iQPYeaoBzwsfRFGMGoMIUg8.jpg'},                     {
        'name': 'Pantaflix', 'id': 177, 'logo': '2tAjxjo1n3H7fsXqMsxWFMeFUWp.jpg'},
    {'name': 'Tubi TV', 'id': 73, 'logo': 'w2TDH9TRI7pltf5LjN3vXzs7QbN.jpg'},                    {
        'name': 'Kanopy', 'id': 191, 'logo': 'wbCleYwRFpUtWcNi7BLP3E1f6VI.jpg'},
    {'name': 'Comedy Central', 'id': 243, 'logo': 'gmU9aPV3XUFusVs4kK1rcICUKqL.jpg'},            {
        'name': 'Microsoft Store', 'id': 68, 'logo': 'shq88b09gTBYC4hA7K7MUL8Q4zP.jpg'},
    {'name': 'Redbox', 'id': 279, 'logo': 'gbyLHzl4eYP0oP9oJZ2oKbpkhND.jpg'},                    {
        'name': 'ABC', 'id': 148, 'logo': 'l9BRdAgQ3MkooOalsuu3yFQv2XP.jpg'},
    {'name': 'Crackle', 'id': 12, 'logo': '7P2JHkfv4AmU2MgSPGaJ0z6nNLG.jpg'},                    {
        'name': 'DIRECTV', 'id': 358, 'logo': 'xL9SUR63qrEjFZAhtsipskeAMR7.jpg'},
    {'name': 'Fandor', 'id': 25, 'logo': 'eAhAUvV2ouai3cGti5y70YOtrBN.jpg'},                     {
        'name': 'MGM Plus', 'id': 34, 'logo': '6A1gRIJqLfFHOoTvbTxDAbuU2nQ.jpg'},
    {'name': 'Freeform', 'id': 211, 'logo': 'rgpmwMkXqFYch9cway9qWMw0uXu.jpg'},                  {
        'name': 'Syfy', 'id': 215, 'logo': 'f7iqKjWYdVoYVIvKP3nboULcrM2.jpg'},
    {'name': 'Lifetime', 'id': 157, 'logo': '3wJNOOCbvqi7fJAdgf1QpL7Wwe2.jpg'},                  {
        'name': 'realeyz', 'id': 14, 'logo': '10BQc1kYmgjXFrFKb3xsRcDDn14.jpg'},
    {'name': 'Shudder', 'id': 99, 'logo': 'pheENW1BxlexXX1CKJ4GyWudyMA.jpg'},                    {
        'name': 'Screambox', 'id': 185, 'logo': 'c2Ey5Q3uUjZgfWWQQIdVIjVfxE4.jpg'},
    {'name': 'Acorn TV', 'id': 87, 'logo': '5P99DkK1jVs95KcE8bYG9MBtGQ.jpg'},                    {
        'name': 'Sundance Now', 'id': 143, 'logo': 'pZ9TSk3wlRYwiwwRxTsQJ7t2but.jpg'},
    {'name': 'Popcornflix', 'id': 241, 'logo': 'olvOut34aWUFf1YoOqiqtjidiTK.jpg'},               {
        'name': 'Pantaya', 'id': 247, 'logo': '94IdHexespnJs96kmGiJlflfiwU.jpg'},
    {'name': 'Boomerang', 'id': 248, 'logo': 'oRXiHzPl2HJMXXFR4eebsb8F5Oc.jpg'},                 {
        'name': 'Urban Movie Channel', 'id': 251, 'logo': '5uTsmZnDQmIOjZPEv8TNTy7GRJB.jpg'},
    {'name': 'Dove Channel', 'id': 254, 'logo': 'cBCzPOX6ir5L8hCoJlfIWycxauh.jpg'},              {
        'name': 'History Vault', 'id': 268, 'logo': '3bm7P1O8WRqK6CYqfffJv4fba2p.jpg'},
    {'name': 'Nickhits', 'id': 261, 'logo': 'oMwjMgYiT2jcR7ELqCH3TPzpgTX.jpg'},                  {
        'name': 'Eros Now', 'id': 218, 'logo': '4XYI2rzRm34skcvamytegQx7Dmu.jpg'},
    {'name': 'Yupp TV', 'id': 255, 'logo': '8qNJcPBHZ4qewHrDJ7C7s2DBQ3V.jpg'},                   {
        'name': 'Magnolia Selects', 'id': 259, 'logo': 'foT1TtL67MgEOWR6Cib8dKyCvJI.jpg'},
    {'name': 'WWE Network', 'id': 260, 'logo': 'rDYZ9v3Y09fuFyan51tHKE1mFId.jpg'},               {
        'name': 'Noggin', 'id': 262, 'logo': 'yxBUPUBFzHE72uFXvFr1l0fnMJA.jpg'},
    {'name': 'Smithsonian Channel', 'id': 276, 'logo': 'UAZ2lJBWszijybQD4frqw2jxRO.jpg'},        {
        'name': 'Laugh Out Loud', 'id': 275, 'logo': 'w4GTJ1EDrgJku49XKSnRag9kKCT.jpg'},
    {'name': 'Hallmark Movies', 'id': 281, 'logo': 'llEJ6av9kAniTQUR9hF9mhVbzlB.jpg'},           {
        'name': 'Pure Flix', 'id': 278, 'logo': 'orsVBNvPWxJNOVSEHMOk2h8R1wA.jpg'},
    {'name': 'Lifetime Movie Club', 'id': 284, 'logo': 'p1v0UKH13xQsMjumRgCGmCdlgKm.jpg'},       {
        'name': 'Cinemax', 'id': 289, 'logo': 'kEnyHRflZPNWEOIXroZPhfdGi46.jpg'},
    {'name': 'OVID', 'id': 433, 'logo': 'nXi2nRDPMNivJyFOifEa2t15Xuu.jpg'},                      {
        'name': 'Cohen Media Amazon', 'id': 1811, 'logo': 'jV7sSPzUYYHHmoATkD9PhFoEZXb.jpg'},
    {'name': 'Viewster Amazon', 'id': 295, 'logo': 'mlH42JbZMrapSF6zc8iTYURcZlH.jpg'},           {
        'name': 'USA Network', 'id': 322, 'logo': 'ldU2RCgdvkcSEBWWbttCpVO450z.jpg'},
    {'name': 'Sling TV Orange and Blue', 'id': 299, 'logo': 'tZ4xzOtCRHjAw7tYJphivEfDr1L.jpg'},  {
        'name': 'HiDive', 'id': 430, 'logo': '9baY98ZKyDaNArp1H9fAWqiR3Zi.jpg'},
    {'name': 'Topic', 'id': 454, 'logo': 'ubWucXFn34TrVlJBaJFgPaC4tOP.jpg'},                     {
        'name': 'Night Flight Plus', 'id': 455, 'logo': 'ba8l0e5CkpVnrdFgzBySP7ckZnZ.jpg'},
    {'name': 'Retrocrush', 'id': 446, 'logo': '9ONs8SMAXtkiyaEIKATTpbwckx8.jpg'},                {
        'name': 'Shout! Factory TV', 'id': 439, 'logo': 'ju3T8MFGNIoPiYpwHFpNlrYNyG7.jpg'},
    {'name': 'Chai Flicks', 'id': 438, 'logo': '3tCqvc5hPm5nl8Hm8o2koDRZlPo.jpg'},               {
        'name': 'PBS Masterpiece Amazon', 'id': 294, 'logo': 'mMALQK52OFGoYUKOSCZILZkfGWs.jpg'},
    {'name': 'The Film Detective', 'id': 470, 'logo': 'rOwEnT8oDSTZ5rDKmyaa3O4gUnc.jpg'},        {
        'name': 'MUBI Amazon', 'id': 201, 'logo': 'aJUiN18NZFbpSkHZQV1C1cTpz8H.jpg'},
    {'name': 'AcornTV Amazon', 'id': 196, 'logo': '8WWD7t5Irwq9kAH4rufQ4Pe1Dog.jpg'},            {
        'name': 'Screambox Amazon', 'id': 202, 'logo': 'naqM14qSfg2q0S2zDylM5zQQ3jn.jpg'},
    {'name': 'Bet+ Amazon', 'id': 343, 'logo': 'obBJU4ak4XvAOUM5iVmSUxDvqC3.jpg'},               {
        'name': 'FlixFling', 'id': 331, 'logo': '4U02VrbgLfUKJAUCHKzxWFtnPx4.jpg'},
    {'name': 'Darkmatter TV', 'id': 355, 'logo': 'x4AFz5koB2R8BRn8WNh6EqXUGHc.jpg'},             {
        'name': 'AMC on Demand', 'id': 352, 'logo': 'kJlVJLgbNPvKDYC0YMp3yA2OKq2.jpg'},
    {'name': 'TCM', 'id': 361, 'logo': '8TbsXATKVD4Humjzi6a8SVaSY7o.jpg'},                       {
        'name': 'TNT', 'id': 363, 'logo': 'gJnQ40Z6T7HyY6fbmmI6qKE0zmK.jpg'},
    {'name': 'BBC America', 'id': 397, 'logo': 'ukSXbR5qFjO2qCHpc6ZhcGPSjTJ.jpg'},               {
        'name': 'IndieFlix', 'id': 368, 'logo': '2NRn6OApVKfDTKLuHDRN8UadLRw.jpg'},
    {'name': 'Here TV', 'id': 417, 'logo': 'sa10pK4Jwr5aA7rvafFP2zyLFjh.jpg'},                   {
        'name': 'Flix Premiere', 'id': 432, 'logo': '6fX0J6x7zXsUCvPFczgOW4oD34D.jpg'},
    {'name': 'TBS', 'id': 506, 'logo': 'rcebVnRvZvPXauK4353Jgiu4DWI.jpg'},                       {
        'name': 'AsianCrush', 'id': 514, 'logo': '3VxDqUk25KU5860XxHKwV9cy3L8.jpg'},
    {'name': 'FILMRISE', 'id': 471, 'logo': 'mEiBVz62M9j3TCebmOspMfqkIn.jpg'},                   {
        'name': 'Revry', 'id': 473, 'logo': 'r1UgUKmt83FSDOIHBdRWKooZPNx.jpg'},
    {'name': 'Spectrum On Demand', 'id': 486, 'logo': '79mRAYq40lcYiXkQm6N7YErSSHd.jpg'},        {
        'name': 'VRV', 'id': 504, 'logo': 'rtTqPKRrVVXxvPV0T9OmSXhwXnY.jpg'},
    {'name': 'Hi-YAH', 'id': 503, 'logo': 'mB2eDIncwSAlyl8WAtfV24qEIkk.jpg'},                    {
        'name': 'tru TV', 'id': 507, 'logo': 'pg4bIFyUsSIhFChqOz5Up1BxuIU.jpg'},
    {'name': 'Discovery Plus', 'id': 520, 'logo': 'wYRiUqIgWcfUvO6OPcXuUNd4tc2.jpg'},            {
        'name': 'ARROW', 'id': 529, 'logo': '4UfmxLzph9Aso9pr9bXohp0V3sr.jpg'},
    {'name': 'Plex', 'id': 538, 'logo': 'wDWvnupneMbY6RhBTHQC9zU0SCX.jpg'},                      {
        'name': 'Alamo on Demand', 'id': 547, 'logo': '1UP7ysjKolfD0rmp2fLmvyRHkdn.jpg'},
    {'name': 'Dogwoof On Demand', 'id': 536, 'logo': '9sk88OAxDZSdMOzg8VuqtGpgWQ3.jpg'},         {
        'name': 'MovieSaints', 'id': 562, 'logo': 'fdWE8jpmQqkZrwg2ZMuCLz6ms5P.jpg'},
    {'name': 'Film Movement Plus', 'id': 579, 'logo': 'tKJdVrC0fjEtQtYYjlVwX9rmqrj.jpg'},        {
        'name': 'Metrograph', 'id': 585, 'logo': '8PmpsrVDLJ3m8I37W6UNFEymhm7.jpg'},
    {'name': 'Freevee', 'id': 613, 'logo': 'uBE4RMH15mrkuz6vXzuJc7ZLXp1.jpg'},                   {
        'name': 'Kino Now', 'id': 640, 'logo': 'ttxbDVmHMuNTKcSLOyIHFs7TdRh.jpg'},
    {'name': 'ShortsTV Amazon', 'id': 688, 'logo': 'm0mvKlSjn38S9w7WVNV7a7XyPIe.jpg'},           {
        'name': 'Bet+', 'id': 1759, 'logo': 'eZVDDqlBHpuk8GELhQchRIkA6th.jpg'},
    {'name': 'ESPN Plus', 'id': 1768, 'logo': 'iJBj5b4HYbjEPiwKJWQfcRr3nP2.jpg'},                {
        'name': 'Paramount+ Showtime', 'id': 1770, 'logo': 'vfUoancVnPRAxj8iBqhllanF0Eq.jpg'},
    {'name': 'Klassiki', 'id': 1793, 'logo': 'fXGdolQR7QlHgdx2hPCxoVQG8eP.jpg'},                 {
        'name': 'Starz Amazon', 'id': 1794, 'logo': 'x36C6aseF5l4uX99Kpse9dbPwBo.jpg'},
    {'name': 'Viaplay', 'id': 76, 'logo': 'cvl65OJnz14LUlC3yGK1KHj8UYs.jpg'},                    {
        'name': 'Popflick', 'id': 1832, 'logo': 'wbKHI2d5417yAAY7QestC3qnXyo.jpg'}
]

media_lists = [
    "'tmdb_movies%'",
    "'tmdb_tv%'",
    "'tmdb_popular_people%'",
    "'tmdb_images_person%'",
    "'tmdb_media%'",
    "'tmdb_company%'",
    "'trakt_movies%'",
    "'trakt_tv%'",
    "'trakt_trending_user_lists%'",
    "'trakt_popular_user_lists%'",
    "'imdb_%'",
    "'tmdb_people%'",
    "'imdb_keyword%'",
    "'imdb_blunders%'",
    "'fenda_discover%'",
    "'fenda_FURK_T_FILE%'",
    "'fenda_pm_instant_transfer%'",
    "'fenda_rd_check_hash%'",
    "'Fenda_AD_%'",
    "'Fenda_RD_%'",
    "'Fenda_FOLDER_%'",
    "'https%'"
]

palette_basic = [
    'FFE8E8E8', 'FFF7D6D4', 'FFFCE1D0', 'FFEBE2DA', 'FFFBFBD6', 'FFDEEFD8', 'FFD5F6D8', 'FFD2ECE4', 'FFDDF3F3', 'FFD5E8F2', 'FFD6DFED', 'FFE5DCED', 'FFEDD2E1', 'FFF8E5EA',
    'FFD1D1D1', 'FFEFADA9', 'FFF9C3A2', 'FFD8C5B6', 'FFF7F7AD', 'FFBCDFB1', 'FFABECB1', 'FFA5D8C9', 'FFBAE7E7', 'FFABD1E5', 'FFAEBEDC', 'FFCBB9DA', 'FFDBA4C3', 'FFF2CCD5',
    'FFBABABA', 'FFE7847F', 'FFF6A673', 'FFC4A891', 'FFF4F483', 'FF9BD08A', 'FF80E389', 'FF78C5AE', 'FF98DCDC', 'FF81BAD8', 'FF859ECB', 'FFB096C8', 'FFCA76A6', 'FFECB2C0',
    'FFA4A4A4', 'FFDF5B54', 'FFF38844', 'FFB08B6C', 'FFF0F05A', 'FF7AC063', 'FF56DA62', 'FF4AB293', 'FF76D0D0', 'FF57A4CB', 'FF5D7EBA', 'FF9673B6', 'FFB84988', 'FFE699AB',
    'FF8D8D8D', 'FFD73229', 'FFF16A15', 'FF9D6E48', 'FFEDED31', 'FF59B03C', 'FF2CD13B', 'FF1D9F78', 'FF54C4C4', 'FF2D8DBE', 'FF345DA9', 'FF7C50A4', 'FFA71B6A', 'FFE07F96',
    'FF727272', 'FFAF2820', 'FFC55610', 'FF7F5939', 'FFC1C127', 'FF479030', 'FF23AB2F', 'FF168161', 'FF43A0A0', 'FF23729B', 'FF294B89', 'FF654085', 'FF881556', 'FFB7677A',
    'FF575757', 'FF851E19', 'FF95410C', 'FF61442C', 'FF92921D', 'FF366D24', 'FF1A8124', 'FF11624A', 'FF337979', 'FF1B5776', 'FF1F3968', 'FF4C3165', 'FF671041', 'FF8A4E5C',
    'FF3B3B3B', 'FF5A1511', 'FF652C08', 'FF422E1E', 'FF636314', 'FF254A19', 'FF125818', 'FF0C4232', 'FF235252', 'FF123B50', 'FF152747', 'FF342145', 'FF460B2C', 'FF5E353F',
    'FF181818', 'FF300B09', 'FF351805', 'FF231810', 'FF35350B', 'FF14270D', 'FF0A2E0D', 'FF06231B', 'FF132C2C', 'FF0A1F2A', 'FF0B1525', 'FF1C1224', 'FF250618', 'FF321C21'
]

palette_material_design = [
    'FFFFEBEE', 'FFFFCDD2', 'FFEF9A9A', 'FFE57373', 'FFEF5350', 'FFF44336', 'FFE53935', 'FFD32F2F', 'FFC62828', 'FFB71C1C', 'FFFF8A80', 'FFFF5252', 'FFFF1744', 'FFD50000',
    'FFFCE4EC', 'FFF8BBD0', 'FFF48FB1', 'FFF06292', 'FFEC407A', 'FFE91E63', 'FFD81B60', 'FFC2185B', 'FFAD1457', 'FF880E4F', 'FFFF80AB', 'FFFF4081', 'FFF50057', 'FFC51162',
    'FFF3E5F5', 'FFE1BEE7', 'FFCE93D8', 'FFBA68C8', 'FFAB47BC', 'FF9C27B0', 'FF8E24AA', 'FF7B1FA2', 'FF6A1B9A', 'FF4A148C', 'FFEA80FC', 'FFE040FB', 'FFD500F9', 'FFAA00FF',
    'FFEDE7F6', 'FFD1C4E9', 'FFB39DDB', 'FF9575CD', 'FF7E57C2', 'FF673AB7', 'FF5E35B1', 'FF512DA8', 'FF4527A0', 'FF311B92', 'FFB388FF', 'FF7C4DFF', 'FF651FFF', 'FF6200EA',
    'FFE8EAF6', 'FFC5CAE9', 'FF9FA8DA', 'FF7986CB', 'FF5C6BC0', 'FF3F51B5', 'FF3949AB', 'FF303F9F', 'FF283593', 'FF1A237E', 'FF8C9EFF', 'FF536DFE', 'FF3D5AFE', 'FF304FFE',
    'FFE3F2FD', 'FFBBDEFB', 'FF90CAF9', 'FF64B5F6', 'FF42A5F5', 'FF2196F3', 'FF1E88E5', 'FF1976D2', 'FF1565C0', 'FF0D47A1', 'FF82B1FF', 'FF448AFF', 'FF2979FF', 'FF2962FF',
    'FFE1F5FE', 'FFB3E5FC', 'FF81D4FA', 'FF4FC3F7', 'FF29B6F6', 'FF03A9F4', 'FF039BE5', 'FF0288D1', 'FF0277BD', 'FF01579B', 'FF80D8FF', 'FF40C4FF', 'FF00B0FF', 'FF0091EA',
    'FFE0F7FA', 'FFB2EBF2', 'FF80DEEA', 'FF4DD0E1', 'FF26C6DA', 'FF00BCD4', 'FF00ACC1', 'FF0097A7', 'FF00838F', 'FF006064', 'FF84FFFF', 'FF18FFFF', 'FF00E5FF', 'FF00B8D4',
    'FFE0F2F1', 'FFB2DFDB', 'FF80CBC4', 'FF4DB6AC', 'FF26A69A', 'FF009688', 'FF00897B', 'FF00796B', 'FF00695C', 'FF004D40', 'FFA7FFEB', 'FF64FFDA', 'FF1DE9B6', 'FF00BFA5',
    'FFE8F5E9', 'FFC8E6C9', 'FFA5D6A7', 'FF81C784', 'FF66BB6A', 'FF4CAF50', 'FF43A047', 'FF388E3C', 'FF2E7D32', 'FF1B5E20', 'FFB9F6CA', 'FF69F0AE', 'FF00E676', 'FF00C853',
    'FFF1F8E9', 'FFDCEDC8', 'FFC5E1A5', 'FFAED581', 'FF9CCC65', 'FF8BC34A', 'FF7CB342', 'FF689F38', 'FF558B2F', 'FF33691E', 'FFCCFF90', 'FFB2FF59', 'FF76FF03', 'FF64DD17',
    'FFF9FBE7', 'FFF0F4C3', 'FFE6EE9C', 'FFDCE775', 'FFD4E157', 'FFCDDC39', 'FFC0CA33', 'FFAFB42B', 'FF9E9D24', 'FF827717', 'FFF4FF81', 'FFEEFF41', 'FFC6FF00', 'FFAEEA00',
    'FFFFFDE7', 'FFFFF9C4', 'FFFFF59D', 'FFFFF176', 'FFFFEE58', 'FFFFEB3B', 'FFFDD835', 'FFFBC02D', 'FFF9A825', 'FFF57F17', 'FFFFFF8D', 'FFFFFF00', 'FFFFEA00', 'FFFFD600',
    'FFFFF8E1', 'FFFFECB3', 'FFFFE082', 'FFFFD54F', 'FFFFCA28', 'FFFFC107', 'FFFFB300', 'FFFFA000', 'FFFF8F00', 'FFFF6F00', 'FFFFE57F', 'FFFFD740', 'FFFFC400', 'FFFFAB00',
    'FFFFF3E0', 'FFFFE0B2', 'FFFFCC80', 'FFFFB74D', 'FFFFA726', 'FFFF9800', 'FFFB8C00', 'FFF57C00', 'FFEF6C00', 'FFE65100', 'FFFFD180', 'FFFFAB40', 'FFFF9100', 'FFFF6D00',
    'FFFBE9E7', 'FFFFCCBC', 'FFFFAB91', 'FFFF8A65', 'FFFF7043', 'FFFF5722', 'FFF4511E', 'FFE64A19', 'FFD84315', 'FFBF360C', 'FFFF9E80', 'FFFF6E40', 'FFFF3D00', 'FFDD2C00',
    'FFEFEBE9', 'FFD7CCC8', 'FFBCAAA4', 'FFA1887F', 'FF8D6E63', 'FF795548', 'FF6D4C41', 'FF5D4037', 'FF4E342E', 'FF3E2723', 'FF7F7F7F', 'C07F7F7F', '817F7F7F', '417F7F7F',
    'FFFAFAFA', 'FFF5F5F5', 'FFEEEEEE', 'FFE0E0E0', 'FFBDBDBD', 'FF9E9E9E', 'FF757575', 'FF616161', 'FF424242', 'FF212121', 'FFFFFFFF', 'C0FFFFFF', '81FFFFFF', '41FFFFFF',
    'FFECEFF1', 'FFCFD8DC', 'FFB0BEC5', 'FF90A4AE', 'FF78909C', 'FF607D8B', 'FF546E7A', 'FF455A64', 'FF37474F', 'FF263238', 'FF000000', 'C0000000', '81000000', '41000000'
]

palette_rainbow = [
    'FFFFFFE3', 'FFFFFAE6', 'FFFEF5E6', 'FFFEF0E5', 'FFFEEBE5', 'FFFFEFEF', 'FFFFE6EA', 'FFFFE6F1', 'FFFEE6F4', 'FFFFE6FB', 'FFFEE6FE', 'FFFAE6FF', 'FFF4E6FF', 'FFF0E6FF',
    'FFEAE7FC', 'FFE6E7FC', 'FFE6EBFF', 'FFE7F0FF', 'FFE7F5FF', 'FFE7FAFF', 'FFE6FFFF', 'FFE6FFFB', 'FFE7FEF4', 'FFE7FFF1', 'FFE6FFEA', 'FFE7FFE7', 'FFEBFFF3', 'FFF1FFE6',
    'FFF5FFE6', 'FFFBFFE6', 'FFFFFFFF', 'FFFFFFCB', 'FFFEFACA', 'FFFFEACB', 'FFFFE0CC', 'FFFED6CC', 'FFFFCACD', 'FFFFCCD5', 'FFFFCDE0', 'FFFFCCEB', 'FFFFCBF5', 'FFFECCFD',
    'FFF6CBFF', 'FFECCCFE', 'FFE0CCFF', 'FFD6CCFE', 'FFCCCCFE', 'FFCDD6FF', 'FFCAE1FF', 'FFCCEBFF', 'FFCEF4FD', 'FFCAFFFF', 'FFCCFFF6', 'FFCBFEEB', 'FFCCFFE0', 'FFCCFFD6',
    'FFCDFFCC', 'FFD7FFCB', 'FFE1FFCD', 'FFEBFFCC', 'FFF5FFCB', 'FFEFEFEF', 'FFFEFFB3', 'FFFFF1B2', 'FFFFE0B2', 'FFFDD2B2', 'FFFFC2B3', 'FFFFB3B3', 'FFFFB2C2', 'FFFFB3D1',
    'FFFFB3E1', 'FFFFB2F4', 'FFFFB3FE', 'FFF0B3FF', 'FFE1B2FF', 'FFD2B3FF', 'FFC1B3FE', 'FFB4B3FF', 'FFB3C1FE', 'FFB2D1FF', 'FFB3E0FF', 'FFB2F0FF', 'FFB3FFFF', 'FFB3FFF0',
    'FFB4FFE0', 'FFB3FFD1', 'FFB4FEC3', 'FFB3FFB4', 'FFC2FFB2', 'FFD1FFB4', 'FFE0FFB3', 'FFF1FFB4', 'FFE0E0E0', 'FFFEFF99', 'FFFFEB9A', 'FFFED699', 'FFFFC299', 'FFFFAD98',
    'FFFF9899', 'FFFF99AE', 'FFFF99C1', 'FFFE99D5', 'FFFF99EC', 'FFFF99FF', 'FFEB99FF', 'FFD699FF', 'FFC299FF', 'FFAE99FF', 'FF9A99FF', 'FF98ADFE', 'FF9AC2FF', 'FF98D6FF',
    'FF99EBFF', 'FF99FFFF', 'FF99FFEA', 'FF99FFD7', 'FF9AFFC3', 'FF99FFAC', 'FF99FF99', 'FFADFF99', 'FFC2FF98', 'FFD6FF99', 'FFEAFF98', 'FFD0D0D0', 'FFFFFF80', 'FFFFE681',
    'FFFFCC80', 'FFFFB381', 'FFFF9980', 'FFFE8081', 'FFFF8199', 'FFFF80B3', 'FFFF80CD', 'FFFF80E7', 'FFFC81FE', 'FFE680FF', 'FFCC7FFF', 'FFB380FF', 'FF9980FF', 'FF807FFE',
    'FF8099FE', 'FF7FB3FF', 'FF80CCFE', 'FF80E6FF', 'FF7FFFFE', 'FF7FFEE0', 'FF80FFCC', 'FF80FFB2', 'FF80FF98', 'FF81FF81', 'FF99FF80', 'FFB3FF80', 'FFCCFF80', 'FFE6FF80',
    'FFC0C0C0', 'FFFFFF6B', 'FFFEE066', 'FFFFC267', 'FFFFA366', 'FFFF8566', 'FFFF6766', 'FFFF6685', 'FFFF66A4', 'FFFF66C1', 'FFFF66E0', 'FFFF66FF', 'FFE166FF', 'FFC366FF',
    'FFA366FF', 'FF8566FF', 'FF6665FE', 'FF6785FF', 'FF66A3FE', 'FF65C2FF', 'FF65E0FF', 'FF65FFFF', 'FF66FFE0', 'FF65FFC1', 'FF66FFA4', 'FF65FF85', 'FF66FF66', 'FF84FF66',
    'FFA2FF66', 'FFC2FF66', 'FFE0FF66', 'FFAFAFAF', 'FFFFFF4D', 'FFFFDB4E', 'FFFFB84E', 'FFFF944C', 'FFFF714D', 'FFFF4D4D', 'FFFF4D6F', 'FFFE4D93', 'FFFE4DB7', 'FFFE4DDB',
    'FFFF4DFF', 'FFDC4DFF', 'FFB84DFF', 'FF944EFF', 'FF704DFF', 'FF4D4CFF', 'FF4D70FE', 'FF4D94FE', 'FF4DB8FF', 'FF4DDBFF', 'FF4DFFFF', 'FF4DFFDB', 'FF4EFFB9', 'FF4EFF95',
    'FF4DFE70', 'FF4CFF4C', 'FF70FF4D', 'FF94FF4D', 'FFB8FE4D', 'FFDAFF4D', 'FF8C8C8C', 'FFFFFF33', 'FFFFD634', 'FFFFAD33', 'FFFF8532', 'FFFF5C33', 'FFFF3334', 'FFFF335C',
    'FFFF3287', 'FFFF33AE', 'FFFF33D6', 'FFFE33FF', 'FFD633FE', 'FFAD34FF', 'FF8534FF', 'FF5D33FF', 'FF3233FF', 'FF325CFE', 'FF3285FF', 'FF33ADFF', 'FF33D6FF', 'FF33FFFE',
    'FF32FFD6', 'FF34FFAD', 'FF33FF84', 'FF32FF5C', 'FF34FF33', 'FF5CFF34', 'FF85FE33', 'FFADFE33', 'FFD5FF33', 'FF7C7C7C', 'FFFFFF19', 'FFFFD119', 'FFFFA418', 'FFFF751A',
    'FFFF4719', 'FFFF1919', 'FFFF1947', 'FFFF1874', 'FFFF19A3', 'FFFF19D1', 'FFFF19FF', 'FFD019FF', 'FFA219FF', 'FF751AFE', 'FF4719FF', 'FF1819FF', 'FF1947FF', 'FF1974FF',
    'FF19A3FE', 'FF18D1FF', 'FF19FFFF', 'FF19FFD1', 'FF19FFA4', 'FF18FF75', 'FF19FF47', 'FF19FF19', 'FF48FF19', 'FF76FF19', 'FFA3FE1A', 'FFD1FF19', 'FF6B6B6B', 'FFFFFF00',
    'FFFFCC00', 'FFFE9900', 'FFFF6600', 'FFFF3300', 'FFFE0000', 'FFFE0032', 'FFFF0066', 'FFFF0198', 'FFFF00CC', 'FFFF00FE', 'FFCC00FF', 'FF9A00FF', 'FF6601FF', 'FF3300FF',
    'FF0000FE', 'FF0033FF', 'FF0166FF', 'FF0097FE', 'FF00CCFF', 'FF00FFFF', 'FF01FFCD', 'FF00FF99', 'FF00FE67', 'FF00FF33', 'FF00FF01', 'FF33FF00', 'FF65FF00', 'FF99FE00',
    'FFCCFF00', 'FF5D5D5D', 'FFE8E500', 'FFE6B800', 'FFE68B00', 'FFE65C01', 'FFE72E00', 'FFE60000', 'FFE6002E', 'FFE6005B', 'FFE80183', 'FFE600B8', 'FFE600E6', 'FFB700E6',
    'FF8900E6', 'FF5C01E5', 'FF2E00E6', 'FF0000E6', 'FF012EE1', 'FF005BE7', 'FF008AE5', 'FF00B8E6', 'FF00E6E6', 'FF00E6B7', 'FF00E78B', 'FF00E65F', 'FF00E532', 'FF00E600',
    'FF2FE600', 'FF5DE600', 'FF8AE501', 'FFB8E600', 'FF4F4F4F', 'FFCDCC00', 'FFCDA301', 'FFCA7B02', 'FFCC5200', 'FFCC2900', 'FFCC0001', 'FFCD0029', 'FFCE0052', 'FFCC007B',
    'FFCD00A3', 'FFCB00CC', 'FFA300CB', 'FF7A01CC', 'FF5201CC', 'FF2A00D0', 'FF0000CC', 'FF0029CB', 'FF0052CC', 'FF007ACD', 'FF00A3CC', 'FF00CCCB', 'FF00CCA3', 'FF01CC7A',
    'FF03CB51', 'FF00CC29', 'FF01CC00', 'FF29CC01', 'FF52CB00', 'FF7ACB00', 'FFA2CC00', 'FF434343', 'FFB4B300', 'FFB38E00', 'FFB36B00', 'FFB34700', 'FFB32501', 'FFB30101',
    'FFB40025', 'FFB40047', 'FFB4006B', 'FFB5008B', 'FFB300B3', 'FF8F00B2', 'FF6B00B2', 'FF4700B4', 'FF2300B2', 'FF0000B2', 'FF0025B4', 'FF0047B3', 'FF006BB3', 'FF008EB2',
    'FF00B3B2', 'FF00B38E', 'FF00B36C', 'FF00B346', 'FF00B324', 'FF00B300', 'FF24B301', 'FF47B200', 'FF6CB201', 'FF90B301', 'FF373737', 'FF999A00', 'FF987A00', 'FF995C01',
    'FF9A3D00', 'FF9A1F00', 'FF990100', 'FF99001F', 'FF9A003E', 'FF99005B', 'FF9A007A', 'FF990099', 'FF7B0099', 'FF5D0099', 'FF3D0099', 'FF1F0099', 'FF000098', 'FF011F99',
    'FF003D98', 'FF005C99', 'FF007A99', 'FF009999', 'FF00997A', 'FF00995B', 'FF00993E', 'FF00991F', 'FF009900', 'FF1E9900', 'FF3C9900', 'FF5C9900', 'FF7A9900', 'FF2E2E2E',
    'FF7F8000', 'FF7F6601', 'FF804C00', 'FF803201', 'FF801A01', 'FF800000', 'FF800019', 'FF800033', 'FF80004B', 'FF810065', 'FF81007F', 'FF660080', 'FF4C007F', 'FF33007F',
    'FF1A0080', 'FF010080', 'FF011A7F', 'FF003480', 'FF004C80', 'FF00667F', 'FF008081', 'FF008067', 'FF037F4B', 'FF008033', 'FF00801B', 'FF008001', 'FF1A8000', 'FF338000',
    'FF4C8001', 'FF668100', 'FF242424', 'FF656600', 'FF675201', 'FF653D00', 'FF672900', 'FF661400', 'FF660000', 'FF660015', 'FF660028', 'FF65003C', 'FF660053', 'FF660066',
    'FF550069', 'FF3D0067', 'FF290066', 'FF150067', 'FF010066', 'FF001465', 'FF012966', 'FF003D66', 'FF005267', 'FF006766', 'FF006651', 'FF00663E', 'FF01662A', 'FF006613',
    'FF006600', 'FF146600', 'FF296600', 'FF3D6600', 'FF516600', 'FF181818', 'FF4B4C00', 'FF4C3E01', 'FF4D2E00', 'FF4C1F00', 'FF4D0F00', 'FF4C0000', 'FF4C000F', 'FF4B001F',
    'FF4C002E', 'FF4C003E', 'FF4C004B', 'FF3D004D', 'FF2E004B', 'FF1F004C', 'FF0E004B', 'FF01004C', 'FF000E4B', 'FF001F4D', 'FF012E4D', 'FF003D4C', 'FF004C4C', 'FF004D3D',
    'FF004C2E', 'FF004C1E', 'FF004C0E', 'FF004C01', 'FF0F4C00', 'FF204C01', 'FF2D4C00', 'FF3E4C01', 'FF000000'
]

palette_web = [
    'FF5D8AA8', 'FFF0F8FF', 'FFE32636', 'FFEFDECD', 'FFE52B50', 'FFFFBF00', 'FFFF7E00', 'FFFF033E', 'FF9966CC', 'FFA4C639', 'FFF2F3F4', 'FFCD9575', 'FF915C83', 'FFFAEBD7',
    'FF008000', 'FF8DB600', 'FFFBCEB1', 'FF00FFFF', 'FF7FFFD4', 'FF4B5320', 'FFE9D66B', 'FFB2BEB5', 'FF87A96B', 'FFFF9966', 'FFA52A2A', 'FFFDEE00', 'FF6E7F80', 'FFFF2052',
    'FF007FFF', 'FFF0FFFF', 'FF89CFF0', 'FFA1CAF1', 'FFF4C2C2', 'FF21ABCD', 'FFFAE7B5', 'FFFFE135', 'FF848482', 'FF98777B', 'FFBCD4E6', 'FF9F8170', 'FFF5F5DC', 'FFFFE4C4',
    'FF3D2B1F', 'FFFE6F5E', 'FF000000', 'FFFFEBCD', 'FF318CE7', 'FFACE5EE', 'FFFAF0BE', 'FF0000FF', 'FF0093AF', 'FF0087BD', 'FF333399', 'FF0247FE', 'FFA2A2D0', 'FF6699CC',
    'FF0D98BA', 'FF8A2BE2', 'FFDE5D83', 'FF79443B', 'FF0095B6', 'FFCC0000', 'FF873260', 'FF0070FF', 'FFB5A642', 'FFCB4154', 'FF1DACD6', 'FF66FF00', 'FFBF94E4', 'FFC32148',
    'FFFF007F', 'FF08E8DE', 'FFD19FE8', 'FFF4BBFF', 'FFFF55A3', 'FFFB607F', 'FF004225', 'FFCD7F32', 'FF964B00', 'FFA52A2A', 'FFFFC1CC', 'FFE7FEFF', 'FFF0DC82', 'FF480607',
    'FF800020', 'FFDEB887', 'FFCC5500', 'FFE97451', 'FF8A3324', 'FFBD33A4', 'FF702963', 'FF536872', 'FF5F9EA0', 'FF91A3B0', 'FF006B3C', 'FFED872D', 'FFE30022', 'FFFFF600',
    'FFA67B5B', 'FF4B3621', 'FF1E4D2B', 'FFA3C1AD', 'FFC19A6B', 'FF78866B', 'FFFFEF00', 'FFFF0800', 'FFE4717A', 'FF00BFFF', 'FF592720', 'FFC41E3A', 'FF00CC99', 'FFFF0040',
    'FFEB4C42', 'FFFF0038', 'FFFFA6C9', 'FFB31B1B', 'FF99BADD', 'FFED9121', 'FFACE1AF', 'FFB2FFFF', 'FF4997D0', 'FFDE3163', 'FFEC3B83', 'FF007BA7', 'FF2A52BE', 'FF007AA5',
    'FFE03C31', 'FFA0785A', 'FFFAD6A5', 'FF36454F', 'FFDFFF00', 'FF7FFF00', 'FFFFB7C5', 'FFCD5C5C', 'FF7B3F00', 'FFD2691E', 'FFFFA700', 'FF98817B', 'FFE34234', 'FFD2691E',
    'FFE4D00A', 'FFFBCCE7', 'FF0047AB', 'FFD2691E', 'FF6F4E37', 'FF9BDDFF', 'FF002E63', 'FF8C92AC', 'FFB87333', 'FF996666', 'FFFF3800', 'FFFF7F50', 'FFF88379', 'FFFF4040',
    'FF893F45', 'FFFBEC5D', 'FFB31B1B', 'FF6495ED', 'FFFFF8DC', 'FFFFF8E7', 'FFFFBCD9', 'FFFFFDD0', 'FFDC143C', 'FFBE0032', 'FF00FFFF', 'FF00B7EB', 'FFFFFF31', 'FFF0E130',
    'FF011222', 'FF654321', 'FF5D3954', 'FFA40000', 'FF08457E', 'FF986960', 'FFCD5B45', 'FF008B8B', 'FF536878', 'FFB8860B', 'FFA9A9A9', 'FF013220', 'FF1A2421', 'FFBDB76B',
    'FF483C32', 'FF734F96', 'FF8B008B', 'FF003366', 'FF556B2F', 'FFFF8C00', 'FF9932CC', 'FF779ECB', 'FF03C03C', 'FF966FD6', 'FFC23B22', 'FFE75480', 'FF003399', 'FF872657',
    'FF8B0000', 'FFE9967A', 'FF560319', 'FF8FBC8F', 'FF3C1414', 'FF483D8B', 'FF2F4F4F', 'FF177245', 'FF918151', 'FFFFA812', 'FF483C32', 'FFCC4E5C', 'FF00CED1', 'FF9400D3',
    'FF00693E', 'FF555555', 'FFD70A53', 'FFA9203E', 'FFEF3038', 'FFE9692C', 'FFDA3287', 'FFFAD6A5', 'FFB94E48', 'FF704241', 'FFC154C1', 'FF004B49', 'FF9955BB', 'FFCC00CC',
    'FFFFCBA4', 'FFFF1493', 'FFFF9933', 'FF00BFFF', 'FF1560BD', 'FFC19A6B', 'FFEDC9AF', 'FF696969', 'FF1E90FF', 'FFD71868', 'FF85BB65', 'FF967117', 'FF00009C', 'FFE1A95F',
    'FFC2B280', 'FF614051', 'FFF0EAD6', 'FF1034A6', 'FF7DF9FF', 'FFFF003F', 'FF00FFFF', 'FF00FF00', 'FF6F00FF', 'FFF4BBFF', 'FFCCFF00', 'FFBF00FF', 'FF3F00FF', 'FF8F00FF',
    'FFFFFF00', 'FF50C878', 'FF96C8A2', 'FFC19A6B', 'FF801818', 'FFB53389', 'FFF400A1', 'FFE5AA70', 'FF4D5D53', 'FF4F7942', 'FFFF2800', 'FF6C541E', 'FFB22222', 'FFCE2029',
    'FFE25822', 'FFFC8EAC', 'FFF7E98E', 'FFEEDC82', 'FFFFFAF0', 'FFFFBF00', 'FFFF1493', 'FFCCFF00', 'FFFF004F', 'FF014421', 'FF228B22', 'FFA67B5B', 'FF0072BB', 'FF86608E',
    'FFF64A8A', 'FFFF00FF', 'FFFF77FF', 'FFE48400', 'FFCC6666', 'FFDCDCDC', 'FFE49B0F', 'FFF8F8FF', 'FFB06500', 'FF6082B6', 'FFE6E8FA', 'FFD4AF37', 'FFFFD700', 'FF996515',
    'FFFCC200', 'FFFFDF00', 'FFDAA520', 'FFA8E4A0', 'FF808080', 'FF7F7F7F', 'FFBEBEBE', 'FF465945', 'FF00FF00', 'FF008000', 'FF00A877', 'FF009F6B', 'FF00A550', 'FF66B032',
    'FFADFF2F', 'FFA99A86', 'FF00FF7F', 'FF663854', 'FF446CCF', 'FF5218FA', 'FFE9D66B', 'FF3FFF00', 'FFC90016', 'FFDA9100', 'FF808000', 'FFDF73FF', 'FFF400A1', 'FFF0FFF0',
    'FF007000', 'FFFF1DCE', 'FFFF69B4', 'FF355E3B', 'FFFCF75E', 'FFB2EC5D', 'FF138808', 'FFCD5C5C', 'FFE3A857', 'FF00416A', 'FF4B0082', 'FF002FA7', 'FFFF4F00', 'FF5A4FCF',
    'FFF4F0EC', 'FF009000', 'FFFFFFF0', 'FF00A86B', 'FFF8DE7E', 'FFD73B3E', 'FFA50B5E', 'FFFADA5E', 'FFBDDA57', 'FF29AB87', 'FF4CBB17', 'FFC3B091', 'FFF0E68C', 'FFE8000D',
    'FF087830', 'FFD6CADD', 'FF26619C', 'FFFEFE22', 'FFA9BA9D', 'FFCF1020', 'FFB57EDC', 'FFE6E6FA', 'FFCCCCFF', 'FFFFF0F5', 'FFC4C3D0', 'FF9457EB', 'FFEE82EE', 'FFE6E6FA',
    'FFFBAED2', 'FF967BB6', 'FFFBA0E3', 'FF7CFC00', 'FFFFF700', 'FFFFFACD', 'FFFDD5B1', 'FFADD8E6', 'FFB5651D', 'FFE66771', 'FFF08080', 'FF93CCEA', 'FFF56991', 'FFE0FFFF',
    'FFF984EF', 'FFFAFAD2', 'FFD3D3D3', 'FF90EE90', 'FFF0E68C', 'FFB19CD9', 'FFFFB6C1', 'FFFFA07A', 'FFFF9999', 'FF20B2AA', 'FF87CEFA', 'FF778899', 'FFB38B6D', 'FFE68FAC',
    'FFFFFFED', 'FFC8A2C8', 'FFBFFF00', 'FF00FF00', 'FF32CD32', 'FF195905', 'FFFAF0E6', 'FFC19A6B', 'FF534B4F', 'FFE62020', 'FFFF00FF', 'FFCA1F7B', 'FFFF0090', 'FFAAF0D1',
    'FFF8F4FF', 'FFC04000', 'FF00B8FF', 'FFFBEC5D', 'FF6050DC', 'FF0BDA51', 'FF979AAA', 'FFFF8243', 'FF74C365', 'FF800000', 'FFB03060', 'FFE0B0FF', 'FF915F6D', 'FFEF98AA',
    'FF73C2FB', 'FFE5B73B', 'FF66DDAA', 'FF0000CD', 'FFE2062C', 'FFAF4035', 'FFF3E5AB', 'FF035096', 'FF1C352D', 'FFDDA0DD', 'FFBA55D3', 'FF0067A5', 'FF9370DB', 'FFBB3385',
    'FF3CB371', 'FF7B68EE', 'FFC9DC87', 'FF00FA9A', 'FF674C47', 'FF0054B4', 'FF48D1CC', 'FFC71585', 'FFFDBCB4', 'FF191970', 'FF004953', 'FFFFC40C', 'FF3EB489', 'FFF5FFFA',
    'FF98FF98', 'FFFFE4E1', 'FFFAEBD7', 'FF967117', 'FF73A9C2', 'FFAE0C00', 'FFADDFAD', 'FF30BA8F', 'FF997A8D', 'FFC54B8C', 'FFF2F3F4', 'FFFFDB58', 'FF21421E', 'FF18453B',
    'FFF6ADC6', 'FF2A8000', 'FFFADA5E', 'FFFFDEAD', 'FF000080', 'FFFFA343', 'FFFE59C2', 'FF39FF14', 'FFA4DDED', 'FF059033', 'FF0077BE', 'FFCC7722', 'FF008000', 'FFCFB53B',
    'FFFDF5E6', 'FF796878', 'FF673147', 'FFC08081', 'FF808000', 'FF6B8E23', 'FF3C341F', 'FF9AB973', 'FF0F0F0F', 'FFB784A7', 'FFFB9902', 'FFFFA500', 'FFFF9F00', 'FFFF4500',
    'FFDA70D6', 'FF654321', 'FF414A4C', 'FFFF6E4A', 'FF002147', 'FF990000', 'FF006600', 'FF273BE2', 'FF682860', 'FFBCD4E6', 'FFAFEEEE', 'FF987654', 'FFAF4035', 'FF9BC4E2',
    'FFDDADAF', 'FFDA8A67', 'FFABCDEF', 'FFE6BE8A', 'FFEEE8AA', 'FF98FB98', 'FFDCD0FF', 'FFF984E5', 'FFFADADD', 'FFDDA0DD', 'FFDB7093', 'FF96DED1', 'FFC9C0BB', 'FFECEBBD',
    'FFBC987E', 'FFDB7093', 'FF78184A', 'FFFFEFD5', 'FF50C878', 'FFAEC6CF', 'FF836953', 'FFCFCFC4', 'FF77DD77', 'FFF49AC2', 'FFFFB347', 'FFFFD1DC', 'FFB39EB5', 'FFFF6961',
    'FFCB99C9', 'FFFDFD96', 'FF800080', 'FF40404F', 'FFFFE5B4', 'FFFFCC99', 'FFFFDAB9', 'FFFADFAD', 'FFD1E231', 'FFEAE0C8', 'FF88D8C0', 'FFE6E200', 'FFCCCCFF', 'FF1C39BB',
    'FF00A693', 'FF32127A', 'FFD99058', 'FFF77FBE', 'FF701C1C', 'FFCC3333', 'FFFE28A2', 'FFDF00FF', 'FF000F89', 'FF123524', 'FFFDDDE6', 'FF01796F', 'FFFFC0CB', 'FFFF9966',
    'FFE7ACCF', 'FFF78FA7', 'FF93C572', 'FFE5E4E2', 'FF8E4585', 'FFDDA0DD', 'FFFF5A36', 'FFB0E0E6', 'FFFF8F00', 'FF701C1C', 'FF003153', 'FFDF00FF', 'FFCC8899', 'FFFF7518',
    'FF800080', 'FF9F00C5', 'FFA020F0', 'FF69359C', 'FF9678B6', 'FFFE4EDA', 'FF50404D', 'FF51484F', 'FFFF355E', 'FFE30B5D', 'FF915F6D', 'FFE25098', 'FFB3446C', 'FF826644',
    'FFFF33CC', 'FFE3256B', 'FFFF0000', 'FFF2003C', 'FFC40233', 'FFED1C24', 'FFFE2712', 'FFA52A2A', 'FFC71585', 'FFAB4E52', 'FF004040', 'FFF1A7FE', 'FFD70040', 'FF0892D0',
    'FFA76BCF', 'FFB666D2', 'FFB03060', 'FF414833', 'FF00CCCC', 'FFFF007F', 'FFF9429E', 'FF674846', 'FFB76E79', 'FFE32636', 'FFFF66CC', 'FFAA98A9', 'FF905D5D', 'FFAB4E52',
    'FF65000B', 'FFD40000', 'FFBC8F8F', 'FF0038A8', 'FF002366', 'FF4169E1', 'FFCA2C92', 'FF7851A9', 'FFE0115F', 'FFFF0028', 'FFBB6528', 'FFE18E96', 'FFA81C07', 'FF80461B',
    'FFB7410E', 'FF00563F', 'FF8B4513', 'FFFF6700', 'FFF4C430', 'FF23297A', 'FFFF8C69', 'FFFF91A4', 'FFC2B280', 'FF967117', 'FFECD540', 'FFF4A460', 'FF967117', 'FF507D2A',
    'FF0F52BA', 'FFCBA135', 'FFFF2400', 'FFFFD800', 'FF76FF7A', 'FF2E8B57', 'FF321414', 'FFFFF5EE', 'FFFFBA00', 'FF704214', 'FF8A795D', 'FF009E60', 'FFFC0FC0', 'FF882D17',
    'FFC0C0C0', 'FFCB410B', 'FF007474', 'FF87CEEB', 'FFCF71AF', 'FF6A5ACD', 'FF708090', 'FF003399', 'FF933D41', 'FF100C08', 'FFFFFAFA', 'FF0FC0FC', 'FFFEFDFF', 'FFA7FC00',
    'FF00FF7F', 'FF4682B4', 'FFFADA5E', 'FF990000', 'FFE4D96F', 'FFFFCC33', 'FFFAD6A5', 'FFD2B48C', 'FFF94D00', 'FFF28500', 'FFFFCC00', 'FF483C32', 'FF8B8589', 'FFD0F0C0',
    'FFF88379', 'FFF4C2C2', 'FF008080', 'FF367588', 'FF006D5B', 'FFCD5700', 'FFE2725B', 'FFD8BFD8', 'FFDE6FA1', 'FFFC89AC', 'FF0ABAB5', 'FFE08D3C', 'FFDBD7D2', 'FFEEE600',
    'FFFF6347', 'FF746CC0', 'FFFFC87C', 'FFFD0E35', 'FF808080', 'FF00755E', 'FF0073CF', 'FF417DC1', 'FFDEAA88', 'FFB57281', 'FF30D5C8', 'FF00FFEF', 'FFA0D6B4', 'FF66424D',
    'FF8A496B', 'FF66023C', 'FF0033AA', 'FFD9004C', 'FF8878C3', 'FF536895', 'FFFFB300', 'FF3CD070', 'FF120A8F', 'FF4166F5', 'FFFF6FFF', 'FF635147', 'FF5B92E5', 'FFB78727',
    'FFFFFF66', 'FF014421', 'FF7B1113', 'FFAE2029', 'FFE1AD21', 'FF990000', 'FFFFCC00', 'FFD3003F', 'FFF3E5AB', 'FFC5B358', 'FFC80815', 'FF43B3AE', 'FFE34234', 'FFA020F0',
    'FF8F00FF', 'FF7F00FF', 'FF8601AF', 'FFEE82EE', 'FF40826D', 'FF922724', 'FF9F1D35', 'FFDA1D81', 'FFFFA089', 'FF9F00FF', 'FF004242', 'FF645452', 'FFF5DEB3', 'FFFFFFFF',
    'FFF5F5F5', 'FFA2ADD0', 'FFFF43A4', 'FFFC6C85', 'FF722F37', 'FFC9A0DC', 'FF738678', 'FF0F4D92', 'FFFFFF00', 'FFEFCC00', 'FFFFD300', 'FFFFEF00', 'FFFEFE33', 'FF9ACD32',
    'FFFFAE42', 'FF0014A8', 'FF2C1608'
]
