## List of Notifications

This is a list of all the NSNotifications used in the Quicksilver code
(as of 2012-01-17). It's kind of sorted by the name of the notification,
lists all files that send out a notification (*Posters*) and all files
that listen to that notification (*Observers*) as well as which method
will be called on the observing class (@selector).

-   **@"CatalogCacheChanged"**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSCatalogPrefPane.m --
            @selector(catalogCacheChanged:) on class: self
-   **@"CatalogEntryChanged"**
    -   *Posters*:
        -   PlugIns-Main/QSCorePlugIn/Code/QSDefaultsObjectSource.m
    -   *Observers*:
        -   No observers
-   **@"InterfaceActivated"**
    -   *Posters*:
        -   Code-QuickStepInterface/QSInterfaceController.m
        -   Code-QuickStepInterface/QSInterfaceController.m
    -   *Observers*:
        -   No observers
-   **@"InterfaceDeactivated"**
    -   *Posters*:
        -   Code-QuickStepInterface/QSInterfaceController.m
    -   *Observers*:
        -   No observers
-   **@"NSWindowDidResignKeyNotification"**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepInterface/QSSearchObjectView.m --
            @selector(hideResultView:) on class: self
-   **@"ObjectModified"**
    -   *Posters*:
        -   Code-QuickStepCore/QSObject_FileHandling.m
        -   Code-QuickStepCore/QSProcessMonitor.m
        -   Code-QuickStepCore/QSProcessMonitor.m
    -   *Observers*:
        -   Code-QuickStepInterface/QSInterfaceController.m --
            @selector(objectModified:) on class: self
-   **@"QSApplicationDidFinishLaunchingNotification"**
    -   *Posters*:
        -   Code-App/QSApp.m
    -   *Observers*:
        -   QSPasteboardController (the Clipboard plug-in)
        -   QSShelfController (the Shelf plug-in)
-   **@"QSApplicationWillRelaunch"**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSUpdateController.m --
            @selector(applicationWasMoved:) on class: self
-   **@"QSEventNotification"**
    -   *Posters*:
        -   Code-App/QSController.m
        -   Code-App/QSController.m
        -   Code-App/QSController.m
        -   Code-QuickStepCore/QSProcessMonitor.m
        -   iTunes Module → Code/QSiTunesSource.m
    -   *Observers*:
        -   No observers (used for Event Triggers)
-   **@"QSPlugInUpdatesFinished"**
    -   *Posters*:
        -   Code-QuickStepCore/QSPlugInManager.m
    -   *Observers*:
        -   Code-App/QSSetupAssistant.m --
            @selector(installStatusChanged:) on class: self
-   **@"QSSourceArrayCreated"**
    -   *Posters*:
        -   QSSpotlightPlugIn_Action (the Spotlight plug-in)
    -   *Observers*:
        -   Code-QuickStepInterface/QSInterfaceController.m --
            @selector(sourceArrayCreated:) on class: self
-   **@"QSSourceArrayUpdated"**
    -   *Posters*:
        -   QSSpotlightPlugIn_Action (the Spotlight plug-in)
    -   *Observers*:
        -   Code-QuickStepInterface/QSInterfaceController.m --
            @selector(sourceArrayChanged:) on class: self
-   **@"QSUpdateControllerStatusChanged"**
    -   *Posters*:
        -   Code-QuickStepCore/QSPlugInManager.m
        -   Code-QuickStepCore/QSPlugInManager.m
    -   *Observers*:
        -   Code-App/QSPlugInsPrefPane.m --
            @selector(installStatusChanged:) on class: self
-   **@"SearchObjectChanged"**
    -   *Posters*:
        -   Code-QuickStepInterface/QSSearchObjectView.m
        -   Code-QuickStepInterface/QSSearchObjectView.m
    -   *Observers*:
        -   Code-QuickStepInterface/QSInterfaceController.m --
            @selector(searchObjectChanged:) on class: self
-   **@"WindowsShouldHide"**
    -   *Posters*:
        -   Code-App/QSController.m
        -   Code-App/QSController.m
        -   Code-App/QSController.m
        -   PlugIns-Main/QSCorePlugIn/Code/QSActionProvider_EmbeddedProviders.m
    -   *Observers*:
        -   No observers
-   **@"com.apple.HIToolbox.beginMenuTrackingNotification"**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepInterface/QSDockingWindow.m -- @selector(lock)
            on class: self
