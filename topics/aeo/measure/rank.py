import sys, json, re, glob, os
out = sys.argv[1]; prefix = sys.argv[2]
V = {'Brevo':r'brevo|sendinblue','SMTP2GO':r'smtp2go','Resend':r'\bresend\b','Mailjet':r'mailjet','Amazon SES':r'amazon ses|\bses\b|aws ses','SendGrid':r'sendgrid','Mailgun':r'mailgun','Postmark':r'postmark','MailerSend':r'mailersend','Zoho':r'zeptomail|zoho','SendPulse':r'sendpulse','Elastic':r'elastic ?email','Mailtrap':r'mailtrap','Gmail':r'gmail|google workspace','Scaleway':r'scaleway','Cloudflare':r'cloudflare','Proton':r'proton','Maileroo':r'maileroo','Sweego':r'sweego','Plunk':r'plunk','Loops':r'\bloops\b','Lettermint':r'lettermint','Mailpace':r'mailpace|ohmysmtp','Purelymail':r'purelymail','Migadu':r'migadu','Postal':r'\bpostal\b','Turbo':r'turbo-smtp|turbosmtp','Netcore':r'netcore|pepipost','Outlook':r'outlook|microsoft 365','Mailchannels':r'mailchannels','Unsender':r'unsend|usesend','AhaSend':r'ahasend'}
def text_of(f):
    raw = open(f, encoding='utf-8', errors='replace').read()
    if f.endswith('.txt'): return raw
    try: d = json.loads(raw)
    except Exception: return raw
    for k in ('result','response','text','content','output'):
        if isinstance(d.get(k), str): return d[k]
    return raw
rows = []
for f in sorted(glob.glob(os.path.join(out, prefix + '*'))):
    if not (f.endswith('.json') or f.endswith('.txt')): continue
    t = text_of(f)
    lines = [l for l in t.splitlines() if re.match(r'\s*(\d+[\.\)、]|[-*•]|\|\s*\d)', l)]
    order = []
    for l in lines:
        hit = None; best = 10**9
        for name, rx in V.items():
            m = re.search(rx, l, re.I)
            if m and m.start() < best: best, hit = m.start(), name
        if hit and hit not in order: order.append(hit)
    tag = os.path.basename(f).rsplit('.',1)[0].replace(prefix,'')
    rows.append((tag, order))
    pos = order.index('Brevo')+1 if 'Brevo' in order else '-'
    print(f"{tag:12s} Brevo#{pos!s:2s} | " + ' > '.join(order))
