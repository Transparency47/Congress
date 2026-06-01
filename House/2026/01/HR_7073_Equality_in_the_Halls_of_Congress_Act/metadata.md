# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7073?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7073
- Title: Equality in the Halls of Congress Act
- Congress: 119
- Bill type: HR
- Bill number: 7073
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-02-04T18:52:05Z
- Update date including text: 2026-02-04T18:52:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7073",
    "number": "7073",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "Equality in the Halls of Congress Act",
    "type": "HR",
    "updateDate": "2026-02-04T18:52:05Z",
    "updateDateIncludingText": "2026-02-04T18:52:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "VI"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "PR"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "MP"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "AS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7073ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7073\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. Moylan (for himself, Ms. Plaskett , Mr. Hern\u00e1ndez , Ms. King-Hinds , and Mrs. Radewagen ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo permit the territories and commonwealths of the United States to provide and furnish statues to the National Statuary Hall Collection.\n#### 1. Short title\nThis Act may be cited as the Equality in the Halls of Congress Act .\n#### 2. Statues from territories and commonwealths in the National Statuary Hall Collection\n##### (a) Placement of statues\nEach of the following may provide and furnish statues for the National Statuary Hall Collection, in accordance with the specifications applicable to the statues provided and furnished by the States under section 1814 of the Revised Statutes of the United States ( 2 U.S.C. 2131 ) and other applicable law:\n**(1)**\nAmerican Samoa.\n**(2)**\nGuam.\n**(3)**\nThe Commonwealth of the Northern Mariana Islands.\n**(4)**\nThe Commonwealth of Puerto Rico.\n**(5)**\nThe United States Virgin Islands.\n##### (b) Conforming amendment\nSection 311 of the Legislative Branch Appropriations Act, 2001 ( 2 U.S.C. 2132 ) is amended by adding at the end the following new subsection:\n(f) In this section, the term State includes American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, the Commonwealth of Puerto Rico, and the United States Virgin Islands. .\n##### (c) Authority of the Architect of the Capitol\nThe Architect of the Capitol shall take such measures necessary to acquire the statues described in this section and to carry out this Act and the amendment made by this Act, including such measures taken on behalf of the Joint Committee of Congress on the Library.",
      "versionDate": "2026-01-14",
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
        "name": "Congress",
        "updateDate": "2026-02-04T18:52:05Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7073ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To permit the territories and commonwealths of the United States to provide and furnish statues to the National Statuary Hall Collection.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:45Z"
    },
    {
      "title": "Equality in the Halls of Congress Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Equality in the Halls of Congress Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```
