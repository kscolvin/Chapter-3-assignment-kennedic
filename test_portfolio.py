"""
Autograder tests for Assignment 3 - Personal Data Portfolio
Tests all required data structures and calculations
"""

import pytest
import sys
from io import StringIO

def test_portfolio_imports():
    """Test that portfolio.py can be imported"""
    try:
        import portfolio
    except ImportError:
        pytest.fail("portfolio.py file not found or has syntax errors")
    except Exception as e:
        pytest.fail(f"Error importing portfolio.py: {str(e)}")

def test_string_variables():
    """Test that all required string variables exist with correct values"""
    import portfolio
    
    assert hasattr(portfolio, 'full_name'), "Missing variable: full_name"
    assert portfolio.full_name == "Jordan Smith", "full_name has incorrect value"
    
    assert hasattr(portfolio, 'student_email'), "Missing variable: student_email"
    assert portfolio.student_email == "jsmith@ncat.edu", "student_email has incorrect value"
    
    assert hasattr(portfolio, 'hometown'), "Missing variable: hometown"
    assert portfolio.hometown == "Charlotte, NC", "hometown has incorrect value"
    
    assert hasattr(portfolio, 'graduation_semester'), "Missing variable: graduation_semester"
    assert portfolio.graduation_semester == "Spring 2028", "graduation_semester has incorrect value"
    
    assert hasattr(portfolio, 'major'), "Missing variable: major"
    assert portfolio.major == "Computer Science", "major has incorrect value"

def test_list_variables():
    """Test that all required list variables exist with correct values"""
    import portfolio
    
    assert hasattr(portfolio, 'current_courses'), "Missing variable: current_courses"
    assert portfolio.current_courses == ["COMP 163", "MATH 150", "ENG 101", "HIS 105"], \
        "current_courses has incorrect values"
    
    assert hasattr(portfolio, 'completed_courses'), "Missing variable: completed_courses"
    assert portfolio.completed_courses == ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"], \
        "completed_courses has incorrect values"
    
    assert hasattr(portfolio, 'credit_hours'), "Missing variable: credit_hours"
    assert portfolio.credit_hours == [3, 3, 3, 3], "credit_hours has incorrect values"
    
    assert hasattr(portfolio, 'gpa_history'), "Missing variable: gpa_history"
    assert portfolio.gpa_history == [3.2, 3.6, 3.4, 3.7], "gpa_history has incorrect values"

def test_tuple_variables():
    """Test that all required tuple variables exist with correct values"""
    import portfolio
    
    assert hasattr(portfolio, 'emergency_contact'), "Missing variable: emergency_contact"
    assert portfolio.emergency_contact == ("Mom", "Hannah Smith", "704-555-0199"), \
        "emergency_contact has incorrect values"
    
    assert hasattr(portfolio, 'home_address'), "Missing variable: home_address"
    assert portfolio.home_address == ("456 Oak Street", "Charlotte, NC", "28202"), \
        "home_address has incorrect values"
    
    assert hasattr(portfolio, 'instagram_info'), "Missing variable: instagram_info"
    assert portfolio.instagram_info == ("Instagram", "@jordan_codes", 312), \
        "instagram_info has incorrect values"
    
    assert hasattr(portfolio, 'twitter_info'), "Missing variable: twitter_info"
    assert portfolio.twitter_info == ("Twitter", "@jordandev", 127), \
        "twitter_info has incorrect values"
    
    assert hasattr(portfolio, 'birthday'), "Missing variable: birthday"
    assert portfolio.birthday == ("Birthday", 5, 22, 2006), "birthday has incorrect values"

def test_set_variables():
    """Test that all required set variables exist with correct values"""
    import portfolio
    
    assert hasattr(portfolio, 'current_skills'), "Missing variable: current_skills"
    expected_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
    assert portfolio.current_skills == expected_skills, "current_skills has incorrect values"
    
    assert hasattr(portfolio, 'skills_to_learn'), "Missing variable: skills_to_learn"
    expected_learning = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
    assert portfolio.skills_to_learn == expected_learning, "skills_to_learn has incorrect values"
    
    assert hasattr(portfolio, 'career_interests'), "Missing variable: career_interests"
    expected_careers = {"Software development", "Web development", "Data science", "Game development"}
    assert portfolio.career_interests == expected_careers, "career_interests has incorrect values"
    
    assert hasattr(portfolio, 'hobbies'), "Missing variable: hobbies"
    expected_hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
    assert portfolio.hobbies == expected_hobbies, "hobbies has incorrect values"
    
    assert hasattr(portfolio, 'entertainment_backlog'), "Missing variable: entertainment_backlog"
    expected_entertainment = {"One Piece", "Barry", "Life", "Incantation", "Memento"}
    assert portfolio.entertainment_backlog == expected_entertainment, "entertainment_backlog has incorrect values"

