import concurrent.futures
import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        return list(executor.map(factorize, numbers))

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    # Measure the execution time of the synchronous version
    start_time = time.time()
    results_sync = factorize(numbers)
    end_time = time.time()
    print("Synchronous version took {:.4f} seconds".format(end_time - start_time))

    # Measure the execution time of the parallel version
    start_time = time.time()
    results_parallel = factorize_parallel(numbers)
    end_time = time.time()
    print("Parallel version took {:.4f} seconds".format(end_time - start_time))

    print("Result of the synchronous version:")
    for result in results_sync:
        print(result)

    print("Result of the parallel version:")
    for result in results_parallel:
        print(result)
