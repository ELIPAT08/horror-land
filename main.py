tiles.set_tilemap(tiles.create_tilemap(hex("""
            1000100001060606060606060606060606060602050a1111111111111211111111110b07050e1209090909090909090909091007050e0909090909090909090909121007050e0909090909090909090909091007050e0909090909090909090909091007050e0909090909090909090909091007050e090909090909090909090909100705120909090909090909090909091007050e09090909090909090909090912070509090909090909090909090909100705090909090909090909090909091007050e0909090909090909090909091007050e0909090909090909090909121007050c090f0f120f0f0f0f0f0f0f0f0d0704080808080808080808080808080803
        """),
        img("""
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 . . . . . . . 2 . . . . . . 2 
                2 . 2 . . . . . . . . . . . . 2 
                2 . . . . . . . . . . . . 2 . 2 
                2 . . . . . . . . . . . . . . 2 
                2 . . . . . . . . . . . . . . 2 
                2 . . . . . . . . . . . . . . 2 
                2 . . . . . . . . . . . . . . 2 
                2 2 . . . . . . . . . . . . . 2 
                2 . . . . . . . . . . . . . 2 2 
                2 . . . . . . . . . . . . . . 2 
                2 . . . . . . . . . . . . . . 2 
                2 . . . . . . . . . . . . . . 2 
                2 . . . . . . . . . . . . 2 . 2 
                2 . . . . 2 . . . . . . . . . 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        """),
        [myTiles.transparency16,
            sprites.dungeon.dark_ground_north_west0,
            sprites.dungeon.dark_ground_north_east0,
            sprites.dungeon.dark_ground_south_east0,
            sprites.dungeon.dark_ground_south_west0,
            sprites.dungeon.dark_ground_west,
            sprites.dungeon.dark_ground_north,
            sprites.dungeon.dark_ground_east,
            sprites.dungeon.dark_ground_south,
            sprites.castle.tile_path5,
            sprites.castle.tile_path1,
            sprites.castle.tile_path3,
            sprites.castle.tile_path7,
            sprites.castle.tile_path9,
            sprites.castle.tile_path4,
            sprites.castle.tile_path8,
            sprites.castle.tile_path6,
            sprites.castle.tile_path2,
            sprites.builtin.forest_tiles0],
        TileScale.SIXTEEN))
mySprite2 = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
tiles.place_on_tile(mySprite2, tiles.get_tile_location(3, 3))
scene.camera_follow_sprite(mySprite2)
controller.move_sprite(mySprite2)