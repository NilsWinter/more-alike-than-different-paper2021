from pipeline.pipeline import main_pipeline


conf_files = [
              'configs/summary_plots_hariri.yaml',

              ]

for conf_file in conf_files:
    main_pipeline(conf_file)
