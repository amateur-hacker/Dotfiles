:set number
:set relativenumber
:set autoindent
:set tabstop=4
:set shiftwidth=4
:set smarttab
:set softtabstop=4
:set mouse=a

call plug#begin()

Plug 'https://github.com/tpope/vim-surround' " Surrounding ysw)
Plug 'https://github.com/preservim/nerdtree' " NerdTree
Plug 'https://github.com/tpope/vim-commentary' " For Commenting gcc & gc
Plug 'https://github.com/vim-airline/vim-airline' " Status bar
Plug 'https://github.com/lifepillar/pgsql.vim' " PSQL Plugging needs :SQLSETTYPE pgsql.vim
Plug 'https://github.com/ap/vim-css-color' " CSS Color preview
Plug 'https://github.com/glepnir/dashboard-nvim'
Plug 'https://github.com/rafi/awesome-vim-colorschemes' " Retro Scheme

let g:dashboard_default_executive ='fzf'

set encoding=UTF-8

call plug#end()
