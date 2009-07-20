""" General matlab interface code """

# Stdlib imports
import os
import re
import tempfile
import numpy as np
from nipype.interfaces.base import CommandLine


class Matlab(object):
    """Object that sets up Matlab specific tools and interfaces

    """
    def __init__(self, matlab_cmd='matlab -nojvm -nosplash'):
        """initializes interface to matlab
        (default 'matlab -nojvm -nosplash'
        """
        self.matlab_cmd = matlab_cmd

    def set_matlabcmd(self, cmd):
        """reset the base matlab command
        """
        self.mtalb_cmd = cmd

    def run_matlab(self,cmd):
        #subprocess.call('%s -r \"%s;exit\" ' % (matlab_cmd, cmd),
        #                shell=True)
        outcmd = '%s -r \"%s;exit\" '%(self.matlab_cmd, cmd)
        out = CommandLine(outcmd).run()
        return out,outcmd

    def run_matlab_script(self,script_lines, script_name='pyscript'):
        ''' Put multiline matlab script into script file and run '''
        mfile = file(script_name + '.m', 'wt')
        mfile.write(script_lines)
        mfile.close()
        return self.run_matlab(script_name)


# Useful Functions for working with matlab

def fltcols(vals):
    ''' Trivial little function to make 1xN float vector '''
    return np.atleast_2d(np.array(vals, dtype=float))


def mlab_tempfile(dir=None):
    """Returns a temporary file-like object with valid matlab name.

    The file name is accessible as the .name attribute of the returned object.
    The caller is responsible for closing the returned object, at which time
    the underlying file gets deleted from the filesystem.

    Parameters
    ----------
    
      dir : str
        A path to use as the starting directory.  Note that this directory must
        already exist, it is NOT created if it doesn't (in that case, OSError
        is raised instead).

    Returns
    -------
      f : A file-like object.

    Examples
    --------

    >>> f = mlab_tempfile()
    >>> '-' not in f.name
    True
    >>> f.close()
    """
    valid_name = re.compile(r'^\w+$')

    # Make temp files until we get one whose name is a valid matlab identifier,
    # since matlab imposes that constraint.  Since the temp file routines may
    # return names that aren't valid matlab names, but we can't control that
    # directly, we just keep trying until we get a valid name.  To avoid an
    # infinite loop for some strange reason, we only try 100 times.
    for n in range(100):
        f = tempfile.NamedTemporaryFile(suffix='.m',prefix='tmp_matlab_',
                                        dir=dir)
        # Check the file name for matlab compilance
        fname =  os.path.splitext(os.path.basename(f.name))[0]
        if valid_name.match(fname):
            break
        # Close the temp file we just made if its name is not valid; the
        # tempfile module then takes care of deleting the actual file on disk.
        f.close()
    else:
        raise ValueError("Could not make temp file after 100 tries")
        
    return f
