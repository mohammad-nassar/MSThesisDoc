-- Start of DDL Script for Table LRT.LRT_CORPUS
-- Generated 1/28/2020 9:52:50 PM from LRT@ORCLM

CREATE TABLE lrt_corpus
    (word_seq                       NUMBER NOT NULL,
    word                           VARCHAR2(80 BYTE) NOT NULL,
    is_diacritized                 CHAR(1 BYTE) DEFAULT 'N' NOT NULL,
    is_valid                       CHAR(1 BYTE) DEFAULT 'Y' NOT NULL,
    itime                          DATE DEFAULT SYSDATE NOT NULL,
    attribute_1                    CHAR(1 BYTE),
    attribute_2                    CHAR(1 BYTE),
    attribute_3                    CHAR(1 BYTE),
    attribute_4                    CHAR(1 BYTE),
    attribute_5                    CHAR(1 BYTE),
    attribute_6                    CHAR(1 BYTE),
    attribute_7                    CHAR(1 BYTE),
    attribute_8                    CHAR(1 BYTE),
    attribute_9                    CHAR(1 BYTE),
    attribute_10                   CHAR(1 BYTE))
  SEGMENT CREATION IMMEDIATE
  PCTFREE     10
  INITRANS    1
  MAXTRANS    255
  TABLESPACE  users
  STORAGE   (
    INITIAL     65536
    NEXT        1048576
    MINEXTENTS  1
    MAXEXTENTS  2147483645
  )
  NOCACHE
  MONITORING
  NOPARALLEL
  LOGGING
/





-- Triggers for LRT_CORPUS

CREATE OR REPLACE TRIGGER word_seq_trg
 BEFORE
  INSERT
 ON lrt_corpus
REFERENCING NEW AS NEW OLD AS OLD
 FOR EACH ROW
BEGIN
  SELECT lrt_word_seq.nextval
  INTO :new.WORD_SEQ
  FROM dual;
END;
/


-- End of DDL Script for Table LRT.LRT_CORPUS

