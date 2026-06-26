# Testing & Quality Assurance

## Testing Workflow

DevBoard follows a structured testing and approval workflow to ensure production-quality code.

## Phase Testing Process

### 1. Development Phase
- Code is implemented according to phase requirements
- Unit tests are included where applicable
- Code follows style guidelines (ESLint, Black, Prettier)
- CI/CD pipeline validates code quality

### 2. Manual Testing Phase
After development of a phase is complete:

1. **Notification**: Developer signals phase is ready for testing
2. **Testing Window**: Project owner tests all functionality
   - Frontend UI/UX
   - Backend API endpoints
   - Database operations
   - Integration between components
   - Error handling
3. **Bug Tracking**: Any issues found are documented
4. **Approval Decision**: 
   - ✅ **Pass**: All tests pass, proceed to next phase
   - ❌ **Fail**: Issues found, developer fixes and reruns testing

### 3. Phase Completion
Once testing passes:
- Owner approves phase in GitHub Project board
- Developer proceeds to next phase implementation
- Commit includes "testing approved" notation

## Testing Checklist by Phase

### Phase 1: User Authentication
- [ ] User can sign up with valid email
- [ ] User can log in with correct credentials
- [ ] Invalid login attempts fail properly
- [ ] JWT tokens work on protected routes
- [ ] Token refresh works
- [ ] Logout clears session
- [ ] Protected routes redirect unauthorized users
- [ ] API returns proper error codes

### Phase 2: Projects CRUD
- [ ] Create new project
- [ ] List projects
- [ ] Edit project details
- [ ] Delete project
- [ ] Archive project functionality
- [ ] Project board creation
- [ ] Proper user isolation (users only see own projects)

### Phase 3: Kanban Board
- [ ] Columns display correctly
- [ ] Tasks drag between columns
- [ ] Task order persists
- [ ] New task creation
- [ ] Task details editing
- [ ] Task deletion
- [ ] Task priority levels
- [ ] Column persistence after refresh

### Phase 4: Dashboard & Analytics
- [ ] Dashboard metrics display
- [ ] Activity feed updates in real-time
- [ ] Charts render correctly
- [ ] Progress calculations accurate
- [ ] Filters work on dashboard
- [ ] Export functionality works

### Phase 5: Advanced Features
- [ ] Labels create and assign
- [ ] Search finds tasks
- [ ] Notifications trigger
- [ ] Time tracking updates
- [ ] Reports generate

### Phase 6: Deployment & Polish
- [ ] Frontend deploys to Vercel
- [ ] Backend deploys to Render
- [ ] Database migrations work
- [ ] Custom domain works
- [ ] HTTPS enabled
- [ ] Performance acceptable
- [ ] No console errors
- [ ] Mobile responsive

## Testing Tools

### Frontend Testing
- **Manual**: Browser DevTools (F12)
- **Automated**: Vitest + React Testing Library
- **E2E**: Playwright (optional)

### Backend Testing
- **Unit Tests**: pytest
- **API Testing**: Postman/Thunder Client
- **Database**: Direct SQL queries

### Load Testing
```bash
# Install Apache Bench
ab -n 100 -c 10 http://localhost:5173

# Or use siege
npm install -g siege
siege -u http://localhost:5173 -r 10 -c 10
```

## Running Tests

### Frontend
```bash
cd frontend
npm run test              # Run all tests
npm run test:ui           # Interactive UI
npm run test:coverage     # Coverage report
```

### Backend
```bash
cd backend
pytest                    # Run all tests
pytest -v                 # Verbose
pytest --cov=app          # Coverage
pytest tests/test_api/    # Specific directory
```

## Approval Workflow

### For Developer

When phase is ready for testing:

```bash
# 1. Create a testing-ready commit
git add .
git commit -m "feat(phase-X): ready for user testing"

# 2. Push to GitHub
git push origin main

# 3. Notify owner
# Message format: "Phase X implementation complete and ready for testing"
```

### For Project Owner

When testing phase:

```
✅ All tests passed
- UI works as expected
- All features functional
- No errors in console
- Database operations correct
- API responses correct

Ready to proceed to Phase X+1
```

Or if issues found:

```
❌ Testing found issues:
- [Issue description with steps to reproduce]
- [Another issue]

Please fix and I'll retest.
```

## Continuous Integration

Every push automatically:
- ✅ Lints frontend code (ESLint)
- ✅ Lints backend code (flake8)
- ✅ Builds frontend
- ✅ Runs backend tests (pytest)
- ✅ Reports results in PR

## Deployment Gates

Before production deployment:

- [ ] All tests pass
- [ ] Code review complete
- [ ] Manual testing approved
- [ ] No critical security issues
- [ ] Performance acceptable
- [ ] Documentation updated

## When Testing Fails

1. **Document the issue**
   - Exact steps to reproduce
   - Expected vs actual behavior
   - Environment details

2. **Developer investigates**
   - Check logs
   - Debug with browser DevTools
   - Check API responses

3. **Fix and test again**
   - Push fix
   - Re-run tests
   - Notify owner for retest

## Testing Timeline

Per phase:
- Development: 3-5 days
- Manual testing: 1-2 days
- Bug fixes (if needed): 1-2 days
- Ready for next phase: ~1 week per phase

## Resources

- [Frontend Testing Guide](../frontend/README.md)
- [Backend Testing Guide](../backend/README.md)
- [API Documentation](./API.md)
- [Development Guide](./DEVELOPMENT.md)

