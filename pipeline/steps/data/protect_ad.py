import pandas as pd
import numpy as np

from pipeline.steps import PipelineStep
from analysis.analysis_nils_alpha import load_data


class ProtectADData(PipelineStep):

    def _execute(self, contrast: int, *args, **kwargs):
        X, y = load_data(filename_id=contrast)

        df = pd.DataFrame({'fmri_filename': X, 'Group': y, 'dummy': np.ones(y.shape[0]),
                           'Proband': np.arange(y.shape[0])})
        df['Group'] = df['Group'].replace({0: 'Non-Responder', 1: 'Responder'})

        self.pipeline.X_names = ['fmri_filename']
        self.pipeline.df = df

