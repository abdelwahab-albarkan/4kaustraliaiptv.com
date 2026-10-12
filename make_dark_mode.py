"""Turns the light theme's hard-coded colours into design tokens, then adds a dark theme that is switched with data-theme="dark"."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
P = 'assets/css/style.css'
css = open(P, encoding='utf8').read()
MARK = '/* ==== theme tokens applied ==== */'
if MARK in css: raise SystemExit('already applied')
i = css.find('LIGHT THEME - clean')
i = css.rfind('/* ====', 0, i)
head, region = css[:i], css[i:]

BG = {'#fff': 'var(--surface)', '#ffffff': 'var(--surface)', '#f8fafc': 'var(--surface-2)', '#f1f5f9': 'var(--surface-3)', '#eff6ff': 'var(--tint)', '#dbeafe': 'var(--tint-2)',
      '#f0fdf4': 'var(--ok-bg)', '#ecfdf5': 'var(--ok-bg)', '#dcfce7': 'var(--ok-bg)', '#fffbeb': 'var(--warn-bg)', '#fef3c7': 'var(--warn-bg)'}
COLOR = {'#0f172a': 'var(--ink)', '#334155': 'var(--ink-2)', '#475569': 'var(--text-muted)', '#64748b': 'var(--text-dim)', '#1d4ed8': 'var(--link-strong)', '#1e40af': 'var(--link-strong)',
         '#15803d': 'var(--ok-text)', '#166534': 'var(--ok-text)', '#92400e': 'var(--warn-text)', '#b45309': 'var(--warn-text)'}
BORDER = {'#e2e8f0': 'var(--border-color)', '#cbd5e1': 'var(--line-2)', '#bfdbfe': 'var(--tint-border)', '#bbf7d0': 'var(--ok-border)', '#fde68a': 'var(--warn-border)', '#fcd9a0': 'var(--warn-border)'}
n = {'bg': 0, 'color': 0, 'border': 0}
def sub_map(v, m, key):
    def r(x):
        n[key] += 1
        return m[x.group(0).lower()]
    return re.sub('|'.join(re.escape(k) + r'\b' for k in sorted(m, key=len, reverse=True)), r, v, flags=re.I)
def decl(m):
    prop, val = m.group(1), m.group(2)
    if prop.startswith('--'): return m.group(0)
    if prop.startswith('background'): val = sub_map(val, BG, 'bg')
    elif prop == 'color': val = sub_map(val, COLOR, 'color')
    elif prop.startswith('border') or prop == 'outline': val = sub_map(val, BORDER, 'border')
    return '%s:%s' % (prop, val) if m.group(0).split(':')[0] == prop else m.group(0)
# keep the original spacing after the colon
def decl2(m):
    prop, sp, val = m.group(1), m.group(2), m.group(3)
    if prop.startswith('--'): return m.group(0)
    v2 = val
    if prop.startswith('background'): v2 = sub_map(val, BG, 'bg')
    elif prop == 'color': v2 = sub_map(val, COLOR, 'color')
    elif prop.startswith('border') or prop == 'outline': v2 = sub_map(val, BORDER, 'border')
    return '%s:%s%s' % (prop, sp, v2)
region = re.sub(r'(?<![\w-])([a-z-]+)\s*:(\s*)([^;{}]+)', decl2, region)
print('replaced:', n)

TOKENS = '''
''' + MARK + '''
:root {
  --surface: #ffffff; --surface-2: #f8fafc; --surface-3: #f1f5f9;
  --tint: #eff6ff; --tint-2: #dbeafe; --tint-border: #bfdbfe;
  --ink: #0f172a; --ink-2: #334155; --link-strong: #1d4ed8;
  --line-2: #cbd5e1;
  --ok-bg: #f0fdf4; --ok-text: #15803d; --ok-border: #bbf7d0;
  --warn-bg: #fffbeb; --warn-text: #92400e; --warn-border: #fde68a;
  color-scheme: light;
}
/* ---------- Dark theme ---------- */
:root[data-theme="dark"] {
  color-scheme: dark;
  --bg-main: #0b1220; --bg-secondary: #0e1626; --bg-card: #111a2e; --bg-card-hover: #111a2e; --bg-glass: #111a2e; --bg-glass-strong: #111a2e;
  --surface: #111a2e; --surface-2: #0e1626; --surface-3: #172238;
  --tint: rgba(37,99,235,.16); --tint-2: rgba(37,99,235,.26); --tint-border: rgba(96,165,250,.38);
  --ink: #e8eef9; --ink-2: #c3cee0; --text-main: #e8eef9; --text-muted: #aab6cb; --text-dim: #8190a8;
  --border-color: rgba(148,163,184,.2); --line-2: rgba(148,163,184,.34); --border-highlight: rgba(96,165,250,.4);
  --primary: #60a5fa; --primary-dark: #93c5fd; --link-strong: #93c5fd;
  --aus-gold: #fcd34d; --aus-green: #4ade80; --gold: #fbbf24;
  --ok-bg: rgba(34,197,94,.14); --ok-text: #86efac; --ok-border: rgba(34,197,94,.32);
  --warn-bg: rgba(245,158,11,.14); --warn-text: #fcd34d; --warn-border: rgba(245,158,11,.34);
  --shadow-sm: 0 1px 2px rgba(0,0,0,.4); --shadow-md: 0 8px 22px rgba(0,0,0,.4); --shadow-lg: 0 18px 44px rgba(0,0,0,.5);
}
:root[data-theme="dark"] a:hover { color: #bfdbfe; }
:root[data-theme="dark"] .site-header, :root[data-theme="dark"] .site-header.scrolled { background: rgba(11,18,32,.92); }
:root[data-theme="dark"] .announcement-bar { background: #070d19; }
:root[data-theme="dark"] .site-footer { background: #070d19; }
:root[data-theme="dark"] .nav-dropdown-menu, :root[data-theme="dark"] .main-nav { background: #0e1626; }
:root[data-theme="dark"] figure.hero-visual::after { background: linear-gradient(180deg, transparent 60%, rgba(17,26,46,.95) 100%); }
:root[data-theme="dark"] .page-banner::after { background: linear-gradient(180deg, transparent 55%, rgba(0,0,0,.35)); }
:root[data-theme="dark"] .sticky-cta { background: rgba(11,18,32,.96); }
:root[data-theme="dark"] .hero-section { background: linear-gradient(180deg, rgba(37,99,235,.14) 0%, var(--bg-main) 70%); }
:root[data-theme="dark"] .btn-primary { background: #2563eb; color: #fff; }
:root[data-theme="dark"] .btn-secondary, :root[data-theme="dark"] .btn-outline { color: var(--ink); border-color: var(--line-2); }
:root[data-theme="dark"] .btn-outline { color: #93c5fd; border-color: rgba(96,165,250,.5); }
:root[data-theme="dark"] .btn-gold, :root[data-theme="dark"] .btn-gold:hover { color: #1c1100; }
:root[data-theme="dark"] .badge-glow-cyan, :root[data-theme="dark"] .badge-glow-mauve { background: rgba(37,99,235,.18); border-color: rgba(96,165,250,.4); color: #bfdbfe; }
:root[data-theme="dark"] .badge-glow-gold { background: rgba(245,158,11,.14); border-color: rgba(245,158,11,.4); color: #fcd34d; }
:root[data-theme="dark"] .badge-glow-green { background: rgba(34,197,94,.14); border-color: rgba(34,197,94,.4); color: #86efac; }
:root[data-theme="dark"] .gradient-text, :root[data-theme="dark"] .mauve-gradient-text { color: #60a5fa; }
:root[data-theme="dark"] .gold-gradient-text { color: #fbbf24; }
:root[data-theme="dark"] .emerald-gradient-text { color: #4ade80; }
:root[data-theme="dark"] .acct-btn.active, :root[data-theme="dark"] .toggle-btn.active { color: #fff; }
:root[data-theme="dark"] .form-control, :root[data-theme="dark"] .bw-card input, :root[data-theme="dark"] .bw-card select { background: var(--surface-2); color: var(--ink); border-color: var(--line-2); }
:root[data-theme="dark"] .modal-overlay { background: rgba(2,6,16,.72); }
:root[data-theme="dark"] .hub-card, :root[data-theme="dark"] .region-card, :root[data-theme="dark"] .criteria, :root[data-theme="dark"] .steps-list li { background: var(--surface); }
:root[data-theme="dark"] img { filter: brightness(.92); }
:root[data-theme="dark"] .pay-logos img, :root[data-theme="dark"] .mosaic-tile img, :root[data-theme="dark"] .hero-visual img, :root[data-theme="dark"] .logo-badge img { filter: none; }
/* payment logos are artwork for white tiles */
:root[data-theme="dark"] .pay-logos img, :root[data-theme="dark"] .pay-chip { background: #fff !important; color: #0f172a; }
:root[data-theme="dark"] .site-footer div[style*="background:#fff"] { background: #fff !important; }
:root[data-theme="dark"] .hero-portal-card [style*="rgba(10,6,20"], :root[data-theme="dark"] [style*="position:absolute"][style*="rgba(10,6,20"] { color: #fff !important; }
:root[data-theme="dark"] [style*="rgba(0,0,0,0.35)"], :root[data-theme="dark"] [style*="rgba(0,0,0,0.4)"], :root[data-theme="dark"] [style*="rgba(0,0,0,0.5)"], :root[data-theme="dark"] [style*="rgba(0,0,0,0.3)"] { background-color: var(--surface-3) !important; }
:root[data-theme="dark"] [style*="background:#f8fafc"] { background: var(--surface-2) !important; }
:root[data-theme="dark"] [style*="color:#ef4444"] { color: #f87171 !important; }
/* ---------- Theme switch button ---------- */
.theme-toggle { display: inline-flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 50%; border: 1px solid var(--border-color); background: var(--surface); color: var(--ink); font-size: 1rem; cursor: pointer; transition: background-color .15s, border-color .15s, transform .15s; flex: 0 0 auto; }
.theme-toggle:hover { border-color: #93c5fd; transform: rotate(-12deg); }
.theme-toggle .fa-sun { display: none; }
:root[data-theme="dark"] .theme-toggle .fa-moon { display: none; }
:root[data-theme="dark"] .theme-toggle .fa-sun { display: inline; color: #fcd34d; }
@media (max-width: 420px) { .theme-toggle { width: 36px; height: 36px; } }
@media (prefers-reduced-motion: reduce) { .theme-toggle:hover { transform: none; } }
'''
open(P, 'w', encoding='utf8').write(head + region + TOKENS)
print('css rewritten:', len(head + region + TOKENS) // 1024, 'KB')
