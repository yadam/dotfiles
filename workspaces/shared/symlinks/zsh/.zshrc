# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

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

# Load antibody
source <(antibody init)
antibody bundle < "$HOME/.antibody_plugins"

test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# tabtab source for serverless package
# uninstall by removing these lines or running `tabtab uninstall serverless`
[[ -f /Users/adambantly/ns8/ns8-salesforcecommerce-switchboard/node_modules/tabtab/.completions/serverless.zsh ]] && . /Users/adambantly/ns8/ns8-salesforcecommerce-switchboard/node_modules/tabtab/.completions/serverless.zsh
# tabtab source for sls package
# uninstall by removing these lines or running `tabtab uninstall sls`
[[ -f /Users/adambantly/ns8/ns8-salesforcecommerce-switchboard/node_modules/tabtab/.completions/sls.zsh ]] && . /Users/adambantly/ns8/ns8-salesforcecommerce-switchboard/node_modules/tabtab/.completions/sls.zsh
# tabtab source for slss package
# uninstall by removing these lines or running `tabtab uninstall slss`
[[ -f /Users/adambantly/ns8/ns8-salesforcecommerce-switchboard/node_modules/tabtab/.completions/slss.zsh ]] && . /Users/adambantly/ns8/ns8-salesforcecommerce-switchboard/node_modules/tabtab/.completions/slss.zsh