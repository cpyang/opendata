SET DEFINE OFF
DROP TABLE CORP_TAX_REGISTRY;
CREATE TABLE CORP_TAX_REGISTRY
  (
    ADDRESS    VARCHAR2(128),
    EIN        NUMBER(10) NOT NULL,
    PARENT_EIN NUMBER(10),
    NAME       VARCHAR2(128),
    CAPITAL    NUMBER(15),
    EST_DATE   NUMBER(8),
    INV        CHAR(1),
    SIC1       NUMBER(8),
    SIC1_NAME  VARCHAR2(128),
    SIC2       NUMBER(8),
    SIC2_NAME  VARCHAR2(128),
    SIC3       NUMBER(8),
    SIC3_NAME  VARCHAR2(128),
    SIC4       NUMBER(8),
    SIC4_NAME  VARCHAR2(128)
  );
