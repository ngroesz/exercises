use strict;
use warnings;

sub partition_sum {
    my ($number) = @_;

    return ($number * ($number + 1)) / 2;
}

sub solution {
    my (@A) = @_;

    my $stable_periods = 0;
    my $last_velocity;
    my $total_stable_periods = 0;

    for(my $i = 0; $i < scalar(@A); ++$i) {
        if (defined($last_velocity) && $i < scalar(@A) - 1 && $last_velocity == $A[$i + 1] - $A[$i]) {
            ++$stable_periods;
        } else {
            $total_stable_periods += partition_sum($stable_periods);
            $stable_periods = 0;
        }

        if ($stable_periods > 1_000_000_000) {
            return -1;
        }

        $last_velocity = $A[$i + 1] - $A[$i]
            if $i < scalar(@A) - 1;
    }

    return $total_stable_periods;
}

my @velocities = (-1, 1, 3, 3, 3, 2, 3, 2, 1, 0);
print solution(@velocities) . "\n";

@velocities = ();

for (my $i = 0; $i < 10_000; ++$i) {
    push(@velocities, 2);
}
print solution(@velocities) . "\n";
