# Gemini API Integration - Quick Setup Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install google-generativeai google-genai Pillow httpx
```

Or install all backend dependencies:
```bash
pip install -r backend/requirements.txt
```

### 2. Get Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy your API key

### 3. Set Your API Key

**Option A: Environment Variable (Recommended)**

Windows (Command Prompt):
```cmd
set GEMINI_API_KEY=your-api-key-here
```

Windows (PowerShell):
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

Linux/Mac:
```bash
export GEMINI_API_KEY=your-api-key-here
```

**Option B: Add to .env File**
```bash
echo "GEMINI_API_KEY=your-api-key-here" >> .env
```

### 4. Run Tests

**Easy Way (Recommended) - All Tests:**

Windows:
```cmd
cd backend\tests
run_gemini_tests.bat
```

Linux/Mac:
```bash
cd backend/tests
./run_gemini_tests.sh
```

**Or run specific test suites:**

```bash
# All tests with interactive menu
python backend/tests/run_all_gemini_tests.py

# SDK-based tests (text, chat, streaming)
python backend/tests/test_gemini_sdk.py

# HTTP API tests
python backend/tests/test_gemini_api.py

# Image generation tests
python backend/tests/test_gemini_image.py
```

**Pass API key directly:**
```bash
python backend/tests/run_all_gemini_tests.py YOUR_API_KEY_HERE
```

## 📁 Files Created

### Test Scripts
- **[test_gemini_sdk.py](backend/tests/test_gemini_sdk.py)** - Text generation testing using `google-generativeai`
- **[test_gemini_api.py](backend/tests/test_gemini_api.py)** - HTTP-based testing (alternative approach)
- **[test_gemini_image.py](backend/tests/test_gemini_image.py)** - Image generation testing using `google-genai`
- **[run_all_gemini_tests.py](backend/tests/run_all_gemini_tests.py)** - Unified test runner with interactive menu

### Helper Scripts
- **[run_gemini_tests.bat](backend/tests/run_gemini_tests.bat)** - Windows batch script to run all tests
- **[run_gemini_tests.sh](backend/tests/run_gemini_tests.sh)** - Linux/Mac shell script to run all tests

### Documentation
- **[GEMINI_TESTING_README.md](backend/tests/GEMINI_TESTING_README.md)** - Comprehensive testing documentation
- **[GEMINI_SETUP.md](GEMINI_SETUP.md)** - This file (Quick setup guide)

### Implementation Examples
- **[gemini_client_example.py](backend/llm/gemini_client_example.py)** - Production-ready Gemini client implementation

### Configuration
- **[.env.example](.env.example)** - Updated with GEMINI_API_KEY placeholder
- **[backend/requirements.txt](backend/requirements.txt)** - Updated with all required packages

## 🧪 What Gets Tested

The complete test suite validates three main areas:

### Text Generation Tests (test_gemini_sdk.py)
1. ✅ **Model Listing** - Verify API connectivity
2. ✅ **Basic Generation** - Simple text generation
3. ✅ **Copywriting** - Multi-variation ad copy
4. ✅ **Social Media** - Platform-specific content
5. ✅ **Image Prompts** - DALL-E/Midjourney prompt generation
6. ✅ **Structured Output** - JSON extraction and parsing
7. ✅ **Safety Settings** - Content filtering
8. ✅ **Streaming** - Real-time response streaming
9. ✅ **Multi-Turn Chat** - Context-aware conversations
10. ✅ **Token Counting** - Cost estimation

### HTTP API Tests (test_gemini_api.py)
- Direct REST API calls
- Manual HTTP request handling
- Response parsing and validation

### Image Generation Tests (test_gemini_image.py)
1. ✅ **Basic Image Generation** - Test image creation
2. ✅ **Campaign Images** - Product photography
3. ✅ **Social Media Images** - Instagram-ready visuals
4. ✅ **Banner Ads** - Wide format advertisements
5. ✅ **Multimodal Generation** - Text + image together

## 📊 Expected Output

```
============================================================
GEMINI SDK TESTING SUITE
============================================================

=== Testing Model Listing ===
✓ Success! Found 5 generative models:
  - models/gemini-1.5-pro (Gemini 1.5 Pro)
  ...

[... additional test output ...]

============================================================
TEST RESULTS SUMMARY
============================================================
Model Listing............................ ✓ PASSED
Basic Generation......................... ✓ PASSED
Copywriting Generation................... ✓ PASSED
Social Media Generation.................. ✓ PASSED
Image Prompt Generation.................. ✓ PASSED
Structured Output........................ ✓ PASSED
Safety Settings.......................... ✓ PASSED
Streaming Response....................... ✓ PASSED
Multi-Turn Conversation.................. ✓ PASSED
Token Counting........................... ✓ PASSED

Total: 10/10 tests passed
============================================================
```

## 🔧 Troubleshooting

### Error: "Module not found: google.generativeai"
```bash
pip install google-generativeai
```

### Error: "API key is required"
Make sure you've set the `GEMINI_API_KEY` environment variable or pass it as a command line argument.

### Error: "403 Forbidden"
- Verify your API key is correct
- Check if the key is active in Google AI Studio
- Ensure you haven't exceeded rate limits

### Error: "Resource exhausted"
You've hit the rate limit. Wait a few minutes and try again.

## 💰 Rate Limits (Free Tier)

- **Requests per minute:** 60
- **Tokens per minute:** 32,000
- **Requests per day:** 1,500

## 🔐 Security Best Practices

⚠️ **IMPORTANT:** Never commit your API key to version control!

- ✅ Use environment variables
- ✅ Add `.env` to `.gitignore`
- ✅ Use secret management for production
- ✅ Rotate keys regularly
- ❌ Never hardcode API keys in source files

## 📚 Additional Resources

- [Google AI Studio](https://makersuite.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Python SDK Documentation](https://ai.google.dev/tutorials/python_quickstart)
- [Rate Limits & Pricing](https://ai.google.dev/pricing)

## 🎯 Next Steps

1. ✅ Run the test suite to verify your setup
2. 📝 Review [GEMINI_TESTING_README.md](backend/tests/GEMINI_TESTING_README.md) for detailed information
3. 🔨 Implement Gemini client in [backend/llm/gemini_client.py](backend/llm/gemini_client.py)
4. 🔗 Integrate with campaign generation pipeline
5. 🚀 Deploy to production

## 💡 Use Cases for 6E Creative Studio

The Gemini API can power:

- 📝 **Campaign Copywriting** - Headlines, body copy, CTAs
- 📱 **Social Media Content** - Platform-specific posts
- 🖼️ **Image Descriptions** - Prompts for DALL-E/Midjourney
- 📊 **Content Analysis** - Extract data from campaign briefs
- 🎨 **Brand Voice** - Maintain consistent tone
- 💬 **Chat Interface** - Interactive campaign planning

---

**Need help?** Check the [detailed documentation](backend/tests/GEMINI_TESTING_README.md) or open an issue.
