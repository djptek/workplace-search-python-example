# Create a deployment of Elastic Enterprise Search
# https://cloud.elastic.co/deployments/create
#
# Choose Workplace Search
# From Elastic Cloud Workplace Search Setup =>
# copy Enterprise Search API endpoint
enterprise_search_endpoint = ''

# From the Workplace Search Deployment =>
# From Create Custom Source Dialogue =>
# copy Custom API Source Access Token
custom_api_source_access_token = ''
# copy Custom API Source Access Key
custom_api_source_key = ''

# install elastic_workplace_search package
try:
    from elastic_workplace_search import Client
except ImportError as e:
    pass  # module not installed, fix that
    print("Error {}, installing".format(e))
    import pip
    pip.main(['install', 'elastic_workplace_search', '--upgrade'])
    from elastic_workplace_search import Client

# create a Client to access the service
client = Client(custom_api_source_access_token,
                enterprise_search_endpoint + "/api/ws/v1")

# Custom Source Documents
# An Array of Documents as JSON Key/Value pairs
documents = [
    {
        "id":
        "wii-sports-wii-2006",
        "name":
        "Wii Sports",
        "year":
        2006,
        "platform":
        "Wii",
        "genre":
        "Sports",
        "publisher":
        "Nintendo",
        "global_sales":
        82.53,
        "critic_score":
        76,
        "user_score":
        8,
        "developer":
        "Nintendo",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Wii_Sports_Europe.jpg/220px-Wii_Sports_Europe.jpg"
    },
    {
        "id":
        "mario-kart-wii-wii-2008",
        "name":
        "Mario Kart Wii",
        "year":
        2008,
        "platform":
        "Wii",
        "genre":
        "Racing",
        "publisher":
        "Nintendo",
        "global_sales":
        35.52,
        "critic_score":
        82,
        "user_score":
        8,
        "developer":
        "Nintendo",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/d/d6/Mario_Kart_Wii.png/220px-Mario_Kart_Wii.png"
    },
    {
        "id":
        "wii-sports-resort-wii-2009",
        "name":
        "Wii Sports Resort",
        "year":
        2009,
        "platform":
        "Wii",
        "genre":
        "Sports",
        "publisher":
        "Nintendo",
        "global_sales":
        32.77,
        "critic_score":
        80,
        "user_score":
        8,
        "developer":
        "Nintendo",
        "image_url":
        "https://www.mobygames.com/images/covers/l/207776-wii-sports-resort-wii-front-cover.png"
    },
    {
        "id":
        "new-super-mario-bros-ds-2006",
        "name":
        "New Super Mario Bros.",
        "year":
        2006,
        "platform":
        "DS",
        "genre":
        "Platform",
        "publisher":
        "Nintendo",
        "global_sales":
        29.8,
        "critic_score":
        89,
        "user_score":
        8,
        "developer":
        "Nintendo",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/NewSuperMarioBrothers.jpg/220px-NewSuperMarioBrothers.jpg"
    },
    {
        "id":
        "wii-play-wii-2006",
        "name":
        "Wii Play",
        "year":
        2006,
        "platform":
        "Wii",
        "genre":
        "Misc",
        "publisher":
        "Nintendo",
        "global_sales":
        28.92,
        "critic_score":
        58,
        "user_score":
        6,
        "developer":
        "Nintendo",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Wii_Play_Europe.jpg/220px-Wii_Play_Europe.jpg"
    },
    {
        "id": "new-super-mario-bros-wii-wii-2009",
        "name": "New Super Mario Bros. Wii",
        "year": 2009,
        "platform": "Wii",
        "genre": "Platform",
        "publisher": "Nintendo",
        "global_sales": 28.32,
        "critic_score": 87,
        "user_score": 8,
        "developer": "Nintendo",
        "image_url": "https://i.ytimg.com/vi/thc0YRXTHB4/maxresdefault.jpg"
    },
    {
        "id":
        "mario-kart-ds-ds-2005",
        "name":
        "Mario Kart DS",
        "year":
        2005,
        "platform":
        "DS",
        "genre":
        "Racing",
        "publisher":
        "Nintendo",
        "global_sales":
        23.21,
        "critic_score":
        91,
        "user_score":
        8,
        "developer":
        "Nintendo",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/a/ad/Mario_Kart_DS_screenshot.png/220px-Mario_Kart_DS_screenshot.png"
    },
    {
        "id":
        "wii-fit-wii-2007",
        "name":
        "Wii Fit",
        "year":
        2007,
        "platform":
        "Wii",
        "genre":
        "Sports",
        "publisher":
        "Nintendo",
        "global_sales":
        22.7,
        "critic_score":
        80,
        "user_score":
        7,
        "developer":
        "Nintendo",
        "image_url":
        "https://www.mobygames.com/images/covers/l/123314-wii-fit-wii-other.jpg"
    },
    {
        "id":
        "kinect-adventures-x360-2010",
        "name":
        "Kinect Adventures!",
        "year":
        2010,
        "platform":
        "X360",
        "genre":
        "Misc",
        "publisher":
        "Microsoft Game Studios",
        "global_sales":
        21.81,
        "critic_score":
        61,
        "user_score":
        6,
        "developer":
        "Good Science Studio",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BZTIzYzUzYmQtOGQ1Ni00NjkzLThhNzgtYTM4ZTE2MjYxMTJkXkEyXkFqcGdeQXVyNjE4Njk5NTM@._V1_.jpg"
    },
    {
        "id":
        "wii-fit-plus-wii-2009",
        "name":
        "Wii Fit Plus",
        "year":
        2009,
        "platform":
        "Wii",
        "genre":
        "Sports",
        "publisher":
        "Nintendo",
        "global_sales":
        21.79,
        "critic_score":
        80,
        "user_score":
        7,
        "developer":
        "Nintendo",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BOTZmMjZkOWMtYmRhMC00MTY5LThhMTQtNThiZDdiMTYxMTg4XkEyXkFqcGdeQXVyNzg5OTk2OA@@._V1_.jpg"
    },
    {
        "id":
        "grand-theft-auto-v-ps3-2013",
        "name":
        "Grand Theft Auto V",
        "year":
        2013,
        "platform":
        "PS3",
        "genre":
        "Action",
        "publisher":
        "Take-Two Interactive",
        "global_sales":
        21.04,
        "critic_score":
        97,
        "user_score":
        8,
        "developer":
        "Rockstar North",
        "image_url":
        "https://pmcvariety.files.wordpress.com/2013/09/gta-v-big.jpg?w=1000&h=563&crop=1"
    },
    {
        "id":
        "grand-theft-auto-san-andreas-ps2-2004",
        "name":
        "Grand Theft Auto: San Andreas",
        "year":
        2004,
        "platform":
        "PS2",
        "genre":
        "Action",
        "publisher":
        "Take-Two Interactive",
        "global_sales":
        20.81,
        "critic_score":
        95,
        "user_score":
        9,
        "developer":
        "Rockstar North",
        "image_url":
        "http://4.bp.blogspot.com/-IITyrVJdS50/Udvw7XLG-oI/AAAAAAAASwY/H1j2GYBjXng/s1600/GTA+SA+0.jpg"
    },
    {
        "id":
        "brain-age-train-your-brain-in-minutes-a-day-ds-2005",
        "name":
        "Brain Age: Train Your Brain in Minutes a Day",
        "year":
        2005,
        "platform":
        "DS",
        "genre":
        "Misc",
        "publisher":
        "Nintendo",
        "global_sales":
        20.15,
        "critic_score":
        77,
        "user_score":
        7,
        "developer":
        "Nintendo",
        "image_url":
        "https://www.mobygames.com/images/covers/l/60551-brain-age-train-your-brain-in-minutes-a-day-nintendo-ds-media.jpg"
    },
    {
        "id":
        "grand-theft-auto-v-x360-2013",
        "name":
        "Grand Theft Auto V",
        "year":
        2013,
        "platform":
        "X360",
        "genre":
        "Action",
        "publisher":
        "Take-Two Interactive",
        "global_sales":
        16.27,
        "critic_score":
        97,
        "user_score":
        8,
        "developer":
        "Rockstar North",
        "image_url":
        "https://pmcvariety.files.wordpress.com/2013/09/gta-v-big.jpg?w=1000&h=563&crop=1"
    },
    {
        "id":
        "grand-theft-auto-vice-city-ps2-2002",
        "name":
        "Grand Theft Auto: Vice City",
        "year":
        2002,
        "platform":
        "PS2",
        "genre":
        "Action",
        "publisher":
        "Take-Two Interactive",
        "global_sales":
        16.15,
        "critic_score":
        95,
        "user_score":
        8,
        "developer":
        "Rockstar North",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BYmIwZGExODItMDE5NC00ODA4LWE0N2YtMGY0MjZjNWFiZmZkXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR4,0,182,268_AL_.jpg"
    },
    {
        "id":
        "brain-age-2-more-training-in-minutes-a-day-ds-2005",
        "name":
        "Brain Age 2: More Training in Minutes a Day",
        "year":
        2005,
        "platform":
        "DS",
        "genre":
        "Puzzle",
        "publisher":
        "Nintendo",
        "global_sales":
        15.29,
        "critic_score":
        77,
        "user_score":
        7,
        "developer":
        "Nintendo",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/f/f4/Brain_Age_2_-_More_Training_in_Minutes_a_Day%21_Coverart.png"
    },
    {
        "id": "gran-turismo-3-a-spec-ps2-2001",
        "name": "Gran Turismo 3: A-Spec",
        "year": 2001,
        "platform": "PS2",
        "genre": "Racing",
        "publisher": "Sony Computer Entertainment",
        "global_sales": 14.98,
        "critic_score": 95,
        "user_score": 8,
        "developer": "Polyphony Digital",
        "image_url": "https://i.ytimg.com/vi/UgDY9I-Ff84/hqdefault.jpg"
    },
    {
        "id":
        "call-of-duty-modern-warfare-3-x360-2011",
        "name":
        "Call of Duty: Modern Warfare 3",
        "year":
        2011,
        "platform":
        "X360",
        "genre":
        "Shooter",
        "publisher":
        "Activision",
        "global_sales":
        14.73,
        "critic_score":
        88,
        "user_score":
        3,
        "developer":
        "Infinity Ward, Sledgehammer Games",
        "image_url":
        "http://www.imfdb.org/images/thumb/e/e6/Cover_MW3.jpg/301px-Cover_MW3.jpg"
    },
    {
        "id":
        "call-of-duty-black-ops-x360-2010",
        "name":
        "Call of Duty: Black Ops",
        "year":
        2010,
        "platform":
        "X360",
        "genre":
        "Shooter",
        "publisher":
        "Activision",
        "global_sales":
        14.61,
        "critic_score":
        87,
        "user_score":
        6,
        "developer":
        "Treyarch",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BMTI5MTY3ODQzMl5BMl5BanBnXkFtZTcwODA2NzQwNA@@._V1_CR0,60,640,360_AL_UX477_CR0,0,477,268_AL_.jpg"
    },
    {
        "id":
        "call-of-duty-black-ops-ii-ps3-2012",
        "name":
        "Call of Duty: Black Ops II",
        "year":
        2012,
        "platform":
        "PS3",
        "genre":
        "Shooter",
        "publisher":
        "Activision",
        "global_sales":
        13.79,
        "critic_score":
        83,
        "user_score":
        5,
        "developer":
        "Treyarch",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BYTZiNTVmNWYtYmFmZi00NmJmLWI1ODYtZWI4Yzg2Y2Y5NGFjXkEyXkFqcGdeQXVyNjM1MzczNjg@._V1_UY268_CR17,0,182,268_AL_.jpg"
    },
    {
        "id":
        "call-of-duty-black-ops-ii-x360-2012",
        "name":
        "Call of Duty: Black Ops II",
        "year":
        2012,
        "platform":
        "X360",
        "genre":
        "Shooter",
        "publisher":
        "Activision",
        "global_sales":
        13.67,
        "critic_score":
        83,
        "user_score":
        4,
        "developer":
        "Treyarch",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BYTZiNTVmNWYtYmFmZi00NmJmLWI1ODYtZWI4Yzg2Y2Y5NGFjXkEyXkFqcGdeQXVyNjM1MzczNjg@._V1_UY268_CR17,0,182,268_AL_.jpg"
    },
    {
        "id":
        "call-of-duty-modern-warfare-2-x360-2009",
        "name":
        "Call of Duty: Modern Warfare 2",
        "year":
        2009,
        "platform":
        "X360",
        "genre":
        "Shooter",
        "publisher":
        "Activision",
        "global_sales":
        13.47,
        "critic_score":
        94,
        "user_score":
        6,
        "developer":
        "Infinity Ward",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Modern_Warfare_2_cover.PNG/220px-Modern_Warfare_2_cover.PNG"
    },
    {
        "id":
        "call-of-duty-modern-warfare-3-ps3-2011",
        "name":
        "Call of Duty: Modern Warfare 3",
        "year":
        2011,
        "platform":
        "PS3",
        "genre":
        "Shooter",
        "publisher":
        "Activision",
        "global_sales":
        13.32,
        "critic_score":
        88,
        "user_score":
        3,
        "developer":
        "Infinity Ward, Sledgehammer Games",
        "image_url":
        "http://www.imfdb.org/images/thumb/e/e6/Cover_MW3.jpg/301px-Cover_MW3.jpg"
    },
    {
        "id":
        "grand-theft-auto-iii-ps2-2001",
        "name":
        "Grand Theft Auto III",
        "year":
        2001,
        "platform":
        "PS2",
        "genre":
        "Action",
        "publisher":
        "Take-Two Interactive",
        "global_sales":
        13.1,
        "critic_score":
        97,
        "user_score":
        8,
        "developer":
        "DMA Design",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BZTcxODc1MmMtZGM4Yy00MWJlLTg1NmEtZWRlYTZhZTY5YTc1XkEyXkFqcGdeQXVyODUzOTIxMjk@._V1_.jpg"
    },
    {
        "id":
        "super-smash-bros-brawl-wii-2008",
        "name":
        "Super Smash Bros. Brawl",
        "year":
        2008,
        "platform":
        "Wii",
        "genre":
        "Fighting",
        "publisher":
        "Nintendo",
        "global_sales":
        12.84,
        "critic_score":
        93,
        "user_score":
        8,
        "developer":
        "Game Arts",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/SSBB_Cover.jpg/220px-SSBB_Cover.jpg"
    },
    {
        "id":
        "mario-kart-7-3ds-2011",
        "name":
        "Mario Kart 7",
        "year":
        2011,
        "platform":
        "3DS",
        "genre":
        "Racing",
        "publisher":
        "Nintendo",
        "global_sales":
        12.66,
        "critic_score":
        85,
        "user_score":
        8,
        "developer":
        "Retro Studios, Entertainment Analysis & Development Division",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BY2U1NWE5MDgtODM3OS00ODU1LWIzYzEtMDZkYzAxNjEyNDJlXkEyXkFqcGdeQXVyNjg0NDkzNTM@._V1_.jpg"
    },
    {
        "id":
        "call-of-duty-black-ops-ps3-2010",
        "name":
        "Call of Duty: Black Ops",
        "year":
        2010,
        "platform":
        "PS3",
        "genre":
        "Shooter",
        "publisher":
        "Activision",
        "global_sales":
        12.63,
        "critic_score":
        88,
        "user_score":
        6,
        "developer":
        "Treyarch",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BMTI5MTY3ODQzMl5BMl5BanBnXkFtZTcwODA2NzQwNA@@._V1_CR0,60,640,360_AL_UX477_CR0,0,477,268_AL_.jpg"
    },
    {
        "id":
        "grand-theft-auto-v-ps4-2014",
        "name":
        "Grand Theft Auto V",
        "year":
        2014,
        "platform":
        "PS4",
        "genre":
        "Action",
        "publisher":
        "Take-Two Interactive",
        "global_sales":
        12.61,
        "critic_score":
        97,
        "user_score":
        8,
        "developer":
        "Rockstar North",
        "image_url":
        "https://media.rockstargames.com/rockstargames/img/global/news/upload/actual_1386036983.jpg"
    },
    {
        "id": "animal-crossing-wild-world-ds-2005",
        "name": "Animal Crossing: Wild World",
        "year": 2005,
        "platform": "DS",
        "genre": "Simulation",
        "publisher": "Nintendo",
        "global_sales": 12.13,
        "critic_score": 86,
        "user_score": 8,
        "developer": "Nintendo",
        "image_url": "https://tcrf.net/images/7/70/ACWW-title.png"
    },
    {
        "id": "halo-3-x360-2007",
        "name": "Halo 3",
        "year": 2007,
        "platform": "X360",
        "genre": "Shooter",
        "publisher": "Microsoft Game Studios",
        "global_sales": 12.12,
        "critic_score": 94,
        "user_score": 7,
        "developer": "Bungie Software, Bungie",
        "image_url": "https://i.ytimg.com/vi/CEeoodGyP3o/maxresdefault.jpg"
    },
    {
        "id": "gran-turismo-4-ps2-2004",
        "name": "Gran Turismo 4",
        "year": 2004,
        "platform": "PS2",
        "genre": "Racing",
        "publisher": "Sony Computer Entertainment",
        "global_sales": 11.66,
        "critic_score": 89,
        "user_score": 8,
        "developer": "Polyphony Digital",
        "image_url": "https://i.ytimg.com/vi/yxtNPx798KU/maxresdefault.jpg"
    },
    {
        "id":
        "super-mario-galaxy-wii-2007",
        "name":
        "Super Mario Galaxy",
        "year":
        2007,
        "platform":
        "Wii",
        "genre":
        "Platform",
        "publisher":
        "Nintendo",
        "global_sales":
        11.35,
        "critic_score":
        97,
        "user_score":
        8,
        "developer":
        "Nintendo",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/SuperMarioGalaxy.jpg/220px-SuperMarioGalaxy.jpg"
    },
    {
        "id":
        "grand-theft-auto-iv-x360-2008",
        "name":
        "Grand Theft Auto IV",
        "year":
        2008,
        "platform":
        "X360",
        "genre":
        "Action",
        "publisher":
        "Take-Two Interactive",
        "global_sales":
        11.01,
        "critic_score":
        98,
        "user_score":
        7,
        "developer":
        "Rockstar North",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/Grand_Theft_Auto_IV_cover.jpg/220px-Grand_Theft_Auto_IV_cover.jpg"
    },
    {
        "id": "gran-turismo-ps-1997",
        "name": "Gran Turismo",
        "year": 1997,
        "platform": "PS",
        "genre": "Racing",
        "publisher": "Sony Computer Entertainment",
        "global_sales": 10.95,
        "critic_score": 96,
        "user_score": 8,
        "developer": "Polyphony Digital",
        "image_url": "https://i.ytimg.com/vi/X6DePq3nvSk/hqdefault.jpg"
    },
    {
        "id":
        "super-mario-3d-land-3ds-2011",
        "name":
        "Super Mario 3D Land",
        "year":
        2011,
        "platform":
        "3DS",
        "genre":
        "Platform",
        "publisher":
        "Nintendo",
        "global_sales":
        10.81,
        "critic_score":
        90,
        "user_score":
        8,
        "developer":
        "Nintendo",
        "image_url":
        "http://hiddenpalace.org/w/images/thumb/6/6e/Super_Mario_3D_Land_%28E3_2011_kiosk_demo%29-title.png/320px-Super_Mario_3D_Land_%28E3_2011_kiosk_demo%29-title.png"
    },
    {
        "id": "gran-turismo-5-ps3-2010",
        "name": "Gran Turismo 5",
        "year": 2010,
        "platform": "PS3",
        "genre": "Racing",
        "publisher": "Sony Computer Entertainment",
        "global_sales": 10.7,
        "critic_score": 84,
        "user_score": 7,
        "developer": "Polyphony Digital",
        "image_url": "https://i.ytimg.com/vi/UrJe2XokCBk/maxresdefault.jpg"
    },
    {
        "id":
        "call-of-duty-modern-warfare-2-ps3-2009",
        "name":
        "Call of Duty: Modern Warfare 2",
        "year":
        2009,
        "platform":
        "PS3",
        "genre":
        "Shooter",
        "publisher":
        "Activision",
        "global_sales":
        10.6,
        "critic_score":
        94,
        "user_score":
        6,
        "developer":
        "Infinity Ward",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Modern_Warfare_2_cover.PNG/220px-Modern_Warfare_2_cover.PNG"
    },
    {
        "id":
        "grand-theft-auto-iv-ps3-2008",
        "name":
        "Grand Theft Auto IV",
        "year":
        2008,
        "platform":
        "PS3",
        "genre":
        "Action",
        "publisher":
        "Take-Two Interactive",
        "global_sales":
        10.5,
        "critic_score":
        98,
        "user_score":
        7,
        "developer":
        "Rockstar North",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/Grand_Theft_Auto_IV_cover.jpg/220px-Grand_Theft_Auto_IV_cover.jpg"
    },
    {
        "id": "call-of-duty-ghosts-x360-2013",
        "name": "Call of Duty: Ghosts",
        "year": 2013,
        "platform": "X360",
        "genre": "Shooter",
        "publisher": "Activision",
        "global_sales": 10.25,
        "critic_score": 73,
        "user_score": 2,
        "developer": "Infinity Ward",
        "image_url": "https://i.ytimg.com/vi/uwrutboTU2M/maxresdefault.jpg"
    },
    {
        "id": "just-dance-3-wii-2011",
        "name": "Just Dance 3",
        "year": 2011,
        "platform": "Wii",
        "genre": "Misc",
        "publisher": "Ubisoft",
        "global_sales": 10.12,
        "critic_score": 74,
        "user_score": 7,
        "developer": "Ubisoft",
        "image_url": "https://i.ytimg.com/vi/0R6anTaISWE/hqdefault.jpg"
    },
    {
        "id":
        "new-super-mario-bros-2-3ds-2012",
        "name":
        "New Super Mario Bros. 2",
        "year":
        2012,
        "platform":
        "3DS",
        "genre":
        "Platform",
        "publisher":
        "Nintendo",
        "global_sales":
        9.9,
        "critic_score":
        78,
        "user_score":
        7,
        "developer":
        "Nintendo",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/3/35/New_Super_Mario_Bros._2_box_artwork.png"
    },
    {
        "id":
        "halo-reach-x360-2010",
        "name":
        "Halo: Reach",
        "year":
        2010,
        "platform":
        "X360",
        "genre":
        "Shooter",
        "publisher":
        "Microsoft Game Studios",
        "global_sales":
        9.86,
        "critic_score":
        91,
        "user_score":
        7,
        "developer":
        "Bungie",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Halo-_Reach_box_art.png/220px-Halo-_Reach_box_art.png"
    },
    {
        "id": "final-fantasy-vii-ps-1997",
        "name": "Final Fantasy VII",
        "year": 1997,
        "platform": "PS",
        "genre": "Role-Playing",
        "publisher": "Sony Computer Entertainment",
        "global_sales": 9.72,
        "critic_score": 92,
        "user_score": 9,
        "developer": "SquareSoft",
        "image_url":
        "https://r.hswstatic.com/w_907/gif/finalfantasyvii-MAIN.jpg"
    },
    {
        "id":
        "halo-4-x360-2012",
        "name":
        "Halo 4",
        "year":
        2012,
        "platform":
        "X360",
        "genre":
        "Shooter",
        "publisher":
        "Microsoft Game Studios",
        "global_sales":
        9.71,
        "critic_score":
        87,
        "user_score":
        7,
        "developer":
        "343 Industries",
        "image_url":
        "https://upload.wikimedia.org/wikipedia/en/0/02/Halo4forwarduntodawn.png"
    },
    {
        "id":
        "gran-turismo-2-ps-1999",
        "name":
        "Gran Turismo 2",
        "year":
        1999,
        "platform":
        "PS",
        "genre":
        "Racing",
        "publisher":
        "Sony Computer Entertainment",
        "global_sales":
        9.49,
        "critic_score":
        93,
        "user_score":
        9,
        "developer":
        "Polyphony Digital",
        "image_url":
        "https://m.media-amazon.com/images/M/MV5BNzNhOTNjODktOTQ3OS00ZDliLThmZjctZDZkYjE2YjBjYzhiXkEyXkFqcGdeQXVyNTM2MDQ5NTU@._V1_.jpg"
    }
]

print("Document indexing results {}".format(
    client.documents.index_documents(custom_api_source_key, documents)))
