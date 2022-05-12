import pandas as pd


class _DBManager:

    @staticmethod
    def _selectDB(db_path: str, keyword=None, _id=None) -> list:
        df = pd.read_csv(db_path)
        rows = df.to_numpy().tolist()
        if _id:
            _id_row: list = []
            for row in rows:
                if _id == row[0]:
                    _id_row = row
            return _id_row
        if keyword:
            keyword_rows = []
            for row in rows:
                for idx, attr in enumerate(row):
                    if idx == 0: continue
                    if keyword in str(attr):
                        keyword_rows.append(row)
                        break
            rows = keyword_rows
        return rows

    @staticmethod
    def _insertDB(data: object, db_path: str) -> int:
        df = pd.read_csv(db_path, index_col='id')
        row = []
        for k, v in data.__dict__.items():
            row.append(v)
        _id = row.pop(0)
        df.loc[_id] = row
        df.to_csv(db_path)
        return _id

    @staticmethod
    def _updateDB(data: object, db_path: str, _id: int) -> bool:
        rows = pd.read_csv(db_path).to_numpy().tolist()
        flag = False
        for i, v in enumerate(rows):
            if v[0] == _id:
                flag = True
                break
        if flag:
            df = pd.read_csv(db_path, index_col='id')
            row = []
            for k, v in data.__dict__.items():
                row.append(v)
            row.pop(0)
            df.loc[_id] = row  # type: ignore
            df.to_csv(db_path)
            return True
        else:
            return False

    @staticmethod
    def _deleteDB(db_path: str, _id: int) -> bool:
        df = pd.read_csv(db_path, index_col='id')
        try:
            df = df.drop(_id)
            df.to_csv(db_path)
            return True
        except Exception as e:
            return False
