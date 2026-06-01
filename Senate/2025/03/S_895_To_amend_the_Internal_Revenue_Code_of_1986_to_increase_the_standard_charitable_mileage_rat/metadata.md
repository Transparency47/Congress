# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/895?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/895
- Title: DELIVER Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 895
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2025-05-08T18:50:02Z
- Update date including text: 2025-05-08T18:50:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/895",
    "number": "895",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "DELIVER Act of 2025",
    "type": "S",
    "updateDate": "2025-05-08T18:50:02Z",
    "updateDateIncludingText": "2025-05-08T18:50:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T19:28:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s895is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 895\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. King (for himself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the standard charitable mileage rate for delivery of meals to elderly, disabled, frail, and at-risk individuals.\n#### 1. Short title\nThis Act may be cited as the Delivering Elderly Lunches and Increasing Volunteer Engagement and Reimbursements Act of 2025 or the DELIVER Act of 2025 .\n#### 2. Increase in standard mileage rate for delivery of meals to elderly, disabled, frail, and at-risk individuals\n##### (a) In general\nSubsection (i) of section 170 of the Internal Revenue Code of 1986 is amended by adding at the end the following: In the case of use of such an automobile for the delivery of meals to homebound individuals who are elderly, disabled, frail, or at risk, the mileage rate used shall be the standard business mileage rate specified by the Internal Revenue Service for the taxable year in which such miles are driven. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply to miles driven on or after the date of the enactment of this Act.",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-08T18:50:02Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s895is.xml"
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
      "title": "DELIVER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T18:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DELIVER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Delivering Elderly Lunches and Increasing Volunteer Engagement and Reimbursements Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the standard charitable mileage rate for delivery of meals to elderly, disabled, frail, and at-risk individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:03:18Z"
    }
  ]
}
```
