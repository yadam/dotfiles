# Local Homebrew tap

This directory defines the `adam/local` tap. The home Brewfile uses this dotfiles
Git repository as its local source, so these casks are included in a dotfiles clone.
Homebrew keeps a separate checkout of the tap under its own prefix.

The digiKam and darktable casks copy Homebrew's official definitions, with the
`disable!` declarations removed. They retain the official project download URLs,
SHA-256 checksums, platform requirements, and uninstall settings. This is a local
exception to Homebrew's Gatekeeper policy. It does not change macOS Gatekeeper
settings or remove quarantine attributes.

## Installation

Run the home Brewfile when ready to install its apps:

```sh
brew bundle --file="$HOME/.dotfiles/workspaces/home/Brewfile"
```

The Brewfile trusts the two casks individually. It does not grant whole-tap trust.
macOS may still require approval to install or open the applications.

## Updates

Check the official definitions before updating a version or checksum:

- https://github.com/Homebrew/homebrew-cask/blob/master/Casks/d/digikam.rb
- https://github.com/Homebrew/homebrew-cask/blob/master/Casks/d/darktable.rb

Commit cask updates to this dotfiles repository, then run `brew update` to refresh
Homebrew's local checkout. Homebrew does not read uncommitted cask changes from
the source repository. Keep checksum verification and the macOS protections intact.
