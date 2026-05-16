# Gemini API Testing Scripts

This directory contains two testing scripts for Google's Gemini API integration with 6E Creative Studio.

## Available Scripts

### 1. `test_gemini_api.py` - HTTP-based testing
Uses direct HTTP requests to test the Gemini API. Minimal dependencies.

### 2. `test_gemini_sdk.py` - SDK-based testing (Recommended)
Uses Google's official `google-generativeai` SDK. More features and easier to use.

## Setup Instructions

### Step 1: Install Dependencies

```bash
# Install the Google Generative AI SDK
pip install google-generativeai

# Or add to requirements.txt and install all dependencies
pip install -r backend/requirements.txt
```

### Step 2: Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

### Step 3: Set Your API Key

#### Option A: Environment Variable (Recommended)

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY=your-api-key-here
```

**Permanent (add to .env file):**
```bash
echo "GEMINI_API_KEY=your-api-key-here" >> .env
```

#### Option B: Pass as Command Line Argument

```bash
python backend/tests/test_gemini_sdk.py YOUR_API_KEY_HERE
```

## Running the Tests

### Run SDK-based tests (Recommended):
```bash
cd backend/tests
python test_gemini_sdk.py
```

### Run HTTP-based tests:
```bash
cd backend/tests
python test_gemini_api.py
```

## Test Suite Coverage

The testing scripts cover the following functionality:

### 1. **Model Listing**
- Lists all available Gemini models
- Verifies API connectivity

### 2. **Basic Text Generation**
- Simple prompt-response generation
- Tests basic API functionality

### 3. **Copywriting Generation**
- Multi-variation ad copy generation
- Tests structured content creation
- Validates JSON output parsing

### 4. **Social Media Content**
- Instagram caption generation
- Tests creative writing capabilities
- Includes emoji and hashtag handling

### 5. **Image Prompt Generation**
- Generates prompts for DALL-E/Midjourney
- Tests detailed scene description
- Validates style and mood specification

### 6. **Structured Output**
- JSON extraction from text
- Campaign brief analysis
- Data structure validation

### 7. **Safety Settings**
- Content filtering configuration
- Harm category blocking
- Professional content generation

### 8. **Streaming Response** (SDK only)
- Real-time token streaming
- Progress feedback
- Chunk handling

### 9. **Multi-Turn Conversation** (SDK only)
- Context-aware chat
- Conversation history
- Follow-up questions

### 10. **Token Counting** (SDK only)
- Prompt token calculation
- Cost estimation
- Rate limit planning

## Expected Output

When all tests pass, you should see:

```
============================================================
GEMINI SDK TESTING SUITE
============================================================

=== Testing Model Listing ===
✓ Success! Found 5 generative models:
  - models/gemini-1.5-pro (Gemini 1.5 Pro)
  ...

=== Testing Basic Text Generation ===
✓ Success! Generated text:
Hydrate responsibly. Refresh sustainably.

...

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

## Troubleshooting

### Error: "google.generativeai not installed"
**Solution:**
```bash
pip install google-generativeai
```

### Error: "API key is required"
**Solution:** Set the GEMINI_API_KEY environment variable or pass it as a command line argument.

### Error: "403 Forbidden" or "401 Unauthorized"
**Solution:** 
- Verify your API key is correct
- Check if your API key is active in Google AI Studio
- Ensure you haven't exceeded rate limits

### Error: "Resource exhausted"
**Solution:** You've hit the rate limit. Wait a few minutes and try again.

### Error: "Model not found"
**Solution:** The model name might have changed. Run the Model Listing test to see available models.

## Rate Limits

Gemini API has the following rate limits (free tier):

- **Requests per minute (RPM):** 60
- **Tokens per minute (TPM):** 32,000
- **Requests per day (RPD):** 1,500

For production use, consider upgrading to a paid plan.

## Integration with 6E Creative Studio

These tests validate that the Gemini API can be used for:

1. **Campaign Copywriting** - Generate headlines, body copy, and CTAs
2. **Social Media Content** - Create platform-specific posts
3. **Image Descriptions** - Generate prompts for image generation
4. **Content Analysis** - Extract structured data from briefs
5. **Brand Voice** - Maintain consistent tone across content

## Next Steps

After successful testing:

1. Update `backend/llm/gemini_client.py` with the SDK implementation
2. Add error handling and retry logic
3. Implement rate limiting
4. Add prompt templates for different use cases
5. Integrate with the campaign generation pipeline

## API Key Security

⚠️ **IMPORTANT:** Never commit your API key to version control!

- Use environment variables
- Add `.env` to `.gitignore`
- Use secret management for production
- Rotate keys regularly

## Additional Resources

- [Google AI Studio](https://makersuite.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Python SDK Documentation](https://ai.google.dev/tutorials/python_quickstart)
- [Rate Limits & Pricing](https://ai.google.dev/pricing)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the [official documentation](https://ai.google.dev/docs)
3. Open an issue in the project repository
