
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