-   **@"com.apple.HIToolbox.endMenuTrackingNotification"**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepInterface/QSDockingWindow.m --
            @selector(unlock) on class: self
-   **@"processesChanged"**
    -   *Posters*:
        -   Code-QuickStepCore/QSProcessMonitor.m
        -   Code-QuickStepCore/QSProcessMonitor.m
        -   Code-QuickStepCore/QSProcessMonitor.m
    -   *Observers*:
        -   No observers
-   **NSApplicationDidFinishLaunchingNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepCore/QSLibrarian.m --
            @selector(scanInvalidIndexes) on class: self
-   **NSApplicationWillResignActiveNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepInterface/QSHotKeyEditor.m --
            @selector(cancel) on class: self
-   **NSBundleDidLoadNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepCore/QSRegistry.m -- @selector(bundleDidLoad:)
            on class: self
-   **NSOutlin**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSTriggersPrefPane.m -- @selector(selectTrigger:)
            on class: self
-   **NSOutlineViewSelectionDidChangeNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSCatalogPrefPane.m --
            @selector(updateEntrySelection) on class: self
-   **NSSplitViewDidResizeSubviewsNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSPreferencesController.m --
            @selector(splitViewDidResizeSubviews:) on class: self
-   **NSSystemColorsDidChangeNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepInterface/QSObjectView.m --
            @selector(setNeedsDisplay:) on class: self
-   **NSTableViewColumnDidResizeNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSAdvancedPrefPane.m -- @selector(columnResized:)
            on class: self
-   **NSTableViewSelectionDidChangeNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSPreferencesController.m --
            @selector(selectModule:) on class: self
-   **NSViewBoundsDidChangeNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepInterface/QSResultController.m --
            @selector(viewChanged:) on class: self
        -   Code-QuickStepInterface/QSResultController.m --
            @selector(childViewChanged:) on class: self
-   **NSWindowDidBecomeKeyNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepInterface/QSFancyTableView.m --
            @selector(_windowDidChangeKeyNotification:) on class: self
        -   Code-QuickStepInterface/QSFancyTableView.m --
            @selector(_windowDidChangeKeyNotification:) on class: self
        -   Code-QuickStepInterface/QSInterfaceController.m --
            @selector(windowDidBecomeKey:) on class: self
-   **NSWindowDidResignKeyNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepInterface/QSFancyTableView.m --
            @selector(_windowDidChangeKeyNotification:) on class: self
        -   Code-QuickStepInterface/QSFancyTableView.m --
            @selector(_windowDidChangeKeyNotification:) on class: self
        -   Code-QuickStepInterface/QSHotKeyEditor.m --
            @selector(cancel) on class: self
        -   Code-QuickStepInterface/QSInterfaceController.m --
            @selector(windowDidResignKey:) on class: self
-   **NSWorkspaceDidLaunchApplicationNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSController.m -- @selector(appLaunched:) on class:
            self
        -   Code-QuickStepCore/QSProcessMonitor.m --
            @selector(appLaunched:) on class: self
        -   Code-QuickStepCore/QSProcessSource.m --
            @selector(appLaunched:) on class: self
-   **NSWorkspaceDidMountNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   PlugIns-Main/QSCorePlugIn/Code/QSVolumesObjectSource.m --
            @selector(invalidateSelf) on class: self
-   **NSWorkspaceDidTerminateApplicationNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-QuickStepCore/QSProcessMonitor.m --
            @selector(appTerminated:) on class: self
        -   Code-QuickStepCore/QSProcessSource.m --
            @selector(appTerminated:) on class: self
-   **NSWorkspaceDidUnmountNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   PlugIns-Main/QSCorePlugIn/Code/QSVolumesObjectSource.m --
            @selector(invalidateSelf) on class: self
-   **NSWorkspaceWillLaunchApplicationNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSController.m -- @selector(appWillLaunch:) on
            class: self
-   **QSActiveApplicationChanged**
    -   *Posters*:
        -   Code-QuickStepCore/QSProcessMonitor.m
        -   Code-QuickStepCore/QSProcessMonitor.m
    -   *Observers*:
        -   Code-App/QSController.m -- @selector(appChanged:) on class:
            self
        -   Code-QuickStepCore/QSProcessMonitor.m --
            @selector(appChanged:) on class: self
        -   Code-QuickStepInterface/QSDockingWindow.m --
            @selector(hideOrOrderOut:) on class: self
        -   Code-QuickStepInterface/QSInterfaceController.m --
            @selector(appChanged:) on class: self
