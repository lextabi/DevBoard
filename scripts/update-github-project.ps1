#!/usr/bin/env pwsh
<#
.SYNOPSIS
GitHub Project Board Automation Helper
.DESCRIPTION
Automates moving issues between project columns and updating checkboxes
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$Action,  # "start", "checklist", "complete"
    
    [Parameter(Mandatory=$true)]
    [int]$IssueNumber,
    
    [string]$Token,
    
    [string]$Checkboxes  # Comma-separated for "checklist" action
)

# GitHub API setup
$owner = "lextabi"
$repo = "DevBoard"
$projectNumber = 1
$baseUrl = "https://api.github.com"

if (-not $Token) {
    $Token = $env:GITHUB_TOKEN
}

if (-not $Token) {
    Write-Error "No GitHub token provided. Set GITHUB_TOKEN or pass -Token parameter"
    exit 1
}

$headers = @{
    "Authorization" = "Bearer $Token"
    "Accept" = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
}

# Column IDs (these need to be fetched from the project, but common values are used here)
$columns = @{
    "Backlog" = 0
    "In Progress" = 1
    "Testing" = 2
    "Done" = 3
}

function Update-ProjectItemStatus {
    param(
        [string]$Status  # "Backlog", "In Progress", "Testing", "Done"
    )
    
    # First, get the project item ID
    query = """
    query {
      repository(owner: \"$owner\", name: \"$repo\") {
        projectV2(number: $projectNumber) {
          items(first: 100) {
            nodes {
              id
              content {
                ... on Issue {
                  number
                }
              }
            }
          }
        }
      }
    }
    """
    
    $body = @{
        query = $query
    } | ConvertTo-Json
    
    $response = Invoke-RestMethod -Method Post `
        -Uri "$baseUrl/graphql" `
        -Headers $headers `
        -Body $body
    
    # Find the item with matching issue number
    $item = $response.data.repository.projectV2.items.nodes | 
        Where-Object { $_.content.number -eq $IssueNumber }
    
    if ($item) {
        $itemId = $item.id
        
        # Update the status field
        $statusUpdate = """
        mutation {
          updateProjectV2ItemFieldValue(input: {
            projectId: \"$projectNumber\"
            itemId: \"$itemId\"
            fieldId: \"Status\"
            value: {singleSelectOptionId: \"$($columns[$Status])\"}
          }) {
            projectV2Item {
              id
            }
          }
        }
        """
        
        $body = @{
            query = $statusUpdate
        } | ConvertTo-Json
        
        $response = Invoke-RestMethod -Method Post `
            -Uri "$baseUrl/graphql" `
            -Headers $headers `
            -Body $body
        
        Write-Host "✅ Moved Issue #$IssueNumber to '$Status'"
    }
}

function Update-Checkboxes {
    param(
        [string[]]$CheckedItems
    )
    
    # Get current issue
    $issueUrl = "$baseUrl/repos/$owner/$repo/issues/$IssueNumber"
    $issue = Invoke-RestMethod -Method Get -Uri $issueUrl -Headers $headers
    
    $body = $issue.body
    
    # Update checkboxes in body
    foreach ($item in $CheckedItems) {
        $body = $body -replace "\[ \] $item", "[x] $item"
    }
    
    # Update issue
    $updateBody = @{
        body = $body
    } | ConvertTo-Json
    
    Invoke-RestMethod -Method Patch `
        -Uri $issueUrl `
        -Headers $headers `
        -Body $updateBody > $null
    
    Write-Host "✅ Updated checkboxes for Issue #$IssueNumber"
}

# Execute action
switch ($Action) {
    "start" {
        Update-ProjectItemStatus "In Progress"
    }
    "checklist" {
        $items = $Checkboxes -split ","
        Update-Checkboxes $items
    }
    "complete" {
        Update-ProjectItemStatus "Done"
    }
    default {
        Write-Error "Unknown action: $Action. Use 'start', 'checklist', or 'complete'"
        exit 1
    }
}
