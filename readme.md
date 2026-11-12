## Blocking, single thread and multi thread

**Blocking:** a blocking call doesn't return until it has something for you.

**Single thread:** one line of execution.

**Multi thread:** multiple lines of execution.

Every program can be described on both axes, blocking and thread count.

| | Blocking calls | select |
|---|---|---|
| **Single thread** | It will wait on either the keyboard or the network. | It will check for both the keyboard and the network. |
| **Multi thread** | Each thread waits on its own thing. A network thread would wait, or a keyboard thread would wait. | It doesn't need to check, because it's already multi thread. There are already multiple threads, and if each thread has a blocking call, then it's fine. |