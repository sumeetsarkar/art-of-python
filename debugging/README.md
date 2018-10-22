# Python Debugging

Python debugging can be accomplished by one of the following ways. Some of which are terminal based, whilst some of them being GUI based. However each of these provide pdb to interact and query objects

1. pdb / breakpoint()
2. pudb
3. web_pdb
4. vscode

<br/>

## pdb

```python
# Set up a breakpoint
import pdb; pdb.set_trace()

# Since python 3.7 onwards,
# instead of wrtiting the cumbersome import pdb; pdb.set_trace(),
# one can simply use the breakpoint()
breakpoint()
```

However, with usage of breakpoint(), there is a neat little trick, using PYTHONBREAKPOINT=0 breakpoint() calls can be skipped.

    PYTHONBREAKPOINT=0 python3 <your-script>.py

![pdb debugging screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/debugging/media/pdb.png)


<br/>
<br/>

## pudb

    $ pip install pudb

```python
# Set up a breakpoint
import pudb; pudb.set_trace()
```
![pudb debugging screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/debugging/media/pudb.png)


<br/>
<br/>

## web_pdb  (GUI based)

    $ pip install web-pdb

```python
# Set up a breakpoint
import web_pdb; web_pdb.set_trace()

# OR, use breakpoint() using PYTHONBREAKPOINT
# PYTHONBREAKPOINT='web_pdb.set_trace' python3 debug_web_pdb.py
breakpoint()

# Once code hits the breakpoint
# Open http://localhost:5555
```

    PYTHONBREAKPOINT='web_pdb.set_trace' python3 <your-script>.py

![web_pdb debugging screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/debugging/media/web_pdb.png)


<br/>
<br/>

## vscode  (GUI based)

[Download vscode](https://code.visualstudio.com/Download)

Set code breakpoint in VSCode editor GUI

Run the program in debug mode (F5)

![vscode debugging screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/debugging/media/vscode.png)
