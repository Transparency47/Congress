# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1061?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1061
- Title: Forest Service Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 1061
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-03-06T20:53:15Z
- Update date including text: 2026-04-15T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1061",
    "number": "1061",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Forest Service Accountability Act",
    "type": "S",
    "updateDate": "2026-03-06T20:53:15Z",
    "updateDateIncludingText": "2026-04-15T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T22:28:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "WY"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "UT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "MT"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1061is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1061\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Lee (for himself, Ms. Lummis , Mr. Curtis , Mr. Sheehy , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Department of Agriculture Reorganization Act of 1994 to provide that the President shall appoint, by and with the advice and consent of the Senate, the Chief of the Forest Service.\n#### 1. Short title\nThis Act may be cited as the Forest Service Accountability Act .\n#### 2. Chief of the Forest Service\nSubtitle E of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6961 ) is amended by adding at the end the following:\n246. Chief of the Forest Service (a) Appointment by the President; Senate advice and consent The President shall appoint, by and with the advice and consent of the Senate, the Chief of the Forest Service. (b) Qualifications An individual appointed under subsection (a) shall have substantial experience and demonstrated competence in forest and natural resources management. (c) Committee referral (1) In general Any nomination of an individual to be the Chief of the Forest Service submitted to the Senate for confirmation, and referred to a committee, shall be referred jointly to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Energy and Natural Resources of the Senate. (2) Rules of Senate Paragraph (1) is enacted\u2014 (A) as an exercise of the rulemaking power of the Senate, and as such is deemed a part of the rules of the Senate and supersedes other rules only to the extent that they are inconsistent with such rules; and (B) with full recognition of the constitutional right of the Senate to change the rules at any time, in the same manner, and to the same extent as in the case of any other rule of the Senate. (d) Application to incumbent Notwithstanding any service by an individual serving in the position of Chief of the Forest Service on the date of enactment of this section, the President shall submit to the Senate a nomination for an individual to be the Chief of the Forest Service not later than 30 days after that date of enactment. .",
      "versionDate": "2025-03-13",
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
        "actionDate": "2025-03-28",
        "text": "Referred to the Subcommittee on Forestry and Horticulture."
      },
      "number": "1762",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Forest Service Accountability Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Department of Agriculture",
            "updateDate": "2026-03-06T20:53:09Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2026-03-06T20:53:15Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2026-03-06T20:52:59Z"
          },
          {
            "name": "Senate",
            "updateDate": "2026-03-06T20:53:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-14T12:39:17Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1061is.xml"
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
      "title": "Forest Service Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Forest Service Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Department of Agriculture Reorganization Act of 1994 to provide that the President shall appoint, by and with the advice and consent of the Senate, the Chief of the Forest Service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:26Z"
    }
  ]
}
```
