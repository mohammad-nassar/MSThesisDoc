-- Start of DDL Script for Table LRT.LRT_WORD_FREQUENCY
-- Generated 11-Jun-2020 17:01:16 from LRT@ORCLM

CREATE TABLE lrt_word_frequency
    (id                             NUMBER(9,0) NOT NULL,
    word                           VARCHAR2(100 BYTE) NOT NULL,
    frequency                      NUMBER(9,0) NOT NULL)
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





-- Triggers for LRT_WORD_FREQUENCY

CREATE OR REPLACE TRIGGER lrt_word_frequency_seq
 BEFORE
  INSERT
 ON lrt_word_frequency
REFERENCING NEW AS NEW OLD AS OLD
 FOR EACH ROW
BEGIN
  SELECT lrt_word_frequency_seq.nextval
  INTO :new.ID
  FROM dual;
END;
/


-- End of DDL Script for Table LRT.LRT_WORD_FREQUENCY

