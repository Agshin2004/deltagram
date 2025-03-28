currentPath = window.location.pathname

function likePost() {
    if (currentPath == '/' || currentPath.includes('post_detail') || currentPath.includes('profile/')) {
        // Like
        let likeCount = parseInt(document.querySelector('.like-count').innerHTML);
        let likeBtns = document.querySelectorAll('.like');
        const auth = document.body.dataset.auth;
        console.log(auth);

        likeBtns.forEach(btn => {
            btn.addEventListener('click', e => {
                const postId = btn.dataset.id;


                e.preventDefault();
                // Check if user is logged in 
                if (auth == 'False') {
                    alertify.error('You must be logged in to be able to like posts!')
                } else {
                    fetch(`/post/like_or_dislike_post/${postId}`)
                        .then(response => response.json())
                        .then(data => {
                            console.log(data);
                        if (data.success == "Liked") {
                            likeCount++;
                            document.querySelector('.like-img').src = "/static/images/liked.png";
                        } else {
                            likeCount--;
                            document.querySelector(".like-img").src = "/static/images/not_liked.png";
                        }
                        document.querySelector('.like-count').innerHTML = likeCount; // Update the content in the DOM
                    })
                } 
            })
        })

    }
}

likePost()
