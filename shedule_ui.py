import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                             QTableWidgetItem, QPushButton, QMessageBox)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._connect_to_db()
        self.setWindowTitle("Editor")
        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)
        self._create_timetable_tab()
        self._create_teacher_tab()
        self._create_subject_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="schedulev3",
                                     user="postgres",
                                     password="privet",
                                     host="localhost",
                                     port="5432")
        self.cursor = self.conn.cursor()

    def _create_timetable_tab(self):
        self.timetable_tab = QWidget()
        self.tabs.addTab(self.timetable_tab, "Timetable")
        self.monday_gbox = QGroupBox("Monday")
        self.tuesday_gbox = QGroupBox("Tuesday")
        self.wednesday_gbox = QGroupBox("Wednesday")
        self.thursday_gbox = QGroupBox("Thursday")
        self.friday_gbox = QGroupBox("Friday")
        self.ttvbox = QVBoxLayout()
        self.tthbox1 = QHBoxLayout()
        self.tthbox2 = QHBoxLayout()
        self.ttvbox.addLayout(self.tthbox1)
        self.ttvbox.addLayout(self.tthbox2)
        self.tthbox1.addWidget(self.monday_gbox)
        self.tthbox1.addWidget(self.tuesday_gbox)
        self.tthbox1.addWidget(self.wednesday_gbox)
        self.tthbox1.addWidget(self.thursday_gbox)
        self.tthbox1.addWidget(self.friday_gbox)
        self._create_timetable_monday_table()
        self._create_timetable_tuesday_table()
        self._create_timetable_wednesday_table()
        self._create_timetable_thursday_table()
        self._create_timetable_friday_table()
        self.update_timetable_button = QPushButton("Update")
        self.tthbox2.addWidget(self.update_timetable_button)
        self.update_timetable_button.clicked.connect(self._update_timetable)
        self.timetable_tab.setLayout(self.ttvbox)


    def _create_teacher_tab(self):
        self.teacher_tab = QWidget()
        self.tabs.addTab(self.teacher_tab, "Teacher")
        self.teacher_gbox = QGroupBox("Teacher")
        self.tvbox = QVBoxLayout()
        self.thbox1 = QHBoxLayout()
        self.thbox2 = QHBoxLayout()
        self.tvbox.addLayout(self.thbox1)
        self.tvbox.addLayout(self.thbox2)
        self.thbox1.addWidget(self.teacher_gbox)
        self._create_teacher_table()
        self.update_teacher_button = QPushButton("Update")
        self.thbox2.addWidget(self.update_teacher_button)
        self.update_teacher_button.clicked.connect(self._update_teacher)
        self.teacher_tab.setLayout(self.tvbox)

    def _create_subject_tab(self):
        self.subject_tab = QWidget()
        self.tabs.addTab(self.subject_tab, "Subject")
        self.subject_gbox = QGroupBox("Subject")
        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.shbox1.addWidget(self.subject_gbox)
        self._create_subject_table()
        self.update_subject_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_subject_button)
        self.update_subject_button.clicked.connect(self._update_subject)
        self.subject_tab.setLayout(self.svbox)

    def _create_timetable_monday_table(self):
        self.timetable_monday_table = QTableWidget()
        self.timetable_monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_monday_table.setColumnCount(9)
        self._update_timetable_monday_table()
        self.ttmvbox = QVBoxLayout()
        self.ttmvbox.addWidget(self.timetable_monday_table)
        self.monday_gbox.setLayout(self.ttmvbox)

    def _create_timetable_tuesday_table(self):
        self.timetable_tuesday_table = QTableWidget()
        self.timetable_tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_tuesday_table.setColumnCount(9)
        self._update_timetable_tuesday_table()
        self.tttuvbox = QVBoxLayout()
        self.tttuvbox.addWidget(self.timetable_tuesday_table)
        self.tuesday_gbox.setLayout(self.tttuvbox)

    def _create_timetable_wednesday_table(self):
        self.timetable_wednesday_table = QTableWidget()
        self.timetable_wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_wednesday_table.setColumnCount(9)
        self._update_timetable_wednesday_table()
        self.ttwvbox = QVBoxLayout()
        self.ttwvbox.addWidget(self.timetable_wednesday_table)
        self.wednesday_gbox.setLayout(self.ttwvbox)

    def _create_timetable_thursday_table(self):
        self.timetable_thursday_table = QTableWidget()
        self.timetable_thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_thursday_table.setColumnCount(9)
        self._update_timetable_thursday_table()
        self.ttthvbox = QVBoxLayout()
        self.ttthvbox.addWidget(self.timetable_thursday_table)
        self.thursday_gbox.setLayout(self.ttthvbox)

    def _create_timetable_friday_table(self):
        self.timetable_friday_table = QTableWidget()
        self.timetable_friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_friday_table.setColumnCount(9)
        self._update_timetable_friday_table()
        self.ttfvbox = QVBoxLayout()
        self.ttfvbox.addWidget(self.timetable_friday_table)
        self.friday_gbox.setLayout(self.ttfvbox)

    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.teacher_table.setColumnCount(5)
        self._update_teacher_table()
        self.tvbox1 = QVBoxLayout()
        self.tvbox1.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.tvbox1)

    def _create_subject_table(self):
        self.subject_table = QTableWidget()
        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.subject_table.setColumnCount(3)
        self._update_subject_table()
        self.svbox1 = QVBoxLayout()
        self.svbox1.addWidget(self.subject_table)
        self.subject_gbox.setLayout(self.svbox1)

    def _update_timetable_monday_table(self):
        self.timetable_monday_table.clear()
        self.timetable_monday_table.setHorizontalHeaderLabels(["id", "day", "weektype", "subject", "teacher", "room_numb", "start_time", "", ""])
        self.cursor.execute("SELECT * FROM timetable WHERE day='Понедельник' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_monday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_monday_table.setItem(i, 0,
                                         QTableWidgetItem(str(r[0])))
            self.timetable_monday_table.setItem(i, 1,
                                         QTableWidgetItem(str(r[1])))
            self.timetable_monday_table.setItem(i, 2,
                                         QTableWidgetItem(str(r[2])))
            self.timetable_monday_table.setItem(i, 3,
                                         QTableWidgetItem(str(r[3])))
            self.timetable_monday_table.setItem(i, 4,
                                         QTableWidgetItem(str(r[4])))
            self.timetable_monday_table.setItem(i, 5,
                                         QTableWidgetItem(str(r[5])))
            self.timetable_monday_table.setItem(i, 6,
                                         QTableWidgetItem(str(r[6])))
            self.timetable_monday_table.setCellWidget(i, 7, joinButton)
            self.timetable_monday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_monday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_monday_table(num))
        #i+=1
        joinButton = QPushButton("Join")
        print(self.timetable_monday_table.rowCount())
        self.timetable_monday_table.setCellWidget(self.timetable_monday_table.rowCount()-1, 7, joinButton)
        joinButton.clicked.connect(lambda state,
                                          num=self.timetable_monday_table.rowCount()-1: self._add_record_to_timetable_monday_table(
            num))
        self.timetable_monday_table.resizeRowsToContents()

    def _update_timetable_tuesday_table(self):
        self.timetable_tuesday_table.clear()
        self.timetable_tuesday_table.setHorizontalHeaderLabels(["id", "day", "weektype", "subject", "teacher", "room_numb", "start_time", "", ""])
        self.cursor.execute("SELECT * FROM timetable WHERE day='Вторник' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_tuesday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_tuesday_table.setItem(i, 0,
                                         QTableWidgetItem(str(r[0])))
            self.timetable_tuesday_table.setItem(i, 1,
                                         QTableWidgetItem(str(r[1])))
            self.timetable_tuesday_table.setItem(i, 2,
                                         QTableWidgetItem(str(r[2])))
            self.timetable_tuesday_table.setItem(i, 3,
                                         QTableWidgetItem(str(r[3])))
            self.timetable_tuesday_table.setItem(i, 4,
                                         QTableWidgetItem(str(r[4])))
            self.timetable_tuesday_table.setItem(i, 5,
                                         QTableWidgetItem(str(r[5])))
            self.timetable_tuesday_table.setItem(i, 6,
                                         QTableWidgetItem(str(r[6])))
            self.timetable_tuesday_table.setCellWidget(i, 7, joinButton)
            self.timetable_tuesday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_tuesday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_tuesday_table(num))
        #i+=1
        joinButton = QPushButton("Join")
        self.timetable_tuesday_table.setCellWidget(self.timetable_tuesday_table.rowCount()-1, 7, joinButton)
        joinButton.clicked.connect(lambda state,
                                          num=self.timetable_tuesday_table.rowCount()-1: self._add_record_to_timetable_tuesday_table(
            num))
        self.timetable_tuesday_table.resizeRowsToContents()

    def _update_timetable_wednesday_table(self):
        self.timetable_wednesday_table.clear()
        self.timetable_wednesday_table.setHorizontalHeaderLabels(["id", "day", "weektype", "subject", "teacher", "room_numb", "start_time", "", ""])
        self.cursor.execute("SELECT * FROM timetable WHERE day='Среда' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_wednesday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_wednesday_table.setItem(i, 0,
                                         QTableWidgetItem(str(r[0])))
            self.timetable_wednesday_table.setItem(i, 1,
                                         QTableWidgetItem(str(r[1])))
            self.timetable_wednesday_table.setItem(i, 2,
                                         QTableWidgetItem(str(r[2])))
            self.timetable_wednesday_table.setItem(i, 3,
                                         QTableWidgetItem(str(r[3])))
            self.timetable_wednesday_table.setItem(i, 4,
                                         QTableWidgetItem(str(r[4])))
            self.timetable_wednesday_table.setItem(i, 5,
                                         QTableWidgetItem(str(r[5])))
            self.timetable_wednesday_table.setItem(i, 6,
                                         QTableWidgetItem(str(r[6])))
            self.timetable_wednesday_table.setCellWidget(i, 7, joinButton)
            self.timetable_wednesday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_wednesday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_wednesday_table(num))
        # i+=1
        joinButton = QPushButton("Join")
        self.timetable_wednesday_table.setCellWidget(self.timetable_wednesday_table.rowCount()-1, 7, joinButton)
        joinButton.clicked.connect(lambda state, num=self.timetable_wednesday_table.rowCount()-1: self._add_record_to_timetable_wednesday_table(num))
        self.timetable_wednesday_table.resizeRowsToContents()

    def _update_timetable_thursday_table(self):
        self.timetable_thursday_table.clear()
        self.timetable_thursday_table.setHorizontalHeaderLabels(["id", "day", "weektype", "subject", "teacher", "room_numb", "start_time", "", ""])
        self.cursor.execute("SELECT * FROM timetable WHERE day='Четверг' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_thursday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_thursday_table.setItem(i, 0,
                                         QTableWidgetItem(str(r[0])))
            self.timetable_thursday_table.setItem(i, 1,
                                         QTableWidgetItem(str(r[1])))
            self.timetable_thursday_table.setItem(i, 2,
                                         QTableWidgetItem(str(r[2])))
            self.timetable_thursday_table.setItem(i, 3,
                                         QTableWidgetItem(str(r[3])))
            self.timetable_thursday_table.setItem(i, 4,
                                         QTableWidgetItem(str(r[4])))
            self.timetable_thursday_table.setItem(i, 5,
                                         QTableWidgetItem(str(r[5])))
            self.timetable_thursday_table.setItem(i, 6,
                                         QTableWidgetItem(str(r[6])))
            self.timetable_thursday_table.setCellWidget(i, 7, joinButton)
            self.timetable_thursday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_thursday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_thursday_table(num))
        # i+=1
        joinButton = QPushButton("Join")
        self.timetable_thursday_table.setCellWidget(self.timetable_thursday_table.rowCount()-1, 7, joinButton)
        joinButton.clicked.connect(lambda state, num=self.timetable_thursday_table.rowCount()-1: self._add_record_to_timetable_thursday_table(num))
        self.timetable_thursday_table.resizeRowsToContents()

    def _update_timetable_friday_table(self):
        self.timetable_friday_table.clear()
        self.timetable_friday_table.setHorizontalHeaderLabels(["id", "day", "weektype", "subject", "teacher", "room_numb", "start_time", "", ""])
        self.cursor.execute("SELECT * FROM timetable WHERE day='Пятница' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_friday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_friday_table.setItem(i, 0,
                                         QTableWidgetItem(str(r[0])))
            self.timetable_friday_table.setItem(i, 1,
                                         QTableWidgetItem(str(r[1])))
            self.timetable_friday_table.setItem(i, 2,
                                         QTableWidgetItem(str(r[2])))
            self.timetable_friday_table.setItem(i, 3,
                                         QTableWidgetItem(str(r[3])))
            self.timetable_friday_table.setItem(i, 4,
                                         QTableWidgetItem(str(r[4])))
            self.timetable_friday_table.setItem(i, 5,
                                         QTableWidgetItem(str(r[5])))
            self.timetable_friday_table.setItem(i, 6,
                                         QTableWidgetItem(str(r[6])))
            self.timetable_friday_table.setCellWidget(i, 7, joinButton)
            self.timetable_friday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_friday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_friday_table(num))
        # i+=1
        joinButton = QPushButton("Join")
        self.timetable_friday_table.setCellWidget(self.timetable_friday_table.rowCount()-1, 7, joinButton)
        joinButton.clicked.connect(lambda state, num=self.timetable_friday_table.rowCount()-1: self._add_record_to_timetable_friday_table(num))
        self.timetable_friday_table.resizeRowsToContents()

    def _update_teacher_table(self):
        self.teacher_table.clear()
        self.teacher_table.setHorizontalHeaderLabels(["id", "full_name", "subject", "", ""])
        self.cursor.execute("SELECT * FROM teacher ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.teacher_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.teacher_table.setItem(i, 0,
                                         QTableWidgetItem(str(r[0])))
            self.teacher_table.setItem(i, 1,
                                         QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem(i, 2,
                                         QTableWidgetItem(str(r[2])))
            self.teacher_table.setCellWidget(i, 3, joinButton)
            self.teacher_table.setCellWidget(i, 4, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_teacher_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_teacher_table(num))
        #i+=1
        joinButton = QPushButton("Join")
        self.teacher_table.setCellWidget(self.teacher_table.rowCount()-1, 3, joinButton)
        joinButton.clicked.connect(
            lambda state, num=self.teacher_table.rowCount()-1: self._add_record_to_teacher_table(
                num))
        self.teacher_table.resizeRowsToContents()

    def _update_subject_table(self):
        self.subject_table.clear()
        self.subject_table.setHorizontalHeaderLabels(["name", "", ""])
        self.cursor.execute("SELECT * FROM subject;")
        records = list(self.cursor.fetchall())
        self.subject_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.subject_table.setItem(i, 0,
                                         QTableWidgetItem(str(r[0])))
            self.subject_table.setCellWidget(i, 1, joinButton)
            self.subject_table.setCellWidget(i, 2, deleteButton)
            joinButton.clicked.connect(lambda state, num=i, arg=str(r[0]): self._change_record_from_subject_table(num, arg))
            deleteButton.clicked.connect(lambda state, arg=str(r[0]): self._delete_record_from_subject_table(arg))
        #i+=1
        joinButton = QPushButton("Join")
        self.subject_table.setCellWidget(self.subject_table.rowCount()-1, 1, joinButton)
        joinButton.clicked.connect(
            lambda state, num=self.subject_table.rowCount()-1: self._add_record_to_subject_table(
                num))
        self.subject_table.resizeRowsToContents()

    def _add_record_to_timetable_monday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_monday_table.columnCount()-2):
            try:
                row.append(self.timetable_monday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("INSERT INTO timetable (day, weektype, subject, teacher, room_numb, start_time) VALUES (%s, %s, %s, %s, %s, %s)",
                                (row[1], row[2], row[3], row[4], row[5], row[6]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _add_record_to_timetable_tuesday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_tuesday_table.columnCount()-2):
            try:
                row.append(self.timetable_tuesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("INSERT INTO timetable (day, weektype, subject, teacher, room_numb, start_time) VALUES (%s, %s, %s, %s, %s, %s)",
                                (row[1], row[2], row[3], row[4], row[5], row[6]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _add_record_to_timetable_wednesday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_wednesday_table.columnCount()-2):
            try:
                row.append(self.timetable_wednesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("INSERT INTO timetable (day, weektype, subject, teacher, room_numb, start_time) VALUES (%s, %s, %s, %s, %s, %s)",
                                (row[1], row[2], row[3], row[4], row[5], row[6]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _add_record_to_timetable_thursday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_thursday_table.columnCount()-2):
            try:
                row.append(self.timetable_thursday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("INSERT INTO timetable (day, weektype, subject, teacher, room_numb, start_time) VALUES (%s, %s, %s, %s, %s, %s)",
                                (row[1], row[2], row[3], row[4], row[5], row[6]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _add_record_to_timetable_friday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_friday_table.columnCount()-2):
            try:
                row.append(self.timetable_friday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("INSERT INTO timetable (day, weektype, subject, teacher, room_numb, start_time) VALUES (%s, %s, %s, %s, %s, %s)",
                                (row[1], row[2], row[3], row[4], row[5], row[6]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _add_record_to_teacher_table(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()-2):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("INSERT INTO teacher (full_name, subject) VALUES (%s, %s)",
                                (row[1], row[2]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _add_record_to_subject_table(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount()-2):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        print(self.subject_table.item(rowNum, 0).text())
        try:
            self.cursor.execute("INSERT INTO subject VALUES (%s)",
                                ([self.subject_table.item(rowNum, 0).text()]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _change_record_from_timetable_monday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_monday_table.columnCount()-2):
            try:
                row.append(self.timetable_monday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, weektype=%s, subject=%s, teacher=%s, room_numb=%s, start_time=%s WHERE id=%s",
                                (row[1], row[2], row[3], row[4], row[5], row[6], row[0]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _change_record_from_timetable_tuesday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_tuesday_table.columnCount()-2):
            try:
                row.append(self.timetable_tuesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, weektype=%s, subject=%s, teacher=%s, room_numb=%s, start_time=%s WHERE id=%s",
                                (row[1], row[2], row[3], row[4], row[5], row[6], row[0]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _change_record_from_timetable_wednesday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_wednesday_table.columnCount()-2):
            try:
                row.append(self.timetable_wednesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, weektype=%s, subject=%s, teacher=%s, room_numb=%s, start_time=%s WHERE id=%s",
                                (row[1], row[2], row[3], row[4], row[5], row[6], row[0]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _change_record_from_timetable_thursday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_thursday_table.columnCount()-2):
            try:
                row.append(self.timetable_thursday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, weektype=%s, subject=%s, teacher=%s, room_numb=%s, start_time=%s WHERE id=%s",
                                (row[1], row[2], row[3], row[4], row[5], row[6], row[0]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _change_record_from_timetable_friday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_friday_table.columnCount()-2):
            try:
                row.append(self.timetable_friday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, weektype=%s, subject=%s, teacher=%s, room_numb=%s, start_time=%s WHERE id=%s",
                                (row[1], row[2], row[3], row[4], row[5], row[6], row[0]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _change_record_from_teacher_table(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()-2):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE teacher SET full_name=%s, subject=%s WHERE id=%s",
                                (row[1], row[2], row[0]))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _change_record_from_subject_table(self, rowNum, arg):
        row = list()
        for i in range(self.subject_table.columnCount()-2):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE subject SET name=%s WHERE name=%s",
                                (row[0], arg))
        except psycopg2.errors.ForeignKeyViolation:
            QMessageBox.about(self, "Error", "Foreign key is not present in table")
            self.cursor.execute("ROLLBACK")
            return
        self.conn.commit()

    def _delete_record_from_timetable_monday_table(self, rowNum):
        row = self.timetable_monday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_timetable_tuesday_table(self, rowNum):
        row = self.timetable_tuesday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_timetable_wednesday_table(self, rowNum):
        row = self.timetable_wednesday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_timetable_thursday_table(self, rowNum):
        row = self.timetable_thursday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_timetable_friday_table(self, rowNum):
        row = self.timetable_friday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_teacher_table(self, rowNum):
        row = self.teacher_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM teacher WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_subject_table(self, arg):
        self.cursor.execute("DELETE FROM subject WHERE name=%s", [arg])
        self.conn.commit()

    def _update_timetable(self):
        self._update_timetable_monday_table()
        self._update_timetable_tuesday_table()
        self._update_timetable_wednesday_table()
        self._update_timetable_thursday_table()
        self._update_timetable_friday_table()

    def _update_teacher(self):
        self._update_teacher_table()

    def _update_subject(self):
        self._update_subject_table()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
