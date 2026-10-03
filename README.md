# my dotfiles

## Installation Checklist

- [ ] Install Homebrew
  ```bash
      $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
  ```
- [ ] Install zero-sh
  ```bash
      $ brew install zero-sh/tap/zero
  ```
- [ ] Install git
  ```bash
      $ brew install git
  ```
- [ ] Clone dotfiles
  ```bash
      $ git clone https://github.com/yadam/dotfiles.git ~/.dotfiles
  ```
- [ ] Run zero-sh
  ```bash
      $ zero setup work|home
  ```
- [ ] Reboot
- [ ] Run zero-sh again to check for updates
  ```bash
      $ zero setup work|home
  ```
- [ ] Configure powerlevel10k
  ```bash
      $ p10k configure
  ```
- [ ] iTerm > Preferences > Profiles > Colors > Color Preset... > Import ... > Import Monokai Remastered.itermcolors
- [ ] iTerm > Preferences > Profiles > Terminal > Unlimited scrollback


## Codex instructions and personal skills

The shared `codex` package stores user instructions in
`workspaces/shared/symlinks/codex/.codex/AGENTS.md` and all personal skill
folders in `workspaces/shared/symlinks/codex/.codex/skills/`.
The `.agents/skills/` entries in the same package point to those folders for
current Codex discovery. The `.codex/skills/` links retain compatibility with
the existing installation. Both paths reach the same files.

`zero setup home` applies shared configuration before home configuration.
The shared `run/before/10-codex-directories.sh` script creates local runtime
roots before Stow links the managed files. This keeps Codex's runtime state
outside the Dotfiles repository. Do not link the entire `.codex` directory or
its entire `skills` directory.

To apply only scripts and symlinks, without installing packages or changing
system defaults, run:

```sh
zero run-scripts home --directory "$HOME/.dotfiles"
zero apply-symlinks home --directory "$HOME/.dotfiles"
```

These commands operate on the shared and home workspaces. Review additional
scripts before running them if those folders gain other setup actions.
On an existing machine, preserve any local skill or instruction file before
replacing it with a managed link. Stow reports conflicts rather than adopting
or overwriting local files.

Edit personal skills through either installed path or their Dotfiles source.
Add a new skill folder under the shared `.codex/skills/` source and a matching
relative link under the package's `.agents/skills/`, then reapply symlinks.
Commit and push the Dotfiles changes to make them available to another machine.
Built-in `.system` skills and plugin caches remain managed by Codex and its
plugins. Install the same plugins separately on each machine.
