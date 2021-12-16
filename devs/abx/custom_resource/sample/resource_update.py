# -*- coding: utf-8 -*-
'''
Created on 1983. 08. 09.
@author: Hye-Churn Jang, CMBU Specialist in Korea, VMware [jangh@vmware.com]
'''

import sys
import importlib
import manifest
sys.path.insert(0, '../../common')
_module = importlib.import_module(manifest.sdk)
for exportObject in _module.exportObjects: __builtins__[exportObject] = _module.__getattribute__(exportObject)
_NEWLINE_ = '\n'

# __ABX_IMPLEMENTATIONS_START__
#===============================================================================
# ABX Code Implementations                                                     #
#===============================================================================
# Import Libraries Here

# Implement Handler Here
def handler(context, inputs):
    # set common values
    vra = VraManager(context, inputs)
    
    # set default values
    if 'var1' not in inputs or not inputs['var1']: raise Exception('var1 property must be required') # Required
    if 'var2' not in inputs: inputs['var2'] = None # Optional Init
    if 'var3' not in inputs or not inputs['var3']: inputs['var3'] = 'default' # Optional Enum Init
    if 'var4' not in inputs: inputs['var4'] = [] # Optional List Init
    if 'var5' not in inputs: inputs['var5'] = {} # Optional Dict Init
    
    # retrieve resource
    resource = vra.get('' + inputs['id'])
    
    # update resource
    if 'var1' in inputs: resource['var1'] = inputs['var1']
    if 'var2' in inputs: resource['var2'] = inputs['var2']
    vra.put('' + inputs['id'], resource)
    
    # publish resource
    outputs = inputs
    outputs.pop('VraManager')
    return outputs
# __ABX_IMPLEMENTATIONS_END__
