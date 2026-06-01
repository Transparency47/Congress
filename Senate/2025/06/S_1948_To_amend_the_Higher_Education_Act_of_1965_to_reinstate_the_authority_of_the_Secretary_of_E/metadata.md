# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1948?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1948
- Title: POST GRAD Act
- Congress: 119
- Bill type: S
- Bill number: 1948
- Origin chamber: Senate
- Introduced date: 2025-06-04
- Update date: 2025-12-05T21:56:15Z
- Update date including text: 2025-12-05T21:56:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in Senate
- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S3235-3236)
- Latest action: 2025-06-04: Introduced in Senate

## Actions

- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S3235-3236)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1948",
    "number": "1948",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "POST GRAD Act",
    "type": "S",
    "updateDate": "2025-12-05T21:56:15Z",
    "updateDateIncludingText": "2025-12-05T21:56:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S3235-3236)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T21:22:32Z",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "IL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MD"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "OR"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1948is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1948\nIN THE SENATE OF THE UNITED STATES\nJune 4, 2025 Mr. Padilla (for himself, Mr. Booker , Ms. Duckworth , Mr. Kim , Mr. Van Hollen , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to reinstate the authority of the Secretary of Education to make Federal Direct Stafford Loans to graduate and professional students.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Students by Terminating Graduate Rates that Add to Debt Act or the POST GRAD Act .\n#### 2. Reinstatement of authority to make Federal Direct Stafford Loans to graduate and professional students\nSection 455(a)(3) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(a)(3) ) is amended\u2014\n**(1)**\nin the paragraph heading, by inserting Temporary before Termination ; and\n**(2)**\nin subparagraph (A), in the matter preceding clause (i), by inserting , and ending on or before June 30, 2023 after 2012 .\n#### 3. Inapplicability of rulemaking requirements\nThe amendments made by this Act shall not be subject to the requirements of section 482(c) or 492 of the Higher Education Act of 1965 ( 20 U.S.C. 1089(c) ; 1098a).",
      "versionDate": "2025-06-04",
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
        "actionDate": "2025-06-04",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "3711",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "POST GRAD Act",
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
        "name": "Education",
        "updateDate": "2025-06-23T14:13:55Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1948is.xml"
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
      "title": "POST GRAD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "POST GRAD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Our Students by Terminating Graduate Rates that Add to Debt Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to reinstate the authority of the Secretary of Education to make Federal Direct Stafford Loans to graduate and professional students.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-10T02:48:18Z"
    }
  ]
}
```
