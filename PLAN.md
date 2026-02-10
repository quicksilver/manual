# Plan: Reorganize developer/ folder content into docs/ and developer/

## Context

A `developer/` folder (formerly a separate GitBook-based wiki) has been added to the manual repo. It contains ~70 markdown files mixing user-facing documentation, developer/contributor docs, AppleScript recipes, and obsolete content. Many files overlap with the existing `docs/` content. The goal is to sort this content: move user-facing material into the MkDocs `docs/` tree and keep only developer/contributor content in `developer/`.

---

## Step 1: Delete overlap, obsolete, and empty files

These files should be removed from `developer/` since they're either already covered or no longer relevant. Before deleting them, check that there is no additional content in them that can be copied over to the new file. For example, the Catalog.md file has images that can be copied over and presents things in a nicer table format. The goal should be to consolidate the different parts.

### Overlap (content exists in docs/)
| File | Redundant with |
|------|---------------|
| `Catalog.md` | `docs/preferences/catalog.md` |
| `Quick-start_Guide.md` | `docs/getting-started/` |
| `Commands.md` | `docs/getting-started/invoking-quicksilver.md` |
| `Executing_actions.md` | Same as Commands.md / docs/ |
| `Comma_Trick.md` | `docs/getting-started/invoking-quicksilver.md` |
| `Event_Triggers.md` | `docs/features/triggers/event-triggers.md` |
| `Proxy_Object.md` | `docs/preferences/catalog.md` |
| `Keyboard_shortcuts.md` | `docs/getting-started/invoking-quicksilver.md` |
| `What_Is_Quicksilver.md` | `docs/index.md` |
| `Ordering_actions.md` | `docs/getting-started/invoking-quicksilver.md` |
| `Grab_'n_Drop.md` | `docs/features/using-the-mouse.md` |

### Obsolete
These should be removed entirely
- `QuickSparrow.md`, `QuickSparrow_(AppleScript).md` — Sparrow is dead
- `SuperTweet_(AppleScript).md` — SuperTweet.net shut down
- `Show_Date_and_Time_with_Growl_(AppleScript).md` — Growl abandoned
- `Dropbox_public_link_(AppleScript).md` — Dropbox Public folder removed 2017
- `TaskUnifier_AddTask_(AppleScript).md` — TaskUnifier defunct
- `Shorten_URL_(AppleScript).md` — goo.gl shut down, bit.ly API deprecated

### Outdated AppleScript recipes (skip)
These should be deleted.
- `Toggle_Bluetooth_(AppleScript).md` — requires Growl, old System Preferences UI
- `Query_WolframAlpha_(AppleScript).md` — requires Growl + PHP, uses HTTP
- `Encode_Decode_URL_(AppleScript).md` — relies on PHP availability
- `Show_Date_and_Time_with_Large_Type_(AppleScript).md` — references Growl
- `Select_File_In_Dialog.md` — deprecated Cocoa dialog UI patterns
- `Quick_Look_(AppleScript).md` — superseded by native QS support
- `Quick_Quick_Look_(AppleScript).md` — edge case, uses qlmanage directly

### Empty/redirect stubs
These should be deleted
- `Quick_Look.md`, `Quick_Quick_Look.md`, `Run_command_in_shell_with_arguments....md`, `Application_and_Plugin_Reference.md`, `Quicksilver_Source_Code.md`

### Other skips
- `Tips_&_Tricks.md` — single-line redirect to Tip_of_The_Day
- `Plugin_Reference.md` — auto-generated plugin pages are sufficient
- `Preferences.md` — just a screenshot, no real content. However the screenshot can be copied to the 'preferences/actions.md' file (create it first). This file should explain the 'Actions' preferences pane in Quicksilver.

---

## Step 2: Move user-facing files to docs/

### → `docs/appendix/` (reference material, tips, troubleshooting additions)

