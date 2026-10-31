# Example data for collections_linkml

This folder contains example data for testing and demonstrating the datamodel,
sorted in subfolders:

- `valid` for data conforming to the datamodel. Used to verify the datamodel.
- `invalid` for data not conforming to the datamodel. Used to verify the validation.
- `problem/invalid` for data that passes the validator but breaks a rule of the
  Collections Ontology that no validator checks; `tests/test_data.py` checks it.

The filenames of all example data must conform to the scheme `classname-###.yaml`
where classname must be the name of a class from the schema. "###" can be a number
or one or more other characters allowed in filenames. The classname is derived by
splitting at the first "-" and taking the part before the "-".
