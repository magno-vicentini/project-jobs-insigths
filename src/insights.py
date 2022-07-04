from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    job_types = set()
    jobs = read(path)
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_jobs = list()
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    unique_industries = set()
    jobs = read(path)
    for job in jobs:
        if (job["industry"] != ''):
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_jobs_by_industry = list()
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs_by_industry.append(job)
    return filtered_jobs_by_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    max_salary_all_jobs = list()
    jobs = read(path)
    for job in jobs:
        if (job["max_salary"].isdigit()):
            max_salary_all_jobs.append(int(job["max_salary"]))
    return max(max_salary_all_jobs)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    min_salary_all_jobs = list()
    jobs = read(path)
    for job in jobs:
        if (job["min_salary"].isdigit()):
            min_salary_all_jobs.append(int(job["min_salary"]))
    return min(min_salary_all_jobs)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if("min_salary"not in job or "max_salary" not in job):
        raise ValueError("doesn't exists")

    if(type(job["min_salary"]) != int or type(job["max_salary"]) != int):
        raise ValueError("aren't valid integers")

    if(job["min_salary"] > job["max_salary"]):
        raise ValueError("min_salary must be lower than max_salary")

    if(type(salary) != int):
        raise ValueError("`salary` isn't a valid integer")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs_by_salary_range = list()
    for job in jobs:
        try:
            if(matches_salary_range(job, salary)):
                filtered_jobs_by_salary_range.append(job)
        except ValueError:
            pass
    return filtered_jobs_by_salary_range
