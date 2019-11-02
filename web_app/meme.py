from .data import data

def fake_talents(wowhead_url):
    fake_buffer = []

    try:
        uri_chunks = wowhead_url.split('/')
        _class = uri_chunks[-2]
        _ = data[_class]
    except (KeyError, AttributeError, IndexError):
        raise ValueError('Invalid Wowhead URL')

    talents = uri_chunks[-1]

    wowhead_tabs = talents.split('-')

    for index, tab in enumerate(data[_class]['tabs']):
        name = tab['name']
        file_name = tab['fileName']
        if index < len(wowhead_tabs):
            total_points = sum([int(talent) for talent in wowhead_tabs[index]])
        else:
            total_points = 0
        fake_buffer.append(f"tinsert (pointsPerSpec, {{'{name}', {total_points}, '{file_name}'}})")

    for tab, tab_string in enumerate(wowhead_tabs):
        talents_data = data[_class]['tabs'][tab]['talents']
        for talent_index, rank in enumerate(tab_string):
            try:
                talent_data = talents_data[talent_index]
            except IndexError:
                continue
            icon = talent_data['icon']
            rank = int(rank)
            tier = talent_data['tier']
            column = talent_data['column']
            tab_id = data[_class]['tabs'][tab]['id']
            max_rank = talent_data['max']

            fake_buffer.append(f"tinsert (talentsSelected, {{{icon}, {rank}, {tier}, {column}, {tab+1}, {tab_id}, {max_rank}}})")

    return fake_buffer
