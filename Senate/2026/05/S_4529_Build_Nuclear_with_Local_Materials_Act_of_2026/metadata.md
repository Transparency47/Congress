# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4529?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4529
- Title: Build Nuclear with Local Materials Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4529
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-29T16:56:00Z
- Update date including text: 2026-05-29T16:56:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2026-05-20 - Committee: Committee on Environment and Public Works Subcommittee on Clean Air, Climate, and Nuclear Innovation and Safety. Hearings held.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2026-05-20 - Committee: Committee on Environment and Public Works Subcommittee on Clean Air, Climate, and Nuclear Innovation and Safety. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4529",
    "number": "4529",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Build Nuclear with Local Materials Act of 2026",
    "type": "S",
    "updateDate": "2026-05-29T16:56:00Z",
    "updateDateIncludingText": "2026-05-29T16:56:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Clean Air, Climate, and Nuclear Innovation and Safety Subcommittee Subcommittee",
          "systemCode": "ssev10"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works Subcommittee on Clean Air, Climate, and Nuclear Innovation and Safety. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T16:13:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T18:15:53Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Clean Air, Climate, and Nuclear Innovation and Safety Subcommittee Subcommittee",
          "systemCode": "ssev10"
        }
      },
      "systemCode": "ssev00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4529is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4529\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Ms. Lummis (for herself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo require the Nuclear Regulatory Commission to allow the use of commercial-grade steel and concrete in non-safety-related structures at nuclear power plants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Build Nuclear with Local Materials Act of 2026 .\n#### 2. Use of commercial-grade steel and concrete\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, the Nuclear Regulatory Commission (referred to in this section as the Commission ) shall initiate a rulemaking that authorizes the use of commercial-grade steel and concrete in non-safety-related structures at nuclear power plants, unless, subject to subsection (b), the Commission determines that stricter material standards are necessary to address a specific safety risk.\n##### (b) Determination\nThe Commission may make a determination under subsection (a) that stricter material standards are necessary to address a specific safety risk if the Commission determines that not using a stricter material standard would be contrary to the common defense and security and adequate protection of the public health and safety (within the meaning of section 182 a. of the Atomic Energy Act of 1954 ( 42 U.S.C. 2232(a) )).",
      "versionDate": "2026-05-14",
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
        "name": "Energy",
        "updateDate": "2026-05-29T16:56:00Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4529is.xml"
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
      "title": "Build Nuclear with Local Materials Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:38Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Build Nuclear with Local Materials Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T03:08:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Nuclear Regulatory Commission to allow the use of commercial-grade steel and concrete in non-safety-related structures at nuclear power plants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T03:03:24Z"
    }
  ]
}
```
