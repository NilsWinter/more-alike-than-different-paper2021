import pandas as pd
import numpy as np

from pipeline.steps import PipelineStep
from pipeline.steps import SampleFilter


class Mikrobiom(PipelineStep):

    def _execute(self, level: str, *args, **kwargs):
        df_mikrobiom = pd.read_csv('../../../mikrobiom_data/{}_hc_nhc.csv'.format(level), index_col='Unnamed: 0')
        df_mikrobiom.drop(axis=1, columns=['labels'], inplace=True)
        new_keys = dict()
        for i, key in enumerate(df_mikrobiom.keys()):
            new_keys[key] = "bacteria_{}".format(i)

        df_mikrobiom.rename(columns=new_keys, inplace=True)
        df_mikrobiom = df_mikrobiom.loc[:, (df_mikrobiom != df_mikrobiom.iloc[0]).any()]

        names = df_mikrobiom.keys()[1:-1]
        ids = pd.read_csv('../../../mikrobiom_data/probID_ID_hcnh.csv', index_col='sample_id')
        df_mikrobiom = df_mikrobiom.join(ids)
        df_mikrobiom.set_index("ProbandenID", inplace=True)
        df_mikrobiom = df_mikrobiom[~df_mikrobiom.index.str.contains("_2")]
        #from sklearn.preprocessing import StandardScaler
        #scaler = StandardScaler()
        #scaler.fit(df_mikrobiom)
        #scaled = scaler.fit_transform(df_mikrobiom)
        #df_mikrobiom = pd.DataFrame(scaled, columns=df_mikrobiom.columns, index=df_mikrobiom.index)

        df_mikrobiom.index = df_mikrobiom.index.astype(int)
        df_clinical = pd.read_csv('../../../mikrobiom_data/Clinical_DataFreeze1-3_macbook.csv',
                                  index_col='Proband', sep=';')
        df_clinical.index = df_clinical.index.astype(int)
        df_clinical = pd.merge(df_mikrobiom, df_clinical, how='inner', left_index=True, right_index=True)
        df_clinical['Proband'] = df_clinical.index
        df_clinical['hc_nhc'] = df_clinical["Group"]
        df_clinical['hc_nhc'][df_clinical["Group"] != 1] = 7
        df_clinical['Group'] = df_clinical['hc_nhc']


        df_clinical, _ = SampleFilter().apply_filter(self.pipeline.filter_name, df_clinical)
        self.pipeline.X_names = names
        self.pipeline.df = df_clinical

