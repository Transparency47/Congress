# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4200?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4200
- Title: End DED Act
- Congress: 119
- Bill type: HR
- Bill number: 4200
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2025-07-25T12:24:04Z
- Update date including text: 2025-07-25T12:24:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4200",
    "number": "4200",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "End DED Act",
    "type": "HR",
    "updateDate": "2025-07-25T12:24:04Z",
    "updateDateIncludingText": "2025-07-25T12:24:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "WI"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AZ"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TX"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "PA"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4200ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4200\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Roy (for himself, Mr. Tiffany , Mr. Gill of Texas , Mr. Crane , Mr. Cloud , and Mr. Perry ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide that no Federal funds may be used for the Deferred Enforced Departure Program, or any successor program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End DED Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 1990, the George H.W. Bush administration first used Deferred Enforced Departure (DED) to avoid removing aliens present in the United States whose home countries could not accept their safe return. DED has no statutory basis in the Immigration and Nationality Act and was never approved by Congress.\n**(2)**\nThe constitutional powers to conduct foreign relations of the President are cited as a basis for DED. However, when the executive branch defers the removal of aliens, it is an immigration benefit, not a foreign policy function. Congress has plenary power over immigration, giving it almost complete authority to decide whether certain aliens may enter or remain in the United States.\n**(3)**\nIn 1990, Congress established Temporary Protected Status (TPS) as a part of the Immigration Act of 1990 to provide temporary protection from removal for foreign nationals whose home countries face ongoing armed conflict, environmental disaster, or other extraordinary circumstances preventing their safe return home.\n**(4)**\nDED recipients are granted work authorization and may be permitted to travel outside the United States, the same as TPS holders.\n**(5)**\nSince 1990, the executive branch has designated DED for certain nationals from the following nine countries: China, Kuwait, El Salvador, Haiti, Liberia, Venezuela, Palestine, Hong Kong, and Lebanon.\n**(6)**\nArticle 1, section 8, clause 18 of the Constitution gives Congress clear jurisdiction on immigration matters. The use of DED through sole executive action undermines Congress's authority to regulate immigration programs in the United States. Congress created TPS to provide certain aliens relief from removal under similar life-threatening circumstances.\n#### 3. No Federal funds for deferred enforced departure\nNotwithstanding any other provision of law, no Federal funds, resources, or fees, made available to the President of the United States, the Secretary of Homeland Security, the Attorney General, the Secretary of State, or to any other official of a Federal agency, by any Act for any fiscal year, may be used to implement, administer or carry out the Deferred Enforced Departure Program, or any successor program.",
      "versionDate": "2025-06-26",
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
        "name": "Immigration",
        "updateDate": "2025-07-25T12:24:04Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4200ih.xml"
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
      "title": "End DED Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-15T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End DED Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that no Federal funds may be used for the Deferred Enforced Departure Program, or any successor program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-15T04:18:32Z"
    }
  ]
}
```
