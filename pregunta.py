"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop(columns= df.columns[0], inplace=True)
    df.dropna(inplace=True)
    for i in ['tipo_de_emprendimiento' , "barrio" ,'comuna_ciudadano']:
        df[i] = df[i].fillna(df[i].mode())

   #

    variables_categ = ['sexo','tipo_de_emprendimiento','idea_negocio','barrio', df.columns[-1]]
    for i in variables_categ:
        df[i] = df[i].str.lower()

    variables_num = ['estrato','comuna_ciudadano','monto_del_credito']
    for i in variables_num:
        df[i] = pd.to_numeric (df[i],errors= 'coerce')

    df['monto_del_credito'] = df['monto_del_credito'].fillna(df['monto_del_credito'].mean())

    df.drop_duplicates(keep = 'last', inplace= True)
 
    print(df)

    df[0].count()


    return df


   
