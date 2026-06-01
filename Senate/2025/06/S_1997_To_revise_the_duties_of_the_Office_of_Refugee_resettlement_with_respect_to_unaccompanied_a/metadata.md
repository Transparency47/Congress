# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1997?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1997
- Title: Stop GAPS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1997
- Origin chamber: Senate
- Introduced date: 2025-06-09
- Update date: 2025-12-05T22:55:55Z
- Update date including text: 2025-12-05T22:55:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in Senate
- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-09: Introduced in Senate

## Actions

- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1997",
    "number": "1997",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Stop GAPS Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:55:55Z",
    "updateDateIncludingText": "2025-12-05T22:55:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-09",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-06-09T22:27:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1997is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1997\nIN THE SENATE OF THE UNITED STATES\nJune 9, 2025 Mrs. Moody introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo revise the duties of the Office of Refugee resettlement with respect to unaccompanied alien children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Government Abandonment and Placement Scandals Act of 2025 or the Stop GAPS Act of 2025 .\n#### 2. Sponsors for unaccompanied minors\nThe Secretary of Homeland Security shall amend section 410.1201(a) of title 45, Code of Federal Regulations, by striking paragraph (6).\n#### 3. Duty of Office of Refugee Resettlement\nThe Director of the Office of Refugee Resettlement shall\u2014\n**(1)**\ntrack each unaccompanied alien child (as defined in section 462(g) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g) )) released from the custody of the Department of Homeland Security while such unaccompanied alien child\u2014\n**(A)**\nis in the United States; and\n**(B)**\ninvolved in ongoing immigration proceedings; and\n**(2)**\nwork with States to find placements for such unaccompanied alien children.",
      "versionDate": "2025-06-09",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4349",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop GAPS Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-07-02T18:11:42Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1997is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Stop GAPS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T11:03:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop GAPS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Government Abandonment and Placement Scandals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to revise the duties of the Office of Refugee resettlement with respect to unaccompanied alien children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:29Z"
    }
  ]
}
```
