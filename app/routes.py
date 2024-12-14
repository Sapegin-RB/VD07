from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import EditProfileForm

bp = Blueprint('main', __name__)

@bp.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Здесь можно сохранить изменения в базу данных
        flash('Изменения сохранены!', 'success')
        return redirect(url_for('main.edit_profile'))

    return render_template('edit_profile.html', form=form)
