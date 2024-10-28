module.exports = [
    {
        "names": ["ntcip-MD024"],
        "description": "No duplicate headings (except 'Overview')",
        "tags": ["headings"],
        "function": function MD024(params, onError) {
            const seenHeadings = new Map(); // To track already seen headings
            const headingTextToAllow = "Overview {.body}"; // The heading to allow duplicates for

            // Loop through all tokens and check for headings
            params.tokens.filter(t => t.type === "heading_open").forEach((heading) => {
                const nextToken = params.tokens[params.tokens.indexOf(heading) + 1];

                // If the heading is "Overview", skip it
                if (nextToken.content === headingTextToAllow) {
                    return;
                }

                // For all other headings, apply the standard logic
                const headingText = nextToken.content;
                const headingLevel = heading.tag;

                // Create a unique key based on heading text and level
                const key = `${headingLevel}|${headingText}`;

                if (seenHeadings.has(key)) {
                    // Duplicate found, trigger error
                    onError({
                        lineNumber: nextToken.lineNumber,
                        detail: `Duplicate heading: "${headingText}"`,
                        context: headingText
                    });
                } else {
                    // Record this heading as seen
                    seenHeadings.set(key, true);
                }
            });
        }
    }
];