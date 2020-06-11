-- Start of DDL Script for Table LRT.LRT_10_GRAM
-- Generated 1/28/2020 9:50:08 PM from LRT@ORCLM

CREATE TABLE lrt_10_gram
    (seq_id                         NUMBER(9,0) NOT NULL,
    gram                           VARCHAR2(30 BYTE) NOT NULL,
    attribute_1                    VARCHAR2(20 BYTE),
    attribute_2                    VARCHAR2(20 BYTE),
    attribute_3                    VARCHAR2(20 BYTE),
    attribute_4                    VARCHAR2(20 BYTE),
    attribute_5                    VARCHAR2(20 BYTE))
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





-- Triggers for LRT_10_GRAM

CREATE OR REPLACE TRIGGER word_10_grm_trg
 BEFORE
  INSERT
 ON lrt_10_gram
REFERENCING NEW AS NEW OLD AS OLD
 FOR EACH ROW
BEGIN
  SELECT lrt_10_gram_seq.nextval
  INTO :new.gram
  FROM dual;
END;
/


-- End of DDL Script for Table LRT.LRT_10_GRAM

