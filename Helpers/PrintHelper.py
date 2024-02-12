from varname import nameof

class PrintHelper:
    def __init__(self) -> None:
        pass

    def print_step(step):
        print(f'--------------------- {step} ---------------------')

    def print_datas(*args):
        for arg in args:
            print(f'valeur de {nameof(arg)} : {arg}')

    def print_dimensions(*args):
        for arg in args:
            print(f'dimensions de {nameof(arg)} : {arg.shape}')