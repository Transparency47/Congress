# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2391?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2391
- Title: BUILD Housing Act
- Congress: 119
- Bill type: S
- Bill number: 2391
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-12-05T22:03:30Z
- Update date including text: 2025-12-05T22:03:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2391",
    "number": "2391",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "BUILD Housing Act",
    "type": "S",
    "updateDate": "2025-12-05T22:03:30Z",
    "updateDateIncludingText": "2025-12-05T22:03:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T15:32:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "SD"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2391is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2391\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Kim (for himself and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo designate an environmental review procedure for certain assistance administered by the Secretary of Housing and Urban Development.\n#### 1. Short title\nThis Act may be cited as the Better Use of Intergovernmental and Local Development for Housing Act or the BUILD Housing Act .\n#### 2. Designation of environmental review procedure\nThe Department of Housing and Urban Development Act ( 42 U.S.C. 3531 et seq. ) is amended by inserting after section 12 ( 42 U.S.C. 3537a ) the following:\n13. Designation of environmental review procedure (a) In general Except as provided in subsection (b), the Secretary may, for purposes of environmental review, decision making, and action pursuant to the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), and other provisions of law that further the purposes of such Act, designate the treatment of assistance administered by the Secretary as funds for a special project for purposes of section 305(c) of the Multifamily Housing Property Disposition Reform Act of 1994 ( 42 U.S.C. 3547 ). (b) Exception The designation described in subsection (a) shall not apply to assistance for which a procedure for carrying out the responsibilities of the Secretary under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), and other provisions of law that further the purposes of such Act, is otherwise specified in law. .\n#### 3. Tribal assumption of environmental review obligations\nSection 305(c) of the Multifamily Housing Property Disposition Reform Act of 1994 ( 42 U.S.C. 3547 ) is amended\u2014\n**(1)**\nby striking State or unit of general local government each place it appears and inserting State, Indian Tribe, or unit of general local government ;\n**(2)**\nin paragraph (1)(C), in the heading, by striking State or unit of general local government and inserting State, Indian Tribe, or unit of general local government ; and\n**(3)**\nby adding at the end the following:\n(5) Definition of Indian Tribe For purposes of this subsection, the term Indian Tribe means a federally recognized tribe, as defined in section 4(13)(B) of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103(13)(B) ). .",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-29",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "4810",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BUILD Housing Act",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-16T15:23:50Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2391is.xml"
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
      "title": "BUILD Housing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BUILD Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Better Use of Intergovernmental and Local Development for Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to designate an environmental review procedure for certain assistance administered by the Secretary of Housing and Urban Development.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:23Z"
    }
  ]
}
```
