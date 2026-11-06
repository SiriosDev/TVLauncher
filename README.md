# TVLauncher

A simple, minimalist launcher for LG webOS TVs.

TVLauncher is made for custom launchers that do not support system applications
or need a simple alternative way to organize them. It provides a direct,
minimal path to the built-in Live TV application.

TVLauncher has been tested on an **LG NANO77**.

## Installation

Download the latest `.ipk` package from the
[Releases](https://github.com/SiriosDev/TVLauncher/releases) page and install it
on your LG webOS TV using one of the methods below.

There is no setup, configuration, account, or additional dependency. Install it,
open it, and use it.

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

Click the upper-right **Install** button (or the equivalent install action).
Select the downloaded `.ipk` file and confirm the installation.

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

## License

TVLauncher is distributed under the [Apache License 2.0](LICENSE).
