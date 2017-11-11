# Development

## Automator

Install the Automator Module plugin. It adds the **Execute Workflow** action, to use it, navigate to a saved Automator .workflow file and the **Execute Workflow** action should be the default.

## Services

The Services Menu Module plugin makes all your Services available in Quicksilver as actions. Services are in the application’s menu and many are only enabled when you have selected text. Depending on the applications you use, some services can be really useful as actions. E.g., if you use Sticky Notes then you’ll love the **Make New Sticky Note** action.

## Terminal

For this section you’ll need the Terminal Module plugin installed. There’s a Command Line Interface Handler that should be set to Terminal. The plugin creates two catalog sources under Modules. Terminal Files looks in `~/Library/Application Support/Terminal/` for any .term (containing Terminal settings) or .command files (containing Terminal commands). Bash Command History parses the `~/.bash_history` file making each line available as an object in the catalog. Note that bash keeps duplicate lines in the history and they appear in Quicksilver’s list as well.

The **Run […]** action will run a command or shell script selected in the first pane with optional arguments entered in text-mode in the third pane. The result of the command (i.e., stdout) is displayed in a new command window. The **Run in Terminal […]** is similar but opens a new window in Terminal to run the command and display the results.

As an aside, Applescripts can be run by choosing the script in the first pane, using the **Process Text…** action and entering text in the third pane.  This can be thought of as a reverse action for any script actions added to the `~/Library/Application Support/Quicksilver/Actions/` folder (see Extending Quicksilver).

If you want to type a command directly into Quicksilver and run it you can use the **Run Command in Shell** action or the **Run a Text command in Terminal** action. The first runs the command in a shell from Quicksilver and displays the result in a new Quicksilver command window, the second does so in a new Terminal window. You can also use these actions with a command from the Bash Command History catalog source. If you look through your history often you might want a trigger for Bash Command History (Catalog) (**Show Contents**). These commands can be handy when the Dock gets confused. E.g., you can do `killall Dock` with the **Run Command in Shell** action to kill the Dock and have it automatically restarted.

The **Go To Directory in Terminal** action will open a Terminal window with the current working directory set to the directory specified in the first pane. You can use text mode to type the name of any directory, e.g., `/System/Library/Fonts`, though if you use `~` the **Go To Directory in Terminal** action doesn’t appear. You can also navigate to a folder in Quicksilver and use the action. If the folder is in the Catalog it should be easy to bring up quickly. If you have a project with a lot of directories you can add them to the catalog. To keep the number of items small you might want to specify just folders and no the files (e.g., this might be useful with a large software project) by putting `‘fold’` in the Types box in the Source Options for the catalog source.

The **Show Man Page** action will show the man page of a command in a Terminal window. You don’t enter the desired man page in text-mode or navigate inside `/usr/share/man/` to a page. Instead it only works on commands (without an extension) which are in the catalog. To set this up open the catalog and select Custom. In the + menu choose a new File & Folder Scanner and select `/usr/bin/` as the directory. A depth of 1 is fine. Now all those command line utilities are directly accessible from Quicksilver and the **Show Man Page** action will work with them.

An alternative is to make use of the url scheme `x-man-path`. Opening an URL such as `x-man-page://units` will show the man page in a terminal window. It can also show different sections using this form: `x-man-page://3/printf`. You can create a web-search for `x-man-page://***` to make this more convenient.

A common issue seems to be that Terminal automatically runs the same command at startup. This a Terminal configuration issue not a Quicksilver one. It happens if you invoke Terminal for a specific command and then open the Window Settings… panel and click Use Settings As Defaults. The command used to invoke Terminal gets saved in `~/Library/Preferences/com.apple.Terminal.plist`. To remove it, run this command: `defaults write com.apple.Terminal ExecutionString`. If you can’t access Terminal try another program like iTerm or running it from Quicksilver with **Run Command in Shell**, or edit the plist file directly.

If you prefer iTerm to Terminal, install the iTerm Module plugin and set the Command Line Interface handler to iTerm. The **Run […]** and **Run Command in Shell** actions don’t change, they still run the commands in Quicksilver. By changing the handler the *Run in Terminal […]*, **Run a Text command in Terminal**, and **Go To Directory in Terminal** actions change to use iTerm. There are also three new explicit actions called **Run in iTerm […]**, **Run a Text Command in iTerm**, and **Go To Directory in iTerm**. So if you even if you have the handler set to one, you can run commands using the other easily.

The **Show Man Page** action is a little different. Setting the handler doesn’t specify which terminal program is used. Instead both the Terminal and iTerm modules define their own versions of this action. Since the name of the terminal used isn’t in the name you have to tell them apart from their icons. If you prefer one to the other but still have both plugins installed, just drag and trop the actions in the actions preferences so that your preferred one has priority. There’s also a small difference between the two versions of this action. The Terminal one exits the terminal when you quit viewing the man page, the iTerm one does not.

## CLIX

