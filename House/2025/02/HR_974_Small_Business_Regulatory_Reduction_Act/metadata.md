# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/974?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/974
- Title: Small Business Regulatory Reduction Act
- Congress: 119
- Bill type: HR
- Bill number: 974
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-12-05T21:52:43Z
- Update date including text: 2025-12-05T21:52:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/974",
    "number": "974",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Small Business Regulatory Reduction Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:52:43Z",
    "updateDateIncludingText": "2025-12-05T21:52:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:09:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "KS"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr974ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 974\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Ms. Van Duyne (for herself, Mr. Meuser , Mr. Bean of Florida , and Mr. Schmidt ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo require the Administrator of the Small Business Administration to ensure that the small business regulatory budget for a small business concern in a fiscal year is not greater than 0, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Regulatory Reduction Act .\n#### 2. Small Business Administration rulemaking costs to small business concerns\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Small Business Administration.\n**(2) Rule; rule making**\nThe terms rule and rule making have the meanings given those terms in section 551 of title 5, United States Code.\n**(3) Small business concern**\nThe term small business concern has the meaning given the term in section 3 of the Small Business Act ( 15 U.S.C. 632 ).\n**(4) Small business regulatory budget**\nThe term small business regulatory budget means the cost to a small business concern of a rule making conducted by the Small Business Administration, including the cost resulting from the issuance of any new rule and the cost resulting from the modification or repeal of an existing rule.\n##### (b) Requirement\nIn fiscal year 2026, and in each fiscal year thereafter, the Administrator shall ensure that the small business regulatory budget for each small business concern for the applicable fiscal year is not greater than 0.\n##### (c) Report\nNot later than 60 days after the end of fiscal year 2025, and annually thereafter, the Administrator shall submit to Congress a report regarding rules issued by other Federal agencies during the preceding fiscal year that have an impact on small business concerns, which shall\u2014\n**(1)**\ninclude each such rule issued during the preceding fiscal year; and\n**(2)**\nbe disaggregated by the Federal agency that issued each such rule.\n#### 3. No additional funds\nNo additional funds are authorized to be appropriated to carry out this Act.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-02-04",
        "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "387",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Small Business Regulatory Reduction Act",
      "type": "S"
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
        "name": "Commerce",
        "updateDate": "2025-03-10T17:06:51Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr974ih.xml"
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
      "title": "Small Business Regulatory Reduction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T07:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Business Regulatory Reduction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Small Business Administration to ensure that the small business regulatory budget for a small business concern in a fiscal year is not greater than 0, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T07:18:36Z"
    }
  ]
}
```
