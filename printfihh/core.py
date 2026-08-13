import sys

FISH_MECHANICAL = {
    "lines": [
        r"                                  ____",
        r"                               /\|    ~~\ ",
        r"                             /'  |   ,-. `\ ",
        r"                            |       | X |  |",
        r"                           _|________`-'   |X",
        r"                         /'          ~~~~~~~~~,",
        r"                       /'             ,_____,/_",
        r"                    ,/'        ___,'~~         ;",
        r"~~~~~~~~|~~~~~~~|---          /  X,~~~~~~~~~~~~,",
        r"        |       |            |  XX'____________'",
        r"        |       |           /' XXX|            ;",
        r"        |       |        --x|  XXX,~~~~~~~~~~~~,",
        r"        |       |          X|     '____________'",
        r"        |   o   |---~~~~\__XX\             |XX",
        r"        |       |          XXX`\          /XXXX",
        r"~~~~~~~~'~~~~~~~'               `\xXXXXx/' \XXX",
        r"                                 /XXXXXX\ ",
        r"                               /XXXXXXXXXX\ ",
        r"                             /XXXXXX/^\XDCAU\ ",
        r"                            ~~~~~~~~   ~~~~~~~"
    ],
    "bubble_indices": (5, 6, 7),
    "pad": 49,
    "bubble_side": "right"
}

FISH_ZEUS = {
    "lines": [
        r"           ,-,           .---'''^\                  O",
        r"          {   \       ,__\,---'''''`-.,      O    O",
        r"           I   \    K`,'^           _  `'.     o",
        r"           \  ,.J..-'`          // (O)   ,,X,    o",
        r"           /  (_               ((   ~  ,;:''`  o",
        r"          /   ,.X'.,            \\      ':;;;",
        r"         (_../      -._                  ,'`",
        r"                     K.=,;.__ /^~/___..'`",
        r"                             /  /`"
    ],
    "bubble_indices": (2, 3, 4),
    "pad": 58,
    "bubble_side": "right"
}

FISH_CROC = {
    "lines": [
        r"              _  _",
        r"    _ _      (0)(0)-._  _.-'^^'^^'^^'^^'^^'--.",
        r"   (.(.)----'`        ^^'                /^   ^^-._",
        r"   (    `                 \             |    _    ^^-._",
        r"    VvvvvvvVv~~`__,/.._>  /:/:/:/:/:/:/:/\  (_..,______^^-.",
        r"     `^^^^^^^^`/  /   /  /`^^^^^^^^^>^^>^`>  >        _`)  )",
        r"              (((`   (((`          (((`  (((`        `'--'^"
    ],
    "bubble_indices": (1, 2, 3),
    "pad": 1,
    "bubble_side": "left"
}

def make_frame(fish_data, message_text):
    msg_len = max(len(message_text), 1)
    side = fish_data.get("bubble_side", "right")
    
    if side == "right":
        bubble_top = "." + "-" * (msg_len + 2) + "."
        bubble_mid = "<  " + message_text.ljust(msg_len) + " |"
        bubble_bot = "'" + "-" * (msg_len + 2) + "'"
    else:
        bubble_top = "." + "-" * (msg_len + 2) + "."
        bubble_mid = "| " + message_text.ljust(msg_len) + "  >"
        bubble_bot = "'" + "-" * (msg_len + 2) + "'"
        
    out_lines = list(fish_data["lines"])
    
    pad = fish_data["pad"]
    i1, i2, i3 = fish_data["bubble_indices"]
    
    if side == "right":
        out_lines[i1] = out_lines[i1].ljust(pad) + bubble_top
        out_lines[i2] = out_lines[i2].ljust(pad) + bubble_mid
        out_lines[i3] = out_lines[i3].ljust(pad) + bubble_bot
    else:
        bubble_width = len(bubble_top)
        total_shift = bubble_width + pad
        out_lines = [" " * total_shift + line for line in out_lines]
        out_lines[i1] = bubble_top + out_lines[i1][bubble_width:]
        out_lines[i2] = bubble_mid + out_lines[i2][bubble_width:]
        out_lines[i3] = bubble_bot + out_lines[i3][bubble_width:]
        
    return "\n".join(out_lines)

def printdeadfihh(message):
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    final_frame = make_frame(FISH_MECHANICAL, message)
    sys.stdout.write(final_frame + "\n")
    sys.stdout.flush()

def printfihh(message):
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    final_frame = make_frame(FISH_ZEUS, message)
    sys.stdout.write(final_frame + "\n")
    sys.stdout.flush()

def printcroc(message):
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    final_frame = make_frame(FISH_CROC, message)
    sys.stdout.write(final_frame + "\n")
    sys.stdout.flush()
