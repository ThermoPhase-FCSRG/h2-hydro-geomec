# h2-hydro-geomec

Hydro-geomechanical simulations for hydrogen cycling in depleted reservoirs.

This repository is intended for research studies on H2 injection, storage, and
cyclic production in porous reservoirs. The numerical work will compare
different levels of hydro-geomechanical coupling and evaluate how those choices
affect pressure response, deformation, porosity/permeability updates, and
production during storage cycles.

The code is based on the earlier repository
[`volpatto/supporting-material-msc`](https://github.com/volpatto/supporting-material-msc),
which contains supporting material for Diego Tavares Volpatto's 2016 MSc
dissertation on hydro-geomechanical methane reservoir simulations. That previous
work focused on CH4 and used small Firedrake scripts for compressible gas flow,
poroelasticity, and fixed-stress splitting. This repository reuses that numerical
lineage, but the target application is different: H2 cycling in depleted
reservoirs, not methane reservoir reproduction and not fracture-focused studies.

## Research Scope

The planned comparisons are:

- **Flow-only baseline**: pressure/production response without geomechanical
  feedback.
- **One-way coupling**: flow affects the mechanical state, but the updated
  deformation does not feed back into the flow equation.
- **Two-way coupling**: pressure, deformation, porosity/permeability, and
  stress-dependent source terms are updated consistently during the simulation.
- **Cycling operation**: repeated injection and withdrawal periods, with the
  objective of measuring how geomechanics changes cycling production indicators.

Quantities of interest will typically include pressure histories, cumulative
injection/production, working gas recovery, porosity and permeability changes,
displacement, stress response, and differences between coupling strategies.

## Requirement: Firedrake

The simulations depend on
[Firedrake](https://www.firedrakeproject.org/), a Python finite-element framework
for solving partial differential equations. This repository does not install
Firedrake automatically.

Follow the official Firedrake installation instructions:

```text
https://www.firedrakeproject.org/install.html
```

After installation, activate the Firedrake environment before running any script.
On many local installations this looks like:

```bash
source ~/firedrake/venv-firedrake/bin/activate
```

If Firedrake was installed in another directory, replace the path above with the
path used on your machine.

Check that the active Python can import Firedrake:

```bash
python -c "import firedrake; print('Firedrake is available')"
```

Also check the plotting dependencies used by the scripts:

```bash
python -c "import numpy, matplotlib; print('NumPy and Matplotlib are available')"
```

If one of these checks fails, the most common reason is that the Firedrake
environment is not active in the terminal where you are running the command.

## Running the Code

Open a terminal and go to the repository root:

```bash
cd path/to/h2-hydro-geomec
```

Activate Firedrake:

```bash
source ~/firedrake/venv-firedrake/bin/activate
```

Run the Picard/linearized pressure version:

```bash
python scripts/compressible_hm_2D_fixed_stress_injection.py
```

Run the Newton pressure version:

```bash
python scripts/compressible_hm_2D_fixed_stress_injection_newton.py
```

These scripts currently do not expose command-line options. Mesh size, final
time, time step, material parameters, and boundary conditions are defined near
the top of each script.

## Output Files

The Picard script writes to:

```text
outputs/2D/compressible_hm_2D_fixed_stress_injection/
```

The Newton script writes to:

```text
outputs/2D/compressible_hm_2D_fixed_stress_injection_newton/
```

Useful files to inspect first:

- `final_fields.png`: final pressure, stress/source, and displacement plots.
- `field_evolution.png`: selected snapshots through time.
- `midheight_profiles.png`: pressure, stress, and source profiles along the
  reservoir mid-height.
- `midheight_profiles_projected.png`: same profiles after visualization
  projection for discontinuous quantities.
- `time_history.csv`: numerical time history of min/max fields and fixed-stress
  iteration counts.
- `run_metadata.txt`: mesh, physical parameters, boundary conditions, and solver
  metadata.
- `fields.pvd` and `fields/`: VTK output that can be opened in ParaView.

If you are not used to code, the simplest first check is to open the PNG files.
The CSV file can be opened in a spreadsheet program. The VTK files are useful
for spatial visualization in ParaView, but they are not required for a first
inspection.

## Common Problems

### `ModuleNotFoundError: No module named 'firedrake'`

The Firedrake environment is not active, or Firedrake has not been installed in
the Python environment being used by the terminal. Activate Firedrake again:

```bash
source ~/firedrake/venv-firedrake/bin/activate
```

Then rerun:

```bash
python -c "import firedrake; print('Firedrake is available')"
```

### The run is slow

The current scripts use a `100 x 100` quadrilateral mesh and direct linear
solvers. This can be expensive on laptops. For a quick test, reduce the mesh
near the top of the script:

```python
numel_x = 40
numel_y = 40
```

After confirming that the workflow runs, increase the mesh resolution again for
scientific comparisons.

### I do not see output files

Run the command from the repository root, not from inside `scripts/`. The scripts
write output paths relative to the repository location.

### The figures still say methane

That reflects the current inherited state of the scripts. The README describes
the intended H2 research direction, but the code still needs an H2 audit before
results should be interpreted as hydrogen simulations.

## Scientific Assumptions To Verify

Before using this repository for scientific conclusions, check at least:

- H2 thermodynamic model: the current `Z(p)` polynomial is inherited from the
  methane material and should not be assumed valid for H2.
- H2 viscosity: the current gas viscosity value is methane-like and must be
  replaced or justified.
- Pressure and temperature range: any fitted equation of state should be valid
  over the simulated operating range.
- Cycling schedule: the present scripts are injection examples, not complete
  injection/withdrawal cycling studies.
- Coupling definitions: document exactly what is meant by uncoupled, one-way,
  and two-way coupling in each comparison.
- Boundary conditions: confirm that hydraulic and mechanical boundary conditions
  represent the intended depleted-reservoir scenario.
- Porosity/permeability law: check whether the inherited law is appropriate for
  the reservoir and deformation regime under study.
- Numerical convergence: monitor fixed-stress iteration counts, nonlinear
  convergence, mesh sensitivity, and time-step sensitivity before comparing
  production indicators.

Some of these assumptions may be wrong for the intended H2 cases. They are
listed explicitly so that future results are not accidentally interpreted as
validated hydrogen-storage simulations before the physics has been updated.

## Relation To The MSc CH4 Work

The predecessor repository supports the MSc dissertation:

```text
Diego Tavares Volpatto,
Modelagem computacional do acoplamento hidro-geomecanico em reservatorios
nao-convencionais de gas,
MSc Dissertation, Laboratorio Nacional de Computacao Cientifica, Petropolis,
2016.
```

That work is the numerical starting point for this repository. When publishing
or reporting results derived from this code lineage, cite the MSc work and make
clear which parts are inherited CH4 methodology and which parts were modified
for H2 cycling.

## AI Statement of Use

Following the CNPq research-integrity directives on generative artificial
intelligence, this repository declares the use of OpenAI Codex as an auxiliary
tool for code development, documentation drafting, refactoring support,
consistency checks, and repository-maintenance tasks.

This use of generative AI does not replace scientific authorship, critical
review, or responsibility for the research. The mathematical model, numerical
formulation, physical assumptions, parameter choices, interpretation of results,
validation strategy, and final decisions about what is included in this
repository remain the responsibility of the human researcher.

AI-assisted outputs in this repository should be checked before being used in
scientific communication, teaching, reporting, or publication. In particular,
model equations, units, references, thermodynamic assumptions, solver settings,
and numerical conclusions must be verified against the intended H2
hydro-geomechanical problem.

The CNPq directive used as reference is available at:

```text
https://www.gov.br/cnpq/pt-br/composicao/comissao-de-integridade/diretrizes
```

## License

This repository is distributed under the BSD 3-Clause License. See
[LICENSE](LICENSE).
