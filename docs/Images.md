# Images

## iPhoto

The iPhoto Module plugin adds two actions and enables you to <kbd>→</kbd> into iPhoto.app to see everything in iPhoto’s left pane: the library, rolls, folders, albums, smart albums and slideshows. The **Show Album** action will open the selected item in iPhoto. The **iPhoto Slideshow** action will use iPhoto to play the slideshow (as opposed to the Finder’s slideshow ability). If you use it on an album or other non-slideshow object, it will create a new slideshow but not save it. It’s the equivalent of using the Play button in iPhoto as opposed to the +Slideshow button. Both actions will start iPhoto if it’s not running, but note that you can navigate through your iPhoto collection without starting iPhoto. 

You can also use <kbd>→</kbd> to  navigate down to an individual image. You can use actions such as **Email to…** or **Set Desktop Picture** actions among others. Note that the **Set Comment…** action (from the File Attribute Action plugin) can be used to set the Spotlight comment of images, but this is different than the comment you can set for a image in iPhoto. 

There are also two proxy objects, Current iPhoto Selection and Selected iPhoto Album which are useful for creating triggers.

## Slideshow

For this section you’ll need the Slideshow Action plugin. It installs two different actions called **Slideshow** that make use of the new slideshow feature added to the Finder in 10.4. One takes an image file or folder as the object, the other works on iPhoto albums and photos (which you’ll need the iPhoto Module plugin to access). As in any Finder slideshow typing <kbd>⎋</kbd> will cancel the slideshow and moving the mouse will bring up some controls. Note this is different than the **iPhoto Slideshow** action which uses iPhoto slideshow capabilities (notably music and the now ubiquitous Ken Burns effect). 

## Desktop Picture Action

The Desktop Picture Action plugin adds a **Set Desktop Picture** action that can act on folders or individual image files (GIF, JPEG, PICT, PNG, or TIFF). For folders, the desktop picture will be chosen from images in that folder and rotated. The time interval for updating and whether the images will be chosen sequentially or randomly are taken from the last-used settings in the Desktop & Screen Saver Preference Pane. If you have multiple displays connected to the computer, the action takes an optional argument which lets you select a display from a list. By default, this action applies to the main display. 

I think it would be great if **Set Desktop Picture** could work on a URL to an image, but it can’t. But if it could, then I could have a trigger of Current Web Page proxy object, **Set Desktop Picture** when viewing a nice image. 

## Screen Capture

The Screen Capture Module plugin installs three Internal Commands that use Grab.app for screen captures. You’ll find them in the Catalog, under Quicksilver, under Internal Commands (make sure this source is enabled).  They are called Capture Screen, Capture Region, and Capture Window and you use them with the **Run** action. You could just use the standard macOS key bindings for these. <kbd>⇧</kbd><kbd>⌘</kbd><kbd>3</kbd> for Capture Screen, <kbd>⇧</kbd><kbd>⌘</kbd><kbd>4</kbd> for Capture Region and <kbd>⇧</kbd><kbd>⌘</kbd><kbd>4</kbd> followed by <kbd>space</kbd> for Capture Window. The one advantage to the Quicksilver commands is that after they run, a new command window appears with the newly generated image selected as the object, ready for you to rename it or move it or do whatever you want.

You could also get at these functions with the Services Module plugin which makes things in the application’s Services menu into actions. This creates the actions **Grab/Screen**, **Grab/Selection**, and **Grab/Timed Screen** which seem to work with any object. These also open a new command window but in B51 it doesn’t seem to work correctly. The object is listed as Unknown Clipboard Object and trying to **Paste** it didn’t work. 

## Image Manipulation

For this section you’ll need the Image Manipulation Actions plugin installed. It only adds two actions but if you work with images you’ll really enjoy them. Both work with an object that is an image file and create a new image in the same folder as the original. Note the new image does not include metadata information such as aperture and camera model of the original. Also both actions when finished open a new command window with the new image in the object pane ready to specify a new action, like **Open** to see the new image.

The first action **Save Image in Format…** changes the format of the image. You specify the desired format as an argument in the third pane via text mode. You can specify “jpg”, “png”, “gif” or “tiff”. Quicksilver is forgiving with these allowing you to say “jpeg” or “tif” as well. In addition you can give resolution levels as “low”, “med”, or “hi” and either “progressive” or “interlaced”. Not all of these work with all formats, you’ll have to experiment. So, for example, you can specify jpg high progressive, or png low, or tif. 

The second action **Scale Image…** changes the size of the image. You specify the scaling factor in the third pane via text mode. You can give a percentage of the original’s size (e.g., `50%` or `200%`) or dimensions in pixels for the new image as *width* x *height*. White space is optional as is either number (the other dimension will be computed maintaining the original’s aspect ratio). If you want to specify just the height, precede it with an x. E.g., `300 x 400`, `150, or x500`. You can also specify a new format for the image by ending the specifier with the word `as` and then using any argument valid for **Save Image in Format…**. E.g., `640x480 as jpg high progressive`. If you often convert images to  some standard size or format (like to post a blog or include in a manual), consider a trigger such as File Selection (**Scale Image…**) `400`.

This isn’t going to replace iPhoto or Photoshop but for some quick changes (e.g., when formatting screenshots for a User Manual) these actions work very well. They work even better when you realize the comma trick works and you can operate on more than on image at a time.

## Flickr Upload

Now that you have your images in the size and format you want, maybe you want to upload them to your flickr account. Install the Flickr Upload plugin to get the **Upload to flickr (with Tags)…** action. Select the image you want as the object. If you want you can tab to the third pane to enter flickr tags for the image in text mode. Type return to start the upload. Quicksilver will connect to your flickr account either making use of your browser’s cookies or opening the browser to the flickr login page. And yes, you can upload more than one file with just one command using the comma trick.
