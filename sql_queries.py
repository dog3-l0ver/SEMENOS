class Queries:
    BatteryTableCreator = """CREATE TABLE IF NOT EXISTS battery(
                                id integer PRIMARY_KEY,
                                model text NOT NULL,
                                remaining_power integer NOT NULL,
                                timestamp text NOT NULL
                            )"""

    CoilTableCreator = """CREATE TABLE IF NOT EXISTS coil(
                            id integer PRIMARY_KEY,
                            model text NOT NULL
                        )"""

    PuffTableCreator = """CREATE TABLE IF NOT EXISTS puff(
                            id integer PRIMARY_KEY,
                            timestamp text NOT NULL,
                            puff_time real NOT NULL,
                            current_power real NOT NULL,
                            current_resistance real NOT NULL
                        )"""