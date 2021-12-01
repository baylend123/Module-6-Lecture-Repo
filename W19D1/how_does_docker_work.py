'''
How does Docker work?
Part 1: Your Computer
In order to understand Docker, we should first discuss
how our computers work to begin with.

Your computer has physical hardware, 
an OS, and a kernel that interfaces between the two, 
which are all tightly coupled.

When we build & deploy apps with this environment, 
we are limited to the performance of our machine 
and the libraries that are compatible with it.
'''

'''
How does Docker work?
Part 2: Why not use a VM?
A VM has an OS that is decoupled from your 
computer’s hardware. With VMs, can have multiple OSs 
running on a computer.

A VM has a kernel & hypervisor. The kernel interfaces 
between the hardware and the OS. The hypervisor creates 
& runs a VM.

A VM is heavy - we often don’t need an entirely separate 
kernel & hypervisor just for the purposes of deploying 
an application.
'''

'''

How does Docker work?
Part 3: Docker containers
A Docker container is like a mini-VM that is hardware 
agnostic - it doesn’t care about the host OS.

It is lightweight - it consists only of a small Linux 
distribution and necessary libraries & resources. 
It does not have its own kernel or hypervisor.

This makes it much more scalable and allows us 
to run many more containers on one machine than VMs.

'''