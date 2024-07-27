#!/usr/bin/env python3
#Student ID = ssachdeva25

class Time:
    
    def __init__(self, hour=12, minute=0, second=0):
        
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
   
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def valid_time(t):
   
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
    return None

def time_to_sec(t):
    
    return t.hour * 3600 + t.minute * 60 + t.second

def sec_to_time(seconds):
   
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    second = seconds % 60
    return Time(hour, minute, second)
