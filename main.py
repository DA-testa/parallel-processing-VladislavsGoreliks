# python3

def parallel_processing(n, m, data):
    output = []
    finish_times = [0] * n
    available_threads = list(range(n))

    for i in range(m):
        job_processing_time = data[i]
        if available_threads:
            thread_idx = available_threads.pop(0)
            start_time = finish_times[thread_idx]
            finish_time = start_time + job_processing_time
            finish_times[thread_idx] = finish_time
        else:
            next_finish_time = min(finish_times)
            thread_idx = finish_times.index(next_finish_time)
            start_time = next_finish_time
            finish_time = next_finish_time + job_processing_time
            finish_times[thread_idx] = finish_time
        output.append([thread_idx, start_time])

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread_idx, start_time in result:
        print(thread_idx, start_time)



if __name__ == "__main__":
    main()
