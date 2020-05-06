sharp_note = {
    "C#": "c",
    "D#": "d",
    "F#": "f",
    "G#": "g",
    "A#": "a"
}


def change_sharp_to_small(music):

    for before, after in sharp_note.items():
        music = music.replace(before, after)


    return music


def get_play_time(start, end):
    pass


def solution(m, musicinfos):
    answer = ''
    real_play = []

    m = change_sharp_to_small(m)
    for i in range(len(musicinfos)):
        musicinfos[i][4] = change_sharp_to_small(musicinfos[i][4])

    return answer


ex = [
    ("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"], "HELLO"),
    ("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"], "FOO"),
    ("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"], "WORLD")
]
for m, mus, r in ex:
    print(solution(m, mus) == r)