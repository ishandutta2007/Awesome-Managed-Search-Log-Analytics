import os
import json
import urllib.request

os.makedirs('C:/Users/hp/Documents/Projects/Awesome-Managed-Search-Log-Analytics/assets', exist_ok=True)

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#1e1b4b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .title { font-family: system-ui, -apple-system, sans-serif; font-weight: 800; font-size: 42px; fill: #ffffff; }
    .subtitle { font-family: system-ui, -apple-system, sans-serif; font-weight: 500; font-size: 20px; fill: #94a3b8; }
    .badge-text { font-family: system-ui, -apple-system, sans-serif; font-weight: 600; font-size: 13px; fill: #38bdf8; }
    
    @keyframes pulse {
      0% { opacity: 0.3; transform: scale(0.98); }
      50% { opacity: 0.7; transform: scale(1.02); }
      100% { opacity: 0.3; transform: scale(0.98); }
    }
    @keyframes float1 {
      0% { transform: translateY(0px); }
      50% { transform: translateY(-10px); }
      100% { transform: translateY(0px); }
    }
    @keyframes float2 {
      0% { transform: translateY(0px); }
      50% { transform: translateY(12px); }
      100% { transform: translateY(0px); }
    }
    .wave { animation: pulse 6s ease-in-out infinite; transform-origin: center; }
    .float-item1 { animation: float1 5s ease-in-out infinite; }
    .float-item2 { animation: float2 7s ease-in-out infinite; }
  </style>

  <!-- Background -->
  <rect width="1200" height="320" rx="16" fill="url(#bg)" />
  
  <!-- Dynamic Background Geometric Elements (Behind Text) -->
  <g opacity="0.25" class="wave">
    <circle cx="150" cy="80" r="120" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6 6" />
    <circle cx="1050" cy="240" r="160" fill="none" stroke="#c084fc" stroke-width="1.5" stroke-dasharray="8 8" />
    <path d="M-50 220 Q 300 120 600 220 T 1250 180" fill="none" stroke="url(#accent)" stroke-width="2" />
  </g>

  <!-- Decorative Animated Floating Graph Bars (Background Accents) -->
  <g class="float-item1" opacity="0.2" transform="translate(920, 60)">
    <rect x="0" y="40" width="18" height="80" rx="4" fill="#38bdf8" />
    <rect x="28" y="10" width="18" height="110" rx="4" fill="#818cf8" />
    <rect x="56" y="60" width="18" height="60" rx="4" fill="#c084fc" />
    <rect x="84" y="25" width="18" height="95" rx="4" fill="#38bdf8" />
  </g>

  <g class="float-item2" opacity="0.15" transform="translate(80, 160)">
    <polygon points="30,10 80,90 10,90" fill="none" stroke="#38bdf8" stroke-width="2" />
    <circle cx="120" cy="40" r="25" fill="none" stroke="#818cf8" stroke-width="2" />
  </g>

  <!-- Accent Top Border Line -->
  <rect x="0" y="0" width="1200" height="5" fill="url(#accent)" />

  <!-- FOREGROUND CONTENT (Guaranteed High Visibility) -->
  <g transform="translate(80, 95)">
    <!-- Category Tag -->
    <rect x="0" y="0" width="250" height="30" rx="15" fill="#1e293b" stroke="#38bdf8" stroke-width="1" />
    <text x="125" y="19" text-anchor="middle" class="badge-text">⚡ SAAS &amp; OPEN-SOURCE ECOSYSTEM</text>
    
    <!-- Title -->
    <text x="0" y="75" class="title" filter="url(#glow)">Awesome Managed Search &amp; Log Analytics</text>
    
    <!-- Subtitle -->
    <text x="0" y="115" class="subtitle">Curated Platform Index for Log Aggregation, Full-Text Search &amp; Observability</text>
    
    <!-- Decorative Line -->
    <line x1="0" y1="140" x2="480" y2="140" stroke="url(#accent)" stroke-width="3" stroke-linecap="round" />
  </g>
</svg>
"""

with open('C:/Users/hp/Documents/Projects/Awesome-Managed-Search-Log-Analytics/assets/banner.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
print("Saved assets/banner.svg")

repos = [
    'apache/druid',
    'apache/pinot',
    'fluent/fluentd',
    'fluent/fluent-bit',
    'vectordotdev/vector'
]

for repo in repos:
    req = urllib.request.Request(f'https://api.github.com/repos/{repo}', headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"{repo}: {data.get('stargazers_count')}")
    except Exception as e:
        print(f"{repo}: error {e}")
