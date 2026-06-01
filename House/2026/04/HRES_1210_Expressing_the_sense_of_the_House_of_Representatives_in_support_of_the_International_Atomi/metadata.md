# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1210?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1210
- Title: Expressing the sense of the House of Representatives in support of the International Atomic Energy Agency's (IAEA) nuclear security role.
- Congress: 119
- Bill type: HRES
- Bill number: 1210
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-04-27T22:52:43Z
- Update date including text: 2026-04-27T22:52:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-23 - IntroReferral: Submitted in House
- Latest action: 2026-04-23: Submitted in House

## Actions

- 2026-04-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1210",
    "number": "1210",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Expressing the sense of the House of Representatives in support of the International Atomic Energy Agency's (IAEA) nuclear security role.",
    "type": "HRES",
    "updateDate": "2026-04-27T22:52:43Z",
    "updateDateIncludingText": "2026-04-27T22:52:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
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
          "date": "2026-04-23T13:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "VA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "DC"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "IL"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "WA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "IL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NV"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1210ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1210\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Foster (for himself, Mr. Beyer , Mr. Castro of Texas , Ms. Norton , Mr. Khanna , Mr. Krishnamoorthi , Mr. Larsen of Washington , Mr. McGovern , Ms. Schakowsky , Ms. Titus , and Mr. Moulton ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nExpressing the sense of the House of Representatives in support of the International Atomic Energy Agency\u2019s (IAEA) nuclear security role.\nThat the House of Representatives\u2014\n**(1)**\nmaintains that the International Atomic Energy Agency (IAEA) plays an indispensable role in strengthening nuclear security and safety around the globe;\n**(2)**\nreaffirms that the United States has a vital interest in preventing the spread of nuclear weapons and securing nuclear materials; and\n**(3)**\nencourages the United States and other member states of the IAEA to take steps to ensure that the IAEA has the resources needed to successfully carry out its duties, including\u2014\n**(A)**\nsupporting the IAEA to continue convening ministerial meetings on nuclear security to promote political commitment;\n**(B)**\ncontributing to the implementation of the IAEA\u2019s Nuclear Security Plan through reliable and sufficient resources;\n**(C)**\nproviding appropriate political, technical, and financial support to the Nuclear Security Fund; and\n**(D)**\ndeveloping a comprehensive strategy to encourage non-state, private sector contributions to the Nuclear Security Fund.",
      "versionDate": "2026-04-23",
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
        "name": "International Affairs",
        "updateDate": "2026-04-27T22:52:43Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1210ih.xml"
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
      "title": "Expressing the sense of the House of Representatives in support of the International Atomic Energy Agency's (IAEA) nuclear security role.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-24T08:18:43Z"
    },
    {
      "title": "Expressing the sense of the House of Representatives in support of the International Atomic Energy Agency's (IAEA) nuclear security role.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T08:06:50Z"
    }
  ]
}
```
