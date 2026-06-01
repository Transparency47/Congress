# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1598?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1598
- Title: Ensuring Access to Medicaid Buy-in Programs Act
- Congress: 119
- Bill type: HR
- Bill number: 1598
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2025-08-18T21:18:45Z
- Update date including text: 2025-08-18T21:18:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1598",
    "number": "1598",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001133",
        "district": "6",
        "firstName": "Juan",
        "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
        "lastName": "Ciscomani",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Ensuring Access to Medicaid Buy-in Programs Act",
    "type": "HR",
    "updateDate": "2025-08-18T21:18:45Z",
    "updateDateIncludingText": "2025-08-18T21:18:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1598ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1598\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Ciscomani (for himself and Ms. Perez ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to remove certain age restrictions on Medicaid eligibility for working adults with disabilities.\n#### 1. Short title\nThis Act may be cited as the Ensuring Access to Medicaid Buy-in Programs Act .\n#### 2. Removing certain age restrictions on Medicaid eligibility for working adults with disabilities\n##### (a) Modification of optional buy-In groups\n**(1) In general**\nSection 1902(a)(10)(A)(ii)(XV) of the Social Security Act ( 42 U.S.C. 1396a(a)(10)(A)(ii)(XV) ) is amended by striking , but less than 65, .\n**(2) Definition modification**\nSection 1905(v)(1)(A) of the Social Security Act ( 42 U.S.C. 1396d(v)(1)(A) ) is amended by striking , but less than 65, .\n##### (b) Application to certain States\nA State that, as of the date of the enactment of this Act, provides for making medical assistance available to individuals described in subclause (XV) or (XVI) of section 1902(a)(10)(A)(ii) of the Social Security Act ( 42 U.S.C. 1396a(a)(10)(A)(ii) ) shall not be regarded as failing to comply with the requirements of either such subclause (as amended by subsection (a)(1)) or with section 1905(v)(1)(A) of the Social Security Act ( 42 U.S.C. 1396d(v)(1)(A) ) (as amended by subsection (a)(2)) before January 1, 2027.",
      "versionDate": "2025-02-26",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability and paralysis",
            "updateDate": "2025-07-24T14:37:11Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-07-24T14:37:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T16:29:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1598",
          "measure-number": "1598",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1598v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ensuring Access to Medicaid Buy-in Programs Act</strong></p><p>This bill removes certain age limitations for the Medicaid buy-in program for disabled, working individuals.\u00a0</p><p>Current law allows disabled, working individuals ages 16 to 64 whose income exceeds applicable income limits to buy into Medicaid at the option of the state. The bill allows those age 65 or over to also buy into Medicaid.</p>"
        },
        "title": "Ensuring Access to Medicaid Buy-in Programs Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1598.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring Access to Medicaid Buy-in Programs Act</strong></p><p>This bill removes certain age limitations for the Medicaid buy-in program for disabled, working individuals.\u00a0</p><p>Current law allows disabled, working individuals ages 16 to 64 whose income exceeds applicable income limits to buy into Medicaid at the option of the state. The bill allows those age 65 or over to also buy into Medicaid.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hr1598"
    },
    "title": "Ensuring Access to Medicaid Buy-in Programs Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring Access to Medicaid Buy-in Programs Act</strong></p><p>This bill removes certain age limitations for the Medicaid buy-in program for disabled, working individuals.\u00a0</p><p>Current law allows disabled, working individuals ages 16 to 64 whose income exceeds applicable income limits to buy into Medicaid at the option of the state. The bill allows those age 65 or over to also buy into Medicaid.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hr1598"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1598ih.xml"
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
      "title": "Ensuring Access to Medicaid Buy-in Programs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-18T04:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Access to Medicaid Buy-in Programs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to remove certain age restrictions on Medicaid eligibility for working adults with disabilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:32Z"
    }
  ]
}
```
