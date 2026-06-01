# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1993?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1993
- Title: RIPPLE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1993
- Origin chamber: Senate
- Introduced date: 2025-06-09
- Update date: 2025-12-05T22:55:23Z
- Update date including text: 2025-12-05T22:55:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in Senate
- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-09: Introduced in Senate

## Actions

- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1993",
    "number": "1993",
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
    "title": "RIPPLE Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:55:23Z",
    "updateDateIncludingText": "2025-12-05T22:55:23Z"
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
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
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
          "date": "2025-06-09T22:33:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1993is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1993\nIN THE SENATE OF THE UNITED STATES\nJune 9, 2025 Mrs. Moody (for herself and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo permit limited reimbursements for the cost of salaries and overtime pay for employees of States performing the functions of immigration officers, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Reimbursements for Immigration Partnerships with Police to allow Local Enforcement Act of 2025 or the RIPPLE Act of 2025 .\n#### 2. Reimbursements to States and localities for performance of immigration functions\nSection 287(g)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g)(1) ) is amended by adding at the end the following: The Attorney General may reimburse a State or a political subdivision for costs incurred by the State or political subdivision for wages (as defined in section 3121(a) of the Internal Revenue Code of 1986), including the renumeration of overtime compensation (as defined in section 7 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 207 )), or salary to an officer or employee of such State or political subdivision for the performance of a function under an agreement under this subsection. .",
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
        "actionDate": "2025-06-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3882",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RIPPLE Act of 2025",
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
        "updateDate": "2025-06-30T13:11:41Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1993is.xml"
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
      "title": "RIPPLE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RIPPLE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reimbursements for Immigration Partnerships with Police to allow Local Enforcement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to permit limited reimbursements for the cost of salaries and overtime pay for employees of States performing the functions of immigration officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:34:05Z"
    }
  ]
}
```
