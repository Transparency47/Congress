# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5472?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5472
- Title: Brownfield Revitalization and Remediation Act
- Congress: 119
- Bill type: HR
- Bill number: 5472
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-12-16T17:05:04Z
- Update date including text: 2025-12-16T17:05:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5472",
    "number": "5472",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Brownfield Revitalization and Remediation Act",
    "type": "HR",
    "updateDate": "2025-12-16T17:05:04Z",
    "updateDateIncludingText": "2025-12-16T17:05:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-09-18T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5472ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5472\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to restore and expand the expensing of qualified environmental remediation expenditures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Brownfield Revitalization and Remediation Act .\n#### 2. Restoring and expanding expensing of qualified environmental remediation expenditures\n##### (a) Restoring expensing\nSection 198(h) of the Internal Revenue Code of 1986 is amended to read as follows:\n(h) Termination This section shall not apply to expenditures paid or incurred\u2014 (1) after December 31, 2011, and before January 1, 2025, or (2) after December 31, 2029. .\n##### (b) Expanding expensing\n**(1) Inclusion of certain assessment, investigation, and monitoring expenses**\nSection 198(b)(1)(B) of such Code is amended by inserting (including reasonable expenditures for the assessment, investigation, and monitoring of such site in connection with such abatement or control) after qualified contaminated site .\n**(2) Special rule for depreciable property with respect to brownfield sites**\nSection 198(b)(2) of such Code is amended by inserting (other than a brownfield site (as defined in section 101(39) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980)) after qualified contaminated site .\n**(3) Treatment of pollutants and contaminants as hazardous substances**\nSection 198(d)(1) of such Code is amended\u2014\n**(A)**\nby striking and at the end of subparagraph (B),\n**(B)**\nby redesignating subparagraph (C) as subparagraph (D), and\n**(C)**\nby inserting after subparagraph (B) the following new subparagraph:\n(C) any substance which is a pollutant or contaminant as defined in section 101(33) of such Act, and .\n##### (c) Effective date\nThe amendments made by this section shall take effect upon the date of the enactment of this Act.",
      "versionDate": "2025-09-18",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-12-16T17:05:04Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5472ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Brownfield Revitalization and Remediation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T08:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Brownfield Revitalization and Remediation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T08:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to restore and expand the expensing of qualified environmental remediation expenditures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T08:48:38Z"
    }
  ]
}
```
