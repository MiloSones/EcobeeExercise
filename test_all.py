import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
from api import get_posts, post_comment, get_posts_comments
from views import view_comments, view_posts_menu


class TestApi(unittest.TestCase):

    @patch('requests.get')
    def test_get_posts(self, mock_get):
        mock_response = MagicMock()
        mock_data = [{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}, {'userId': 1, 'id': 2, 'title': 'qui est esse', 'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'}, {'userId': 1, 'id': 3, 'title': 'ea molestias quasi exercitationem repellat qui ipsa sit aut', 'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'}]
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        result = get_posts()
        self.assertEqual(result, mock_data)

    @patch('requests.get')  
    def test_get_comments(self, mock_get):
        mock_response = MagicMock()
        mock_data = [
            {
                'postId': 1, 
                'id': 1, 
                'name': 'id labore ex et quam laborum', 
                'email': 'Eliseo@gardner.biz', 
                'body': 'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium'
            },
            {
                'postId': 1, 
                'id': 2, 
                'name': 'quo vero reiciendis velit similique earum', 
                'email': 'Jayne_Kuhic@sydney.com', 
                'body': 'est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et'
            }
        ]
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        result = get_posts_comments(1)
        self.assertEqual(result, mock_data)

    @patch('requests.post')
    def test_post_comment(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_data = {
            'id': 101,
            'postId': 1,
            'name': 'test name',
            'email': 'test@example.com',
            'body': 'test comment'
        }

        mock_response.json.return_value = mock_data
        mock_post.return_value = mock_response


        result = post_comment(1,mock_data)


        self.assertEqual(result, mock_response.status_code)
        


class TestPrint(unittest.TestCase):
    @patch('views.view_comments_menu')
    @patch('views.get_posts_comments')
    @patch('sys.stdout', new_callable=StringIO)
    def test_comment_printing(self, mock_stdout, mock_fetch ,mock_helper):
        mock_helper.return_value = None
        mock_fetch.return_value = [
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\n"
                        "tempora quo necessitatibus\n"
                        "dolor quam autem quasi\n"
                        "reiciendis et nam sapiente accusantium"
            },
            {
                "postId": 1,
                "id": 2,
                "name": "quo vero reiciendis velit similique earum",
                "email": "Jayne_Kuhic@sydney.com",
                "body": "est natus enim nihil est dolore omnis voluptatem numquam\n"
                        "et omnis occaecati quod ullam at\n"
                        "voluptatem error expedita pariatur\n"
                        "nihil sint nostrum voluptatem reiciendis et"
            }
        ]

        view_comments(1)


        output = mock_stdout.getvalue()


        expected_output = (
            "[Eliseo@gardner.biz] id labore ex et quam laborum\n"
            "\n"
            "laudantium enim quasi est quidem magnam voluptate ipsam eos\n"
            "tempora quo necessitatibus\n"
            "dolor quam autem quasi\n"
            "reiciendis et nam sapiente accusantium\n"
            "\n"
            "[Jayne_Kuhic@sydney.com] quo vero reiciendis velit similique earum\n"
            "\n"
            "est natus enim nihil est dolore omnis voluptatem numquam\n"
            "et omnis occaecati quod ullam at\n"
            "voluptatem error expedita pariatur\n"
            "nihil sint nostrum voluptatem reiciendis et\n"
            "\n"
        )

        mock_helper.assert_called_once()
        self.assertEqual(output, expected_output)

# class TestUserValidation(unittest.TestCase):
#     @patch('sys.stdout', new_callable=StringIO)
#     @patch('builtins.input')
#     def test_nonnumeric_input(self, mock_input, mock_stdout):
#         mock_input.side_effect = ['a', '1']
#         view_posts_menu()

#         self.assertEqual(mock_stdout.getvalue(),
#         "Choose an option:\n"
#         "1. View 10 random post titles\n"
#         "2. View 10 most commented post titles\n"
#         "3. exit\n"
#         "Enter your choice (1-3): a\n"
#         "Enter your choice (1-3): 1")


#     @patch('sys.stdout', new_callable=StringIO)
#     @patch('builtins.input')
#     def test_out_of_bounds(self, mock_input, mock_stdout):
#         mock_input.side_effect = ['4', '1']

#         view_posts_menu()

#         self.assertEqual(mock_stdout.getvalue(),
#         "Choose an option:\n"
#         "1. View 10 random post titles\n"
#         "2. View 10 most commented post titles\n"
#         "3. exit\n"
#         "Enter your choice (1-3): 4\n"
#         "Enter your choice (1-3): 1")

#     @patch('views.view_random_posts')
#     @patch('builtins.input', return_value="1")
#     def test_valid_input(self, mock_called_function):
        
#         view_posts_menu()

#         mock_called_function.assert_called_once()

if __name__ == "__main__":
    unittest.main()