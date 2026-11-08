[![Version](https://img.shields.io/github/v/tag/SiriosDev/TVLauncher?style=for-the-badge&label=version&sort=semver)][VERSION_URL]
[![Downloads](https://img.shields.io/github/downloads/SiriosDev/TVLauncher/total?style=for-the-badge)][DOWNLOAD_URL]

[VERSION_URL]: https://github.com/SiriosDev/TVLauncher/releases/latest
[DOWNLOAD_URL]: https://github.com/SiriosDev/TVLauncher/releases/

[![License](https://img.shields.io/github/license/SiriosDev/TVLauncher?style=for-the-badge)][LICENSE_URL]
[![Release](https://img.shields.io/github/actions/workflow/status/SiriosDev/TVLauncher/release.yml?style=for-the-badge&label=Release)][RELEASE_URL]
[![Desc](https://img.shields.io/github/actions/workflow/status/SiriosDev/TVLauncher/update-description.yml?style=for-the-badge&label=Desc)][DESC_URL]

[LICENSE_URL]: https://github.com/SiriosDev/TVLauncher/blob/main/LICENSE
[RELEASE_URL]: https://github.com/SiriosDev/TVLauncher/actions/workflows/release.yml
[DESC_URL]: https://github.com/SiriosDev/TVLauncher/actions/workflows/update-description.yml


# TVLauncher

A simple, minimalist launcher for LG webOS TVs.

TVLauncher is made for custom launchers that do not support system applications
or need a simple alternative way to organize them. It provides a direct,
minimal path to the built-in Live TV application.

## Installation

Download the latest `.ipk` package from the
[Releases](https://github.com/SiriosDev/TVLauncher/releases) page and install it
on your LG webOS TV using one of the methods below.

There is no setup, configuration, account, or additional dependency. Install it,
reorder it in you custom home, and launch it.

### Homebrew Channel

Before using the installation methods below, add the TVLauncher repository to
the [Homebrew Channel](https://www.webosbrew.org/). In the Homebrew Channel's
custom repositories, add:

```text
https://raw.githubusercontent.com/SiriosDev/TVLauncher/main/repo.json
```

TVLauncher will then appear in the available apps and can be installed
directly on the TV.

### Ares CLI

Install the [webOS CLI](https://webostv.developer.lge.com/develop/tools/cli-installation),
register your TV as a developer device, and install the package from a terminal.
You can download the package from the Releases page or install it through the
Homebrew Channel repository above:

```bash
npm install --global @webos-tools/cli
ares-setup-device #If you haven't already registered your TV
ares-install --device <device-name> <downloaded_file_name>.ipk
```

Replace `<device-name>` with the name configured in Ares.

### webOS Dev Manager Desktop

Click the upper-right **Install** button (or the equivalent install action) in **Apps**
section. Select the downloaded `.ipk` file and confirm the installation.

### LG Dev Manager

Add the custom repository with:

```text
https://raw.githubusercontent.com/SiriosDev/TVLauncher/main/repo.json
```

Navigate to the repository and install TVLauncher.
Alternatively, you can install the downloaded `.ipk` file directly from the
**Apps > Installed** section, clicking the **Install** button in the upper side,
or by drag'n'dropping the file (only on Desktop Browser).

## Usage

Open **TV Launcher** from your TV's apps. The app immediately launches the
built-in Live TV application and closes after the launch succeeds.

No settings are required and there is nothing else to configure.

## Tests

TVLauncher has been tested only on **NANO77**. 
It should work on any version of webOS 4.0 or later.
Reports, suggestions, and compatibility feedback are always welcome
in the issues.

## Credits

Installation and development information was cross-checked against the
following public projects and documentation:

- [LG webOS CLI documentation](https://webostv.developer.lge.com/develop/tools/cli-installation)
- [webos-homebrew-channel](https://github.com/webosbrew/webos-homebrew-channel)
- [webOS Dev Manager Desktop](https://github.com/webosbrew/dev-manager-desktop)
- [LG Dev Manager](https://github.com/Scoty/lg-dev-manager)

## AI Usage

AI assistance was used for researching sources and documentation, writing
commit messages, and code autocomplete during development.

## License

TVLauncher is distributed under the [Apache License 2.0](LICENSE).

## Disclaimer

LG, LG Electronics, webOS, and Live TV are trademarks or registered trademarks of their respective owners.

TVLauncher is an independent, community-developed, open-source project. It is not affiliated with, endorsed by, sponsored by, or officially associated with LG Electronics or any of its subsidiaries.

All trademarks, logos, product names, and brand names mentioned in this project are the property of their respective owners and are used solely for identification and compatibility purposes.

The use of these trademarks does not imply any partnership, endorsement, or authorization by their respective owners.
