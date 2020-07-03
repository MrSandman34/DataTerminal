def ts_code_trans(ts_code: str):
    if ts_code != '':
        beginning_letter = ts_code[0]
        if beginning_letter == '6':
            return f"{ts_code}.SH"
        if beginning_letter == '9':
            return f"{ts_code}.SH"
        else:
            return f"{ts_code}.SZ"

