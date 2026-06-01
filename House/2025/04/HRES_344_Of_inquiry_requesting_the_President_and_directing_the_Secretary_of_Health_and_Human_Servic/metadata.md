# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/344?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/344
- Title: Of inquiry requesting the President, and directing the Secretary of Health and Human Services, to transmit respectively, to the House of Representatives certain documents relating to the elimination of the Administration for Community Living-.
- Congress: 119
- Bill type: HRES
- Bill number: 344
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-04-24 - IntroReferral: Submitted in House
- 2025-04-24 - IntroReferral: Submitted in House
- Latest action: 2025-04-24: Submitted in House

## Actions

- 2025-04-24 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-04-24 - IntroReferral: Submitted in House
- 2025-04-24 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/344",
    "number": "344",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Of inquiry requesting the President, and directing the Secretary of Health and Human Services, to transmit respectively, to the House of Representatives certain documents relating to the elimination of the Administration for Community Living-.",
    "type": "HRES",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-04-24T15:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "VA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "FL"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "CT"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MN"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "CA"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CT"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "PA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres344ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 344\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Ms. Bonamici (for herself, Mr. Scott of Virginia , Ms. Wilson of Florida , Mr. Takano , Mrs. Hayes , Ms. Omar , and Mr. DeSaulnier ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nOf inquiry requesting the President, and directing the Secretary of Health and Human Services, to transmit respectively, to the House of Representatives certain documents relating to the elimination of the Administration for Community Living.\nThat the President is requested, and the Secretary of Health and Human Services is directed, to transmit respectively, to the House of Representatives, not later than 14 days after the date of the adoption of this resolution, unredacted copies of all documents, memoranda, legal opinions, notes from meetings, records (including telephone records, electronic mail records, and screen shots), correspondence (electronic or otherwise), and other communications (or any portion of any such communications) that are in the possession of the President or the Secretary, respectively, that refer or relate to the following:\n**(1)**\nThe proposed elimination of the Administration for Community Living.\n**(2)**\nAny reduction in force or other downsizing measures at the Administration for Community Living.\n**(3)**\nAny action taken pursuant to the Health and Human Services March 27, 2025, communication HHS Announces Transformation to Make America Healthy Again , and the accompanying Fact Sheet, resulted in the alteration of the functions and responsibilities of the Administration for Community Living.\n**(4)**\nAny action taken to dismiss career staff in leadership positions within the Administration for Community Living.\n**(5)**\nAny determination made by the Executive Office of the President, the Secretary of Health and Human Services, the Principal Deputy Administrator for the Administration for Community Living, or the staff of the Department of Health and Human Services or the Administration for Community Living, that the staff remaining at the Department after any reduction in force, other downsizing measure, or closure would be sufficient to ensure that the Administrator, the individual designated with the responsibilities of the Administrator if that position no longer exists, or the Assistant Secretary of Aging, as appropriate, could faithfully execute the laws Congress has directed the Administrator or the Assistant Secretary of Aging, as appropriate, to enforce or implement, including but not limited to\u2014\n**(A)**\nthe Older Americans Act of 1965 ( 42 U.S.C. 3001 );\n**(B)**\nthe Assistive Technology Act of 2004 (AT Act) ( 29 U.S.C. 3001 et seq. );\n**(C)**\nthe Developmental Disabilities Assistance and Bill of Rights Act (DD ACT) ( 42 U.S.C. 15001 et seq. ); and\n**(D)**\nthe Rehabilitation Act of 1973 ( 29 U.S.C. 701 et seq. ).\n**(6)**\nAny action taken to terminate a grant awarded by the Department through the Administration for Community Living.",
      "versionDate": "2025-04-24",
      "versionType": "IH"
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
        "updateDate": "2025-05-19T16:17:58Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres344ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Of inquiry requesting the President, and directing the Secretary of Health and Human Services, to transmit respectively, to the House of Representatives certain documents relating to the elimination of the Administration for Community Living-.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T08:18:23Z"
    },
    {
      "title": "Of inquiry requesting the President, and directing the Secretary of Health and Human Services, to transmit respectively, to the House of Representatives certain documents relating to the elimination of the Administration for Community Living-.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T08:05:38Z"
    }
  ]
}
```
