import unittest
from unittest.mock import patch, Mock
from tmdb_client import get_single_movie, get_movie_images, get_single_movie_cast

class TestTmdbClient(unittest.TestCase):

    @patch('tmdb_client.requests.get')
    def test_get_single_movie(self, mock_get):
        # Mock response data
        mock_response = {
            'title': 'Movie Title',
            'overview': 'Movie overview text',
            'release_date': '2023-01-01'
            # Add more fields as needed to simulate a realistic response
        }
        mock_get.return_value.json.return_value = mock_response
        movie_id = 123

        # Call the function under test
        result = get_single_movie(movie_id)

        # Assert that the mock request was called with the correct URL
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        mock_get.assert_called_once_with(url, params={'api_key': '0f214f28296c208dc3cf6d2dce154551'})

        # Assert the returned data matches the expected mock_response
        self.assertEqual(result['title'], 'Movie Title')
        self.assertEqual(result['overview'], 'Movie overview text')
        self.assertEqual(result['release_date'], '2023-01-01')

    @patch('tmdb_client.requests.get')
    def test_get_movie_images(self, mock_get):
        # Mock response data
        mock_response = {
            'backdrops': [{'file_path': '/path/to/backdrop.jpg'}],
            'posters': [{'file_path': '/path/to/poster.jpg'}]
            # Add more fields as needed to simulate a realistic response
        }
        mock_get.return_value.json.return_value = mock_response
        movie_id = 123

        # Call the function under test
        result = get_movie_images(movie_id)

        # Assert that the mock request was called with the correct URL
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
        mock_get.assert_called_once_with(url, params={'api_key': '0f214f28296c208dc3cf6d2dce154551'})

        # Assert the returned data matches the expected mock_response
        self.assertEqual(result['backdrops'][0]['file_path'], '/path/to/backdrop.jpg')
        self.assertEqual(result['posters'][0]['file_path'], '/path/to/poster.jpg')

    @patch('tmdb_client.requests.get')
    def test_get_single_movie_cast(self, mock_get):
        # Mock response data
        mock_response = {
            'cast': [
                {'name': 'Actor 1', 'character': 'Character 1'},
                {'name': 'Actor 2', 'character': 'Character 2'}
            ]
            # Add more fields as needed to simulate a realistic response
        }
        mock_get.return_value.json.return_value = mock_response
        movie_id = 123

        # Call the function under test
        result = get_single_movie_cast(movie_id)

        # Assert that the mock request was called with the correct URL
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
        mock_get.assert_called_once_with(url, params={'api_key': '0f214f28296c208dc3cf6d2dce154551'})

        # Assert the returned data matches the expected mock_response
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'Actor 1')
        self.assertEqual(result[1]['character'], 'Character 2')

if __name__ == '__main__':
    unittest.main()