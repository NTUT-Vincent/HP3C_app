/INSERT INTO/ {                              # parse INSERT commands
    split($0, values, "VALUES");             # extract everything after VALUES
    split(values[1], name, "INSERT INTO");   # get tablename
    tablename = name[2];                     #
    gsub(/[\047\042]/, "", tablename);         # remove single and double quotes from name
    gsub(/[\047,]/, "", values[2]);          # remove single-quotes and commas
    sizes[tablename] += length(values[2]) - 3; # subtract 3 for parens and semicolon
    counts[tablename] += 1;
}

END {
    print "table\tcount\test. size"
    for(k in sizes) {
        # print and sort in descending order:
        print k "\t" counts[k] "\t" sizes[k] | "sort -k3 -n -r";

        # or, if you don't have the sort command:
        print k "\t" counts[k] "\t" sizes[k];
    }
}