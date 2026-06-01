# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7869?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7869
- Title: RAD Conversion Continuity Act
- Congress: 119
- Bill type: HR
- Bill number: 7869
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-02T19:17:54Z
- Update date including text: 2026-04-02T19:17:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7869",
    "number": "7869",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "RAD Conversion Continuity Act",
    "type": "HR",
    "updateDate": "2026-04-02T19:17:54Z",
    "updateDateIncludingText": "2026-04-02T19:17:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:02:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7869ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7869\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Goldman of New York introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo allow public housing projects under the rental demonstration program to retain prior approval of housing plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rental Assistance Demonstration Conversion Continuity Act or the RAD Conversion Continuity Act .\n#### 2. Approvals related to rental assistance demonstration program\n##### (a) In general\nWith respect to a public housing project under the rental assistance demonstration program, such project for which housing plans have been approved under section 7 of the United States Housing Act of 1937 ( 42 U.S.C. 1437e ) may\u2014\n**(1)**\nretain such approval after conversion to the rental assistance demonstration program; and\n**(2)**\ncontinue to use such approval process for any future approval.\n##### (b) Requirements\nA project that retains approval pursuant to subsection (a) shall\u2014\n**(1)**\ncontinue to be subject to any terms or conditions of such approval; and\n**(2)**\ngo through the same process to receive a certification as such project initially was certified under section 9 of the United States Housing Act of 1937 ( 42 U.S.C. 1437g ).\n##### (c) Rental assistance demonstration program defined\nIn this section, the term rental assistance demonstration program means the program described under the heading Rental Assistance Demonstration in title II of the Transportation, Housing and Urban Development, and Related Agencies Appropriations Act, 2012 (division C of Public Law 112\u201355 ; 125 Stat. 673).",
      "versionDate": "2026-03-09",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-04-02T19:17:54Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7869ih.xml"
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
      "title": "RAD Conversion Continuity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RAD Conversion Continuity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rental Assistance Demonstration Conversion Continuity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow public housing projects under the rental demonstration program to retain prior approval of housing plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:22Z"
    }
  ]
}
```
