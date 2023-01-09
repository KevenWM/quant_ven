from base64 import encode
import re
import fitz
import pandas as pd
import pathlib

# Abre o documento

links_pdf = ['output\CVM358_1023.pdf',
             'output\CVM358_14206.pdf',
             'output\CVM358_14451.pdf',
             'output\CVM358_26174.pdf',
             'output\CVM358_26069.pdf',
             'output\CVM358_11258.pdf',
             'output\CVM358_15423.pdf',
             'output\CVM358_24406.pdf',
             'output\CVM358_22594.pdf',
             'output\CVM358_18589.pdf',
             'output\CVM358_20990.pdf',
             'output\CVM358_15253.pdf',
             'output\CVM358_21733.pdf',
             'output\CVM358_15539.pdf',
             'output\CVM358_24660.pdf',
             'output\CVM358_15709.pdf',
             'output\CVM358_15741.pdf',
             'output\CVM358_17949.pdf',
             'output\CVM358_25577.pdf',
             'output\CVM358_6041.pdf',
             'output\CVM358_25160.pdf',
             'output\CVM358_19186.pdf',
             'output\CVM358_16292.pdf',
             'output\CVM358_20044.pdf',
             'output\CVM358_23000.pdf',
             'output\CVM358_18708.pdf',
             'output\CVM358_16551.pdf',
             'output\CVM358_16527.pdf',
             'output\CVM358_16659.pdf',
             'output\CVM358_16632.pdf',
             'output\CVM358_26050.pdf',
             'output\CVM358_20443.pdf',
             'output\CVM358_24813.pdf',
             'output\CVM358_16985.pdf',
             'output\CVM358_16993.pdf',
             'output\CVM358_17485.pdf',
             'output\CVM358_20800.pdf',
             'output\CVM358_24910.pdf',
             'output\CVM358_24872.pdf',
             'output\CVM358_18414.pdf',
             'output\CVM358_17450.pdf',
             'output\CVM358_24929.pdf',
             'output\CVM358_18660.pdf',
             'output\CVM358_17329.pdf',
             'output\CVM358_17930.pdf',
             'output\CVM358_20397.pdf',
             'output\CVM358_17671.pdf',
             'output\CVM358_25496.pdf',
             'output\CVM358_17922.pdf',
             'output\CVM358_17892.pdf',
             'output\CVM358_17973.pdf',
             'output\CVM358_18821.pdf',
             'output\CVM358_22454.pdf',
             'output\CVM358_20575.pdf',
             'output\CVM358_21431.pdf',
             'output\CVM358_20478.pdf',
             'output\CVM358_18376.pdf',
             'output\CVM358_18376.pdf',
             'output\CVM358_19330.pdf',
             'output\CVM358_20010.pdf',
             'output\CVM358_25780.pdf',
             'output\CVM358_19879.pdf',
             'output\CVM358_19879.pdf',
             'output\CVM358_14605.pdf',
             'output\CVM358_18775.pdf',
             # 'output\CVM358_18759.pdf',
             'output\CVM358_26093.pdf',
             'output\CVM358_18724.pdf',
             'output\CVM358_20788.pdf',
             'output\CVM358_18953.pdf',
             'output\CVM358_19763.pdf',
             'output\CVM358_19100.pdf',
             'output\CVM358_22799.pdf',
             'output\CVM358_19453.pdf',
             'output\CVM358_19275.pdf',
             'output\CVM358_24015.pdf',
             'output\CVM358_26808.pdf',
             'output\CVM358_24740.pdf',
             'output\CVM358_21237.pdf',
             'output\CVM358_21555.pdf',
             'output\CVM358_21555.pdf',
             'output\CVM358_24945.pdf',
             'output\CVM358_19305.pdf',
             'output\CVM358_20613.pdf',
             'output\CVM358_18309.pdf',
             'output\CVM358_922.pdf',
             'output\CVM358_922.pdf',
             'output\CVM358_1171.pdf',
             'output\CVM358_26166.pdf',
             'output\CVM358_23221.pdf',
             'output\CVM358_24708.pdf',
             'output\CVM358_24392.pdf',
             'output\CVM358_26301.pdf',
             'output\CVM358_26387.pdf',
             'output\CVM358_22357.pdf',
             'output\CVM358_25895.pdf',
             'output\CVM358_24821.pdf',
             'output\CVM358_25372.pdf',
             'output\CVM358_19569.pdf',
             'output\CVM358_16608.pdf',
             'output\CVM358_25410.pdf',
             'output\CVM358_22608.pdf',
             'output\CVM358_19909.pdf',
             'output\CVM358_19925.pdf',
             'output\CVM358_23981.pdf',
             'output\CVM358_23531.pdf',
             'output\CVM358_14869.pdf',
             'output\CVM358_19720.pdf',
             'output\CVM358_20338.pdf',
             'output\CVM358_1228.pdf',
             'output\CVM358_24864.pdf',
             'output\CVM358_25003.pdf',
             'output\CVM358_23965.pdf',
             'output\CVM358_23264.pdf',
             'output\CVM358_24260.pdf',
             'output\CVM358_20036.pdf',
             'output\CVM358_26425.pdf',
             'output\CVM358_20087.pdf',
             'output\CVM358_26557.pdf',
             'output\CVM358_20966.pdf',
             'output\CVM358_26158.pdf',
             'output\CVM358_20982.pdf',
             'output\CVM358_20630.pdf',
             'output\CVM358_26697.pdf',
             'output\CVM358_80187.pdf',
             'output\CVM358_80020.pdf',
             'output\CVM358_80020.pdf',
             'output\CVM358_24473.pdf',
             'output\CVM358_20257.pdf',
             'output\CVM358_24902.pdf',
             'output\CVM358_20435.pdf',
             'output\CVM358_20370.pdf',
             'output\CVM358_23175.pdf',
             'output\CVM358_26026.pdf',
             'output\CVM358_26590.pdf',
             'output\CVM358_20605.pdf',
             'output\CVM358_20770.pdf',
             'output\CVM358_26522.pdf',
             'output\CVM358_18139.pdf',
             'output\CVM358_20915.pdf',
             'output\CVM358_21490.pdf',
             'output\CVM358_26603.pdf',
             'output\CVM358_4669.pdf',
             'output\CVM358_11215.pdf',
             'output\CVM358_20540.pdf',
             'output\CVM358_20648.pdf',
             'output\CVM358_21636.pdf',
             'output\CVM358_21636.pdf',
             'output\CVM358_21636.pdf',
             'output\CVM358_24546.pdf',
             'output\CVM358_21180.pdf',
             'output\CVM358_21008.pdf',
             'output\CVM358_25224.pdf',
             'output\CVM358_23930.pdf',
             'output\CVM358_23612.pdf',
             'output\CVM358_25100.pdf',
             'output\CVM358_21040.pdf',
             'output\CVM358_21016.pdf',
             'output\CVM358_21130.pdf',
             'output\CVM358_21903.pdf',
             'output\CVM358_25585.pdf',
             'output\CVM358_23493.pdf',
             'output\CVM358_23272.pdf',
             'output\CVM358_25500.pdf',
             'output\CVM358_25348.pdf',
             'output\CVM358_22225.pdf',
             'output\CVM358_21938.pdf',
             'output\CVM358_21342.pdf',
             'output\CVM358_25534.pdf',
             'output\CVM358_4685.pdf',
             'output\CVM358_25798.pdf',
             'output\CVM358_25712.pdf',
             'output\CVM358_25976.pdf',
             'output\CVM358_23248.pdf',
             'output\CVM358_22519.pdf',
             'output\CVM358_24112.pdf',
             'output\CVM358_21610.pdf',
             'output\CVM358_25569.pdf',
             'output\CVM358_26271.pdf',
             'output\CVM358_24279.pdf',
             'output\CVM358_25399.pdf',
             'output\CVM358_22691.pdf',
             'output\CVM358_22691.pdf',
             'output\CVM358_22691.pdf',
             'output\CVM358_23680.pdf',
             'output\CVM358_23671.pdf',
             'output\CVM358_25011.pdf',
             'output\CVM358_26921.pdf',
             'output\CVM358_22179.pdf',
             'output\CVM358_26140.pdf',
             'output\CVM358_23329.pdf',
             'output\CVM358_22268.pdf',
             'output\CVM358_25437.pdf',
             'output\CVM358_22187.pdf',
             'output\CVM358_25860.pdf',
             'output\CVM358_23310.pdf',
             'output\CVM358_25704.pdf',
             'output\CVM358_14362.pdf',
             'output\CVM358_22411.pdf',
             'output\CVM358_24350.pdf',
             'output\CVM358_23604.pdf',
             'output\CVM358_25550.pdf',
             'output\CVM358_25550.pdf',
             'output\CVM358_22365.pdf',
             # 'output\CVM358_22217.pdf',
             # 'output\CVM358_22217.pdf',
             'output\CVM358_25135.pdf',
             'output\CVM358_22497.pdf',
             'output\CVM358_21067.pdf',
             'output\CVM358_25291.pdf',
             'output\CVM358_26123.pdf',
             'output\CVM358_25046.pdf',
             'output\CVM358_25119.pdf',
             'output\CVM358_25682.pdf',
             'output\CVM358_22977.pdf',
             'output\CVM358_25283.pdf',
             'output\CVM358_24961.pdf',
             'output\CVM358_22675.pdf',
             'output\CVM358_1120.pdf',
             'output\CVM358_1120.pdf',
             'output\CVM358_18996.pdf',
             'output\CVM358_24694.pdf',
             'output\CVM358_25879.pdf',
             'output\CVM358_22586.pdf',
             'output\CVM358_24996.pdf',
             'output\CVM358_24317.pdf',
             'output\CVM358_26379.pdf',
             'output\CVM358_26379.pdf',
             'output\CVM358_25232.pdf',
             'output\CVM358_25887.pdf',
             'output\CVM358_25518.pdf',
             'output\CVM358_25402.pdf',
             'output\CVM358_12696.pdf',
             'output\CVM358_23620.pdf',
             'output\CVM358_80152.pdf',
             'output\CVM358_26638.pdf',
             'output\CVM358_14524.pdf',
             'output\CVM358_3069.pdf',
             'output\CVM358_3115.pdf',
             'output\CVM358_5576.pdf',
             'output\CVM358_23582.pdf',
             'output\CVM358_13986.pdf',
             'output\CVM358_22349.pdf',
             'output\CVM358_21350.pdf',
             'output\CVM358_19739.pdf',
             'output\CVM358_25690.pdf',
             'output\CVM358_25275.pdf',
             'output\CVM358_25259.pdf',
             'output\CVM358_2453.pdf',
             'output\CVM358_4782.pdf',
             'output\CVM358_9954.pdf',
             'output\CVM358_3891.pdf',
             'output\CVM358_1325.pdf',
             'output\CVM358_4707.pdf',
             'output\CVM358_23370.pdf',
             'output\CVM358_3077.pdf',
             'output\CVM358_19445.pdf',
             'output\CVM358_23574.pdf',
             'output\CVM358_23159.pdf',
             'output\CVM358_26760.pdf',
             'output\CVM358_26336.pdf',
             'output\CVM358_25836.pdf',
             'output\CVM358_25089.pdf',
             'output\CVM358_25933.pdf',
             'output\CVM358_24236.pdf',
             'output\CVM358_26565.pdf',
             'output\CVM358_23884.pdf',
             'output\CVM358_24090.pdf',
             'output\CVM358_25909.pdf',
             'output\CVM358_24155.pdf',
             'output\CVM358_3271.pdf',
             'output\CVM358_26085.pdf',
             'output\CVM358_25330.pdf',
             'output\CVM358_23507.pdf',
             'output\CVM358_26417.pdf',
             'output\CVM358_25658.pdf',
             'output\CVM358_4081.pdf',
             'output\CVM358_23825.pdf',
             'output\CVM358_25127.pdf',
             'output\CVM358_24139.pdf',
             'output\CVM358_20621.pdf',
             'output\CVM358_23795.pdf',
             'output\CVM358_25305.pdf',
             'output\CVM358_24716.pdf',
             'output\CVM358_24716.pdf',
             'output\CVM358_26689.pdf',
             'output\CVM358_25070.pdf',
             'output\CVM358_24830.pdf',
             'output\CVM358_80209.pdf',
             'output\CVM358_26204.pdf',
             'output\CVM358_15300.pdf',
             'output\CVM358_25186.pdf',
             'output\CVM358_26280.pdf',
             'output\CVM358_26816.pdf',
             'output\CVM358_26077.pdf',
             'output\CVM358_25062.pdf',
             'output\CVM358_25445.pdf',
             'output\CVM358_24341.pdf',
             'output\CVM358_24457.pdf',
             'output\CVM358_22012.pdf',
             'output\CVM358_24481.pdf',
             'output\CVM358_1155.pdf',
             'output\CVM358_1155.pdf',
             'output\CVM358_15342.pdf',
             'output\CVM358_20958.pdf',
             'output\CVM358_24589.pdf',
             'output\CVM358_26620.pdf',
             'output\CVM358_24422.pdf',
             'output\CVM358_24430.pdf',
             'output\CVM358_13781.pdf',
             'output\CVM358_22985.pdf',
             'output\CVM358_21121.pdf',
             'output\CVM358_22616.pdf',
             'output\CVM358_13366.pdf',
             'output\CVM358_25755.pdf',
             'output\CVM358_25461.pdf',
             'output\CVM358_25810.pdf',
             'output\CVM358_26409.pdf',
             'output\CVM358_21202.pdf',
             'output\CVM358_24783.pdf',
             # 'output\CVM358_9512.pdf',
             'output\CVM358_7811.pdf',
             'output\CVM358_8540.pdf',
             'output\CVM358_6505.pdf',
             'output\CVM358_4030.pdf',
             'output\CVM358_3050.pdf',
             'output\CVM358_3824.pdf',
             'output\CVM358_8893.pdf',
             'output\CVM358_20028.pdf',
             'output\CVM358_26247.pdf',
             'output\CVM358_11070.pdf',
             'output\CVM358_18465.pdf',
             'output\CVM358_24180.pdf',
             'output\CVM358_9989.pdf',
             'output\CVM358_25917.pdf',
             'output\CVM358_11231.pdf',
             'output\CVM358_26484.pdf',
             'output\CVM358_4170.pdf',
             # 'output\CVM358_3980.pdf',
             'output\CVM358_24805.pdf',
             'output\CVM358_11592.pdf',
             'output\CVM358_1309.pdf',
             'output\CVM358_24295.pdf',
             'output\CVM358_26581.pdf',
             'output\CVM358_23302.pdf',
             'output\CVM358_26948.pdf',
             'output\CVM358_26875.pdf',
             'output\CVM358_23817.pdf',
             'output\CVM358_25640.pdf',
             'output\CVM358_26328.pdf',
             'output\CVM358_80195.pdf',
             'output\CVM358_25747.pdf',
             'output\CVM358_26832.pdf',
             'output\CVM358_26930.pdf',
             'output\CVM358_17850.pdf',
             'output\CVM358_26530.pdf',
             'output\CVM358_25674.pdf',
             'output\CVM358_26000.pdf',
             'output\CVM358_26905.pdf',
             'output\CVM358_4820.pdf',
             'output\CVM358_20710.pdf',
             'output\CVM358_23590.pdf',
             'output\CVM358_26727.pdf',
             'output\CVM358_26441.pdf',
             'output\CVM358_80217.pdf',
             'output\CVM358_24058.pdf',
             'output\CVM358_25631.pdf',
             'output\CVM358_20524.pdf',
             'output\CVM358_14443.pdf',
             'output\CVM358_26506.pdf',
             'output\CVM358_26913.pdf',
             'output\CVM358_24848.pdf',
             'output\CVM358_25763.pdf',
             'output\CVM358_20346.pdf',
             'output\CVM358_701.pdf',
             'output\CVM358_16241.pdf',
             'output\CVM358_14826.pdf',
             'output\CVM358_19640.pdf',
             'output\CVM358_22470.pdf',
             'output\CVM358_20877.pdf',
             'output\CVM358_21440.pdf',
             'output\CVM358_12190.pdf',
             'output\CVM358_19836.pdf',
             'output\CVM358_11762.pdf',
             'output\CVM358_21334.pdf',
             'output\CVM358_20516.pdf',
             'output\CVM358_13471.pdf',
             'output\CVM358_22020.pdf',
             'output\CVM358_19992.pdf',
             'output\CVM358_14850.pdf',
             'output\CVM358_5770.pdf',
             'output\CVM358_7510.pdf',
             'output\CVM358_20125.pdf',
             'output\CVM358_24627.pdf',
             'output\CVM358_21199.pdf',
             'output\CVM358_25208.pdf',
             'output\CVM358_26034.pdf',
             'output\CVM358_13447.pdf',
             'output\CVM358_9393.pdf',
             'output\CVM358_8036.pdf',
             'output\CVM358_8575.pdf',
             'output\CVM358_10472.pdf',
             'output\CVM358_24953.pdf',
             'output\CVM358_8672.pdf',
             'output\CVM358_12319.pdf',
             'output\CVM358_9067.pdf',
             'output\CVM358_906.pdf',
             'output\CVM358_1384.pdf',
             'output\CVM358_21881.pdf',
             'output\CVM358_1520.pdf',
             'output\CVM358_19348.pdf',
             'output\CVM358_14320.pdf',
             'output\CVM358_8397.pdf',
             'output\CVM358_16306.pdf',
             'output\CVM358_10456.pdf',
             'output\CVM358_5762.pdf',
             'output\CVM358_5762.pdf',
             'output\CVM358_11932.pdf',
             'output\CVM358_24600.pdf',
             'output\CVM358_22055.pdf',
             'output\CVM358_26700.pdf',
             'output\CVM358_11975.pdf',
             'output\CVM358_25984.pdf',
             'output\CVM358_19623.pdf',
             'output\CVM358_7617.pdf',
             'output\CVM358_3190.pdf',
             'output\CVM358_5258.pdf',
             'output\CVM358_14176.pdf',
             'output\CVM358_15636.pdf',
             'output\CVM358_20567.pdf',
             'output\CVM358_20567.pdf',
             'output\CVM358_21466.pdf',
             'output\CVM358_25526.pdf',
             'output\CVM358_24228.pdf',
             'output\CVM358_14214.pdf',
             'output\CVM358_20451.pdf',
             'output\CVM358_20702.pdf',
             'output\CVM358_20931.pdf',
             'output\CVM358_21148.pdf',
             'output\CVM358_19550.pdf',
             'output\CVM358_14460.pdf',
             'output\CVM358_24171.pdf',
             'output\CVM358_23280.pdf',
             'output\CVM358_14311.pdf',
             'output\CVM358_14311.pdf',
             'output\CVM358_18627.pdf',
             'output\CVM358_11312.pdf',
             'output\CVM358_8605.pdf',
             'output\CVM358_26786.pdf',
             'output\CVM358_20362.pdf',
             'output\CVM358_26395.pdf',
             'output\CVM358_16861.pdf',
             'output\CVM358_4146.pdf',
             'output\CVM358_25453.pdf',
             'output\CVM358_7544.pdf',
             'output\CVM358_13773.pdf',
             'output\CVM358_2461.pdf',
             'output\CVM358_5410.pdf',
             'output\CVM358_6343.pdf',
             'output\CVM358_5207.pdf',
             'output\CVM358_11991.pdf',
             'output\CVM358_26255.pdf',
             'output\CVM358_14664.pdf',
             'output\CVM358_8753.pdf',
             'output\CVM358_19658.pdf',
             'output\CVM358_10561.pdf',
             'output\CVM358_3298.pdf',
             'output\CVM358_6211.pdf',
             'output\CVM358_6211.pdf',
             'output\CVM358_5312.pdf',
             'output\CVM358_8451.pdf',
             'output\CVM358_8451.pdf',
             'output\CVM358_9539.pdf',
             'output\CVM358_14109.pdf',
             'output\CVM358_20745.pdf',
             'output\CVM358_20060.pdf',
             'output\CVM358_12653.pdf',
             'output\CVM358_19615.pdf',
             'output\CVM358_13765.pdf',
             'output\CVM358_20532.pdf',
             'output\CVM358_22780.pdf',
             'output\CVM358_12572.pdf',
             'output\CVM358_6076.pdf',
             'output\CVM358_7870.pdf',
             'output\CVM358_4537.pdf',
             'output\CVM358_8192.pdf',
             'output\CVM358_9342.pdf',
             # 'output\CVM358_8656.pdf',
             'output\CVM358_94.pdf',
             'output\CVM358_1210.pdf',
             'output\CVM358_3204.pdf',
             'output\CVM358_6629.pdf',
             'output\CVM358_8133.pdf',
             'output\CVM358_6173.pdf',
             'output\CVM358_2429.pdf',
             'output\CVM358_2429.pdf',
             'output\CVM358_25950.pdf',
             'output\CVM358_25143.pdf',
             'output\CVM358_25038.pdf',
             'output\CVM358_4693.pdf',
             'output\CVM358_21091.pdf',
             'output\CVM358_21091.pdf', ]


