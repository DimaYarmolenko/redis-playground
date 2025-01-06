from enum import StrEnum


class EventType(StrEnum):
    PRODUCER_OUTPUT = "PRODUCER_OUTPUT"
    PROC_A_OUTPUT = "PROC_A_OUTPUT"
    PROC_B_OUTPUT = "PROC_B_OUTPUT"
