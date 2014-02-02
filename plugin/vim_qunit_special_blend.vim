" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
python << endOfPython
import vim_qunit_special_blend as sb
def command_to_run_tests():
    if int(vim.eval('exists("g:special_blend_run")')) != 0:
        return vim.eval("g:special_blend_run")
    else:
        return "grunt test"
endOfPython

function! RunSingleModule()
python << endOfPython

current_line_index = vim.current.window.cursor[0]
current_module_line_num = sb.get_line_num_of_current_module(current_line_index, vim.current.buffer)
if current_module_line_num >= 0:
    vim.current.buffer[current_module_line_num] = sb.sub_current_module_with_singleModule(current_module_line_num, vim.current.buffer)
    vim.command(':!{}'.format(command_to_run_tests()))
    vim.current.buffer[current_module_line_num] = sb.sub_singleModule_with_module(current_module_line_num, vim.current.buffer)
    vim.command('silent wall')
else:
    print("This doesn't look like a QUnit test file.")

endOfPython
endfunction

function! RunSingleTest()
python << endOfPython

current_line_index = vim.current.window.cursor[0]
current_test_line_num = sb.get_line_num_of_current_test(current_line_index, vim.current.buffer)
if current_test_line_num >= 0:
    vim.current.buffer[current_test_line_num] = sb.sub_current_test_with_singleTest(current_test_line_num, vim.current.buffer)
    vim.command(':!{}'.format(command_to_run_tests()))
    vim.current.buffer[current_test_line_num] = sb.sub_singleTest_with_test(current_test_line_num, vim.current.buffer)
    vim.command('silent wall')
else:
    print("This doesn't look like a QUnit test file.")

endOfPython
endfunction

function! RunAllTests()
python << endOfPython

vim.command(':!{}'.format(command_to_run_tests()))

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! RunSingleQunitModule call RunSingleModule()
command! RunSingleQunitTest call RunSingleTest()
command! RunAllQunitTests call RunAllTests()
