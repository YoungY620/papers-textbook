#!/usr/bin/env bash
# Build the English book (site root) and the Chinese book (/zh/) into _site/.
set -euo pipefail
cd "$(dirname "$0")"

python3 tools/build_glossary.py glossary.yml src zh/src

mdbook build
python3 tools/restore_math.py book

(cd zh && mdbook build)
python3 tools/restore_math.py zh/book

rm -rf _site
mkdir -p _site/zh
cp -R book/. _site/
cp -R zh/book/. _site/zh/
touch _site/.nojekyll

echo "built _site/ ($(find _site -name '*.html' | wc -l | tr -d ' ') pages)"
