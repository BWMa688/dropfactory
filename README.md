> This repository is associated to the paper "A soft matter discovery robot driven by child-like curiosity" by Jonathan Grizou, Laurie J. Points, Abhishek Sharma and Leroy Cronin. A draft version of the paper is [available on Chemarxiv](https://chemrxiv.org/articles/A_Closed_Loop_Discovery_Robot_Driven_by_a_Curiosity_Algorithm_Discovers_Proto-Cells_That_Show_Complex_and_Emergent_Behaviours/6958334) and a brief overview of the scientific approach can be found at https://croningp.github.io/tutorial_icdl_epirob_2017/.

# Dropfactory

Dropfactory is a robotic platform able to perform and record oil-in-water droplet experiments at a large scale.

![Dropfactory](media/gif/dropfactory.gif)

[[Dropfactory Cycle Video]](https://www.youtube.com/watch?v=o8ZTkoZ-j6M)

Dropfactory is capable of running, in total autonomy, an arbitrary droplet experiment lasting 1min30sec every 1min50sec. We routinely performed more than 350 Experiments per working day on this platform. This enabled us to explore the efficiency of exploration and optimization algorithms directly on our physicochemical system, that is directly sampling the real world.

Here is an example of droplet behaviors:

![Droplets](media/gif/droplets.gif)

[[Droplet Compilation Video]](https://www.youtube.com/watch?v=ysEswhRS5CQ)

## Principles

The platform is organized as a little factory, enabling us to fully parallelize all required operations (mixing, droplet placing, recording, cleaning, drying). An oil-in-water experiment consists of placing small oil droplets (made from an arbitrary mixture of oils) at the surface of an aqueous medium (made from a mixture of aqueous phases), we then need to video record the droplet movements to later analyse them.

To be able to run continuously such experiments, the platform must be able to mix, sample, clean and dry both oils and aqueous phases. Previous designs had to do all such steps in sequence, Dropfactory does them in parallel thanks to its design around two geneva wheel mechanisms.

![Diagram](media/diagram/dropfactory.png)

This design allows to move the oil vials and the petri dish at specialized working stations, rather than having the tools move to those containers. As a result, Dropfactory is:

- **robust**, because there are much less moving parts. Each working station can perform only its specific task at the location it was designed to work. This means less tubing moving around.
- **easier to maintain**, because all working stations are clearly separated, both physically and digitally, identifying a bug or a mechanical failure is quick and fixing them is easier.
- **fast**, because while an oil mixture is prepared, a previous one is being cleaned, another three are being dried, another is sampled by a syringe to be placed on a previously filled petri dish. At the same time, another petri dish is being filled, one is being cleaned, three are drying, and one contains droplets and is being recorded under a camera.

Dropfactory enables to record 1 experiment of 1min30sec every 1min50sec, gaining a factor of 6 versus our previous sequential platform. Thanks to its robustness, the platform was consistently running for months in the lab collecting more than 30,000 droplet experiments.

## Repository Organization

A detailed README is available for all folders:

- [doc](doc) folder is the place to start, it explains the logic behind all choices done in Dropfactory and contains the links to the corresponding files
- [software](software) folder holds all the python code to control and send jobs to the platform
- [hardware](hardware) folder holds all the 3D files designed for Dropfactory as well as many links to source its components.
- [media](media) folder contains some useful images and video links of the platform

This repository contains only the hardware and software used to build and operate Dropfactory. It is complemented by:

- [dropfactory_exploration](https://github.com/croningp/dropfactory_exploration) for the algorithms that use the dropfactory platform as a means to sample the real world.
- [dropfactory_analysis](https://github.com/croningp/dropfactory_analysis) for all the analysis and display of the results of our various droplets experiments and algorithms comparison.

## Author

Design and code by [Jonathan Grizou](http://jgrizou.com/) while working in the [CroninGroup](http://www.chem.gla.ac.uk/cronin/).

Thanks to Vasilis Duros and Graham Keenan for proofreading the documentation.

## License

[![GPL V3](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl.html)
