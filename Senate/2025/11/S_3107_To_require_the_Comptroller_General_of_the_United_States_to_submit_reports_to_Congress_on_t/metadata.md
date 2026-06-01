# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3107
- Title: USPS Act
- Congress: 119
- Bill type: S
- Bill number: 3107
- Origin chamber: Senate
- Introduced date: 2025-11-05
- Update date: 2025-12-09T21:09:26Z
- Update date including text: 2025-12-09T21:09:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-05: Introduced in Senate
- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-11-05: Introduced in Senate

## Actions

- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-05",
    "latestAction": {
      "actionDate": "2025-11-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3107",
    "number": "3107",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "USPS Act",
    "type": "S",
    "updateDate": "2025-12-09T21:09:26Z",
    "updateDateIncludingText": "2025-12-09T21:09:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-05",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-05",
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
          "date": "2025-11-05T19:36:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-11-05",
      "state": "MS"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-05",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3107is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3107\nIN THE SENATE OF THE UNITED STATES\nNovember 5, 2025 Mr. Cruz (for himself, Mrs. Hyde-Smith , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Comptroller General of the United States to submit reports to Congress on theft of mail and United States Postal Service property, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Upholding a Secure Postal System Act or the USPS Act .\n#### 2. Reports on mail and Postal Service property theft\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act and each year thereafter for 5 years, the Comptroller General of the United States shall investigate nationwide patterns and instances of theft of mail and United States Postal Service property and submit a report on each such investigation to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives.\n##### (b) Contents\nEach report under subsection (a) shall include a description of any measures the Postal Service has in place to address such theft, and recommendations on how the Postal Service and Congress can combat such theft.\n##### (c) Consultation\nIn carrying out this section, the Comptroller General shall consult with the Inspector General of the Postal Service and the United States Postal Inspection Service.",
      "versionDate": "2025-11-05",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-09T21:09:26Z"
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
      "date": "2025-11-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3107is.xml"
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
      "title": "USPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "USPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Upholding a Secure Postal System Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Comptroller General of the United States to submit reports to Congress on theft of mail and United States Postal Service property, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:18:20Z"
    }
  ]
}
```
