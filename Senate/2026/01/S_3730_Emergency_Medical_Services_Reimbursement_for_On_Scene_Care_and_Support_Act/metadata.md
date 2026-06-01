# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3730?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3730
- Title: Emergency Medical Services Reimbursement for On-Scene Care and Support Act
- Congress: 119
- Bill type: S
- Bill number: 3730
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-20T17:35:25Z
- Update date including text: 2026-02-20T17:35:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3730",
    "number": "3730",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Emergency Medical Services Reimbursement for On-Scene Care and Support Act",
    "type": "S",
    "updateDate": "2026-02-20T17:35:25Z",
    "updateDateIncludingText": "2026-02-20T17:35:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
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
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T17:47:17Z",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-01-29",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "MN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "MN"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "PA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3730is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3730\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Welch (for himself, Mr. Sanders , Ms. Smith , Ms. Klobuchar , Mr. Fetterman , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide Medicare coverage of ambulance services that do not include transportation.\n#### 1. Short title\nThis Act may be cited as the Emergency Medical Services Reimbursement for On-Scene Care and Support Act .\n#### 2. Coverage of ambulance services that do not include transportation\nSection 1861(s)(7) of the Social Security Act ( 42 U.S.C. 1395x(s)(7) ) is amended\u2014\n**(1)**\nby inserting (A) after (7) ;\n**(2)**\nin subparagraph (A), as added by paragraph (1), by inserting and after the semicolon; and\n**(3)**\nby adding at the end the following new subparagraph:\n(B) notwithstanding subparagraph (A), ambulance service includes such services described in such subparagraph that are furnished on or after January 1, 2027, to an individual by a provider or supplier of ambulance services regardless of whether the provider or supplier provides the transport for the individual at a reimbursement comparable to the transport reimbursement; .",
      "versionDate": "2026-01-29",
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
        "actionDate": "2026-01-30",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7277",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Emergency Medical Services Reimbursement for On-Scene and Support Act",
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
        "name": "Health",
        "updateDate": "2026-02-20T17:35:25Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3730is.xml"
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
      "title": "Emergency Medical Services Reimbursement for On-Scene Care and Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T05:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Emergency Medical Services Reimbursement for On-Scene Care and Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide Medicare coverage of ambulance services that do not include transportation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:40Z"
    }
  ]
}
```
