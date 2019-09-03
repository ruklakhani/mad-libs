mad_libs = [
('DONTINPUT', 'Once upon a time there was a ')
('INPUT', 'noun ')
('DONTINPUT', 'name ')
('INPUT', 'name')
('DONTINPUT', '. Sometimes, when ')
('INPUT', 'name ')
('DONTINPUT', 'went outside, they would ')
('INPUT', 'verb ')
('DONTINPUT', '.')
]

def make_story (parts_of_speech: str):
    print("Fill in {}")
    return imput()


def write_madlibs(mad_libs: list):
    story = ""
    for lib in mad_libs:
        if lib [0] is 'INPUT'
            story += make_story(lib[1])
        else:
            story += (lib[1])
            print(lib[1])
    return story

print("""Your Story is:
{}""".format(write_madlibs(mad_libs)))
