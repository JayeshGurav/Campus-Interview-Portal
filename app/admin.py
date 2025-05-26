from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import User, StudentEnrollment

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('student.dashboard'))
    return render_template('admin/dashboard.html')

@admin_bp.route('/students')
@login_required
def students():
    if current_user.role != 'admin':
        return redirect(url_for('student.dashboard'))
    
    enrollments = StudentEnrollment.query.join(User).all()
    return render_template('admin/students.html', enrollments=enrollments)