If you use [CLIX](http://rixstep.com/4/0/clix/index.shtml) from Rixstep to perform command line operations, you’ll want the Quicksilver CLIX Module plugin. It lets you configure a custom catalog source for a .clix file and converts all the commands inside it into text objects that you can run using **Run Command in Shell** or **Run a Text Command in Terminal** actions. To configure it, open the Catalog and choose the Custom set. Click on the + button at the bottom to add a new custom source. Choose File & Folder Scanner from the pop-up menu. Enter the path to the .clix file, you must have a separate source for each .clix file. The trick to make this work is to go to the Source Options tab and for Include Contents choose QSCLiXPlugin. At the bottom you probably want to check Omit source item. Rescan the source and you should see the CLIX commands in the Catalog. Activate Quicksilver, select one of the commands and choose one of the available **Run** actions such as **Run Command in Shell**.

## Command Line Tool

If you use the command line you may find that you’ll want it to be able to interact with Quicksilver. Install the Command Line Tool plugin and a Quicksilver preference pane is installed under General called Command Line Tool. It contains an install button to install a `qs` program in `/usr/bin/`. 

Invoke `qs` with one or more files as arguments and Quicksilver will be activated with those files selected in the object pane. With an argument of `-` it will read from stdin though piping in filenames results in the file names being in the object pane as text, which is not the the same as having the files selected. If you use the `-s` or `--shelf` option the files or text will be put on the shelf.

If you are an Emacs user, here’s an Emacs command to pass the current file (of a buffer, in dired, or buffer-menu mode) to Quicksilver using ```qs`. You could bind it to “C-c q” using something like: `(global-set-key "\C-cq" 'buffer-file-to-quicksilver)`

```emacs-lisp
(defun buffer-file-to-quicksilver ()
  "Opens the current file in Quicksilver"
  (interactive)
  (cond ((and buffer-file-name (file-exists-p buffer-file-name))
         (call-process-shell-command (concat "qs \"" buffer-file-name "\"")))
        ;; dired handling
        ((eq major-mode 'dired-mode)
         (dired-do-shell-command "qs * "
                                 current-prefix-arg
                                 (dired-get-marked-files t current-prefix-arg)))
        ;; buffer-menu mode
        ((and (eq major-mode 'Buffer-menu-mode)
              (file-exists-p (buffer-file-name (Buffer-menu-buffer nil))))
         (call-process-shell-command
          (concat "qs \"" (buffer-file-name (Buffer-menu-buffer nil)) "\"")))
        (t
         (error "Not visiting a file or file doesn't exist"))))
```

Here’s another function.  It will send the contents of the Emacs region to Quicksilver as text. With the text in the first pane you can do whatever Quicksilver can do with it, e.g., the **Find With…** action or the **Email to…** actions. I bind it to “C-c w” using: `(global-set-key "\C-cw" 'region-to-quicksilver)`

```emacs-lisp
(defun region-to-quicksilver (start end)
  "Opens the contents of the region in Quicksilver as text."
  (interactive "r")
  (call-process-region start end "qs" nil 0 nil "-"))
``` 

## Developer Documentation

If you’ve installed the OS X Developer Tools then you probably want to install Quicksilver’s Developer Module plugin. This adds to the catalog under Modules, Developer:

- applications under `/Developer/Applications`
- documents under `/Developer/ADC Reference Library/documentation/`
- frameworks under `/System/Library/Frameworks and /System/Library/PrivateFrameworks`
- headers for AppKit, Foundation and CoreFoundation frameworks.

## Subversion

The Subversion Module plugin adds the following actions. For all of them you give the directory or file you want to work on as the object in the first pane. You can use the comma trick to have one command operate on multiple files. If you add your project to the catalog, it will make it easier to bring up the files to operate on. Those that take an argument in the third pane are noted.

- **SVN Add All Directory Contents**
- **SVN Add Item**
- **SVN Check Out To Directory** - enter the subversion URL in the third pane
- **SVN Commit** - enter comment for log in the third pane
- **SVN Delete Item**
- **SVN Log**
- **SVN Status**
- **SVN Update**

The **SVN Add All Directory Contents** action takes a directory as the object and adds all the files and directories in the directory to the subversion repository. It can take a while to run but progress displays in the Quicksilver Task Viewer.

The subversion plugin calls the `svn` command to perform the actions, so obviously you must have subversion installed on the system. The plugin expects the `svn` command to be in `/usr/local/bin/svn` if it’s some place else you can run the following command in a terminal shell to tell Quicksilver where to find it, just replace path with the full path of the svn command:

    defaults write com.blacktree.Quicksilver QSSVNPluginSVNPATH path

By default you will not be shown a list of changed files on commit. If you would like to see such a list use the following command in a terminal shell:

    defaults write com.blacktree.Quicksilver QSSVNShowChangedFiles 1

Change the 1 to a 0 to revert back to the default behavior. To always show a text window with the results of the command issue the following command in a terminal shell (change the 1 to 0 to resume the default behavior).

    defaults write com.blacktree.Quicksilver QSSVNAllWaysShowTextWindow 1

## Eclipse

The beta Eclipse plugin indexes workspaces and logs into the catalog. Use the **Open** action with them. Note, installing this plugin causes a very slow search of the user’s entire directory looking for Eclipse workspaces. See documentation at: http://code.google.com/p/qseclipse/w/list

## Remote Desktop
