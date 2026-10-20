"""Assemble and validate the English RFC using only the Python standard library."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json
import posixpath
import re
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
PARTS = sorted((ROOT / 'chapters').glob('*.md')) + sorted((ROOT / 'appendices').glob('*.md'))
LINK = re.compile(r'(!?\[[^\]\n]*\]\()([^\s)]+)(\))')
ANCHOR = re.compile(r'<a id="([^"]+)"></a>')
IDENTIFIER = re.compile(r'\b(?:R-\d{2}-\d{2}|(?:V|Q|H|INV|E|B)-\d{2})\b')
DEFINITION = re.compile(r'^\| ((?:R-\d{2}-\d{2}|(?:V|Q|H|INV|E|B)-\d{2}))(?=\s|:|\|)|^\*\*(R-\d{2}-\d{2})\b', re.M)


def read(path):
    return path.read_text(encoding='utf-8')


def title(path):
    return re.search(r'^# (.+)$', read(path), re.M).group(1)


def assemble():
    entries = {p.relative_to(ROOT).as_posix(): ANCHOR.search(read(p)).group(1) for p in PARTS}
    output = ['# Codex Studio', '', '## A Project-Centric Engineering Workspace for Agentic Software Development', '',
              '**TechSoft · Full RFC · English public edition · 2026-10-21**', '',
              'Based on the complete version 1.1 review draft. This independent proposal is not an announced OpenAI product. Images are conceptual illustrations; no Studio prototype or product evaluation is claimed.', '',
              '[Repository guide](README.md) · [Publication review](REVIEW.md) · [Community article](https://community.openai.com/t/codex-studio-a-project-centric-engineering-workspace-for-agentic-software-development/1408219)', '',
              'This file is generated from the chapter and appendix sources. Edit those sources and run `python tools/build_rfc.py` to rebuild it.', '',
              '## Contents', '']
    output.extend('- [' + title(p) + '](#' + entries[p.relative_to(ROOT).as_posix()] + ')' for p in PARTS)
    for part in PARTS:
        text = read(part)
        def relocate(match):
            destination = match.group(2)
            url = urlsplit(destination)
            if url.scheme or url.netloc or not url.path:
                return match.group(0)
            target = posixpath.normpath(posixpath.join(part.parent.relative_to(ROOT).as_posix(), url.path))
            if target in entries:
                destination = '#' + (url.fragment or entries[target])
            else:
                destination = target + ('#' + url.fragment if url.fragment else '')
            return match.group(1) + destination + match.group(3)
        text = LINK.sub(relocate, text)
        lines = []
        fenced = False
        for line in text.splitlines():
            if line.startswith('```'):
                fenced = not fenced
            if not fenced and line.startswith('#'):
                line = '#' + line
            lines.append(line)
        output.extend(['', '---', '', '\n'.join(lines)])
    return '\n'.join(output).rstrip() + '\n'


def validate():
    errors = []
    if len(PARTS) != 20 or len(list((ROOT/'chapters').glob('*.md'))) != 15:
        errors.append('Expected 15 chapters and 5 appendices.')
    markdown = sorted(ROOT.glob('*.md')) + PARTS
    for path in markdown:
        text = read(path)
        label = path.relative_to(ROOT).as_posix()
        if re.search(r'[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff]', text):
            errors.append(label + ': unexpected Arabic-script text or BOM.')
        anchors = ANCHOR.findall(text)
        if len(anchors) != len(set(anchors)):
            errors.append(label + ': duplicate explicit anchors.')
        if len(re.findall(r'^```', text, re.M)) % 2:
            errors.append(label + ': unbalanced code fences.')
        columns = None
        for line in text.splitlines():
            if line.startswith('|'):
                width = len(re.split(r'(?<!\\)\|', line)) - 2
                if columns is not None and width != columns:
                    errors.append(label + ': inconsistent table column count: ' + line[:70])
                columns = width
            else:
                columns = None
        for match in LINK.finditer(text):
            destination = unquote(match.group(2))
            url = urlsplit(destination)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / url.path).resolve() if url.path else path
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(label + ': missing or out-of-repository link ' + destination)
            elif url.fragment and (target.suffix != '.md' or url.fragment not in ANCHOR.findall(read(target))):
                errors.append(label + ': missing explicit target anchor ' + destination)
    source = '\n'.join(read(p) for p in PARTS)
    definitions = Counter(a or b for a,b in DEFINITION.findall(source))
    for ident, count in definitions.items():
        if count != 1:
            errors.append(ident + ': duplicate definition.')
    for ident in sorted(set(IDENTIFIER.findall(source)) - set(definitions)):
        errors.append(ident + ': reference without a definition.')
    images = json.loads(read(ROOT/'assets/manifest.json'))['images']
    if len(images) != 6 or {p.name for p in (ROOT/'assets').glob('*.png')} != {Path(i['file']).name for i in images}:
        errors.append('Expected exactly six registered PNGs.')
    for item in images:
        data = (ROOT / item['file']).read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II', data[16:24]) != (item['width'], item['height']):
            errors.append(item['file'] + ': invalid PNG or dimension mismatch.')
        if hashlib.sha256(data).hexdigest() != item['sha256']:
            errors.append(item['file'] + ': hash mismatch.')
    return errors, Counter(ident.split('-')[0] for ident in definitions)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate without writing; fail if FULL-RFC.md is stale.')
    args = parser.parse_args()
    full = assemble()
    destination = ROOT / 'FULL-RFC.md'
    if not args.check:
        destination.write_text(full, encoding='utf-8', newline='\n')
    errors, counts = validate()
    if not destination.exists() or read(destination) != full:
        errors.append('FULL-RFC.md is missing or stale; run python tools/build_rfc.py.')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print('PASS: 15 chapters, 5 appendices, 6 PNGs; local links, anchors, tables, identifiers and generated document are consistent.')
    print('Definitions: ' + ', '.join(f'{key}={counts[key]}' for key in ('R','V','Q','H','INV','E','B')))
    print('External websites and proposed product behaviors are not tested by this command.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
