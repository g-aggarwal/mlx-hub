# Copyright (c) 2024 Gaurav Aggarwal

import unittest
import mlx_hub

TEST_MODEL = "mlx-community/TinyDolphin-2.8-1.1b-4bit-mlx"
TEST_SEARCH_PHRASE_MANY_RESULTS = "llama"
TEST_SEARCH_PHRASE_FEW_RESULTS = "bert"
TEST_SEARCH_PHRASE_NO_RESULTS = "bad_search_phrase"
TEST_SEARCH_PHRASE_EMPTY = ""


class TestMLXHub(unittest.TestCase):
    def test_search(self):
        result = mlx_hub.search(TEST_SEARCH_PHRASE_MANY_RESULTS)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), mlx_hub.SEARCH_LIMIT)

        for model_id in result:
            self.assertIsNotNone(model_id)
            self.assertGreater(len(model_id), 0)
            self.assertEqual(len(model_id.split("/")), 2)

        result = mlx_hub.search(TEST_SEARCH_PHRASE_FEW_RESULTS)
        self.assertIsNotNone(result)
        self.assertLess(len(result), mlx_hub.SEARCH_LIMIT)

        for model_id in result:
            self.assertIsNotNone(model_id)
            self.assertGreater(len(model_id), 0)
            self.assertEqual(len(model_id.split("/")), 2)

        result = mlx_hub.search(TEST_SEARCH_PHRASE_NO_RESULTS)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 0)

        result = mlx_hub.search(TEST_SEARCH_PHRASE_EMPTY)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), mlx_hub.SEARCH_LIMIT)

    def test_suggest(self):
        result = mlx_hub.suggest()
        self.assertIsNotNone(result)
        self.assertGreaterEqual(len(result), 0)

        for model_id in result:
            self.assertIsNotNone(model_id)
            self.assertGreater(len(model_id), 0)
            self.assertEqual(len(model_id.split("/")), 2)

    def test_scan(self):
        result = mlx_hub.scan()
        self.assertIsNotNone(result)
        self.assertGreaterEqual(len(result), 0)

        if TEST_MODEL not in result:
            download_result = mlx_hub.download(TEST_MODEL)
            self.assertEqual(download_result, True)
            result = mlx_hub.scan()
            self.assertIn(TEST_MODEL, result)

        for model_id in result:
            self.assertIsNotNone(model_id)
            self.assertGreater(len(model_id), 0)
            self.assertEqual(len(model_id.split("/")), 2)

    def test_download(self):
        scan_result_before_download = mlx_hub.scan()

        if TEST_MODEL in scan_result_before_download:
            delete_result = mlx_hub.delete(TEST_MODEL)
            self.assertEqual(delete_result, True)
            self.assertNotIn(TEST_MODEL, mlx_hub.scan())

        download_result = mlx_hub.download(TEST_MODEL)
        self.assertTrue(download_result)

        scan_result_after = mlx_hub.scan()
        self.assertIn(TEST_MODEL, scan_result_after)

    def test_delete(self):
        scan_results_before_delete = mlx_hub.scan()

        if TEST_MODEL not in scan_results_before_delete:
            download_result = mlx_hub.download(TEST_MODEL)
            self.assertEqual(download_result, True)
            scan_results_after_download = mlx_hub.scan()
            self.assertIn(TEST_MODEL, scan_results_after_download)

        delete_result = mlx_hub.delete(TEST_MODEL)
        self.assertEqual(delete_result, True)

        scan_results_after_delete = mlx_hub.scan()
        self.assertNotIn(TEST_MODEL, scan_results_after_delete)


if __name__ == '__main__':
    unittest.main()
