"""Read saved "best X" listicle HTML files and print where Brevo ranks.

Usage: python3 -I listicle.py [--loose] page1.html page2.html ...

Default mode counts only numbered headings ("1. Brevo", "#2 SMTP2GO").
--loose counts every short h2-h4 heading, for pages that do not number entries.
Also counts Brevo affiliate links. Edit V to measure another category.
"""
import html
import os
import re
import sys
from html.parser import HTMLParser

V = {
    'Brevo': r'brevo|sendinblue', 'SMTP2GO': r'smtp2go', 'Resend': r'\bresend\b',
    'Mailjet': r'mailjet', 'Amazon SES': r'amazon ses|\bses\b', 'SendGrid': r'sendgrid',
    'Mailgun': r'mailgun', 'Postmark': r'postmark', 'MailerSend': r'mailersend',
    'Mailtrap': r'mailtrap', 'SendPulse': r'sendpulse', 'Sender': r'\bsender\b(?!\.net/blog)',
    'UniOne': r'unione', 'SendLayer': r'sendlayer', 'SMTPfast': r'smtpfast|smtpfa\.st',
    'Groundmail': r'groundmail', 'Elastic': r'elastic ?email', 'Zoho': r'zeptomail|zoho',
    'turboSMTP': r'turbo ?smtp', 'Mailsoftly': r'mailsoftly', 'Moosend': r'moosend',
    'Gmail': r'gmail', 'SMTP.com': r'smtp\.com', 'Lettr': r'lettr', 'DeBounce': r'debounce',
}
TARGET = 'Brevo'
AFFILIATE = r'get\.brevo\.com|brevo\.com[^"\']*(?:ref=|tap_a=|aff|partner|utm_source)|sendinblue\.com[^"\']*(?:ref|aff)'


class Headings(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cur, self.buf, self.found = None, '', []

    def handle_starttag(self, tag, attrs):
        if tag in ('h2', 'h3', 'h4'):
            self.cur, self.buf = tag, ''

    def handle_endtag(self, tag):
        if tag == self.cur:
            self.found.append(re.sub(r'\s+', ' ', self.buf).strip())
            self.cur = None

    def handle_data(self, data):
        if self.cur:
            self.buf += data


def first_vendor(text):
    best, pos = None, 10 ** 9
    for name, rx in V.items():
        m = re.search(rx, text, re.I)
        if m and m.start() < pos:
            pos, best = m.start(), name
    return best


def main(argv):
    loose = '--loose' in argv
    files = [a for a in argv if a != '--loose']
    for f in files:
        src = open(f, encoding='utf-8', errors='replace').read()
        parser = Headings()
        parser.feed(src)
        order = []
        for h in parser.found:
            if loose:
                if len(h) > 90:
                    continue
            elif not re.match(r'^\s*(#?\d+[\.\):]|\d+\s*[-–—])', h):
                continue
            v = first_vendor(h)
            if v and v not in order:
                order.append(v)
        text = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', src, flags=re.S | re.I)
        text = html.unescape(re.sub(r'<[^>]+>', ' ', text))
        mentions = {n: len(re.findall(V[n], text, re.I)) for n in ('Brevo', 'SMTP2GO', 'Resend', 'Mailjet')}
        aff = len(re.findall(AFFILIATE, src, re.I))
        if TARGET in order:
            rank = '#' + str(order.index(TARGET) + 1)
        else:
            rank = 'mentioned' if mentions[TARGET] else 'absent'
        name = os.path.basename(f).replace('.html', '')
        print(f"{name:20s} {TARGET} {rank:9s} mentions={mentions} affiliate_links={aff} | top: {' > '.join(order[:6])}")


if __name__ == '__main__':
    main(sys.argv[1:])
