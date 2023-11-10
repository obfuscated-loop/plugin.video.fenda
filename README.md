# Fenda
Fenda is a WIP (work-in-progress) fork of the Fen addon for Kodi, this was created after [Tikipeter announced that Fen will no longer receive development updates](https://github.com/Tikipeter/repository.tikipeter/issues/331).

## About
So far, there are no *major* new features - I have rebranded and formatted the existing code. I will be applying updates to the codebase as I see fit.

**Additions:**
- Ability to disable 'Next Episode' window and just automatically skip at whatever playback percentage trigger you have applied (no getting out of bed to click play for the next episode). This setting is called `Disable action window` (inside of Fenda settings) and you must have `Auto Play` and `Autoplay Next Episode` enabled. The default playback percentage trigger has also been upped to `97%`.
- SQLite executions are going through a speed-up, which should help the addon as a whole; see *[#4](https://github.com/obfuscated-loop/plugin.video.fenda/issues/4)*.
- API requests should be faster as they now use `requests.Session()` rather than making individual sessions per request.

**Plans:**
- The codebase is in desperate need of a refactor, I thought a quick formatting would help - and it did a bit but not by much; I will most likely start work on this once I wrap my head around everything else here.
- Fenda assets need to be created - would appreciate some help with these as I can't use GIMP for the life of me.
- More useful features and suggestions from community etc..


## Installing
#### 1) Adding the source
- Enable `Unknown sources` inside of `Settings > System > Add-ons`
- Open `Settings > File manager` and select `Add source`
- Select `<None>` and add the URL: **`https://fenda.live/`**
- Enter a name for the media source; I.E `Fenda Archive`

#### 2) Installing the plugin from zip file
- Goto `Settings > Add-ons > Install from zip file`
- Select the Fenda source you just added; I.E `Fenda Archive`
- Select `zips/plugin.video.fenda/plugin.video.fenda-1.0.0.zip`

*A repository addon will be created soon...*

### 

## Contributing
I will be accepting PRs and will strongly consider suggestions if they are to come my way, so feel free to open Issues/PRs (no stupid ones please).