-   **QSApplicationWillRelaunchNotification**
    -   *Posters*:
        -   Code-QuickStepFoundation/NSApplication_BLTRExtensions.m
    -   *Observers*:
        -   Code-App/QSPreferencesController.m --
            @selector(applicationWillRelaunch:) on class: self
-   **QSCatalogEntryChanged**
    -   *Posters*:
        -   Code-App/QSCatalogPrefPane.m
        -   Code-App/QSCatalogPrefPane.m
        -   PlugIns-Main/QSCorePlugIn/Code/QSFileSystemObjectSource.m
        -   PlugIns-Main/QSCorePlugIn/Code/QSFileSystemObjectSource.m
    -   *Observers*:
        -   Code-App/QSCatalogPrefPane.m -- @selector(catalogChanged:)
            on class: self
        -   Code-QuickStepCore/QSExecutor.m -- @selector(writeCatalog:)
            on class: self
        -   Code-QuickStepCore/QSLibrarian.m -- @selector(writeCatalog:)
            on class: self
-   **QSCatalogEntryIndexed**
    -   *Posters*:
        -   Code-QuickStepCore/QSCatalogEntry.m
        -   Code-QuickStepCore/QSCatalogEntry.m
        -   Code-QuickStepCore/QSLibrarian.m
    -   *Observers*:
        -   Code-App/QSCatalogPrefPane.m -- @selector(catalogIndexed:)
            on class: self
        -   Code-QuickStepCore/QSLibrarian.m -- @selector(reloadSets:)
            on class: self
-   **QSCatalogEntryIsIndexing**
    -   *Posters*:
        -   Code-QuickStepCore/QSCatalogEntry.m
    -   *Observers*:
        -   Code-App/QSSetupAssistant.m -- @selector(catalogIndexed:) on
            class: self
-   **QSCatalogIndexed**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   Code-App/QSSetupAssistant.m -- @selector(catalogIndexed:) on
            class: self
-   **QSCatalogIndexingCompleted**
    -   *Posters*:
        -   Code-QuickStepCore/QSLibrarian.m
    -   *Observers*:
        -   Code-App/QSSetupAssistant.m --
            @selector(catalogIndexingFinished:) on class: self
-   **QSCatalogSourceInvalidated**
    -   *Posters*:
        -   Code-QuickStepCore/QSObjectSource.m
    -   *Observers*:
        -   Code-QuickStepCore/QSLibrarian.m -- @selector(reloadSource:)
            on class: self
-   **QSCatalogStructureChanged**
    -   *Posters*:
        -   Code-App/QSCatalogPrefPane.m
        -   Code-App/QSCatalogPrefPane.m
        -   Code-App/QSCatalogPrefPane.m
        -   Code-App/QSTriggersPrefPane.m
        -   Code-QuickStepCore/QSLibrarian.m
    -   *Observers*:
        -   Code-QuickStepCore/QSLibrarian.m -- @selector(writeCatalog:)
            on class: self
        -   Code-QuickStepCore/QSLibrarian.m --
            @selector(reloadIDDictionary:) on class: self
        -   PlugIns-Main/QSCorePlugIn/Code/QSCatalogEntrySource.m --
            @selector(invalidateSelf) on class: self
-   **QSIconLoaderDelegateCanceled**
    -   *Posters*:
        -   Code-QuickStepCore/QSIconLoader.m
    -   *Observers*:
        -   Code-QuickStepCore/QSIconLoader.m --
            @selector(cancelLoading:) on class: self
-   **QSInterfaceChangedNotification**
    -   *Posters*:
        -   Code-App/QSController.m
        -   Code-App/QSMainPreferencePanes.m
    -   *Observers*:
        -   Code-QuickStepCore/QSObject.m -- @selector(interfaceChanged)
            on class: self
-   **QSPlugInInfoFailedNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSPlugInManager.m
    -   *Observers*:
        -   Code-App/QSSetupAssistant.m -- @selector(plugInInfoFailed)
            on class: self
-   **QSPlugInInfoLoadedNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSPlugInManager.m
    -   *Observers*:
        -   Code-App/QSPlugInsPrefPane.m --
            @selector(reloadPlugInsList:) on class: self
        -   Code-App/QSSetupAssistant.m -- @selector(plugInInfoLoaded)
            on class: self
