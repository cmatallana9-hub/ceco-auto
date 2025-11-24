let luz = 0
// Mensaje de bienvenida al iniciar
basic.showString("BIENVENIDOS")
basic.forever(function () {
    // Sensor de luz simulado
    luz = input.lightLevel()
    // Control de iluminación automática
    if (luz < 80) {
        // Luz baja
        basic.showIcon(IconNames.Happy)
    } else {
        // Luz suficiente
        basic.clearScreen()
    }
    // Registro de asistencia
    if (input.buttonIsPressed(Button.A)) {
        basic.showString("ASISTENCIA")
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 2000, 500, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
        basic.showIcon(IconNames.Yes)
        basic.pause(1000)
    }
    // Alerta educativa (cambio de modulo)
    if (input.buttonIsPressed(Button.B)) {
        basic.showString("CAMBIO")
        music.playTone(988, music.beat(BeatFraction.Quarter))
        // ← ICONO VÁLIDO
        basic.showIcon
basic.pause(1000)
    }
})
