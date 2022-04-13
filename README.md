# sf_reference

Planned Branching Strategy

Main Branch --> Updated to latest kedro version without any integration

Tag for each version of kedro eg[0.17.6, 0.17.7, 0.18.1] 


```mermaid
 gitGraph
    commit
    commit
    branch develop
    checkout develop
    commit
    commit
    checkout main
    merge develop
    commit
    commit
 ```

