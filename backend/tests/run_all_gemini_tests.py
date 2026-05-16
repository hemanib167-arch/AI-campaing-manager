"""
Unified Gemini API Test Runner
Runs all Gemini API tests with proper API key authentication.
"""

import os
import sys
import asyncio


def check_dependencies():
    """Check if required packages are installed."""
    missing = []

    try:
        import google.generativeai
    except ImportError:
        missing.append("google-generativeai")

    try:
        from google import genai
    except ImportError:
        missing.append("google-genai")

    try:
        from PIL import Image
    except ImportError:
        missing.append("Pillow")

    try:
        import httpx
    except ImportError:
        missing.append("httpx")

    if missing:
        print("❌ Missing required packages:")
        for pkg in missing:
            print(f"  - {pkg}")
        print("\nInstall them with:")
        print(f"  pip install {' '.join(missing)}")
        return False

    return True


def get_api_key():
    """Get API key from environment or command line."""
    # Check command line argument
    if len(sys.argv) > 1:
        return sys.argv[1]

    # Check environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        return api_key

    # Check .env file
    env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1].strip()

    return None


async def run_sdk_tests(api_key):
    """Run SDK-based tests."""
    print("\n" + "=" * 70)
    print("RUNNING SDK-BASED TESTS (google-generativeai)")
    print("=" * 70)

    try:
        from test_gemini_sdk import GeminiSDKTester
        tester = GeminiSDKTester(api_key=api_key)
        result = tester.run_all_tests()
        return result
    except Exception as e:
        print(f"❌ SDK tests failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def run_api_tests(api_key):
    """Run HTTP API-based tests."""
    print("\n" + "=" * 70)
    print("RUNNING HTTP API-BASED TESTS")
    print("=" * 70)

    try:
        from test_gemini_api import GeminiAPITester
        tester = GeminiAPITester(api_key=api_key)
        result = await tester.run_all_tests()
        return result
    except Exception as e:
        print(f"❌ API tests failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def run_image_tests(api_key):
    """Run image generation tests."""
    print("\n" + "=" * 70)
    print("RUNNING IMAGE GENERATION TESTS (google-genai)")
    print("=" * 70)

    try:
        from test_gemini_image import GeminiImageTester
        tester = GeminiImageTester(api_key=api_key)
        result = tester.run_all_tests()
        return result
    except Exception as e:
        print(f"❌ Image tests failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Main test runner."""
    print("=" * 70)
    print("GEMINI API COMPLETE TEST SUITE")
    print("=" * 70)

    # Check dependencies
    print("\n📦 Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    print("✓ All dependencies installed")

    # Get API key
    print("\n🔑 Checking API key...")
    api_key = get_api_key()

    if not api_key:
        print("❌ API key not found!")
        print("\nPlease provide your Gemini API key using one of these methods:")
        print("  1. Command line: python run_all_gemini_tests.py YOUR_API_KEY")
        print("  2. Environment variable: set GEMINI_API_KEY=your-key-here")
        print("  3. .env file: add GEMINI_API_KEY=your-key-here")
        print("\nGet your API key from: https://makersuite.google.com/app/apikey")
        sys.exit(1)

    print(f"✓ API key found: {api_key[:8]}...{api_key[-4:]}")

    # Ask which tests to run
    print("\n🧪 Test Suites Available:")
    print("  1. SDK Tests (google-generativeai) - Text generation, chat, streaming")
    print("  2. HTTP API Tests - Direct REST API calls")
    print("  3. Image Generation Tests (google-genai) - Image creation")
    print("  4. ALL TESTS")

    choice = input("\nSelect test suite to run (1-4) [4]: ").strip() or "4"

    results = {}

    if choice == "1":
        results["SDK Tests"] = await run_sdk_tests(api_key)
    elif choice == "2":
        results["HTTP API Tests"] = await run_api_tests(api_key)
    elif choice == "3":
        results["Image Tests"] = run_image_tests(api_key)
    elif choice == "4":
        results["SDK Tests"] = await run_sdk_tests(api_key)
        results["HTTP API Tests"] = await run_api_tests(api_key)
        results["Image Tests"] = run_image_tests(api_key)
    else:
        print("❌ Invalid choice")
        sys.exit(1)

    # Final summary
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)

    for suite_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{suite_name:.<50} {status}")

    all_passed = all(results.values())
    total = len(results)
    passed_count = sum(1 for r in results.values() if r)

    print(f"\nOverall: {passed_count}/{total} test suites passed")

    if all_passed:
        print("\n🎉 All tests passed successfully!")
        sys.exit(0)
    else:
        print("\n⚠️ Some tests failed. Check the output above for details.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️ Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
