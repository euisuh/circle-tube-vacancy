"""Write TikZ figure bodies from the exact limit formulas (no plotting deps).

Run from the repository root:  python3 manuscript/make_figures.py
"""
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import circle_research as cr  # noqa: E402

OUT = Path(__file__).resolve().parent / 'figures'
LAM, Q, A2 = cr.LAMBDA, math.sin(cr.ALPHA), math.cos(cr.ALPHA) ** 2


def v_delta(c):
    if c >= math.pi * Q:
        return A2
    t = c / math.pi
    return A2 + Q * Q - 4 * t * Q + 3 * t * t + 2 * t * t * math.log(Q / t)


def path(points, xs, ys):
    return ' -- '.join(f'({xs(x):.4f},{ys(y):.4f})' for x, y in points)


def phase_figure():
    """V(x,c)-V(0,c) against phase x, three widths."""
    xs = np.linspace(0, LAM, 241)
    lines = []
    scale_x, scale_y = 10 / LAM, 5 / 0.0065
    styles = {1: 'thick, black', 2: 'thick, black, dashed', 3: 'thick, black, dotted'}
    for c in (1, 2, 3):
        pts = [(x, cr.predictor(c, x) - cr.predictor(c, 0)) for x in xs]
        lines.append(f'\\draw[{styles[c]}] ' + path(pts, lambda x: x * scale_x, lambda y: y * scale_y) + ';')
        x_end, y_end = pts[{1: 30, 2: 120, 3: 190}[c]]
        anchor = {1: 'above left', 2: 'above', 3: 'above right'}[c]
        lines.append(f'\\node[{anchor}, font=\\small] at ({x_end*scale_x:.3f},{y_end*scale_y:.3f}) {{$c={c}$}};')
    axes = [r'\draw[->] (0,0) -- (10.6,0) node[right] {$x$};',
            r'\draw[->] (0,0) -- (0,5.3) node[above] {$V(x,c)-V(0,c)$};']
    for t in (0, 0.2, 0.4):
        axes.append(f'\\draw ({t*scale_x:.3f},0) -- ({t*scale_x:.3f},-0.1) node[below, font=\\small] {{{t}}};')
    axes.append(f'\\draw ({LAM*scale_x:.3f},0) -- ({LAM*scale_x:.3f},-0.1) node[below, font=\\small] {{$\\lambda$}};')
    for t in (0, 0.002, 0.004, 0.006):
        axes.append(f'\\draw (0,{t*scale_y:.3f}) -- (-0.1,{t*scale_y:.3f}) node[left, font=\\small] {{{t}}};')
    return '\n'.join(axes + lines)


def threshold_figure():
    """Oscillation amplitude and gap to the uniform envelope against c."""
    cs = np.linspace(0.02, 6.2, 311)
    xs = np.linspace(0, LAM, 121)
    sx, sy = 10 / 6.2, 5 / 0.008
    amp = [(c, max(cr.predictor(c, x) for x in xs) - cr.predictor(c, 0)) for c in cs]
    gap = [(c, cr.predictor(c, 0) - v_delta(c)) for c in cs]
    out = [r'\draw[->] (0,0) -- (10.6,0) node[right] {$c$};',
           r'\draw[->] (0,0) -- (0,5.3);']
    for t in range(7):
        out.append(f'\\draw ({t*sx:.3f},0) -- ({t*sx:.3f},-0.1) node[below, font=\\small] {{{t}}};')
    for t in (0, 0.002, 0.004, 0.006, 0.008):
        out.append(f'\\draw (0,{t*sy:.3f}) -- (-0.1,{t*sy:.3f}) node[left, font=\\small] {{{t}}};')
    cstar = math.pi * Q / (math.sqrt(5) * LAM ** 3)
    out.append(f'\\draw[gray, densely dotted] ({cstar*sx:.3f},0) -- ({cstar*sx:.3f},2) node[above, font=\\small] {{$c_*$}};')
    out.append(f'\\draw[gray, densely dotted] ({math.pi*Q*sx:.3f},0) -- ({math.pi*Q*sx:.3f},3) node[above, font=\\small] {{$\\pi Q$}};')
    out.append('\\draw[thick, black] ' + path(amp, lambda c: c * sx, lambda v: v * sy) + ';')
    out.append('\\draw[thick, black, dashed] ' + path(gap, lambda c: c * sx, lambda v: v * sy) + ';')
    return '\n'.join(out)


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / 'phase.tex').write_text(phase_figure() + '\n')
    (OUT / 'threshold.tex').write_text(threshold_figure() + '\n')
    print('wrote', OUT / 'phase.tex', OUT / 'threshold.tex')


if __name__ == '__main__':
    main()
