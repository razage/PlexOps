# PlexOps
PlexOps is a simple collection of renaming and moving functions to simplify moving media to a Plex server. Currently I have only tested it with anime naming schemes, but you should be able to use whatever regex you want.

## Use
The simplest way to use PlexOps is to double click run_plexops.py Should you not want to do both operations, simple instantiate PlexOps and run the PlexOps.renamer.rename or PlexOps.uploader.uploadfiles

### Configuration
PlexOps expects a settings.json file to be present in its directory. It will stop if this file is not present. The following settings are required:
* operation_location: This is the directory that PlexOps will look at. This should be an escaped path (Ex: C:\\ for C drive)
* server_location: This is the directory that files are uploaded to. It should be the root of whatever library you want to upload to and escaped (Ex: Z:\\Movies\\)
* name_regex: This is a regular expression for extracting the series name from a file that hasn't been renamed yet.
* epsiode_regex: This is a regular expression for extracting the episode number from a file that hasn't been renamed yet.
* plexname_regex: This is a regular expression for extracting the series name from a file that has been renamed.
* plexseason_regex: This is a regular expression for extracting the season number from a file that has been renamed.
* plexep_regex: This is a regular expression for extracting the episode number from a file that has been renamed.
* show_settings {}: This is a collection of various shows and their settings. This is how the renamer and uploader know what to do with a given show.

#### Show Configuration
Each item in the show_settings collection should use its title as the key. This title should be what appears on the file when you download it. Several settings are available, but none of them are mandatory; if you don't need to use a setting, simply don't include it. If a show doesn't need to be altered in any of these methods, don't include it in the list.
* altname: This is what you want the series to be called. For instance, if you downloaded a show and it was called "Show A" and you set its altname to "Show B", the renamer would rename the file "Show B"
* season: This is used to determine what season a given series is. The renamer assumes a series is season one of itself, so use this if you need it to be season 2 or greater.
* adjust: This is a number used to subtract from the file's episode number to get the actual episode number. For instance, HorribleSubs labels the current episode of "Fairy Tail S2" as episode 64. Using an adjust of 51 renames the episode number as 13 (64-51)

View the example.json to see how your settings.json should look. Included are the regular expressions I use for anime. 
