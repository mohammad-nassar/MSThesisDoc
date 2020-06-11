-- Start of DDL Script for Table LRT.LRT_NONWORDS
-- Generated 11-Jun-2020 17:01:01 from LRT@ORCLM

CREATE TABLE lrt_nonwords
    (id                             NUMBER(9,0),
    word_id                        NUMBER(9,0),
    non_word                       VARCHAR2(100 BYTE),
    type                           NUMBER(*,0),
    replace_char_index             NUMBER(*,0),
    replaced_char                  VARCHAR2(10 BYTE),
    prefix                         VARCHAR2(80 BYTE),
    original_char                  VARCHAR2(10 BYTE),
    postfix                        VARCHAR2(80 BYTE),
    itime                          DATE DEFAULT sysdate,
    is_nonword                     VARCHAR2(5 BYTE))
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





-- Triggers for LRT_NONWORDS

CREATE OR REPLACE TRIGGER lrt_nonwords_trg
 BEFORE
  INSERT
 ON lrt_nonwords
REFERENCING NEW AS NEW OLD AS OLD
 FOR EACH ROW
BEGIN
  SELECT lrt_nonwords_seq.nextval
  INTO :new.ID
  FROM dual;
END;
/


-- End of DDL Script for Table LRT.LRT_NONWORDS

