# 636 Exclusive Time of Functions

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        exec_times = [0] * n

        call_stack = []

        prev_start_time = 0

        for log in logs:
            func_id, call_type, timestamp = log.split(":")

            func_id = int(func_id)
            timestamp = int(timestamp)

            if call_type == "start":
                if call_stack:
                    exec_times[call_stack[-1]] += timestamp - prev_start_time
                
                call_stack.append(func_id)
                prev_start_time = timestamp
            else:
                exec_times[call_stack.pop()] += timestamp - prev_start_time + 1
                prev_start_time = timestamp + 1
        
        return exec_times
        