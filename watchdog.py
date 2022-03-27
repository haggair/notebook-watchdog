import os

class NotebookWatchDog():
    __CELL_INITIAL_STATE__ = -1
    __CURRENT_CELL_STATE__ = 0
    __CELL_STATE_FILE__ = "cell.state"
    
    
    def __init__(self, ipython):
        self.shell = ipython
    
    def __write_cell_state(self, current_state):
         with open(self.__CELL_STATE_FILE__, "w") as fw:
                fw.write(str(current_state))
                fw.flush()
                fw.close()

    def watch(self, line, cell=None):
        current_state = self.__CELL_INITIAL_STATE__
        if os.path.exists(self.__CELL_STATE_FILE__):
            with open(self.__CELL_STATE_FILE__, "r") as fr:
                current_state = int(fr.read())
                fr.close()
        if  self.__CURRENT_CELL_STATE__ > current_state:
            self.shell.ex(cell)
            self.__write_cell_state(self.__CURRENT_CELL_STATE__)
        else:
            print(f"skipping cell...")
        self.__CURRENT_CELL_STATE__ += 1
              
            
    def unwatch(self, line, cell=None):
        if os.path.exists(self.__CELL_STATE_FILE__):
            os.remove(self.__CELL_STATE_FILE__)
            
    def skip(self, line, cell=None):
        print(f"skipping cell...")
        return
            

def load_ipython_extension(shell):
    wd = NotebookWatchDog(shell)
    '''Registers the watchdog magic when the extension loads.'''
    shell.register_magic_function(wd.watch, 'line_cell')
    shell.register_magic_function(wd.unwatch, 'line_cell')
    shell.register_magic_function(wd.skip, 'line_cell')

def unload_ipython_extension(shell):
    '''Unregisters the watchdog magic when the extension unloads.'''
    del shell.magics_manager.magics['cell']['watch']
    del shell.magics_manager.magics['cell']['unwatch']
    del shell.magics_manager.magics['cell']['skip']
