# Emotion-Detection---SemEval-2025-Task-11
Este repositório foi criado para participar da Task 11 do SemEval 2025, que aborda a detecção de emoções percebidas em texto. O objetivo é explorar como as emoções são expressas e percebidas em diferentes contextos culturais e linguísticos, preenchendo lacunas nos métodos atuais de detecção de emoções baseados em texto.


## Baseline
Executando a baseline em português na track A temos os seguintes resultados:

- SEM ADICIONAR PESO NAS CLASSES
MICRO recall: 0.358, precision: 0.5415, f1: 0.431
MACRO recall: 0.2, precision: 0.1083, f1: 0.1405

Micro: Calcula as métricas considerando todas as instâncias igualmente.
Macro: Calcula as métricas para cada classe individualmente e depois faz a média.

o observado para as classes individualmente é que o modelo "chuta" para as classes menos frequentes no dataset

- ADICIONANDO PESO AS CLASSES:

MICRO recall: 0.7232, precision: 0.4329, f1: 0.5416<br>
MACRO recall: 0.6047, precision: 0.3711, f1: 0.4571


