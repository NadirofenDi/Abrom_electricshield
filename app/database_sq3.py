import sqlite3


modules = [
    ('0', 1, 'klemma_yellow'),
    ('1', 2, 'WB-MR6C v.2'),
    ('2', 3, 'WB-MRGBW-D'),
    ('3', 4, 'HTS-400-24-LS'),
    ('4', 5, 'klemma_6_wb-mr6c'),
    ('5', 6, 'klemma_4_wb-led'),
    ('6', 7, 'klemma_2_wb-mwac'),
    ('7', 8, 'WBIO-DO-R10A-8'),
    ('8', 9, 'klemma_8'),
    ('9', 10, 'power'),
    ('10', 11, 'klemma_4'),
    ('11', 12, 'QFs3-QFs(avtomat)'),
    ('12', 13, 'skat'),
    ('13', 14, 'controller'),
    ('14', 15, 'WBIO-DI-WD-14'),
    ('15', 16, 'avtomat'),
    ('16', 17, 'WB-MWAC')
]




with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS modules (file_name TEXT, module_id INT, module_name TEXT)""")
    db.execute("""CREATE TABLE IF NOT EXISTS modules_in_case (id INT, module_id INT, module_amount INT, row_id INT)""")

    # db.executemany("""INSERT INTO modules VALUES (?,?,?)""", modules)

