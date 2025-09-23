import pyopencl as cl
import numpy as np
import os
class OPENCL_TAG:
    def __init__(self, tag_name):
        if os.getenv("OPENCL_TAG") is not None:
            platform = cl.get_platforms()[0]
            device = platform.get_devices()[0]
            self.context = cl.Context([device])
            self.queue = cl.CommandQueue(self.context)
            # Step 2: Create a user event
            self.user_event = cl.UserEvent(self.context)
            # Step 3: Set the user event status to complete
            self.user_event.set_status(cl.command_execution_status.COMPLETE)
            # Step 4: Create a simple kernel
            program_source = "__kernel void " + tag_name + "(__global float* data) { data[0] += 1.0f; }"
            program = cl.Program(self.context, program_source).build(cache_dir=os.getcwd())
            self.kernel = getattr(program, tag_name)
            #self.kernel = program.dummy1111111
    def tag(self):
        if os.getenv("OPENCL_TAG") is not None:
            # Step 5: Create buffer and set kernel argument
            data = np.array([0.0], dtype=np.float32)
            buffer = cl.Buffer(self.context, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=data)
            self.kernel.set_arg(0, buffer)
            global_size = (1,)
            # Step 6: Enqueue kernel with user event as dependency
            event = cl.enqueue_nd_range_kernel(self.queue, self.kernel, global_size, None, wait_for=[self.user_event])
            event.wait()

