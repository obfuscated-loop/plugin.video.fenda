# Fenda
Fenda is a WIP (work-in-progress) fork of the Fen addon for Kodi, this was created after [Tikipeter announced that Fen will no longer receive development updates](https://github.com/Tikipeter/repository.tikipeter/issues/331).

## About
So far, there are no *major* new features - I have rebranded and formatted the existing code. I will be applying updates to the codebase as I see fit.

**Additions:**
- Ability to disable 'Next Episode' window and just automatically skip at whatever playback percentage trigger you have applied (no getting out of bed to click play for the next episode). This setting is called `Disable action window` and you must have `Auto Play` and `Autoplay Next Episode` enabled. The default playback percentage trigger has also been upped to `97%`.
- RealDebrid requests should be faster as they now use `requests.Session()` rather than making individual sessions per request.

**Plans:**
- The codebase is in desperate need of a refactor, which I will most likely start work on once I wrap my head around everything here.
- Fenda assets need to be created - would appreciate some help with these as I can't use GIMP for the life of me.
- More useful features and suggestions from community etc..

**I also haven't set up a repo yet, though I plan on doing so very soon.**

## Installing
As there isn't a repo set-up at the moment, you can install the addon via zip - [just download the addon as a zip](https://github.com/obfuscated-loop/plugin.video.fenda/archive/refs/heads/main.zip) and *[Install from zip file](https://kodi.wiki/view/Archive:Install_add-ons_from_zip_files)* within Kodi.

## Contributing
I will be accepting PRs and will strongly consider suggestions if they are to come my way, so feel free to open Issues/PRs (no stupid ones please).