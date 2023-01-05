-------------------------------------------------
-- DT'S NEOVIM CONFIGURATION
-- Neovim website: https://neovim.io/
-- DT's dotfiles: https://gitlab.com/dwt1/dotfiles
-------------------------------------------------

local status, packer = pcall(require, "packer")
if not status then
	print("Packer is not installed")
	return
end

-- Reloads Neovim after whenever you save plugins.lua
vim.cmd([[
    augroup packer_user_config
      autocmd!
     autocmd BufWritePost plugins.lua source <afile> | PackerSync
  augroup END
]])

packer.startup(function(use)
	-- Packer can manage itself
	use("wbthomason/packer.nvim")

	-- Dashboard is a nice start screen for nvim
	use("glepnir/dashboard-nvim")

	-- Telescope
	use({
		"nvim-telescope/telescope.nvim",
		tag = "0.1.0",
		requires = { { "nvim-lua/plenary.nvim" } },
	})
	use("nvim-telescope/telescope-file-browser.nvim")

	use("nvim-treesitter/nvim-treesitter") -- Treesitter Syntax Highlighting

	-- Productivity
	use("vimwiki/vimwiki")
	use("jreybert/vimagit")
	use("nvim-orgmode/orgmode")

	use("folke/which-key.nvim") -- Which Key
	use("nvim-lualine/lualine.nvim") -- A better statusline

	-- File management --
	use("vifm/vifm.vim")
	use("scrooloose/nerdtree")
	-- use("tiagofumo/vim-nerdtree-syntax-highlight")
	use("ryanoasis/vim-devicons")

	-- Tim Pope Plugins --
	use("tpope/vim-surround")
	use("tpope/vim-commentary")

	-- Syntax Highlighting and Colors --
	use("PotatoesMaster/i3-vim-syntax")
	use("kovetskiy/sxhkd-vim")
	use("vim-python/python-syntax")
	use("ap/vim-css-color")

	-- Junegunn Choi Plugins --
	use("junegunn/goyo.vim")
	use("junegunn/limelight.vim")
	use("junegunn/vim-emoji")

	-- Colorschemes --
	use("RRethy/nvim-base16")
	use("kyazdani42/nvim-palenight.lua")
	use("folke/tokyonight.nvim")
	use("LunarVim/onedarker.nvim")
	use("olimorris/onedarkpro.nvim")
	use("tanvirtin/monokai.nvim")
	use("navarasu/onedark.nvim")
	use("cpea2506/one_monokai.nvim")
	use("rafi/awesome-vim-colorschemes")

	-- Vim Multiple Cursors --
	use("terryma/vim-multiple-cursors")

	-- Tagbar ---
	use("preservim/tagbar")

	-- Minimap ---
	use("wfxr/minimap.vim")

	-- Toggleterm
	use({ "akinsho/toggleterm.nvim", commit = "2a787c426ef00cb3488c11b14f5dcf892bbd0bda" })

	-- Other stuff --
	use("frazrepo/vim-rainbow")
	use({
		"rcarriga/nvim-notify",
		config = function()
			require("notify").setup({
				stages = "fade_in_slide_out",
				background_colour = "FloatShadow",
				timeout = 0.5,
			})
			vim.notify = require("notify")
		end,
	})

	if packer_bootstrap then
		packer.sync()
	end
end)
