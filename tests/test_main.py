"""Tests for the QR code generator."""

import os
from main import generate_qr_code


def test_generate_qr_code(tmp_path, monkeypatch):
    monkeypatch.setenv("QR_CODE_DIR", str(tmp_path))
    path = generate_qr_code("https://example.com", "test_qr.png")
    assert os.path.exists(path)


def test_generate_returns_path():
    path = generate_qr_code("https://njit.edu", "njit_qr.png")
    assert path.endswith("njit_qr.png")