luz = 0
# Mensaje de bienvenida al iniciar
basic.show_string("BIENVENIDOS")

def on_forever():
    global luz
    # Sensor de luz simulado
    luz = input.light_level()
    # Control de iluminación automática
    if luz < 80:
        # Luz baja
        basic.show_icon(IconNames.HAPPY)
    else:
        # Luz suficiente
        basic.clear_screen()
    # Registro de asistencia
    if input.button_is_pressed(Button.A):
        basic.show_string("ASISTENCIA")
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                2000,
                500,
                255,
                0,
                300,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
        basic.show_icon(IconNames.YES)
        basic.pause(1000)
    # Alerta educativa (cambio de modulo)
    if input.button_is_pressed(Button.B):
        basic.show_string("CAMBIO")
        music.play_tone(988, music.beat(BeatFraction.QUARTER))
        # ← ICONO VÁLIDO
        basic.show_icon
        basic.pause(1000)
basic.forever(on_forever)
