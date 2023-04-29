from gf_utils2.gamedata import GameData


def get_stc_data(stc_dir, table_dir=None, subset=None, to_dict=True):
    return GameData(stc_dir, table_dir, to_dict)


def convert_text(data, text_table, fill_empty=True):
    if isinstance(data, list):
        return [convert_text(i, text_table, fill_empty) for i in data]
    elif isinstance(data, dict):
        return {k: convert_text(v, text_table, fill_empty) for k, v in data.items()}
    else:
        text = text_table(data)
        if text != "":
            return text
        else:
            return data if fill_empty else ""
