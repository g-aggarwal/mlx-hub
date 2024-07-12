def print_string_list(list):
    for item in list: print(item)

def print_repo_list(model_list):
    for model in sorted(model_list, key=lambda repo: repo.repo_path):
        print(model.repo_id)

def print_model_list(model_list):
    for model in sorted(model_list, key=lambda model: model.id):
        print(model.id)