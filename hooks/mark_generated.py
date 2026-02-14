"""Mark generated plugin docs so git-revision-date-localized uses build date."""

import fnmatch


def on_files(files, config):
    for f in files:
        if fnmatch.fnmatch(f.src_path, "plugins/*.md") and f.src_path != "plugins/index.md":
            f.generated_by = "plugindocs"
