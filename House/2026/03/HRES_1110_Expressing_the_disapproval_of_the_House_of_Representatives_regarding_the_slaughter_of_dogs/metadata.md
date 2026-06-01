# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1110
- Title: Expressing the disapproval of the House of Representatives regarding the slaughter of dogs and cats for human consumption and encouraging Japan to enact a nationwide ban on such practices.
- Congress: 119
- Bill type: HRES
- Bill number: 1110
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-05-21T08:08:20Z
- Update date including text: 2026-05-21T08:08:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-09 - IntroReferral: Submitted in House
- 2026-03-09 - IntroReferral: Submitted in House
- Latest action: 2026-03-09: Submitted in House

## Actions

- 2026-03-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-09 - IntroReferral: Submitted in House
- 2026-03-09 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1110",
    "number": "1110",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Expressing the disapproval of the House of Representatives regarding the slaughter of dogs and cats for human consumption and encouraging Japan to enact a nationwide ban on such practices.",
    "type": "HRES",
    "updateDate": "2026-05-21T08:08:20Z",
    "updateDateIncludingText": "2026-05-21T08:08:20Z"
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
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:01:00Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "NC"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AZ"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "OH"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "FL"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MD"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1110ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1110\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Garbarino (for himself and Mr. Davis of North Carolina ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nExpressing the disapproval of the House of Representatives regarding the slaughter of dogs and cats for human consumption and encouraging Japan to enact a nationwide ban on such practices.\nThat the House of Representatives\u2014\n**(1)**\nencourages Japan to enact a nationwide ban on the slaughter of dogs and cats for human consumption;\n**(2)**\naffirms the shared values between the United States and Japan regarding the protection of animals, particularly those considered companion animals and service animals;\n**(3)**\nurges continued bilateral cooperation between the United States and Japan on animal rights and animal welfare initiatives;\n**(4)**\ndoes not seek to interfere with or limit religious or cultural practices protected under domestic or international law;\n**(5)**\ncondemns the cruel and inhumane practice of killing and trafficking millions of dogs and cats for meat, which has no place in the 21st century; and\n**(6)**\ncommends the efforts of civil society organizations, including the World Dog Alliance, for their advocacy to end the human consumption of dog and cat meat worldwide.",
      "versionDate": "2026-03-09",
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
        "updateDate": "2026-03-11T22:55:15Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1110ih.xml"
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
      "title": "Expressing the disapproval of the House of Representatives regarding the slaughter of dogs and cats for human consumption and encouraging Japan to enact a nationwide ban on such practices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T08:18:33Z"
    },
    {
      "title": "Expressing the disapproval of the House of Representatives regarding the slaughter of dogs and cats for human consumption and encouraging Japan to enact a nationwide ban on such practices.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T08:05:46Z"
    }
  ]
}
```
