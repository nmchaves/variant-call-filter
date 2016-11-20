# variant-caller

A "variant caller" or "variant filter" is the last stage of a genomics pipeline. It takes a set of proposed variants (variant calls) as inputs, and it attempts to filter out the false positives based on several features associated with each variant call.

The Broad Intitute's Genome Analysis Toolkit (GATK) includes a variant caller known as the Variant Quality Score Recalibrator (VQSR). In short, VQSR fits a Gaussian Mixture Model to genetic variant data in order to classify proposed variants as true variants or not.

I'm currently developing a variant caller. My goal is to attain similar performance to VQSR without requiring as many modeling assumptions or manual user input.
