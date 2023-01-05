require("dt.base") -- General Settings
require("dt.highlights") -- Colourscheme and other highlights
require("dt.maps") -- Keymaps
require("dt.plugins") -- Plugins
require("dt.bootstrap") -- Packer Auto-Installer
require("dt.lualine")   -- lualine 
require("dt.toggleterm")
vim.cmd "inoremap jk <Esc>"
vim.cmd "inoremap kj <Esc>"
-- vim.cmd "nnoremap <TAB> :bnext<CR>"
vim.cmd "nmap <C-k> :NERDTreeToggle<CR>"
vim.cmd "nmap <C-l> :TagbarToggle<CR>"
vim.cmd "nmap <C-j> :ToggleTerm<CR>"
-- vim.cmd ":let NERDTreeShowHidden=1"

--- Few basic settings for minimap
-- vim.cmd "let g:minimap_width = 10"
-- vim.cmd "let g:minimap_auto_start = 1"
-- vim.cmd "let g:minimap_auto_start_win_enter = 1"
-- vim.cmd "hi MinimapCurrentLine ctermfg=Green guifg=#50FA7B guibg=#32302f"
-- vim.cmd "let g:minimap_cursor_color = 'MinimapCurrentLine'"
-- vim.cmd "highlight minimapCursor ctermbg=59  ctermfg=228 guibg=#5F5F5F guifg=#FFFF87"
-- vim.cmd "let g:minimap_enable_highlight_colorgroup=1"
