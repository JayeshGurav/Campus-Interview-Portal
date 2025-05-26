from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import EnrollmentForm
from app.models import StudentEnrollment
from app import db

student_bp = Blueprint('student', __name__)

@student_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'student':
        return redirect(url_for('admin.dashboard'))
    
    enrollment = StudentEnrollment.query.filter_by(user_id=current_user.id).first()
    return render_template('student/dashboard.html', enrollment=enrollment)

@student_bp.route('/form', methods=['GET', 'POST'])
@login_required
def form():
    if current_user.role != 'student':
        return redirect(url_for('admin.dashboard'))
    
    # Check if already enrolled
    existing_enrollment = StudentEnrollment.query.filter_by(user_id=current_user.id).first()
    if existing_enrollment:
        flash('You have already submitted your application')
        return redirect(url_for('student.dashboard'))
    
    form = EnrollmentForm()
    if form.validate_on_submit():
        enrollment = StudentEnrollment(
            user_id=current_user.id,
            roll_number=form.roll_number.data,
            department=form.department.data,
            cgpa=form.cgpa.data,
            graduation_year=form.graduation_year.data,
            skills=form.skills.data,
            certifications=form.certifications.data,
            projects=form.projects.data
        )
        db.session.add(enrollment)
        db.session.commit()
        flash('Your application has been submitted successfully!')
        return redirect(url_for('student.dashboard'))
    return render_template('student/form.html', form=form)