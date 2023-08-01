import pygame

DRUM_BASS = 0
DRUM_CYMBAL = 1
DRUM_FLOOR_TOM = 2
DRUM_HH = 3
DRUM_HH_CLOSED = 4
DRUM_HH_OPEN = 5
DRUM_MEDIUM_TOM = 6
DRUM_SMALL_TOM = 7
DRUM_SNARE = 8

MAPPING = {
    12: DRUM_SNARE, # Down
    0: DRUM_SNARE,  # X
    10: DRUM_BASS,  # R1
    1: DRUM_HH,     # O
}

RESOURCE_MAPPING = {
    DRUM_BASS: "sounds\Bass-Drum-Hit-Level-5a-www.fesliyanstudios.com.mp3",
    DRUM_CYMBAL: "sounds\Crash-Cymbal-Hit-B-www.fesliyanstudios.com.mp3",
    DRUM_FLOOR_TOM: "sounds\Floor-Tom-Drum-Hit-Level-5A-www.fesliyanstudios.com.mp3",
    DRUM_HH_CLOSED: "sounds\Hi-Hat-Closed-Hit-A1-www.fesliyanstudios.com.mp3",
    DRUM_HH_OPEN: "sounds\Hi-Hat-Open-Hit-B3-www.fesliyanstudios.com.mp3",
    DRUM_MEDIUM_TOM: "sounds\Medium-Tom-Drum-Hit-Level-5A-www.fesliyanstudios.com.mp3",
    DRUM_SMALL_TOM: "sounds\Small-Tom-Drum-Hit-Level-5A-www.fesliyanstudios.com.mp3",
    DRUM_SNARE: "sounds\Snare-Drum-Hit-Level-5a-www.fesliyanstudios.com.mp3"
}

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

pygame.mixer.init()
mixer_channel = [pygame.mixer.Channel(x) for x in range(pygame.mixer.get_num_channels())]


pygame.display.set_mode((500, 700))
pygame.display.set_caption("Joystick example")

j1 = pygame.joystick.Joystick(0)
j1.init()

drum_sounds = {}
for k, v in RESOURCE_MAPPING.items():
    drum_sounds[k] = pygame.mixer.Sound(v)

run = True

while run:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
            run = False
            break

        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
            if event.button in MAPPING:
                sound_type = MAPPING.get(event.button)
                if sound_type == DRUM_HH:
                    print(j1.get_axis(4))
                    if j1.get_axis(4) > 0.3:
                        drum_sounds[DRUM_HH_CLOSED].play()
                    else:
                        drum_sounds[DRUM_HH_OPEN].play()
                else:
                    drum_sounds[sound_type].play()
    
    # HH open/close handle
    # if j1.get_axis(4) < 0.5:
    #     if mixer_channel[drum_sounds[DRUM_HH_OPEN].get_num_channels()].get_busy():
    #         print("?")
    #         drum_sounds[DRUM_HH_OPEN].stop()
    #         #drum_sounds[DRUM_HH_CLOSED].play()

    clock.tick(240)

pygame.quit()