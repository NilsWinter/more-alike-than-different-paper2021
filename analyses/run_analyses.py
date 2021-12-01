from pipeline.pipeline import main_pipeline


debug = True

analyses = {'configs/protect_ad_contrast_1.yaml': True}

task_list = list()
for conf_file, flag in analyses.items():
    if flag:
        if debug:
            main_pipeline(conf_file)
        else:
            try:
                main_pipeline(conf_file)
            except BaseException as e:
                print(e)
