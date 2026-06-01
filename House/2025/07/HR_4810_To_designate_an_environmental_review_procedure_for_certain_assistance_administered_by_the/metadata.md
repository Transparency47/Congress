# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4810?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4810
- Title: BUILD Housing Act
- Congress: 119
- Bill type: HR
- Bill number: 4810
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-03-19T08:07:21Z
- Update date including text: 2026-03-19T08:07:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4810",
    "number": "4810",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "L000607",
        "district": "16",
        "firstName": "Sam",
        "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
        "lastName": "Liccardo",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "BUILD Housing Act",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:21Z",
    "updateDateIncludingText": "2026-03-19T08:07:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-07-29T21:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NE"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4810ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4810\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Liccardo (for himself and Mr. Flood ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo designate an environmental review procedure for certain assistance administered by the Secretary of Housing and Urban Development.\n#### 1. Short title\nThis Act may be cited as the Better Use of Intergovernmental and Local Development for Housing Act or the BUILD Housing Act .\n#### 2. Designation of environmental review procedure\nThe Department of Housing and Urban Development Act ( 42 U.S.C. 3531 et seq. ) is amended by inserting after section 12 ( 42 U.S.C. 3537a ) the following:\n13. Designation of environmental review procedure (a) In general Except as provided in subsection (b), the Secretary may, for purposes of environmental review, decision making, and action pursuant to the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), and other provisions of law that further the purposes of such Act, designate the treatment of assistance administered by the Secretary as funds for a special project for purposes of section 305(c) of the Multifamily Housing Property Disposition Reform Act of 1994 ( 42 U.S.C. 3547 ). (b) Exception The designation described in subsection (a) shall not apply to assistance for which a procedure for carrying out the responsibilities of the Secretary under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), and other provisions of law that further the purposes of such Act, is otherwise specified in law. .\n#### 3. Tribal assumption of environmental review obligations\nSection 305(c) of the Multifamily Housing Property Disposition Reform Act of 1994 ( 42 U.S.C. 3547 ) is amended\u2014\n**(1)**\nby striking State or unit of general local government each place it appears and inserting State, Indian Tribe, or unit of general local government ;\n**(2)**\nin paragraph (1)(C), in the heading, by striking State or unit of general local government and inserting State, Indian Tribe, or unit of general local government ; and\n**(3)**\nby adding at the end the following:\n(5) Definition of Indian Tribe For purposes of this subsection, the term Indian Tribe means a federally recognized tribe, as defined in section 4(13)(B) of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103(13)(B) ). .",
      "versionDate": "2025-07-29",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-23",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2391",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BUILD Housing Act",
      "type": "S"
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
        "updateDate": "2025-09-16T15:25:34Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4810ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "updateDate": "2025-08-06T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BUILD Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Better Use of Intergovernmental and Local Development for Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate an environmental review procedure for certain assistance administered by the Secretary of Housing and Urban Development.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T05:48:55Z"
    }
  ]
}
```