| File | Proposed docs/ name | Notes |
|------|-------------------|-------|
| `FAQ.md` | Merge unique Q&As into `docs/appendix/FAQ.md` | Has some items not in existing FAQ |
| `Hidden_Defaults.md` | `docs/appendix/hidden-defaults.md` | Table of `defaults write` preferences |
| `Hidden_Secrets.md` | Merge into hidden-defaults.md | Single entry |
| `Known_Bad_Applications.md` | `docs/appendix/known-bad-applications.md` | List of apps that interfere with QS |
| `Tip_of_The_Day.md` | `docs/appendix/tips.md` | Large collection of tips |
| `Support_and_Troubleshooting.md` | Merge links into `docs/appendix/Troubleshooting.md` | |
| `Crash_Reports.md` | Merge into `docs/appendix/Troubleshooting.md` | |
| `Tutorials.md` | `docs/appendix/tutorials.md` | External tutorial links |
| `Quicksilver_User's_Guide.md` | Merge into `docs/appendix/index.md` | Link to Howard Melman's PDF |
| `Where_is_everything.md` | Merge useful bits into `docs/appendix/FAQ.md` | Download/docs/help links |

### → `docs/features/` (feature documentation)

| File | Proposed docs/ name | Notes |
|------|-------------------|-------|
| `Alternate_Actions.md` | `docs/features/alternate-actions.md` | Table of Cmd+Return alternate actions |
| `Finder_Selection.md` | `docs/features/finder-selection.md` | Proxy objects vs service for Finder |
| `Interfaces.md` | `docs/features/interfaces.md` | Visual gallery of interface themes |
| `DeMinimizer_Module.md` | Remove | Plugin-specific content |

### → `docs/features/applescript/` (new section for AppleScript recipes)

| File | Proposed docs/ name |
|------|-------------------|
| `AppleScripts.md` | `docs/features/applescript/index.md` (overview) |
| `AppleScript_Actions.md` | `docs/features/applescript/custom-actions.md` |
| `AppleScript_Action_templates.md` | `docs/features/applescript/templates.md` |
| `Color_Picker_(AppleScript).md` | `docs/features/applescript/color-picker.md` |
| `Convert_Units_To.md` | `docs/features/applescript/convert-units.md` |
| `Open_AirDrop_(AppleScript).md` | `docs/features/applescript/open-airdrop.md` |
| `Paste_file_path_(AppleScript).md` | `docs/features/applescript/paste-file-path.md` |
| `Run_command_in_shell_with_arguments.md` | `docs/features/applescript/run-shell-command.md` |

---

## Step 3: Keep developer-facing files in developer/

These stay in `developer/` (will become the developer docs site later):

| File | Content |
|------|---------|
| `Building_Quicksilver.md` | Building from source |
| `Debugging_Quicksilver.md` | Debugging in Xcode |
| `Developer_Information.md` | Developer index page |
| `Github.md` | Coding style, PR workflow |
| `Notifications.md` | NSNotification reference |
| `UnitTests.md` | Test guide |
| `Release_Process.md` | Release checklist |
| `Localization.md` | i18n/l10n guide |
| `Plugins_Template.md` | Plugin doc template |
| `QSApp.com.md` | Website/infra docs |
| `Helping_Quicksilver.md` | Contributing guide |
| `Tech/Quicksilver_Server.md` | Server protocol docs |
| `Tech/Updating_the_Plugins_List.md` | Plugin list maintenance |

---

## Step 4: Update mkdocs.yml nav

Add new sections to `mkdocs.yml`:

- Add "AppleScript" subsection under Features
- Add new appendix entries (hidden-defaults, known-bad-applications, tips, tutorials)
- Add new feature entries (alternate-actions, finder-selection, interfaces)

---

## Step 5: Clean up developer/ artifacts

- Remove `developer/.git/` (nested git repo)
- Remove `developer/SUMMARY.md` and `developer/README.md` (GitBook files)
- Remove `developer/LICENSE` if redundant with repo root
- Move any images referenced by kept developer files; remove the rest

---

## Verification

1. Run `venv/bin/mkdocs build` and confirm zero warnings
2. Spot-check that moved pages render correctly at their new URLs
3. Confirm no broken internal links between pages
