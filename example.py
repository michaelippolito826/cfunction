import re

def convert_if_to_function(c_file_path):
    # read the C file
    with open(c_file_path, 'r') as f:
        c_code = f.read()
    
    # define the regex pattern to match if statements with a test number
    if_pattern = r'if\s*\(\s*test_number\s*==\s*(\d+)\s*\)\s*\{\s*(.*?)\s*\}'
    
    # find all if statements with a test number in the code
    if_matches = re.findall(if_pattern, c_code, re.DOTALL)
    
    # iterate over the matches and create functions
    for i, match in enumerate(if_matches):
        # extract the test number and the code block
        test_number = match[0]
        code_block = match[1]
        
        # create a function name based on the test number
        func_name = 'test_{}'.format(test_number)
        
        # create the function code
        func_code = 'void {}() {{\n{}\n}}\n'.format(func_name, code_block)
        
        # replace the if statement with a function call
        call_code = '{}();\n'.format(func_name)
        c_code = re.sub(if_pattern, call_code, c_code, count=1)
        
        # add the new function to the code
        c_code += func_code
    
    # write the modified code back to the file
    with open(c_file_path, 'w') as f:
        f.write(c_code)
        
convert_if_to_function()