import re
from content.courts import courts


def filters_to_show(args):
    args_as_dict = args.to_dict()

    # Remove the filters we don't want to show by key
    if 'neutral_citation' in args_as_dict.keys():
        del args_as_dict['neutral_citation']

    if 'search_term' in args_as_dict.keys():
        del args_as_dict['search_term']

    if 'courts' in args_as_dict.keys():
        if args_as_dict['courts'] == 'all':
            del args_as_dict['courts']

    if 'collections' in args_as_dict.keys():
        if args_as_dict['collections'] == 'all':
            del args_as_dict['collections']

    # Remove any argument that has an empty value
    items_to_show = {i : args_as_dict[i] for i in args_as_dict.keys() if args_as_dict[i] != ''}

    return items_to_show


def remove_current_item_from_query_string(url, item):
    pattern = re.compile(f'{item}[^&]*&?')
    cleaned_url = pattern.sub('', url)
    return cleaned_url


def translate_to_human_readable_label(str):
    labels = {
        'neutral_citation': 'Neutral citation only',
        'party_name': 'Party name',
        'judge_name': 'Judge name',
        'courts': 'Courts',
        'collections': 'Collections',
        'from_date': 'From date',
        'to_date': 'To date',
        'y': 'Yes',
        'all': 'All'
    }

    cts = {i['code']: i['name'] for i in courts}

    pairs = {**labels, **cts}

    if str in pairs.keys():
        return pairs[str]

    return str
