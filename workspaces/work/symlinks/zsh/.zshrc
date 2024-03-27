# Load environment.
if [ -f "$HOME/.environment" ]; then
    source "$HOME/.environment"
fi

# Load aliases.
if [ -f "$HOME/.aliases" ]; then
    source "$HOME/.aliases"
fi

# Load private data.
if [ -f "$HOME/.private" ]; then
    source "$HOME/.private"
fi

autoload -Uz compinit && compinit

# source antidote
source $(brew --prefix)/opt/antidote/share/antidote/antidote.zsh

# initialize plugins statically with ${ZDOTDIR:-~}/.zsh_plugins.txt
antidote load

# bun completions
[ -s "/Users/adam.bantly/.bun/_bun" ] && source "/Users/adam.bantly/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Moov
export GOPRIVATE="github.com/moov-io/*,github.com/moovfinancial/*"
export GOPATH=$HOME/go
export GOROOT="$(brew --prefix golang)/libexec"
export PATH=$PATH:${GOPATH}/bin:${GOROOT}/bin
