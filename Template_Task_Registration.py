from clearml import Task

CONFIG_CONNECTION = True

task = Task.create(
    project_name="Heatmap",
    task_name="heatmap_template_task",
    task_type=Task.TaskTypes.application
)


if CONFIG_CONNECTION:
    import config
    config_dict = {}
    for k, v in vars(config).items():
        if k.startswith('__'):
            continue
        
        # If the value is a set (es. PHYSICAL_POSITIVE_CATS), we convert it into a list
        if isinstance(v, set):
            config_dict[k] = list(v)
        else:
            config_dict[k] = v

    print(f"Config loading: {len(config_dict)} variables found.")

    task.set_configuration_object(
        name="General",       # Nome della sezione nella UI
        config_dict=config_dict, 
        description="Config generated from logic/config.py"
    )

task.set_repo(
    repo="https://github.com/disit/heatmap-predictions-clearml",
    branch="main",
    commit=""
)

task.set_script(
    working_dir=".",
    entry_point="tasks/task_heatmap.py"
)

print("Template created!")
print("Task ID:", task.id)

# If configurations

