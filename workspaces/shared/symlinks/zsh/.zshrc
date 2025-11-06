autoload -Uz compinit && compinit

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

# source antidote
source $(brew --prefix)/opt/antidote/share/antidote/antidote.zsh

# initialize plugins statically with ${ZDOTDIR:-~}/.zsh_plugins.txt
antidote load # This loads nvm bash_completion

# autoload -Uz promptinit && promptinit && prompt common