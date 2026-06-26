
import argparse, hashlib, json, time, multiprocessing

def hash_bytes(algo, data):
    h = hashlib.new(algo)
    h.update(data)
    return h.digest()

def worker(start, step, msg, difficulty, algo, stop, q):
    target = 1 << (len(hash_bytes(algo,b""))*8 - difficulty)
    nonce = start
    checked = 0
    t0 = time.time()
    while not stop.is_set():
        d = f"{nonce}{msg}".encode()
        dg = hash_bytes(algo,d)
        checked += 1
        if int.from_bytes(dg,"big") < target:
            stop.set()
            q.put((nonce,dg.hex(),checked,time.time()-t0))
            return
        nonce += step

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--message",default="Hello Blockchain")
    ap.add_argument("--difficulty",type=int,default=20)
    ap.add_argument("--algorithm",default="sha256",
                    choices=hashlib.algorithms_guaranteed)
    ap.add_argument("--workers",type=int,default=multiprocessing.cpu_count())
    ap.add_argument("--output",default="result.json")
    args=ap.parse_args()
    stop=multiprocessing.Event()
    q=multiprocessing.Queue()
    procs=[]
    t=time.time()
    for i in range(args.workers):
        p=multiprocessing.Process(target=worker,args=(i,args.workers,args.message,args.difficulty,args.algorithm,stop,q))
        p.start(); procs.append(p)
    nonce,hx,checked,elapsed=q.get()
    total=time.time()-t
    for p in procs: p.join(timeout=0.2)
    res={
      "message":args.message,
      "difficulty":args.difficulty,
      "algorithm":args.algorithm,
      "nonce":nonce,
      "hash":hx,
      "elapsed_seconds":total,
      "approx_hash_rate": checked/max(elapsed,1e-9)*args.workers
    }
    with open(args.output,"w") as f: json.dump(res,f,indent=2)
    print(json.dumps(res,indent=2))

if __name__=="__main__":
    main()
