class CodeBuilder():
    indent_size = 2
    def __init__(self, root_name):
        self.class_name = root_name
        self.params:dict = {}
    def add_field(self, type, name):
        self.params[type] = name
        return self
    def __str__(self):
        str_build = f'class {self.class_name}:'
        if not self.params:
            str_build += '\n' + self.indent_size * ' ' + 'pass'
            return str_build
        str_build +='\n' + self.indent_size * ' ' + 'def __init__(self):'              
        for key, value in self.params.items():
            str_build +=f'\n'+ self.indent_size * '  ' + f'self.{key} = {value}'
        return str_build
cb  = CodeBuilder('a')
print(cb)