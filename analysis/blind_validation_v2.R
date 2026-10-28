args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2) {
  stop("usage: Rscript analysis/blind_validation_v2.R RESULTS_CSV OUTPUT_DIR")
}

fail <- function(message) {
  stop(message, call. = FALSE)
}

required_columns <- c(
  "fixture",
  "exact_recovery",
  "character_matches",
  "target_length",
  "recovered_erase_triplets",
  "erase_exact"
)

results <- read.csv(args[[1]], stringsAsFactors = FALSE, check.names = FALSE)
missing_columns <- setdiff(required_columns, names(results))
if (length(missing_columns) > 0) {
  fail(sprintf(
    "missing required column(s): %s",
    paste(missing_columns, collapse = ", ")
  ))
}

if (nrow(results) != 10) {
  fail(sprintf("expected exactly 10 fixture rows; found %d", nrow(results)))
}

fixtures <- trimws(as.character(results$fixture))
if (any(is.na(fixtures)) || any(fixtures == "")) {
  fail("fixture must be nonempty for every row")
}
if (anyDuplicated(fixtures)) {
  fail("fixture values must be unique")
}
expected_fixtures <- sprintf("blind-v2-%02d.typescript", seq_len(10))
if (!setequal(fixtures, expected_fixtures)) {
  fail("fixture values must be exactly blind-v2-01.typescript through blind-v2-10.typescript")
}

binary_column <- function(values, name) {
  parsed <- suppressWarnings(as.numeric(as.character(values)))
  if (any(is.na(parsed)) || any(!is.finite(parsed)) ||
      any(!(parsed %in% c(0, 1)))) {
    fail(sprintf("%s must contain only 0 or 1", name))
  }
  as.integer(parsed)
}

numeric_column <- function(values, name) {
  parsed <- suppressWarnings(as.numeric(as.character(values)))
  if (any(is.na(parsed)) || any(!is.finite(parsed))) {
    fail(sprintf("%s must contain finite numeric values", name))
  }
  parsed
}

exact_recovery <- binary_column(results$exact_recovery, "exact_recovery")
erase_exact <- binary_column(results$erase_exact, "erase_exact")

target_length <- numeric_column(results$target_length, "target_length")
if (any(target_length != 15)) {
  fail("target_length must equal 15 for every fixture")
}
target_length <- as.integer(target_length)

character_matches <- numeric_column(results$character_matches, "character_matches")
if (any(character_matches != floor(character_matches)) ||
    any(character_matches < 0) ||
    any(character_matches > target_length)) {
  fail("character_matches must be an integer from 0 through target_length")
}
character_matches <- as.integer(character_matches)

recovered_erase_triplets <- numeric_column(
  results$recovered_erase_triplets,
  "recovered_erase_triplets"
)
if (any(recovered_erase_triplets != floor(recovered_erase_triplets)) ||
    any(recovered_erase_triplets < 0)) {
  fail("recovered_erase_triplets must be a nonnegative integer")
}
recovered_erase_triplets <- as.integer(recovered_erase_triplets)

if (any(exact_recovery != as.integer(character_matches == target_length))) {
  fail("exact_recovery must agree with character_matches == target_length")
}
if (any(erase_exact != as.integer(recovered_erase_triplets == 15))) {
  fail("erase_exact must agree with recovered_erase_triplets == 15")
}

results$exact_recovery <- exact_recovery
results$character_matches <- character_matches
results$target_length <- target_length
results$recovered_erase_triplets <- recovered_erase_triplets
results$erase_exact <- erase_exact

successes <- sum(results$exact_recovery == 1)
trials <- nrow(results)
test <- binom.test(successes, trials, p = 0.5, alternative = "two.sided",
                   conf.level = 0.95)

output_dir <- args[[2]]
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

summary <- data.frame(
  metric = c(
    "fixtures_exact",
    "fixtures_total",
    "observed_exact_rate",
    "clopper_pearson_95_lower",
    "clopper_pearson_95_upper",
    "null_rate_used_by_binom_test",
    "two_sided_binomial_p_value",
    "character_matches_descriptive",
    "character_positions_descriptive",
    "erase_counts_exact",
    "erase_counts_total"
  ),
  value = c(
    successes,
    trials,
    successes / trials,
    unname(test$conf.int[[1]]),
    unname(test$conf.int[[2]]),
    0.5,
    test$p.value,
    sum(results$character_matches),
    sum(results$target_length),
    sum(results$erase_exact == 1),
    trials
  ),
  note = c(
    "Primary exact-string endpoint",
    "Procedurally blinded fixtures",
    "Observed proportion; not a universal error rate",
    "Exact two-sided interval",
    "Exact two-sided interval",
    "Illustrative equal-success null, declared post-generation",
    "Not a t test; limited by n=10 and fixture dependence assumptions",
    "Descriptive only; character positions are clustered within fixtures",
    "Descriptive only; character positions are clustered within fixtures",
    "Exact triplet-count endpoint",
    "Procedurally blinded fixtures"
  ),
  stringsAsFactors = FALSE
)

write.csv(summary, file.path(output_dir, "r-summary.csv"), row.names = FALSE,
          quote = TRUE)

report <- capture.output({
  cat("BACKSPACE GATE BLIND VALIDATION V2 — R CROSS-CHECK\n\n")
  print(test)
  cat("\nCharacter-level agreement is descriptive because positions are clustered.\n")
  cat("A t test is not appropriate for binary exact-match outcomes.\n")
})
writeLines(report, file.path(output_dir, "r-binom-test.txt"), useBytes = TRUE)

