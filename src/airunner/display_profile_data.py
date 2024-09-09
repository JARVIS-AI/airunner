import line_profiler
from line_profiler import load_stats, show_text


def display_profile_data(profile_file):
    profile = line_profiler.LineProfiler()
    profile.add_function("showEvent")  # Add the function you want to profile
    profile.enable_by_count()

    # Load the profile data
    profile_data = load_stats(profile_file)

    show_text(profile_data.timings, profile_data.unit, output_unit=1.0)

# Run this function with the profile data file generated by kernprof
display_profile_data('main.py.lprof')
