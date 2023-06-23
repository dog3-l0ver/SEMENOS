class Queries:
    CurrentPuffTableCreator = """CREATE TABLE IF NOT EXISTS current_puff(
                                id integer PRIMARY_KEY,
                                date text NOT NULL,
                                voltage real NOT NULL,
                                current real NOT NULL,
                                temperature real NOT NULL,
                                puff_length real NOT NULL
                            )"""

    PuffsTableCreator = """CREATE TABLE IF NOT EXISTS puffs(
                                    id integer PRIMARY_KEY,
                                    time_sum real NOT NULL,
                                    puff_count integer NOT NULL
                                )"""
