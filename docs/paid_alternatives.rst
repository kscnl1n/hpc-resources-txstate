Paid Alternatives
=================

Companies like Lambda labs, Coreweave, and others offer HPC/GPU cluster access via contract or 
subscription (often used for AI/ML workloads). These aren't traditional academic "allocations" 
but researchers with grant funding can budget for them if appropriate for research tasks.

Common Research Compute Providers
-----------------------------------

1. Cloud Hyperscalers
^^^^^^^^^^^^^^^^^^^^^
The most common path is using cloud hyperscalers like Amazon Web Services, Microsoft Azure, or 
Google Cloud Platform. These let you spin up full HPC clusters on demand, complete with schedulers 
like Slurm, GPU nodes, high-speed networking, and parallel storage.

**Examples include:**
- `Amazon Web Services (AWS HPC + ParallelCluster) <https://aws.amazon.com/hpc/>`_
- `Microsoft Azure (CycleCloud / Azure Batch) <https://azure.microsoft.com/en-us/solutions/high-performance-computing/>`_
- `Google Cloud Platform (HPC VM + Slurm setups) <https://cloud.google.com/hpc>`_
- `Oracle Cloud Infrastructure (RDMA + bare metal HPC) <https://www.oracle.com/cloud/hpc/>`_

If you need more nodes or GPUs, you just scale up and pay for it. For AI workloads, 
large simulations, or data pipelines, this is usually the most widely-used, flexible, and realistic option.

2. HPC-as-a-Service Providers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you don’t want to deal with setting up and managing clusters yourself, there are HPC-as-a-service 
platforms like Rescale or IBM Cloud. These sit on top of cloud providers like AWS and abstract away most of 
the infrastructure work. Instead of configuring networking, schedulers, and environments, you just 
submit jobs through a web interface or API. They often come with preconfigured software stacks for 
things like CFD, genomics, or machine learning, which makes them especially useful if your research 
group doesn’t have deep HPC experience but still needs large compute.

**Proivders:**

- `Rescale <https://rescale.com/>`_
- `IBM Cloud <https://www.ibm.com/cloud/high-performance-computing>`_
- `AceCloud <https://acecloud.ai/>`_

3. Enterprise Hybrid HPC Providers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Depending on your institution's partnerships, you may have access to enterprise HPC providers that
can build on-premise clusters or hybrid cloud solutions. Companies like Dell, HPE, and Lenovo offer
HPC hardware and services, and they often have partnerships with universities to provide research computing
resources.

Check with your department to see which resources are available to you.
