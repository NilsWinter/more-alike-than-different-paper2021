from pipeline.pipeline import main_pipeline


debug = False

analyses = {'configs/protect_ad_contrast_1.yaml': True,
            'configs/protect_ad_contrast_2.yaml': True,
            'configs/protect_ad_contrast_3.yaml': True,
            'configs/protect_ad_contrast_4.yaml': True,
            'configs/protect_ad_contrast_5.yaml': True,
            'configs/protect_ad_contrast_6.yaml': True,
            'configs/protect_ad_contrast_7.yaml': True,
            'configs/protect_ad_contrast_8.yaml': True,
            'configs/protect_ad_contrast_9.yaml': True,
            }

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
