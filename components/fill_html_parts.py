from pathlib import Path


def parse_toc():
    raw = Path('./toc.tsv').read_text().strip()
    lines = raw.split('\n')
    sessions = [a.split('\t') for a in lines]
    return sessions


sessions = parse_toc()

# 1: players
# 2: toc
# 3: function declaration
# 4: path declaration (main script)
mode = 1

if mode == 1:
    out = []
    for n, entry in enumerate(sessions):
        _, name, url = entry
        name_a, name_b = name.split(' ')

        player = f"""
                dedent(\"\"\"\\
                  <p id="tsiksum{n+1}" style="font-size: 26pt; color: brown;">{name}</p>         
                  <audio id="hyperplayer{n+1}" style="position:relative; width:97%" src="{url}" type="audio/m4a" controlsList="nodownload" controls></audio>
                \"\"\"),"""
        out.append(player)
    out = ''.join(out)
    Path('players.txt').write_text(out)

elif mode == 2:
    out = []
    for n, entry in enumerate(sessions):
        _, name, url = entry
        name_a, name_b = name.split(' ')

        toc = f'''          <p style="font-size: 20pt;"><a href="#tsiksum{n+1}">{name}</a><br></p>'''
        out.append(toc)
    out = '\n'.join(out)
    Path('toc.txt').write_text(out)

elif mode == 3:
    out = []
    for n, entry in enumerate(sessions):
        declaration = f'''          new HyperaudioLite("hypertranscript{n+1}", "hyperplayer{n+1}", minimizedMode, autoScroll, doubleClick, webMonetization);'''
        out.append(declaration)
    out = '\n'.join(out)
    Path('declaration.txt').write_text(out)

elif mode == 4:
    out = []
    for n, entry in enumerate(sessions):
        name, _, _ = entry
        p = f'''    Path('components/{name}.srt'),'''
        out.append(p)
    out = '\n'.join(out)
    Path('paths.txt').write_text(out)