import pandas as pd

from pipeline.steps import PipelineStep
from analysis.analysis_nils_alpha import load_data


class ProtectADData(PipelineStep):

    def _execute(self, contrast: int, *args, **kwargs):
        X, y = load_data(filename_id=contrast)

        df = pd.DataFrame({'fmri_filename': X, 'Group': y})

        self.pipeline.X_names = ['fmri_filename']
        self.pipeline.df = df

