define audio.music1 = "audio/ACOUSTICCOUNTRY MUSIC Happy Piano Guitar ROYALTY FREE Download No Copyright Content _ 12 MORNINGS.mp3"
define audio.music2 = "audio/AMBIENT MUSIC Suspense Tension Light ROYALTY FREE Download No Copyright Content _ A WALK INTO SPACE.mp3"

define audio.driving = 'audio/sfx/66048__bidone__cars-drive-slow-wet-snow.mp3'
define audio.phone_notification = 'audio/sfx/400697__daphne_in_wonderland__messenger-notification-sound-imitation.ogg'
define audio.phone_call = 'audio/sfx/348584__aldenb4610__phone-outgoing-call.wav'
define audio.clangclang = 'audio/sfx/460181__johanwestling__mechanic_old_cog_chain_medieval_gate_metal_wood_impact_m10.wav'
define audio.car_break = 'audio/sfx/542448__200154michaela__car-pulling-up-and-break-squeak.wav'
define audio.car_door = 'audio/sfx/556689__nachtmahrtv__car-door-open-and-close.ogg'
define audio.car_arriving = 'audio/sfx/136536__jmdh__cararriveandstop.wav'

$ renpy.music.register_channel("sfx1", "sfx", loop=True)

# ffmpeg -i my_sound_file.wav my_sound_file.ogg