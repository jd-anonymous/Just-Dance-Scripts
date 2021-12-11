import json

def beat_generator(beats_count: int, bpm: int):
    """
    Function for generating beats
    
    :param beats_count: Count of beats
    :param bpm: Beats per minute
    :return: List of beats
    """

    # Getting beat
    beat: int = round((60 * 1000) / bpm)

    # Making beats list
    beats: list[int] = list()

    # Generating beats
    for index in range(beats_count):
        # Multiple index by our beat
        new_beat: int = (index * beat) * 48

        # Pushing our new beat to beats list
        beats.append(new_beat)

    # Returns a list of beats
    return beats

def create_musictrack(mapname: str, beats: list):
    """
    Function for creating musictrack

    :param mapname: MapName
    :param beats: Generated beats
    :returns: Musictrack as dict
    """

    # Creating musictrack
    musictrack: dict = dict(
        __class="Actor_Template",
        WIP=0,
        LOWUPDATE=0,
        UPDATE_LAYER=0,
        PROCEDURAL=0,
        STARTPAUSED=0,
        FORCEISENVIRONMENT=0,
        COMPONENTS=[
            dict(
                __class="MusicTrackComponent_Template",
                trackData=dict(
                    __class="MusicTrackData",
                    structure=dict(
                        __class="MusicTrackStructure",
                        markers=beats,
                        signatures=[
                            dict(
                                __class="MusicSignature",
                                marker=8,
                                beats=4
                            )
                        ],
                        sections=[
                            dict(
                                __class="MusicSection",
                                marker=16,
                                sectionType=4,
                                comments="jdmega is flop"
                            )
                        ],
                        startBeat=0,
                        endBeat=len(beats),
                        videoStartTime=0.0,
                        previewEntry=round(len(beats) / 4),
                        previewLoopStart=round(len(beats) / 3),
                        previewLoopEnd=round(len(beats) / 2),
                        volume=0.0
                    ),
                    path=f"world/maps/{mapname.lower()}/audio/{mapname.lower()}.wav",
                    url="jmcs://jd-contents/{mapname}/{mapname}.ogg"
                )
           )
        ]
    )

    # Returns a musictrack
    return musictrack

def main():
    # Welcome screen
    print("""
    ========================================

    W E L C O M E  T O  N 0 T  F L O P P E D
    B E A T  G E N E R A T O R  B Y  F A G
    
    A N D  R E C O D E D  B Y  4 C H A N
    U S E R

    =======================================
    """)
    
    # Getting BPM from user
    bpm: int = int(input("BPM: "))

    # Getting count of beats from user
    count_of_beats: int = int(input("Count of beats: "))

    # Getting map name of beats from user
    map_name: str = input("MapName: ")

    # Creating musictrack
    with open(f"{map_name.lower()}_musictrack.tpl.ckd", "w") as file:
        # Generating beats
        beats: list[int] = beat_generator(count_of_beats, bpm)

        # Creating musictrack
        musictrack: dict = create_musictrack(map_name, beats)

        # Writing our generated musictrack to file
        json.dump(musictrack, file)

if __name__ == "__main__":
    main()