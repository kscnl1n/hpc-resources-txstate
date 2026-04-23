What is HPC?
============

High-Performance Computing (HPC) systems are **powerful, interconnected computing systems.**

Instead of relying on a single processor, HPC systems combine thousands of CPUs and often GPUs 
across many nodes, connected by high-speed networks, to perform calculations in parallel. 
HPC environments typically include specialized hardware, large shared memory resources, 
high-performance storage systems, and job schedulers (such as Slurm ) that efficiently distribute
tasks across the cluster. 

While a standard desktop machine might only have one CPU, HPC systems' multi-core parallelism 
allows them to solve much more complicated problems than standard desktop machines. Some HPC 
systems are so large they take up `entire rooms! <https://tacc.utexas.edu/systems/frontera/>`_

**Benefits to Your Research**
------------------------------
The primary benefit(s) to using HPC systems to run computing tasks are:

 ● **Faster processing speeds**
Faster compute fundamentally changes how quickly researchers can iterate on ideas. 
In fields like transcriptomics, RNA-seq pipelines using tools such as STAR and DESeq2 
can process hundreds of samples in hours instead of days, allowing scientists to test 
multiple hypotheses about gene expression in a single day. In climate science, models 
like WRF can simulate atmospheric conditions much faster, enabling rapid analysis of 
extreme weather scenarios.

 ● **Larger data input handling**
HPC systems allow researchers to work with complete datasets rather than relying on smaller samples. 
In genomics and transcriptomics, this means analyzing entire sequencing datasets, improving the ability 
to detect rare mutations or subtle gene expression changes. In astronomy, researchers can process full 
datasets from observatories like the Vera C. Rubin Observatory, enabling discovery of faint or short-lived 
cosmic events that might otherwise be missed.

 ● **Higher-resolution modeling**
 Access to high-memory nodes enables entirely new classes of problems to be tackled.

 ● **Larger memory capacity**
More nodes and more memory allow for larger models and more complex simulations.

 ● **Improved reproducibility through standardized software environments**
HPC systems support reproducibility by providing consistent, shareable environments for running experiments.
Containerization methods like **Apptainer** make it easy to ensure analysis pipelines can be reliably reproduced
across different HPC systems, even as software dependencies evolve.

 ● **Allows access to scientific software stacks (ex: MPI, OpenMP, Cuda, etc.)**
HPC environments provide access to powerful parallel and GPU-accelerated tools that are essential for 
modern research. For example, in physics, distributed computing with MPI allows simulations of large-scale systems, 
such as particle interactions or cosmological evolution, across thousands of nodes.

Together, these capabilities expand not just the speed of research, but the scope,
allowing researchers to ask more complex questions, use richer datasets, and produce more accurate 
and impactful results.

How to Access HPC Resources
---------------------------
Many HPC centers dedicated to scientific research provide free compute time on their systems 
through **allocation-based systems** where researchers can apply for storage space and compute 
time. HPC systems can be ranked from small to incredibly large. 

Although even small, departmental-based clusters are typically enough for independent research tasks, 
HPC systems can typically be ranked in power as follows: 

Tier Example Comparison 
------------------------

 ● **Departmental Cluster**, ex: Small lab HPC - Smaller - (100-2,000 cores) 

 ● **University Production Cluster**, ex: LEAP2 (Texas State), AGES (Texas A&M) - Strong (2,000-20,00 0 cores) 

 ● **National Academic HPC**, ex: Stampede3 (TACC), Perlmutter (NERSC) - Larger (50,000-300, 000 cores) 

 ● **Leadership-Class**, ex: Frontera / Frontier (TACC) - Much larger (300,000-millions of cores)
