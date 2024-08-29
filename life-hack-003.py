import torch
import subprocess
import time
import logging

# Takes about 8GB
ndim = 25_000
logging.basicConfig(format='[%(asctime)s] %(filename)s [%(levelname).1s] %(message)s', level=logging.DEBUG)

def get_gpu_usage(gpu_index=1):
    command = f"nvidia-smi -i {gpu_index} --query-gpu=memory.total,memory.used,memory.free --format=csv,noheader,nounits"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")
    mem_total, mem_used, mem_free = map(lambda x: int(x.strip()), lines[0].split(","))
    logging.info(f"GPU {gpu_index} Stats: Total: {mem_total}, Free: {mem_free} Used: {mem_used}")
    return mem_used / mem_free

def run_dummy_job():
    start = time.time()
    random1 = torch.randn([ndim, ndim]).to("cuda:1")
    random2 = torch.randn([ndim, ndim]).to("cuda:1")
    while time.time() - start < 0.5 * 60:
        random1 = random1 * random2
        random2 = random2 * random1
    del random1, random2
    torch.cuda.empty_cache()

def main():
    while True:
        usage = get_gpu_usage()
        logging.info(f"Initial GPU usage: {usage}")
        run_dummy_job()
        usage = get_gpu_usage()
        logging.info(f"Final GPU usage: {usage}")
        time.sleep(5)  # Sleep for 5 seconds before running the job again

if __name__ == "__main__":
    main()
