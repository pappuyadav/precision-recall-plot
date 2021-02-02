@author: pyada
"""

import matplotlib.pyplot as plt
import pandas as pd

recall_path=r'Path of your recall text file'
precision_path=r'Path of your precision text file'

def pr_plot(recall_path,precision_path):
    data = pd.read_csv(recall_path, sep=',', header=None)
    data1= pd.read_csv(precision_path, sep=',', header=None)

    for i, col in enumerate(data.columns):
        data.iloc[:, i] = data.iloc[:, i].str.replace("'", '')
        recall=data.loc[0]
    recall=pd.to_numeric(recall)


    for j, col1 in enumerate(data1.columns):
        data1.iloc[:, j] = data1.iloc[:, j].str.replace("'", '')
        precision=data1.loc[0]
    precision=pd.to_numeric(precision)


    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    fig.subplots_adjust(hspace=0.5)


    ax1.plot(recall, precision,label='Logistic',color='r')
    ax1.set_xlabel('Recall')
    ax1.set_ylabel('Precision')
    ax1.grid(True)
    fig.savefig('precision-recall.png',dpi=1200)

    ax2.plot(recall,label='Logistic',color='b')
    ax2.set_xlabel('Steps')
    ax2.set_ylabel('Recall')
    ax2.grid(True)
    fig.savefig('recall-steps.png',dpi=1200)

    ax3.plot(precision,label='Logistic',color='g')
    ax3.set_xlabel('Steps')
    ax3.set_ylabel('Precision')
    fig.savefig('precision-steps.png',dpi=1200)

    
    plt.legend()
    plt.show()


pr_plot(recall_path,precision_path)
