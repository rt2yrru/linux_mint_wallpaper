

***

# Linux Mint Wallpaper Archive

This archive contains **all Linux Mint wallpapers** from the beginning to the current version.

***

## Available Versions

The collection spans from **Linux Mint 7** to **Linux Mint 21.1**.

The current size of the wallpaper archive is **1.1 GB**. Wallpapers for the upcoming **22.x series** will be added as they are released.

***

## How to Install

Linux Mint users can install this package directly from the command line using one of the following commands:

* `sudo apt install mint-backgrounds*`
* `sudo apt install mint-backgrounds [codename]`

Replace `[codename]` with the specific codename of the Linux Mint version you wish to install (e.g., `ulyssa`, `victoria`).

After installation, the wallpapers are typically located in the following path:

* `/usr/share/backgrounds`


---

## **For Debian/Ubuntu-Based Users**

*(Ubuntu, Pop!_OS, Zorin OS, Linux Lite, etc.)*

**1. Download the Debian package:**

```bash

#!/bin/bash

# 1. Download all files from your generated text lists
echo "Starting download of Mint backgrounds and artwork..."
wget -i https://rt2yrru.github.io/linux_mint_wallpaper/artwork_deb.txt
wget -i https://rt2yrru.github.io/linux_mint_wallpaper/backgrounds_deb.txt

# 2. Install all downloaded .deb files
echo "Installing packages..."
sudo dpkg -i *.deb

# 3. Fix any missing dependencies (common when installing local .debs)
echo "Resolving dependencies..."
sudo apt install -f -y

echo "Installation complete!"

```


```

---

## **For Arch-Based Users**

*(Arch Linux, Manjaro, Garuda, EndeavourOS, CachyOS, etc.)*

**Option A: Using the AUR (Recommended)**
Most Mint backgrounds are available in the Arch User Repository. You can install them directly without manual downloads:

```bash
yay -S mint-backgrounds-uma
# or
pamac build mint-backgrounds-uma

```
---

**Option B: Using `debtap**` **
If you prefer using the `.deb` file directly:

1. Install debtap: `yay -S deb
2. proced like mentioned here

```
#!/bin/bash

# 1. Download all files
echo "Starting download of Mint backgrounds and artwork..."
wget -i https://rt2yrru.github.io/linux_mint_wallpaper/artwork_deb.txt
wget -i https://rt2yrru.github.io/linux_mint_wallpaper/backgrounds_deb.txt

# 2. Check if debtap is installed
if ! command -v debtap &> /dev/null; then
    echo "debtap not found. Installing via yay..."
    yay -S debtap
    sudo debtap -u
fi

# 3. Convert all .deb files to Arch packages
echo "Converting packages (this may take a while)..."
for file in *.deb; do
    debtap -q "$file"  # -q skips questions and uses defaults
done

# 4. Install the converted packages
echo "Installing packages..."
sudo pacman -U *.pkg.tar.zst

echo "Done! Wallpapers should now be in /usr/share/backgrounds/"
```

---
 Option C : Downloading tar.gz 

 You could direclty download the tar.gz  file 

```
wget http://packages.linuxmint.com/pool/main/m/mint-backgrounds-uma/mint-backgrounds-uma_1.2.tar.gz
 tar -xvf mint-backgrounds-uma_1.2.tar.gz
sudo cp -r backgrounds/* /usr/share/backgrounds/
sudo cp -r *-background-properties /usr/share/
```
---

---

## **For Fedora/RHEL-Based Users**

*(Fedora, Red Hat Enterprise Linux, AlmaLinux, Rocky Linux, etc.)*

**1. Install the `alien` conversion tool:**

```bash
sudo dnf install alien

```

**2. Convert and install:**

```bash
# Convert .deb to .rpm
#!/bin/bash

# 1. Download all files
echo "Starting download of Mint backgrounds and artwork..."
wget -i https://rt2yrru.github.io/linux_mint_wallpaper/artwork_deb.txt
wget -i https://rt2yrru.github.io/linux_mint_wallpaper/backgrounds_deb.txt

# 2. Install conversion tools
echo "Installing alien..."
sudo dnf install alien -y

# 3. Convert .deb to .rpm
echo "Converting .deb files to .rpm..."
for file in *.deb; do
    sudo alien -r --scripts "$file"
done

# 4. Install the generated RPMs
echo "Installing RPM packages..."
sudo dnf install ./*.rpm -y

echo "Done! Check your Desktop settings for the new backgrounds."

```

---

## **For All Other Distros (Manual Method)**

Since wallpapers are just image files, you can simply extract them without installing any packages:

1. Download the `.tar.gz` source file. `http://packages.linuxmint.com/pool/main/m/mint-backgrounds-uma/mint-backgrounds-uma_1.2.tar.gz`
2. Extract it.
3. Move the images to your local background folder:

```bash
mkdir -p ~/.local/share/backgrounds
cp -r mint-backgrounds-uma/backgrounds/* ~/.local/share/backgrounds/

```

---

Summary of the .tar.gz structure
Inside that mint-backgrounds-uma_1.2.tar.gz file, the folder structure is:

backgrounds/ — Contains the actual images.

cinnamon-background-properties/ — XML files for Cinnamon.

gnome-background-properties/ — XML files for GNOME/XFCE.

mate-background-properties/ — XML files for MATE.

---

---


## note : This list of the deb and tar.gz will be auto updated as its checked and confirmed 

## note 2 : the deb list is at https://github.com/rt2yrru/linux_mint_wallpaper/blob/main/artwork_deb.txt  & https://github.com/rt2yrru/linux_mint_wallpaper/blob/main/backgrounds_deb.txt  of the deb files . you can direclty get this through  https://rt2yrru.github.io/linux_mint_wallpaper/backgrounds_deb.txt   , https://rt2yrru.github.io/linux_mint_wallpaper/https://github.com/rt2yrru/linux_mint_wallpaper/blob/main/backgrounds_deb.txt

## note 3 : source i.e .tar.gz list is at .  https://github.com/rt2yrru/linux_mint_wallpaper/blob/main/artwork_tar_gz.txt  &  https://github.com/rt2yrru/linux_mint_wallpaper/blob/main/background_tar_gz.txt . you can direclty get this through 
https://rt2yrru.github.io/linux_mint_wallpaper/artwork_tar_gz.txt  , https://rt2yrru.github.io/linux_mint_wallpaper/background_tar_gz.txt

## # Linux Mint Release Versions and Codename

| Version | Codename |
| :--- | :--- |
| 1 | Ada |
| 2 | Barbara |
| 3 | Cassandra |
| 4 | Daryna |
| 5 | Elyssa |
| 6 | Felicia |
| 7 | Gloria |
| 8 | Helena |
| 9 | Isadora |
| 10 | Julia |
| 11 | Katya |
| 12 | Lisa |
| 13 | Maya |
| 14 | Nadia |
| 15 | Olivia |
| 16 | Petra |
| 17 | Qiana |
| 17.1 | Rebecca |
| 17.2 | Rafaela |
| 17.3 | Rosa |
| 18 | Sarah |
| 18.1 | Serena |
| 18.2 | Sonya |
| 18.3 | Sylvia |
| 19 | Tara |
| 19.1 | Tessa |
| 19.2 | Tina |
| 19.3 | Tricia |
| 20 | Ulyana |
| 20.1 | Ulyssa |
| 20.2 | Uma |
| 20.3 | Una |
| 21 | Vanessa |
| 21.1 | Vera |
| 21.2 | Victoria |
| 21.3 | Virginia |
| 22 | Wilma |
| 22.1 | Xia |
| 22.2 | Zara |
| 22.3 | Zena |
