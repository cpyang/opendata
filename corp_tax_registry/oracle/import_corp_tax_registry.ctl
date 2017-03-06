load data CHARACTERSET AL32UTF8
infile 'corp_tax_registry.csv' "str '\n'"
append
into table CORP_TAX_REGISTRY
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( ADDRESS CHAR(4000),
             EIN CHAR(4000),
             PARENT_EIN CHAR(4000),
             NAME CHAR(4000),
             CAPITAL CHAR(4000),
             EST_DATE CHAR(4000),
             INV CHAR(4000),
             SIC1 CHAR(4000),
             SIC1_NAME CHAR(4000),
             SIC2 CHAR(4000),
             SIC2_NAME CHAR(4000),
             SIC3 CHAR(4000),
             SIC3_NAME CHAR(4000),
             SIC4 CHAR(4000),
             SIC4_NAME CHAR(4000)
           )
