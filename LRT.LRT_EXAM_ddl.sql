-- Start of DDL Script for Table LRT.LRT_EXAM
-- Generated 11-Jun-2020 16:59:48 from LRT@ORCLM

CREATE TABLE lrt_exam
    (exam_id                        NUMBER DEFAULT 1 ,
    age                            NUMBER(2,0),
    gender                         CHAR(1 BYTE),
    score                          FLOAT(126),
    native                         CHAR(1 BYTE),
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





-- Constraints for LRT_EXAM

ALTER TABLE lrt_exam
ADD CONSTRAINT lrt_exam_pk PRIMARY KEY (exam_id)
USING INDEX
  PCTFREE     10
  INITRANS    2
  MAXTRANS    255
  TABLESPACE  users
  STORAGE   (
    INITIAL     65536
    NEXT        1048576
    MINEXTENTS  1
    MAXEXTENTS  2147483645
  )
/


-- Triggers for LRT_EXAM

CREATE OR REPLACE TRIGGER lrt_exam_trg
 BEFORE
  INSERT
 ON lrt_exam
REFERENCING NEW AS NEW OLD AS OLD
 FOR EACH ROW
BEGIN
  SELECT lrt_exam_seq.nextval
  INTO :new.student_id
  FROM dual;
END;
/


-- End of DDL Script for Table LRT.LRT_EXAM

