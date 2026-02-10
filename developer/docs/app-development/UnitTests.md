Right now there aren't many unit tests in the Quicksilver code base. But
with [pull request
\#713](https://github.com/quicksilver/Quicksilver/pull/713), we added
unit testing capabilities to the Quicksilver XCode project.

So, if you work on something that can be tested, please add some tests
for it. Remember: Any tests are better than no tests.

## Adding Tests

The test classes should go in the corresponding group in XCode and the
correct folder on disk, to keep them separate from the actual
applications files. For example for tests of the *QSCore.framework*
should go in Tests/QSCoreTests group and in the folder
Tests/Tests-QSCore/.

They also need to be added to the correct test target. Currently, there
are five different test targets: One for each of the four Quicksilver
frameworks (*QSCoreTests*, *QSEffectsTests*, *QSFoundationTests*, and
*QSInterfaceTests*). Put any tests directly related to each framework
here. And one test target called *QuicksilverTests*. Put all other tests
here. And don't add your test files to any of the normal
(non-test-)targets.

For each test target there currently is a dummy test file. That needs to
be there, because the target will fail if there are no test files. Once
there are any real tests for a test target, the dummy test file can be
removed.

## Running Tests

To run the tests, just choose the target that contains your tests, and
build it (with XCode 3) or (with Xcode 4) choose Test, not Build.

There is also a target called "Run All Tests", which doesn't contain any
tests itself, but instead runs each of the five test targets on turn.