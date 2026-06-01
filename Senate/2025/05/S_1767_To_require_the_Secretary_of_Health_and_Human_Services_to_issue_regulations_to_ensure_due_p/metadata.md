# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1767?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1767
- Title: Physician and Patient Safety Act
- Congress: 119
- Bill type: S
- Bill number: 1767
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2025-12-05T22:49:07Z
- Update date including text: 2025-12-05T22:49:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1767",
    "number": "1767",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Physician and Patient Safety Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:07Z",
    "updateDateIncludingText": "2025-12-05T22:49:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T21:29:31Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "MA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1767is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1767\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Marshall (for himself and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require the Secretary of Health and Human Services to issue regulations to ensure due process rights for physicians before any termination, restriction, or reduction of the professional activity of such physicians or staff privileges of such physicians.\n#### 1. Short title\nThis Act may be cited as the Physician and Patient Safety Act .\n#### 2. Regulations to ensure due process rights for physicians\n##### (a) In general\nThe Secretary of Health and Human Services shall issue final regulations to provide that physicians who have been granted medical staff privileges at a hospital have a fair hearing and appellate review through appropriate medical staff mechanisms before any termination, restriction, or reduction of the professional activity of such physicians or staff privileges of such physicians at such hospital.\n##### (b) Requirements of regulations\nThe regulations described in subsection (a) shall provide that\u2014\n**(1)**\na hearing or appellate review may not be denied through a third-party contract;\n**(2)**\na physician shall not be requested or required to waive their rights to such a hearing or appellate review as a condition of employment, either with the hospital or with a third-party contractor; and\n**(3)**\nany such hearing or appellate review shall be confidential and not reportable to any entity, including the National Practitioner Data Bank or future workplaces or employers, unless there is an ongoing threat to patient safety, or as otherwise required under the reporting requirements for hospitals established by the National Practitioner Data Bank.\n##### (c) Effective date\nThe final regulations promulgated under subsection (a) shall take effect not later than 18 months after the date of enactment of this Act.",
      "versionDate": "2025-05-14",
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
        "actionDate": "2025-05-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3413",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Physician and Patient Safety Act",
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
        "updateDate": "2025-05-28T17:04:18Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1767is.xml"
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
      "title": "Physician and Patient Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Physician and Patient Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Health and Human Services to issue regulations to ensure due process rights for physicians before any termination, restriction, or reduction of the professional activity of such physicians or staff privileges of such physicians.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:49Z"
    }
  ]
}
```
