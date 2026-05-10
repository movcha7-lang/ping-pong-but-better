from pygame import*

init()

mixer.init()
sound_wallhit = mixer.Sound('beep.wav')
sound_wallhit.set_volume(1.0)

sound_bounce = mixer.Sound('bounce.wav')
sound_bounce.set_volume(1.0)

sound_loss = mixer.Sound('loss.wav')
sound_loss.set_volume(1.0)

sound_victory = mixer.Sound('victory.wav')
sound_victory.set_volume(1.0)

sound_wallhit.play()
input("67")