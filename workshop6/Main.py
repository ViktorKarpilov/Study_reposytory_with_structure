""" Viktor Karpilov KM-82 """

if __name__ == '__main__':
    dataset_path = "src/test/test_dataset.py"
    try:
        import importlib.util as imp
        spec = imp.spec_from_file_location("test_dataset", dataset_path)
        dataset_builder = imp.module_from_spec(spec)
        spec.loader.exec_module(dataset_builder)
    except Exception as exc:
        print("You have a sysyem problem , that looks like {0}".format(exc))
    try:
        dataset_builder.Main("data/friday.csv","result/result.html")
    except Exception as exc:
        print("Something very wrong : {0} in file {1}".format(exc,dataset_path))
