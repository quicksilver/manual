#!/usr/bin/env bash

set -Eeuf -o pipefail
shopt -s inherit_errexit

main() {
  cd /data/manual
  git pull --dry-run
  venv/bin/python plugindocs.py
  venv/bin/python -m mkdocs build
}
main "$@"
