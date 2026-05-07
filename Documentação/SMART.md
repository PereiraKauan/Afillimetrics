# Analise SMART  


**Data:** 02/05/2026


## O que é o método SMART?


| Critério | Significado | Pergunta |
|----------|-------------|----------|
| **S** | Específico | O que de fato será feito? |
| **M** | Mensurável | Como o progresso é medido? |
| **A** | Atingível | O que fazer para alcançar a meta? |
| **R** | Relevante | De que maneira contribui para o projeto? |
| **T** | Temporal | Quando será realizado? Qual o prazo? |



---



## VIABILIDADE OPERACIONAL

### Objetivo 1 – Dashboard de Controle Financeiro

| Critério | Descrição |
|----------|-----------|
| **S** | Implementar dashboard principal com exibição de vendas, comissões, links ativos, taxa de conversão, metas financeiras e semáforo colorido. |
| **M** | Dashboard deve carregar em até 3 segundos (RNF02). Gráficos devem ser interativos. Semáforo deve mudar de cor com base na meta. |
| **A** | Buscar dados via API com cache no front-end. Utilizar React Query para otimizar requisições. Gráficos com Chart.js. Indicadores com Styled Components. |
| **R** | Permitir que o afiliado visualize seu desempenho em tempo real, identifique produtos mais lucrativos e tome decisões estratégicas. |
| **T** | Dashboard finalizado e testado em até 3 meses. |

**Descrição:**  
Será implementada uma tela principal (dashboard) que reunirá todas as métricas importantes para o afiliado em um só lugar. O dashboard exibirá o total de vendas, o valor de comissões recebidas, a quantidade de links ativos, a taxa de conversão e um semáforo financeiro (verde, amarelo, vermelho) que indica se o afiliado está atingindo suas metas.



---



### Objetivo 2 – Segurança e Conformidade com a LGPD

| Critério | Descrição |
|----------|-----------|
| **S** | Implementar medidas de segurança para proteger dados pessoais dos afiliados e seus clientes, garantindo conformidade com a LGPD. |
| **M** | 100% das senhas devem ser armazenadas. 100% das comunicações devem usar HTTPS. O sistema deve permitir exportar e excluir dados do usuário. |
| **A** | Utilizar ferramentas para proteção de senhas, HTTPS com certificado SSL/TLS. |
| **R** | Evitar multas, proteger a imagem do sistema, e garantir confiança dos afiliados. |
| **T** | Medidas implementadas até a data de lançamento do sistema. |

**Descrição:**  

