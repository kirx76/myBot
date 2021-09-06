def info(message):
    print(f'[INFO] {message}')


def log(message):
    print(f'[LOG] {message}')


def error(message):
    print(f'[ERROR] {message}')


def generate_function_description(name, description):
    return {'name': name, 'description': description}


def get_all_functions(function_list, is_text):
    if is_text:
        var = "=" * 25 + '\n'
        for func in function_list:
            var = var + f'{func["name"].capitalize()}: {func["description"].capitalize()}\n{"=" * 25}\n'
        return var
    return function_list
