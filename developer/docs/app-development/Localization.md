## Localising Quicksilver

In order to help localise Quicksilver, visit the [Quicksilver
Transifex](https://www.transifex.com/quicksilver/quicksilver/) Project
page. All files that are currently localisable are shown on Transifex.

Thank you for helping!

## Localisation for Developers

### Localising Strings in the code

**For developers only:**

All strings that are eventually visible to the user should be localised,
excluding NSLog strings (discussion needed). Note that NO strings other
than English strings should be translated downstream of the Transifex
project. The workflow is to *push* only English files and *pull* all
other translations from Transifex.

If you are working on the core App using the
`NSLocalizedString(@"my english string",nil)` method. There is no need
to create a corresponding entry in any .strings file, as if none exists,
the original string will be used.

In order to localise plugins, you should use the
`NSLocalizedStringFromTableInBundle(@"Error renaming File: %@ to %@", nil, [NSBundle bundleForClass:[self class]], nil)`.

In both the above cases, `nil` was passed as the last argument. This is
a 'comment' entry. See [Apple's
documentation](https://developer.apple.com/library/mac/#documentation/cocoa/reference/foundation/miscellaneous/foundation_functions/reference/reference.html).

Passing `nil` as the table (as has been done in the above two cases),
the default 'Localizable' table (or Localizable.strings file) is used
for storing and subsequently translating the string. Use

    NSString *NSLocalizedStringFromTable(NSString *key,
       NSString *tableName,
       NSString *comment)

if you want to set the table for the main bundle (that is, the core
App), or set the table string in

    NSString *NSLocalizedStringFromTableInBundle(NSString *key,
       NSString *tableName,
       NSBundle *bundle,
       NSString *comment)

for a plugin.

As has previously been stated. There should be no need to create an
English string in the .strings file, as by default the
`NSLocalizedString…` methods return the input string if nothing is find.
Secondly, we use `genstrings` to do all the heavy lifting for us anyway.

### Genstrings

This will be implemented as a build phase in the Quicksilver project. It
will output all the required .strings files ready for submission to
Transifex.

Right now, you can generate for strings using the `genstrings` tool in
Tools, or directly using `stringstool` and `ibtool`.

1. To generate strings for an .m file, and add it to an existing file:
`Quicksilver/Tools/stringstool --output-directory Quicksilver/Localized/en.lproj extract-mfiles Quicksilver/Code-App/QSUpdateController.m`

2. To generate strings for all xibs:

`find . ! -path '*/Code-External/*' ! -path '*/PlugIns-Main/*' -name "*.xib" -exec ./Tools/stringstool --output-directory Localized/en.lproj extract-interface-builder {} \;`

### Pushing and Pulling from Transifex

Updated source .stings files are automatically pushed to Transifex, and
updated translations are automatically pulled from Transifex. The file
in `.tx/config.yml` defines which strings files get pushed and pulled.
Update that file to add new strings files.

**Adding New Translation Files to Xcode**

If a new language gets added in Transifex, new .strings files in the
relevant <lang>.lproj folder will get added to the git repository.
Xcode, however, won't know about these files until you add them to the
Xcode project.

When new .strings files are added to the repository, open up Xcode and
'tick' the corresponding language in Xcode. Xcode will ask you if you
want to use the existing file, choose 'yes'.

### Fixing Transifex Parser Quirks

Transifex has issues with the '↩' character ([see
here](https://community.transifex.com/t/special-character-conflict-with-transifex-keyboards/96/6)).
Ever time a file is translated, it converts the '↩' character to \r. The
fix for this is manual, and involves running a search/replace:

    cd Quicksilver
    find . -name *.strings -exec perl -pi -e "s/\(\\\r\)/\(↩\)/g" {} \;
    find . -name *.strings -exec perl -pi -e "s/\(⌘\\\r\)/\(⌘↩\)/g" {} \;
    find . -name *.strings -exec git add {} \;
    git commit -m "Update strings files (change \r to ↩)"

### Dealing with difficult files

Quicksilver uses many different plist formats for getting information.
One example is DefaultsMap.plist. For these 'awkward' files, **always**
do a diff between the English and localised files, to make sure strings
that shouldn't be translated have been left. An example of strings that
should be left as they are in DefaultsMap.plist are those referring to a
User Default key of some sort.