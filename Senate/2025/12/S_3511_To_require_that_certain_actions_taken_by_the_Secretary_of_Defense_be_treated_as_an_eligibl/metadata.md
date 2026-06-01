# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3511?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3511
- Title: PRIMED Act
- Congress: 119
- Bill type: S
- Bill number: 3511
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-01-12T16:49:28Z
- Update date including text: 2026-01-12T16:49:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3511",
    "number": "3511",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001208",
        "district": "",
        "firstName": "Elissa",
        "fullName": "Sen. Slotkin, Elissa [D-MI]",
        "lastName": "Slotkin",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "PRIMED Act",
    "type": "S",
    "updateDate": "2026-01-12T16:49:28Z",
    "updateDateIncludingText": "2026-01-12T16:49:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T22:31:01Z",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3511is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3511\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Ms. Slotkin (for herself and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require that certain actions taken by the Secretary of Defense be treated as an eligible transportation project, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Permit Reform In Mining for Energy and Defense Act or the PRIMED Act .\n#### 2. Treatment of certain actions by Secretary of Defense under the Defense Production Act of 1950 for Federal permitting improvement purposes\n##### (a) In general\nExcept as provided in subsection (c), an action described in subsection (b) shall be\u2014\n**(1)**\ntreated as a covered project, as defined in section 41001(6) of the FAST Act ( 42 U.S.C. 4370m(6) ), without regard to whether the action would qualify as a covered project under that section; and\n**(2)**\nincluded in the Permitting Dashboard maintained pursuant to section 41003(b) of that Act ( 42 U.S.C. 4370m\u20132(b) ).\n##### (b) Actions described\nAn action described in this subsection is an action taken by the Secretary of Defense pursuant to Presidential Determination 2022\u201311 (87 Fed. Reg. 19775; relating to certain actions under section 303 of the Defense Production Act of 1950) or the Presidential Memorandum of February 27, 2023, titled Presidential Waiver of Statutory Requirements Pursuant to Section 303 of the Defense Production Act of 1950, as amended, on Department of Defense Supply Chains Resilience (88 Fed. Reg. 13015) to create, maintain, protect, expand, or restore sustainable and responsible domestic production capabilities through\u2014\n**(1)**\nsupporting feasibility studies for mature mining, beneficiation, and value-added processing projects;\n**(2)**\nbyproduct and co-product production at existing mining, mine waste reclamation, and other industrial facilities;\n**(3)**\nmodernization of mining, beneficiation, and value-added processing to increase productivity, environmental sustainability, and workforce safety; or\n**(4)**\nany other activity authorized under section 303(a)(1) of the Defense Production Act of 1950 ( 50 U.S.C. 4533(a)(1) ).\n##### (c) Exception\nAn action described in subsection (b) may not be treated as a covered project or be included in the Permitting Dashboard under subsection (a) if the project sponsor (as defined in section 41001(18) of the FAST Act ( 42 U.S.C. 4370m(18) )) requests that the action not be treated as a covered project.",
      "versionDate": "2025-12-16",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-12T16:49:28Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3511is.xml"
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
      "title": "PRIMED Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-10T09:09:07Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PRIMED Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:09:05Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Permit Reform In Mining for Energy and Defense Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:09:05Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require that certain actions taken by the Secretary of Defense be treated as an eligible transportation project, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:03:27Z"
    }
  ]
}
```
