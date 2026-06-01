# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2731?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2731
- Title: Empowering Striking Workers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2731
- Origin chamber: Senate
- Introduced date: 2025-09-08
- Update date: 2026-02-10T12:03:17Z
- Update date including text: 2026-04-15T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in Senate
- 2025-09-08 - IntroReferral: Introduced in Senate
- 2025-09-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-08: Introduced in Senate

## Actions

- 2025-09-08 - IntroReferral: Introduced in Senate
- 2025-09-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2731",
    "number": "2731",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Empowering Striking Workers Act of 2025",
    "type": "S",
    "updateDate": "2026-02-10T12:03:17Z",
    "updateDateIncludingText": "2026-04-15T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
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
        "item": [
          {
            "date": "2025-09-08T21:07:29Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-08T21:07:29Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "AZ"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NJ"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-02-09",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2731is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2731\nIN THE SENATE OF THE UNITED STATES\nSeptember 8, 2025 Mr. Schiff introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 and the Social Security Act to provide that an individual engaged in a labor dispute may receive unemployment benefits.\n#### 1. Short title\nThis Act may be cited as the Empowering Striking Workers Act of 2025 .\n#### 2. Unemployment insurance for striking workers\n##### (a) In general\nSection 3304(a) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (18), by striking the period at the end of paragraph (19) and inserting ; and , and by adding at the end the following:\n(20) in the case of an individual who is employed but unable to work due to a labor dispute (including any controversy concerning terms, tenure or conditions of employment, or concerning the association or representation of persons in negotiating, fixing, maintaining, changing, or seeking to arrange terms or conditions of employment, regardless of whether the disputants stand in the proximate relation of employer and employee), including an individual unable to work as an indirect result of such a labor dispute, compensation is payable to such individual as though such individual were unemployed beginning on the date that is the earlier of\u2014 (A) the date that is 14 days after the date on which a strike began; (B) the date on which a lock-out began; (C) the date on which the employer hired permanent replacement workers; or (D) the date on which the strike or lock-out ended and the individual became unemployed. .\n##### (b) Exemption from work availability requirement\nSection 303(a)(12) of the Social Security Act ( 42 U.S.C. 503(a)(12) ) is amended by inserting (other than a claimant who is an individual unable to work due to a labor dispute as described in section 3304(a)(20) of the Internal Revenue Code of 1986) after claimant .",
      "versionDate": "2025-09-08",
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
        "actionDate": "2025-09-08",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5206",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Empowering Striking Workers Act of 2025",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-23T15:07:55Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2731is.xml"
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
      "title": "Empowering Striking Workers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Empowering Striking Workers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T04:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 and the Social Security Act to provide that an individual engaged in a labor dispute may receive unemployment benefits.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T04:48:14Z"
    }
  ]
}
```