# Criando lista que vai armazenar os valores

export_result = {'Code': [], 'Data': [], 'Empresa': [], 'Membro': [],
                 'Ativo': [], 'Qnt. Inicial': [], 'Qnt. Final': [], 'Saldo': []}

for file_path in (links_pdf):

    # Separando o código do arquivo
    code = file_path.split('_')
    code = code[1].split('.')
    code = code[0]

    print(code)

    # file_path = "output/CVM358_11258.pdf"
    pdf = fitz.open(file_path)

    # Conta o número de páginas e definindo texto consolidados
    pages = pdf.page_count

    full_doc = ""

    # Consolida as páginas em 1 texto e acha nome da empresa
    for i in range(pages):

        page = pdf.load_page(i)

        text = page.get_text('text').strip()

        full_doc = full_doc + text

    full_doc.encode('utf-8', 'ignore')
    full_doc = full_doc.encode('latin-1', 'replace').decode('latin-1')

    # Definir ranges dos nomes (companhia ou controladora)
    inicio_nome = [m.start() for m in re.finditer('Denominação da', full_doc)]
    fim_nome = [m.start() for m in re.finditer(
        'Grupo e Pessoas', full_doc)]

    # Definir ranges de posição consolidado

    position_inicial = [m.start()
                        for m in re.finditer('Saldo Inicial', full_doc)]

    forms_cons = [m.start()
                  for m in re.finditer('FORMULÁRIO CONSOLIDADO', full_doc)]

    # Definir ranges das movimentações (compras e vendas)
    inicial_mov = [m.start()
                   for m in re.finditer('Movimentações no Mês', full_doc)]
    final_mov = [m.start() for m in re.finditer('Saldo Final', full_doc)]

    # Tipo de membro que está operando

    range_membros_inicio = [m.start()
                            for m in re.finditer('Grupo e Pessoas', full_doc)]
    range_membros_fim = [m.start()
                         for m in re.finditer('Saldo Inicial', full_doc)]

    # Achando a data do documento

    range_data_i = [m.start()
                    for m in re.finditer('Em', full_doc)]

    data = full_doc[range_data_i[0]:range_data_i[0]+11].strip().split(" ")
    data = data[1]

    # Lista que irá remover palavras
    remove_pos_in = ["Saldo Inicial",
                     "Valor Mobiliário Derivativo",
                     "Características dos Títulos",
                     "Quantidade", "Saldo Final",
                     "Dados da reapresentação:",
                     "RECEBIVEIS IMOBILIARIOS",
                     "CRI BSCS COD 13H0098728",
                     "10 EMISSAO SERIE UNICA",
                     "2A SERIE DA 6A EMISSAO",
                     "LIQUIDACAO FINANCEIRA",
                     "MRSL17 – 7 EMISSAO DE",
                     "DIREITO DE SUBSCRICAO",
                     "MRSL17 ? 7 EMISSAO DE",
                     "1 ACAO ORDINARIA E 04",
                     "BONDS CUSIP 71647NAA7",
                     "AO AUMENTO DE CAPITAL",
                     "CONVERSIVEIS EM ACOES",
                     "1 ACAO ORDINARIA E 4",
                     "9 EMISSAO – 1 SERIE ",
                     "SWAP REFERENCIADO EM",
                     "COTAS CERTIFICADO DE",
                     "CERT REC AGRONEGOCIO",
                     "ACOES PREFERENCIAIS",
                     "ACOES PREFREENCIAIS",
                     "OPCOES DE COMPRA DE",
                     "7 EMISSAO ? 1 SERIE",
                     "7 EMISSAO – 1 SERIE",
                     "9 EMISSAO ? 1 SERIE",
                     '9 EMISSAO ? 2 SERIE',
                     "9 EMISSAO – 2 SERIE",
                     "DEVELOPMENT LIMITED",
                     "PETR 45 4A SERIE 5A",
                     "COTA FGTS PETROBRAS",
                     "FORWARD DE ACOES PN",
                     "BONUS DECORRENTE DE",
                     "AMERICAN DEPOSITARY",
                     "PLANO DE OUTORGA DE",
                     "DEBENTURES PRIVADA",
                     "ACOES PREFRENCIAIS",
                     "ACOES PREFERENCIAS",
                     "DEBENTURES 1 SERIE",
                     "SUBSCRICAO PRIVADA",
                     "OPCOES DE VENDA DE",
                     "AUMENTO DE CAPITAL",
                     "VANTAGEM ADICIONAL",
                     "TOTAL RETURN SWAPS",
                     "PLANOS DE OPCAO DE",
                     "9 EMISSAO 2 SERIE",
                     "DERIVATIVO EQUITY",
                     "1 EMISSAO 2 SERIE",
                     "01 ORDINARIAS E 4",
                     "1 EMISSAO 1 SERIE",
                     "7 EMISSAO 2 SERIE",
                     "SOBRAS AUMENTO DE",
                     "INARIA E 4 ACOES",
                     "3 EMISSAO IVPR13",
                     "ACOES ORDINARIAS",
                     " REFERENCIADO EM",
                     "PETROBRAS GLOBAL",
                     "OPCAO DE COMPRA",
                     "CRA CRA0150000M",
                     "CRA CRA0150000O",
                     "OPCOES DE ACOES",
                     "PARTICIPACAO EM",
                     "ESTATE PROPERTY",
                     "PLANOS DE OPCAO",
                     "PLANO DE OUTORG",
                     "DM 2829 BIDI12",
                     "DERIVATIVO COM",
                     "CERTIFICADO DE",
                     "1 E 2 EMISSOES",
                     "CRI 13H0098728",
                     "CRI 13J0119974",
                     "NOTES 01172027",
                     "PREFERENCIAIS",
                     "ADMINISTRADOR",
                     "DATA DE POSSE",
                     "ADR ORDINARIA",
                     "DE 2 EMISSAO",
                     "DE 1 EMISSAO",
                     "2 EMISSAO DE",
                     "CONVERSIVEIS",
                     "1 ON E 2 PN",
                     "CRA0150000O",
                     "CRA0150000M",
                     "10A EMISSAO",
                     "11A EMISSAO",
                     "12A EMISSAO",
                     "13A EMISSAO",
                     "ADR ORD PBR",
                     "RCA27112018",
                     "SIMPLES NAO",
                     "22 EMISSAO",
                     "ENTRADA DE",
                     "13H0098728",
                     "13J0119974",
                     "13J0119975",
                     "14J0045610",
                     "DEBENTURES",
                     "RCA27112018"
                     "1A EMISSAO",
                     "2A EMISSAO",
                     "3A EMISSAO",
                     "4A EMISSAO",
                     "5A EMISSAO",
                     "6A EMISSAO",
                     "7A EMISSAO",
                     "8A EMISSAO",
                     "9A EMISSAO",
                     "COTA FUNDO",
                     "COMPRA SOP",
                     "8 EMISSAO",
                     "5 EMISSAO",
                     "2 EMISSAO",
                     "1 EMISSAO",
                     "3 EMISSAO",
                     "4 EMISSAO",
                     "ORDINARIA",
                     "COTA FGTS",
                     "SELECIONE",
                     "PETROBRAS",
                     "SINTETICA",
                     "POSSE DE",
                     "0150000M",
                     "0150000O",
                     "ADR PREF",
                     "CAPITAL",
                     "CRA JSL",
                     "1  E 2 ",
                     "ABEVF13",
                     "ABEVF42",
                     "PETR 28",
                     "PETR 17",
                     "PETR 27",
                     "PETR 45",
                     "EMISSAO",
                     "1  E 2",
                     "RDNT15",
                     "TAEE11",
                     "TAEE26",
                     "TAEEC2",
                     "VLID11",
                     "EQUITY",
                     "TASA17",
                     "TASA15",
                     "TASA13",
                     "FJTA13",
                     "FJTA15",
                     "FJTA17",
                     "FJTA11",
                     "SHARES",
                     "HYPE3",
                     "ACOES",
                     "POSSE",
                     "PETR4",
                     "UNITS",
                     "SWAP",
                     "PNR",
                     "PNA",
                     "PNB",
                     "PNC",
                     "CRA",
                     "CRI",
                     "CDB",
                     "JSL",
                     "ADR",
                     "USD",
                     "ON",
                     "PN",
                     " ",
                     ]

    # Salvando nomes

    for i in range(len(inicial_mov)):

        nome = full_doc[inicio_nome[i]:fim_nome[i]].strip().split(':')
        nome = nome[1].strip()

        range_membros = full_doc[range_membros_inicio[i]:range_membros_fim[i]].strip()
        range_pos_inicial = full_doc[position_inicial[i]:inicial_mov[i]].strip()

        # test se tem "FORMULÁRIO"
        if len(forms_cons) < i+2:
            form_location = final_mov[i] + 310
        else:
            form_location = forms_cons[i+1]

        range_pos_final = full_doc[final_mov[i]:form_location].strip()

        for remov in (remove_pos_in):
            range_pos_inicial = range_pos_inicial.replace(remov, "").strip()
            range_pos_final = range_pos_final.replace(remov, "").strip()

        # transformando string em lista - Inicial
        range_pos_inicial = range_pos_inicial.split('/')
        range_pos_inicial = str(range_pos_inicial[0]).split('\n')

        # transformando string em lista - Final
        range_pos_final = range_pos_final.split('/')
        range_pos_final = str(range_pos_final[0]).split('\n')

        # FILTRA EMPRTY ELEMENTS
        range_pos_inicial = list(filter(None, range_pos_inicial))
        range_pos_final = list(filter(None, range_pos_final))

        # Achando quem comprou (membro)

        position_x = range_membros.find("X")
        range_membros = range_membros[position_x:].strip().replace(
            "(", "").split(")")

        limp_dir = range_membros[1].strip()
        limp_dir = limp_dir.split("ria")
        limp_dir = str(limp_dir[0].strip())

        # Nome do ativo
        # print(len(range_pos_inicial))
        # Identifica o tipo de ativo

        if not range_pos_inicial:

            qnt_inicial = 0
            qnt_final = 0
            nome_ativo = str("None")

        else:

            if len(range_pos_inicial) <= 2:

                # TEM 2 ELEMENTOS

                if range_pos_inicial[0] == "Ações":
                    qnt_inicial = range_pos_inicial[1]
                    qnt_final = range_pos_final[1]
                    nome_ativo = str(range_pos_inicial[0])
                elif range_pos_inicial[0] == "Outros":
                    qnt_inicial = 0
                    qnt_final = 0
                    nome_ativo = str(range_pos_inicial[0])
                elif range_pos_inicial[0] == "Debêntures":
                    qnt_inicial = 0
                    qnt_final = 0
                    nome_ativo = str(range_pos_inicial[0])
                else:
                    qnt_inicial = range_pos_inicial[1]
                    qnt_final = range_pos_final[1]
                    nome_ativo = str(range_pos_inicial[0])

                export_result['Code'].append(code)
                export_result['Data'].append(data)
                export_result['Empresa'].append(nome)
                export_result['Membro'].append(limp_dir)
                export_result['Ativo'].append(nome_ativo)
                export_result['Qnt. Inicial'].append(qnt_inicial)
                export_result['Qnt. Final'].append(qnt_final)
                export_result['Saldo'].append("0")

            else:
                # TEM MAIS TE 2 ELEMENTOS

                size_pos = int((len(range_pos_inicial)/2))

                add_name = 0
                add_pos = 1

                for sss in range(size_pos):

                    y1_pos = sss+add_pos
                    y2_name = sss+add_name

                    qnt_inicial = range_pos_inicial[y1_pos]
                    qnt_final = range_pos_final[y1_pos]
                    nome_ativo = str(range_pos_inicial[y2_name])

                    add_pos = add_pos + 1
                    add_name = add_name + 1

                    # if nome_ativo == "Outros":
                    #    qnt_inicial = 0
                    #    qnt_final = 0
                    # elif nome_ativo == "Debêntures":
                    #    qnt_inicial = 0
                    #    qnt_final = 0

                    export_result['Code'].append(code)
                    export_result['Data'].append(data)
                    export_result['Empresa'].append(nome)
                    export_result['Membro'].append(limp_dir)
                    export_result['Ativo'].append(nome_ativo)
                    export_result['Qnt. Inicial'].append(qnt_inicial)
                    export_result['Qnt. Final'].append(qnt_final)
                    export_result['Saldo'].append("0")


# EXPORTAR PARA CSV

df = pd.DataFrame(export_result)
path = str(pathlib.Path().resolve())

df.to_csv(path + '/consolidado_cvm_julho.csv',
          encoding="latin-1", sep=',', index=None)