def test_dictionary_variables():
    """Test that all required dictionary variables exist with correct values"""
    import portfolio
    
    assert hasattr(portfolio, 'course_credits'), "Missing variable: course_credits"
    assert portfolio.course_credits == {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}, \
        "course_credits has incorrect values"
    
    assert hasattr(portfolio, 'course_professors'), "Missing variable: course_professors"
    expected_profs = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", 
                      "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
    assert portfolio.course_professors == expected_profs, "course_professors has incorrect values"
    
    assert hasattr(portfolio, 'course_rooms'), "Missing variable: course_rooms"
    expected_rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", 
                      "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
    assert portfolio.course_rooms == expected_rooms, "course_rooms has incorrect values"
    
    assert hasattr(portfolio, 'monthly_budget'), "Missing variable: monthly_budget"
    assert portfolio.monthly_budget == {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}, \
        "monthly_budget has incorrect values"
    
    assert hasattr(portfolio, 'study_hours'), "Missing variable: study_hours"
    assert portfolio.study_hours == {"Programming": 10, "Math": 8, "English": 4, "History": 3}, \
        "study_hours has incorrect values"
    
    assert hasattr(portfolio, 'contact_directory'), "Missing variable: contact_directory"
    expected_contacts = {"Mom": "704-555-0199", "Roommate": "336-555-7821", 
                        "Academic Advisor": "336-334-5000"}
    assert portfolio.contact_directory == expected_contacts, "contact_directory has incorrect values"

def test_calculations():
    """Test that all required calculations are present and correct"""
    import portfolio
    
    # Total current credits
    assert hasattr(portfolio, 'total_credits'), "Missing calculation: total_credits"
    assert portfolio.total_credits == 12, f"total_credits should be 12, got {portfolio.total_credits}"
    
    # Cumulative GPA
    assert hasattr(portfolio, 'cumulative_gpa'), "Missing calculation: cumulative_gpa"
    expected_gpa = round(sum([3.2, 3.6, 3.4, 3.7]) / 4, 2)
    assert abs(portfolio.cumulative_gpa - expected_gpa) < 0.01, \
        f"cumulative_gpa should be {expected_gpa}, got {portfolio.cumulative_gpa}"
    
    # Completed courses count
    assert hasattr(portfolio, 'completed_count'), "Missing calculation: completed_count"
    assert portfolio.completed_count == 5, f"completed_count should be 5, got {portfolio.completed_count}"
    
    # Total weekly study hours
    assert hasattr(portfolio, 'total_study_hours'), "Missing calculation: total_study_hours"
    assert portfolio.total_study_hours == 25, f"total_study_hours should be 25, got {portfolio.total_study_hours}"
    
    # Academic load
    assert hasattr(portfolio, 'academic_load'), "Missing calculation: academic_load"
    assert portfolio.academic_load == 37, f"academic_load should be 37, got {portfolio.academic_load}"
    
    # Monthly budget total
    assert hasattr(portfolio, 'monthly_total'), "Missing calculation: monthly_total"
    assert portfolio.monthly_total == 875, f"monthly_total should be 875, got {portfolio.monthly_total}"
    
    # Daily food budget
    assert hasattr(portfolio, 'daily_food_budget'), "Missing calculation: daily_food_budget"
    assert portfolio.daily_food_budget == 15.0, \
        f"daily_food_budget should be 15.0, got {portfolio.daily_food_budget}"
    
    # Annual budget projection
    assert hasattr(portfolio, 'annual_budget'), "Missing calculation: annual_budget"
    assert portfolio.annual_budget == 10500, f"annual_budget should be 10500, got {portfolio.annual_budget}"
    
    # Study cost per hour
    assert hasattr(portfolio, 'cost_per_hour'), "Missing calculation: cost_per_hour"
    assert portfolio.cost_per_hour == 5.0, f"cost_per_hour should be 5.0, got {portfolio.cost_per_hour}"
    
    # Total social media followers
    assert hasattr(portfolio, 'total_followers'), "Missing calculation: total_followers"
    assert portfolio.total_followers == 439, f"total_followers should be 439, got {portfolio.total_followers}"
    
    # Skills count comparison
    assert hasattr(portfolio, 'current_skills_count'), "Missing calculation: current_skills_count"
    assert portfolio.current_skills_count == 5, \
        f"current_skills_count should be 5, got {portfolio.current_skills_count}"
    
    assert hasattr(portfolio, 'skills_to_learn_count'), "Missing calculation: skills_to_learn_count"
    assert portfolio.skills_to_learn_count == 5, \
        f"skills_to_learn_count should be 5, got {portfolio.skills_to_learn_count}"
    
    # Contact directory size
    assert hasattr(portfolio, 'contact_count'), "Missing calculation: contact_count"
    assert portfolio.contact_count == 3, f"contact_count should be 3, got {portfolio.contact_count}"

def test_no_functions_used():
    """Test that students did not use functions (not covered in Chapter 3)"""
    import portfolio
    import inspect
    
    # Get all functions defined in the module (excluding built-ins)
    functions = [name for name, obj in inspect.getmembers(portfolio, inspect.isfunction)
                 if obj.__module__ == 'portfolio']
    
    assert len(functions) == 0, \
        f"Functions are not allowed for this assignment. Found: {', '.join(functions)}"

def test_code_runs():
    """Test that the code runs without errors"""
    import portfolio
    # If we got here, the code imported and ran successfully
    assert True