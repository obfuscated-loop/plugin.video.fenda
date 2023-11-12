# Fenda

Fenda is a WIP (work-in-progress) fork of the Fen addon for Kodi, this was created after [Tikipeter announced that Fen will no longer receive development updates](https://github.com/Tikipeter/repository.tikipeter/issues/331).

🔴 *[fenda.live](https://fenda.live/), and this Github repository are [rolling-releases](https://en.wikipedia.org/wiki/Rolling_release), expect app-breaking bugs and instability.*

🔵 *It is the user's choice to install/update from zip file (for stability) or automatically via the Fenda Archive Kodi repository.*

## About
The aim of Fenda is to be a high-speed Kodi addon for most devices used in the scene. I have rebranded and formatted the existing code of Fen; starting a refactoring process as well as applying various fixes. I currently work on this in my freetime but have high aspirations for this project.

**Additions:**
- Ability to disable 'Next Episode' window and just automatically skip at whatever playback percentage trigger you have applied (no getting out of bed to click play for the next episode). This setting is called `Disable action window` (inside of Fenda settings) and you must have `Auto Play` and `Autoplay Next Episode` enabled. The default playback percentage trigger has also been upped to `97%`.
- SQLite executions have gone, and are going, through a speed-up. This should help the addon as a whole; see *[#4](https://github.com/obfuscated-loop/plugin.video.fenda/issues/4)*.
- API requests should be faster as they now use `requests.Session()` rather than making individual sessions per request.

**Plans:**
- Refactor the way pages/pagination is done for each module, hopefully for a speed-boost.
- Bugfixes and improvements to the DOM parsing used for modules. 
- Fenda assets need to be created - would appreciate some help with these as I can't use GIMP for the life of me.
- Existing assets to be converted to WebP.
- Add dynamic media options to the player - allowing for video+audio seamlessly.
- Suggestions from the community.

## Installing
#### 1) Adding the source
- Enable `Unknown sources` inside of `Settings > System > Add-ons`
- Open `Settings > File manager` and select `Add source`
- Select `<None>` and add the URL: **`https://fenda.live/`**
- Enter a name for the media source; I.E `Fenda Archive`

#### 2) Installing the plugin from zip file
- Goto `Settings > Add-ons > Install from zip file`
- Select the Fenda source you just added; I.E `Fenda Archive`
- Select `zips/plugin.video.fenda/plugin.video.fenda-1.x.x.zip`

### 

## Contributing
I will be accepting PRs and will strongly consider suggestions if they are to come my way, so feel free to open Issues/PRs (no stupid ones please).
 