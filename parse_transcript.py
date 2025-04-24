from pathlib import Path
import re
from datetime import timedelta

import srt

from components.html_parts import *


def parse_srt(in_file):
    """
    :param in_file: .srt utf-8 file
    :return: [{'start': <start-time-in-milliseconds>, 'end': <end-time-in-milliseconds>, 'content': <string>}, ...]
    """
    def to_milli(time):
        return int(time.total_seconds()*1000)

    raw = Path(in_file).read_text()
    sub_raw = list(srt.parse(raw))

    parsed = []
    for sub in sub_raw:
        start = to_milli(sub.start)
        end = to_milli(sub.end)
        content = sub.content
        content = normalize_punct(content)
        s = {'start': start, 'end': end, 'content': content}
        parsed.append(s)
    return parsed


def normalize_punct(string):
    string = string.strip().replace('་ ', '་')
    if string.endswith(' །'):
        pass
    elif string.endswith('།') or string.endswith('ཿ') or string.endswith('༔'):
        string += ' '
    return string


def gen_ha_page(in_file):
    # A. parse and prepare chunks
    parsed = parse_srt(in_file)
    chunks = []
    cur = []
    slide_num = []
    for p in parsed:
        if p['content'].startswith('{'):
            # add to chunks
            if cur:
                num = []
                if slide_num:
                    num = slide_num
                chunks.append((num, cur))
                cur = []
                slide_num = []

            # start new chunk
            text = p['content']
            while '}' in text:
                s_num, text = text.split('}', 1)
                slide_num.append(int(s_num[1:]))
            p['content'] = text
            cur.append(p)
        else:
            cur.append(p)
    # trailing chunk
    if cur:
        chunks.append((slide_num, cur))

    # B. format and add ha html code
    ha_trans = []
    for s_num, chunk in chunks:
        # add slide to html
        if s_num:
            for n, s in enumerate(s_num):
                img = f'\n<img src="components/slides/slide_{s}.jpg" alt="slide {s}">\n'
                if len(s_num) > 1 and n < len(s_num)-1:
                    img += '<br>'
                ha_trans.append(img)
        # add text
        ha_trans.append('<p>')
        for p in chunk:
            start = p['start']
            duration = p['end'] - p['start']
            content = p['content']
            # further process content here ########################################
            if (content.endswith('།') and not content.endswith(' །')) or content.endswith('༔'):
                content += ' '

            # #######################################################################

            # add units while ignoring empty segments
            if content.strip():
                duration = timedelta(milliseconds=duration)
                dur = str(duration)
                dur = dur[:dur.find('.')]
                if dur.startswith('0:'):
                    dur = dur[2:]

                trans = f'<a data-m="{start}" data-d="{duration}"><span style="font-family:arial; font-size: 20px;">{dur}</span>{content}</a>'

                ha_trans.append(trans)

        ha_trans.append('</p>')

    return ''.join(ha_trans), chunks

def format_text(chunks):
    out = []
    for _, chunk in chunks:
        c = ''.join([c['content'] for c in chunk])
        out.append(c)
    return '\n\n'.join(out)

file_paths = [
    Path('components/tsiksum_commentary_a_1.srt'),
    Path('components/tsiksum_commentary_a_2.srt'),
    Path('components/tsiksum_commentary_a_3.srt'),
    Path('components/tsiksum_commentary_c_1.srt'),
    Path('components/tsiksum_commentary_c_2.srt'),
    Path('components/tsiksum_commentary_c_3.srt'),
    Path('components/tsiksum_commentary_f_1.srt'),
    Path('components/tsiksum_commentary_f_2.srt'),
    Path('components/tsiksum_commentary_f_3.srt'),
    Path('components/tsiksum_commentary_f_4.srt'),
    Path('components/tsiksum_commentary_k_1.srt'),
    Path('components/tsiksum_commentary_k_2.srt'),
    Path('components/tsiksum_commentary_k_3.srt'),
    Path('components/tsiksum_commentary_k_4.srt'),
    Path('components/tsiksum_commentary_k_5.srt'),
    Path('components/tsiksum_commentary_d_1.srt'),
    Path('components/tsiksum_commentary_d_2_unfinished.srt'),
    Path('components/tsiksum_commentary_h_onlybeginning.srt'),
    Path('components/tsiksum_commentary_g_nobeginning.srt'),
    Path('components/tsiksum_commentary_b_onlyend.srt'),
    Path('components/tsiksum_commentary_e_unfinished.srt'),
    Path('components/tsiksum_commentary_l_1.srt'),
    Path('components/tsiksum_commentary_l_2.srt'),
    Path('components/tsiksum_commentary_l_3.srt'),
    Path('components/tsiksum_commentary_l_4.srt'),
    Path('components/tsiksum_commentary_l_5.srt'),
    Path('components/tsiksum_commentary_l_6.srt'),
    Path('components/tsiksum_commentary_l_7.srt'),
    Path('components/tsiksum_commentary_l_8.srt'),
    Path('components/tsiksum_commentary_l_9.srt'),
    Path('components/tsiksum_commentary_l_10.srt'),
    Path('components/tsiksum_commentary_thrilung_b_1.srt'),
    Path('components/tsiksum_commentary_thrilung_b_2.srt'),
    Path('components/tsiksum_commentary_thrilung_b_3.srt'),
    Path('components/tsiksum_commentary_thrilung_b_4.srt'),
    Path('components/tsiksum_commentary_thrilung_b_5.srt'),
    Path('components/tsiksum_commentary_j_1.srt'),
    Path('components/tsiksum_commentary_j_2.srt'),
    Path('components/tsiksum_commentary_j_3.srt'),
    Path('components/tsiksum_commentary_j_4.srt'),
    Path('components/tsiksum_commentary_thrilung_a.srt'),
    Path('components/tsiksum_roottext_thrilung_a_1.srt'),
    Path('components/tsiksum_roottext_overview_a.srt'),
]

transcriptions = []
for i, in_file in enumerate(file_paths):
    transcription, chunks = gen_ha_page(in_file)
    p = players[i] + '\n'
    p += transcript_start.replace('###', str(i+1))
    transcriptions.append(f'{p}\n{transcription}\n{transcript_end}\n\n')
    text = format_text(chunks)

html_page = '\n'.join([head, body_beginning, '\n'.join(transcriptions), body_end])
Path('index.html').write_text(html_page)


