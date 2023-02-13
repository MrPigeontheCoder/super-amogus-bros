def on_a_pressed():
    if Player1.is_hitting_tile(CollisionDirection.BOTTOM):
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                400,
                600,
                255,
                0,
                250,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        Player1.set_velocity(Player1.vx, -100)
        pause(500)
        Player1.set_velocity(Player1.vx, 75)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

# This sets up the game and stuff
Player1: Sprite = None
print("game started")
# This creates the player sprite and makes it move and makes the camera follow it
Player1 = sprites.create(assets.image("""
    Player1Right
"""), SpriteKind.player)
controller.move_sprite(Player1, 50, 0)
scene.camera_follow_sprite(Player1)
info.set_life(5)
print("player created, lives set")
console.log_value("lives", 5)
# This sets the level1 and also sets up the sky
tiles.set_current_tilemap(tilemap("""
    level1
"""))
scene.set_background_image(assets.image("""
    Sky
"""))
# This places the player at the start of the level
tiles.place_on_tile(Player1, tiles.get_tile_location(0, 11))
print("player placed on position")
# This shows the name of the game and copyright and stuff
# 
game.splash("SUPER AMOGUS BROS.", "Copyright Amogus Co. 2022")
print("name splashed")
Moving_Enemy_1 = sprites.create(assets.image("""
    enemy1left
"""), SpriteKind.enemy)
tiles.place_on_tile(Moving_Enemy_1, tiles.get_tile_location(3, 12))
Moving_Enemy_1.set_velocity(50, 0)
Moving_Enemy_1.set_bounce_on_wall(True)
print("enemy set")

def on_forever():
    if not (controller.A.is_pressed()):
        Player1.vy = 75
forever(on_forever)

def on_forever2():
    if Moving_Enemy_1.vx == 50:
        Moving_Enemy_1.set_image(assets.image("""
            enemy1right
        """))
    elif Moving_Enemy_1.vx == -50:
        Moving_Enemy_1.set_image(assets.image("""
            enemy1left
        """))
forever(on_forever2)

def on_forever3():
    if Player1.vx >= 50:
        Player1.set_image(assets.image("""
            Player1Right
        """))
    elif Player1.vx <= -50:
        Player1.set_image(assets.image("""
            Player1Left
        """))
forever(on_forever3)

def on_forever4():
    if controller.B.is_pressed():
        controller.move_sprite(Player1, 75, 0)
    else:
        controller.move_sprite(Player1, 50, 0)
forever(on_forever4)

def on_forever5():
    if info.life() == 0:
        game.over(False, effects.dissolve)
forever(on_forever5)
