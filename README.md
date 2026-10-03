# my dotfiles

## Installation Checklist

- [ ] Install Homebrew

  ```bash
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
  ```

- [ ] Install zero-sh

  ```bash
      brew install zero-sh/tap/zero
  ```

- [ ] Install git

  ```bash
      brew install git
  ```

- [ ] Clone dotfiles

  ```bash
      git clone https://github.com/yadam/dotfiles.git ~/.dotfiles
  ```

- [ ] Run zero-sh

  ```bash
      zero setup work|home
  ```

- [ ] Reboot
- [ ] Run zero-sh again to check for updates

  ```bash
      zero setup work|home
  ```
