# PWM_Gatekeeper package

Clover demo application that can be used as a template.

Contents:

* The main Python script (`src/main.py`).
* The main launch file (`launch/main.launch`).
* The systemd service file: (`debian/service.em`).
* The web part served with `roswww` or `roswww_static` (`www`).

## How to convert your app to a Debian package

Install prerequisites:

```bash
sudo apt-get install python3-bloom fakeroot debhelper dpkg-dev
```

Go to your package directory:

```bash
roscd clover_app
```

Generate Debian files:

```bash
bloom-generate rosdebian
```

Build Debian package:

```bash
fakeroot debian/rules binary
```

## How to install the package

The built Debian packages are located one directory upper then your package directory:

```bash
cd ..
```

Install the package with `dpkg`. E. g.:

```bash
sudo dpkg -i ros-noetic-clover-app_0.0.0-0buster_armhf.deb
```

## Checking installation

The systemd service file is installed as `<package_name>.service`, e. g. `ros-noetic-clover-app.service`. It will be started automatically. You can see the status using `systemctl` command, e. g.:

```bash
sudo systemctl status ros-noetic-clover-app
```

The web part should be available at `http://<hostname>/<package_name>`, e. g. http://192.168.11.1/clover_app.

## Using as a template

Change all the `clover_app` occurrences to your app's name. Keeping `clover_` prefix is recommended.

## Publishing

Finished Debian package can be [published at packages.coex.tech](https://github.com/CopterExpress/packages).
