// static/js/script.js
document.addEventListener('DOMContentLoaded', () => {
  console.log('Call App Loaded');
  // Add any dynamic behavior here (e.g., WebRTC initialization)
});

document.addEventListener('DOMContentLoaded', function () {
    const profilePicture = document.getElementById('profilePicture');
    const profileModalElement = document.getElementById('profileModal');
    const modalProfileImage = document.getElementById('modalProfileImage');

    // Initialize the Bootstrap modal
    const profileModal = new bootstrap.Modal(profileModalElement);

    if (profilePicture) {
        profilePicture.addEventListener('click', function () {
            modalProfileImage.src = profilePicture.src;
            profileModal.show();
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    console.log('Auth pages loaded');
    // Future enhancements: client-side form validation can be added here.
});

document.addEventListener('DOMContentLoaded', () => {
    console.log('Edit Profile page loaded');
    // For example, add a live preview for the profile picture if needed:
    const pictureInput = document.querySelector('input[type="file"]');
    if (pictureInput) {
        pictureInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (evt) {
                    // Create or update an image element to preview
                    let preview = document.getElementById('profilePreview');
                    if (!preview) {
                        preview = document.createElement('img');
                        preview.id = 'profilePreview';
                        preview.style.maxWidth = '200px';
                        preview.style.marginBottom = '15px';
                        pictureInput.parentNode.insertBefore(preview, pictureInput);
                    }
                    preview.src = evt.target.result;
                }
                reader.readAsDataURL(file);
            }
        });
    }
});
