# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/501?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/501
- Title: BUDS Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 501
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-09-18T08:06:54Z
- Update date including text: 2025-09-18T08:06:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Rules.
- 2025-06-11 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Submitted in House
- Latest action: 2025-06-11: Submitted in House

## Actions

- 2025-06-11 - IntroReferral: Referred to the House Committee on Rules.
- 2025-06-11 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/501",
    "number": "501",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001061",
        "district": "5",
        "firstName": "Emanuel",
        "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
        "lastName": "Cleaver",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "BUDS Resolution",
    "type": "HRES",
    "updateDate": "2025-09-18T08:06:54Z",
    "updateDateIncludingText": "2025-09-18T08:06:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "SC"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "OH"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "FL"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "GU"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "NY"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "IL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "NE"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "TX"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "WA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "MP"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres501ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 501\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Cleaver (for himself, Mrs. Kim , Mr. Peters , Mr. Timmons , Mr. Mullin , Mr. Carey , Ms. Castor of Florida , Mr. Moylan , Mr. Frost , Mr. Lawler , Mr. Quigley , and Mr. Bacon ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nAuthorizing two Members to serve as joint sponsors of a bill, resolution, or joint resolution in the House of Representatives if one of the Members is from the majority party and the other is from the minority party.\n#### 1. Short title\nThis resolution may be cited as the Building Unity through Dual Sponsors Resolution or the BUDS Resolution .\n#### 2. Joint sponsorship of bills and resolutions\n##### (a) Authorizing joint sponsorship\nClause 7 of rule XII of the Rules of the House of Representatives is amended by adding at the end the following new paragraph:\n(e) A public bill or public resolution may be sponsored jointly by two Members, including the Delegates and the Resident Commissioner, if one of the Members is from the majority party and the other Member is from the minority party. .\n##### (b) Conforming amendment relating to authority To name cosponsors\nClause 7(b)(1) of rule XII of the Rules of the House of Representatives is amended by inserting after the first sentence the following: In the case of a public bill or public resolution which is sponsored jointly by two Members pursuant to paragraph (e), both of the sponsors may name cosponsors. .\n##### (c) Conforming amendment relating to submission of constitutional authority statement\nClause 7(c)(1) of rule XII of the Rules of the House of Representatives is amended by striking the sponsor submits and inserting the sponsor submits (or, in the case of a public bill or public resolution which is sponsored jointly by two Members pursuant to paragraph (e), both of the sponsors submit) .",
      "versionDate": "2025-06-11",
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
        "name": "Congress",
        "updateDate": "2025-06-26T14:40:52Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres501ih.xml"
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
      "title": "BUDS Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BUDS Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Building Unity through Dual Sponsors Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Authorizing two Members to serve as joint sponsors of a bill, resolution, or joint resolution in the House of Representatives if one of the Members is from the majority party and the other is from the minority party.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T08:18:21Z"
    }
  ]
}
```
