controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Player1.isHittingTile(CollisionDirection.Bottom)) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 400, 600, 255, 0, 250, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        Player1.setVelocity(Player1.vx, -100)
        pause(500)
        Player1.setVelocity(Player1.vx, 50)
    }
})
let Player1: Sprite = null
// This creates the player sprite and makes it move and makes the camera follow it
Player1 = sprites.create(assets.image`Player1`, SpriteKind.Player)
controller.moveSprite(Player1, 50, 0)
scene.cameraFollowSprite(Player1)
let lives = 5
// This sets the level1 and also sets up the sky
tiles.setCurrentTilemap(tilemap`level1`)
scene.setBackgroundImage(assets.image`Sky`)
// This places the player at the start of the level
tiles.placeOnTile(Player1, tiles.getTileLocation(0, 11))
// This shows the name of the game and copyright and stuff
// 
game.splash("SUPER AMOGUS BROS.", "Copyright Amogus Co. 2022")
// This shows the lives
game.showLongText("" + lives + " x Lives", DialogLayout.Full)
let Moving_Enemy = sprites.create(assets.image`enemy1left`, SpriteKind.Enemy)
tiles.placeOnTile(Moving_Enemy, tiles.getTileLocation(3, 12))
Moving_Enemy.setVelocity(50, 0)
Moving_Enemy.setBounceOnWall(true)
forever(function () {
    if (!(controller.A.isPressed())) {
        Player1.vy = 50
    }
})
forever(function () {
    if (Moving_Enemy.vx == 50) {
        Moving_Enemy.setImage(assets.image`enemy1right`)
    } else if (Moving_Enemy.vx == -50) {
        Moving_Enemy.setImage(assets.image`enemy1left`)
    }
})
forever(function () {
    if (controller.B.isPressed()) {
        controller.moveSprite(Player1, 75, 0)
    } else {
        controller.moveSprite(Player1, 50, 0)
    }
})
