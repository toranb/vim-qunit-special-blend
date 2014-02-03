# vim-qunit-special-blend

Ever want to run a single qunit test from your test suite with karma?
Yeah, so did I.

This plugin was created to leverage the functionality provided by the
`quint-special-blend` npm package to run QUnit tests from within Vim. With this
plugin you will be able to run all of your tests, a single test module, and
even an individual test.

## The Plugin In Action

JavaScript: Notice how there are 3 tests and we only run one of them.
![javascript](https://f.cloud.github.com/assets/4416952/2059633/1a1c7a84-8bc3-11e3-8f63-da3e2f1184e4.gif)

CoffeeScript: Here we only run the first module which has two tests.
![coffee](https://f.cloud.github.com/assets/4416952/2059635/3b35a844-8bc3-11e3-85f8-212db6925e64.gif)

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/JarrodCTaylor/vim-qunit-special-blend ~/.vim/bundle/vim-qunit-special-blend`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/JarrodCTaylor/vim-qunit-special-blend'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/JarrodCTaylor/vim-qunit-special-blend'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/JarrodCTaylor/vim-qunit-special-blend'` to .vimrc
  - Run `:PlugInstall`

## Requirements

This plugin assumes that you are running your JavaScript tests with karma.
You will need to `npm install qunit-special-blend`. Then in your projects `karma.conf.js`
have the files array configured as follows:

``` javascript
  files: [
    /* The special blend */
    'node_modules/qunit-special-blend/qunit-special-blend.js',
    /* App and test files here */
    'your/app/js/*.js',
    'your/tests/*.js',
    /* Run the special blend */
    'node_modules/qunit-special-blend/run-qunit-special-blend.js'
  ],
```

## Usage

The plugin provides three commands:

``` text
  RunAllQunitTests
  RunSingleQunitModule
  RunSingleQunitTest
```

Ensure that your cursor is within a module or test as appropriate for the
desired command that you are trying to run.


## Custom Settings

The plugin assumes that your JS tests are configured to be run with `grunt
test` from the command line. If this is not the case you can specify the
command that will run your tests with the `special_blend_run` variable in your
`.vimrc` like so:

``` text
let g:special_blend_run='karma start'
```
