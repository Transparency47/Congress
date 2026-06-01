# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2158?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2158
- Title: Stopping the Fraudulent Sale of Firearms Act
- Congress: 119
- Bill type: S
- Bill number: 2158
- Origin chamber: Senate
- Introduced date: 2025-06-24
- Update date: 2025-12-05T21:51:23Z
- Update date including text: 2025-12-05T21:51:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in Senate
- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S3517-3518)
- Latest action: 2025-06-24: Introduced in Senate

## Actions

- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S3517-3518)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2158",
    "number": "2158",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "Stopping the Fraudulent Sale of Firearms Act",
    "type": "S",
    "updateDate": "2025-12-05T21:51:23Z",
    "updateDateIncludingText": "2025-12-05T21:51:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S3517-3518)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T21:10:52Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2158is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2158\nIN THE SENATE OF THE UNITED STATES\nJune 24, 2025 Mr. Padilla (for himself, Mr. Blumenthal , Mr. Schiff , Mr. Booker , Mr. Kim , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to make fraudulent dealings in firearms and ammunition unlawful, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping the Fraudulent Sale of Firearms Act .\n#### 2. Fraudulent dealings in firearms\n##### (a) In general\nSection 922(a) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (9), by striking the period and at the end and inserting ; and ; and\n**(2)**\nby adding at the end the following:\n(10) for any person\u2014 (A) to import, manufacture, or sell a firearm or ammunition by means of false or fraudulent pretenses, representations, or promises; and (B) to transmit or cause to be transmitted, by means of wire, radio, or television communication in interstate or foreign commerce, any communication relating to the importation, manufacture, or sale described in subparagraph (A). .\n##### (b) Penalty\nSection 924(a)(1)(B) of title 18, United States Code, is amended by inserting (a)(10), before (f) .",
      "versionDate": "2025-06-24",
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
        "actionDate": "2025-06-30",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4261",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stopping the Fraudulent Sales of Firearms Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-14T15:59:24Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2158is.xml"
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
      "title": "Stopping the Fraudulent Sale of Firearms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-04T02:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stopping the Fraudulent Sale of Firearms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-04T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to make fraudulent dealings in firearms and ammunition unlawful, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-04T02:18:33Z"
    }
  ]
}
```
