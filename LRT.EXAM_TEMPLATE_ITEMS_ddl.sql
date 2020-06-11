-- Start of DDL Script for Table LRT.EXAM_TEMPLATE_ITEMS
-- Generated 11-Jun-2020 16:54:55 from LRT@ORCLM

CREATE TABLE exam_template_items
    (temp_id                        NUMBER,
    id                             NUMBER(9,0),
    word_id                        NUMBER(9,0),
    non_word                       VARCHAR2(100 BYTE),
    type                           NUMBER)
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





-- End of DDL Script for Table LRT.EXAM_TEMPLATE_ITEMS

