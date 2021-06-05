import thecampy
import sys

from .models import Article
from .config import name, bday, edate, uname, id, pw

# thecampy API 사양 참고하여 config.py를 새로 만들면 됨.
# ex) '홍길동', 20010101, 20210607, '육군훈련소'

SOLDIER = thecampy.Soldier(
    name, bday, edate, uname
)
tc = thecampy.client()


def send_letter(letter: Article):
    try:
        title = f'{letter.title} ({letter.last_updated_at})'
        message = thecampy.Message(title, letter.content[:1500])

        print(f"[+] LETTER: {title}, {letter.content[:1500]}", file=sys.stderr)

        tc.login(id, pw)
        print(f"[+] Successfully logged in.", file=sys.stderr)
        tc.get_soldier(SOLDIER)
        print(f"[+] Found the soldier.", file=sys.stderr)
        tc.send_message(SOLDIER, message)
        print(f"[+] Successfully sent the letter.", file=sys.stderr)

        return True

    except Exception as p:
        return False
