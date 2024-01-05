rule all:
    input: "output/tRNA_scan_result.txt",
            "output/G_intestinalis.tRNA",
            expand("output/tRNAscan/{sp}.tRNA", sp=["G_muris", "G_intestinalis"])



rule tRNAscan:
    input: "resource/Genome/G_intestinalis.fasta"
    output: "output/tRNA_scan_result.txt"
    conda: "env/env.yaml"
    shell: """tRNAscan-SE {input} -o {output}"""

rule tRNAscan_stats:
    input:
        genome="resource/Genome/G_intestinalis.fasta"
    output:
        tRNA="output/G_intestinalis.tRNA",
        stats="output/G_intestinalis.stats"
    params:
        threads=2
    conda:
        "env/env.yaml"
    script:
        "scripts/tRNAscan_stats.py"

rule tRNAscan_stats_wildcard:
    input:
        genome="resource/Genome/{genome}.fasta"
    output:
        tRNA="output/tRNAscan/{genome}.tRNA",
        stats="output/tRNAscan/{genome}.stats"
    params:
        threads=2

    conda:
        "env/env.yaml"
    script:
        "scripts/tRNAscan_stats.py"

