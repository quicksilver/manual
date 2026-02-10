# Plugin Release Process

Plugins are released by CD when pushing tags to the github repo in question. Here's an [example](https://github.com/quicksilver/com.apple.AddressBook-qsplugin/releases/tag/v2.3.1) of one tag with a changelog.


## Release steps 

Follow these steps to release your plugin:

* Build your plugin, documentation and bump the version and build numbers
* Create a tag named the version number in question. The git tag message can contain markdown for the changelog. E.g.
```
git tag -a v2.1.3 -m "Version 2.1.3

* New feature
* Fix bug [123](https://example.com/123)"
```
* Push the main and tag to origin:
```
git push origin main
git push origin v2.1.3
```


## Other times to make a release

-   When [updating QSRequirements](../plugin-development/reference/requirements.md) because a plugin is seen to break with a new QS or macOS version, or QS drops/adds support for a given release.