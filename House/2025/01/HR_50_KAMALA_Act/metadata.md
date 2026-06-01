# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/50?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/50
- Title: KAMALA Act
- Congress: 119
- Bill type: HR
- Bill number: 50
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-01-22T20:26:16Z
- Update date including text: 2026-01-22T20:26:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/50",
    "number": "50",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "KAMALA Act",
    "type": "HR",
    "updateDate": "2026-01-22T20:26:16Z",
    "updateDateIncludingText": "2026-01-22T20:26:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:08:40Z",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr50ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 50\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Ogles , Mr. Crane , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prohibit grants provided under section 106 of the Housing and Community Development Act of 1974 from being used to assist persons who are neither a national of the United States nor lawfully admitted for permanent residence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Keeping Aid for Municipalities And Localities Accountable Act or the KAMALA Act .\n#### 2. Prohibition on assistance for persons not lawfully present\n##### (a) In general\nSection 105 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5305 ) is amended by adding at the end the following:\n(i) Prohibition on use of assistance for persons not lawfully present Notwithstanding any other provision of law, no amount from a grant under section 106 made in fiscal year 2024 or any succeeding fiscal year may be used to assist persons who are neither a national of the United States nor lawfully admitted for permanent residence under section 101(a)(20) of the Immigration and Nationality Act. .\n#### 3. Prohibition on grants to entities that provide assistance to persons not lawfully present\nSection 103 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5303 ) is amended\u2014\n**(1)**\nby striking The Secretary is authorized to and inserting:\n(a) In general The Secretary is authorized to ; and\n**(2)**\nby adding at the end the following:\n(b) Limitation The Secretary may not make a grant to any State, unit of general local government, or Indian tribe to carry out activities in accordance with the provisions of this title if such State, unit of general local government, or Indian tribe carries out any housing or community development related program that provides assistance to persons who are neither a national of the United States nor lawfully admitted for permanent residence under section 101(a)(20) of the Immigration and Nationality Act. .",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-06-04T14:55:18Z"
          },
          {
            "name": "Department of Housing and Urban Development",
            "updateDate": "2025-06-04T14:55:07Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-06-04T14:52:19Z"
          },
          {
            "name": "Housing supply and affordability",
            "updateDate": "2025-06-04T14:50:58Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-06-04T14:48:59Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-06-04T14:49:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-03T14:50:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr50",
          "measure-number": "50",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr50v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keeping Aid for Municipalities And Localities Accountable Act or the KAMALA Act</strong></p><p>This bill prohibits the use of Community Development Block Grant (CDBG) funding to assist non-U.S. nationals (<em>aliens</em> under federal law) who are not lawfully admitted permanent residents. The CDBG program is administered by the Department of Housing and Urban Development (HUD) and provides states, local governments, and Indian tribes with funds for economic and community development.</p><p>The bill also specifically prohibits HUD from making a CDBG grant to any state, local government, or Indian tribe that carries out a housing or community development program that assists such individuals.\u00a0</p>"
        },
        "title": "KAMALA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr50.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keeping Aid for Municipalities And Localities Accountable Act or the KAMALA Act</strong></p><p>This bill prohibits the use of Community Development Block Grant (CDBG) funding to assist non-U.S. nationals (<em>aliens</em> under federal law) who are not lawfully admitted permanent residents. The CDBG program is administered by the Department of Housing and Urban Development (HUD) and provides states, local governments, and Indian tribes with funds for economic and community development.</p><p>The bill also specifically prohibits HUD from making a CDBG grant to any state, local government, or Indian tribe that carries out a housing or community development program that assists such individuals.\u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr50"
    },
    "title": "KAMALA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keeping Aid for Municipalities And Localities Accountable Act or the KAMALA Act</strong></p><p>This bill prohibits the use of Community Development Block Grant (CDBG) funding to assist non-U.S. nationals (<em>aliens</em> under federal law) who are not lawfully admitted permanent residents. The CDBG program is administered by the Department of Housing and Urban Development (HUD) and provides states, local governments, and Indian tribes with funds for economic and community development.</p><p>The bill also specifically prohibits HUD from making a CDBG grant to any state, local government, or Indian tribe that carries out a housing or community development program that assists such individuals.\u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr50"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr50ih.xml"
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
      "title": "KAMALA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T11:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "KAMALA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keeping Aid for Municipalities And Localities Accountable Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit grants provided under section 106 of the Housing and Community Development Act of 1974 from being used to assist persons who are neither a national of the United States nor lawfully admitted for permanent residence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T11:18:27Z"
    }
  ]
}
```