-   **QSPlugInInstalledNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSPlugInManager.m
        -   Code-QuickStepCore/QSRegistry.m
    -   *Observers*:
        -   Code-App/QSPlugInsPrefPane.m --
            @selector(reloadPlugInsList:) on class: self
        -   Code-QuickStepCore/QSPlugInManager.m --
            @selector(plugInDidInstall:) on class: self
-   **QSPlugInLoadedNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSPlugIn.m
    -   *Observers*:
        -   Code-App/QSHelpersPrefPane.m --
            @selector(reloadHelpersList:) on class: self
        -   Code-App/QSMainPreferencePanes.m --
            @selector(updateInterfacePopUp) on class: self
        -   Code-App/QSPlugInsPrefPane.m --
            @selector(reloadPlugInsList:) on class: self
        -   Code-App/QSPreferencesController.m --
            @selector(reloadPlugInInfo:) on class: self
        -   Code-App/QSTriggersPrefPane.m -- @selector(populateTypeMenu)
            on class: self
        -   Code-QuickStepCore/QSPlugInManager.m --
            @selector(plugInDidLoad:) on class: self
-   **QSReleaseAllCachesNotification**
    -   *Posters*:
        -   Code-App/QSController.m
        -   Code-App/QSMainPreferencePanes.m
    -   *Observers*:
        -   Code-QuickStepCore/QSObject.m --
            @selector(purgeAllImagesAndChildren) on class: self
-   **QSReleaseAllNotification**
    -   *Posters*:
        -   Code-App/QSController.m
    -   *Observers*:
        -   Code-QuickStepInterface/QSSearchObjectView.m --
            @selector(clearAll) on class: self
-   **QSReleaseOldCachesNotification**
    -   *Posters*:
        -   Code-QuickStepInterface/QSInterfaceController.m
    -   *Observers*:
        -   Code-QuickStepCore/QSObject.m --
            @selector(purgeOldImagesAndChildren) on class: self
        -   Code-QuickStepCore/QSObject.m --
            @selector(cleanObjectDictionary) on class: self
-   **QSTaskAddedNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSTaskController.m
    -   *Observers*:
        -   Code-App/QSTaskViewer.m -- @selector(taskAdded:) on class:
            self
        -   Code-App/QSTaskViewer.m -- @selector(refreshAllTasks:) on
            class: self
-   **QSTaskChangedNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSTaskController.m
    -   *Observers*:
        -   Code-App/QSTaskViewer.m -- @selector(refreshAllTasks:) on
            class: self
-   **QSTaskRemovedNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSTaskController.m
    -   *Observers*:
        -   Code-App/QSTaskViewer.m -- @selector(refreshAllTasks:) on
            class: self
-   **QSTasksEndedNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSTaskController.m
    -   *Observers*:
        -   Code-App/QSTaskViewer.m -- @selector(tasksEnded:) on class:
            self
        -   Code-QuickStepInterface/QSInterfaceController.m --
            @selector(stopAnimation:) on class: progressIndicator
-   **QSTasksStartedNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSTaskController.m
    -   *Observers*:
        -   Code-QuickStepInterface/QSInterfaceController.m --
            @selector(startAnimation:) on class: progressIndicator
-   **QSTriggerChangedNotification**
    -   *Posters*:
        -   Code-QuickStepCore/QSTrigger.m
        -   Code-QuickStepCore/QSTriggerCenter.m
        -   Code-QuickStepCore/QSTriggerCenter.m
        -   Code-QuickStepCore/QSTriggerCenter.m
    -   *Observers*:
        -   Code-App/QSTriggersPrefPane.m -- @selector(triggerChanged:)
            on class: self
-   **UKKQueueFileWrittenToNotification**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   PlugIns-Main/QSCorePlugIn/Code/QSFileSystemObjectSource.m --
            @selector(invalidateIndex:) on class: entry
-   **nil**
    -   *Posters*:
        -   No posters
    -   *Observers*:
        -   PlugIns-Main/QSCorePlugIn/Code/QSDefaultsObjectSource.m --
            @selector(invalidateIndex:) on class: entry
        -   PlugIns-Main/QSCorePlugIn/Code/QSFileSystemObjectSource.m --
            @selector(invalidateIndex:) on class: entry
-   **nm**
    -   *Posters*:
        -   Code-QuickStepCore/QSVoyeur.m
    -   *Observers*:
        -   No observers
-   **QSiTunesTrackChangeNotification**
    -   *Posters*:
        -   iTunes Module → Code/QSiTunesSource.m
    -   *Observers*:
        -   No observers