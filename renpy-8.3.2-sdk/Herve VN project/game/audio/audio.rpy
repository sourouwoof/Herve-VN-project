define audio.music1 = "audio/ACOUSTICCOUNTRY MUSIC Happy Piano Guitar ROYALTY FREE Download No Copyright Content _ 12 MORNINGS.mp3"
define audio.music2 = "audio/AMBIENT MUSIC Suspense Tension Light ROYALTY FREE Download No Copyright Content _ A WALK INTO SPACE.mp3"

define audio.driving = "audio/sfx/66048__bidone__cars-drive-slow-wet-snow.mp3"
define audio.phone_notification = "audio/sfx/400697__daphne_in_wonderland__messenger-notification-sound-imitation.ogg"
define audio.phone_call = "audio/sfx/348584__aldenb4610__phone-outgoing-call.ogg"
define audio.clangclang = "audio/sfx/460181__johanwestling__mechanic_old_cog_chain_medieval_gate_metal_wood_impact_m10.ogg"
define audio.car_break = "audio/sfx/542448__200154michaela__car-pulling-up-and-break-squeak.ogg"
define audio.car_door = "audio/sfx/556689__nachtmahrtv__car-door-open-and-close.ogg"
define audio.car_arriving = "audio/sfx/136536__jmdh__cararriveandstop.ogg"
define audio.knockknock = "audio/sfx/629987__flem0527__knocking-on-wood-door-1.ogg"
define audio.fireplace = "audio/sfx/81800__silencyo__silencyo_cc_fire-in-fireplace_close-up_reverberant.ogg"
define audio.stomachgrowl = "audio/sfx/703168__cropdub6425__favstomachgrowl.ogg"
define audio.phone_vibrating = "audio/sfx/369842__splicesound__cell-phone-vibrate-in-bag-backpack.ogg"
define audio.phone_endcall = "audio/sfx/235911__yfjesse__notification-sound.ogg"
define audio.light_switch = "audio/sfx/440498__christutorials__light-switch-turn-on-sound.ogg"
define audio.snowstorm1 = "audio/sfx/348167__klankbeeld__room-tone-wind-6bft-150518_03.ogg"
define audio.microwave_finish = "audio/sfx/738770__cheatinsloth__microwave-bell-ring.ogg"
define audio.snores = "audio/sfx/534385__magic_fxmakeupforfilms__snoring.ogg"
define audio.snowstorm2 = "audio/sfx/521820__fission9__polar-wind.ogg"
define audio.broken_glass = "audio/sfx/440773__mgamabile__smashing-glass.ogg"

init:
    $ renpy.music.register_channel("sfx1", "music", loop=True)

# ffmpeg -i my_sound_file.ogg my_sound_file.ogg
# ffmpeg -i 703168__cropdub6425__favstomachgrowl.m4a -b:a 192K -vn 703168__cropdub6425__favstomachgrowl.ogg
# for f in *.wav; do ffmpeg -i "${f}" "${f%%.*}.ogg"; done