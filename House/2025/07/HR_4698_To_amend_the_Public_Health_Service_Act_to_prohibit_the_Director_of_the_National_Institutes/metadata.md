# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4698?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4698
- Title: PAAW Act
- Congress: 119
- Bill type: HR
- Bill number: 4698
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-08T08:05:56Z
- Update date including text: 2026-05-08T08:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4698",
    "number": "4698",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "PAAW Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:05:56Z",
    "updateDateIncludingText": "2026-05-08T08:05:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:14:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
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
      "sponsorshipDate": "2025-07-23",
      "state": "DC"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IN"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NV"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "HI"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4698ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4698\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Mace (for herself, Mr. Soto , Mr. Obernolte , Mr. Davis of North Carolina , Mr. Lawler , Ms. Norton , Mr. Nehls , Mr. Carson , Ms. Malliotakis , Ms. Titus , Mr. Webster of Florida , Ms. Tokuda , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to prohibit the Director of the National Institutes of Health from conducting or funding research that causes significant pain or distress to a dog or cat, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Animal Abuse and Waste Act or the PAAW Act .\n#### 2. Prohibition on research causing significant pain or distress to dogs and cats\n##### (a) In general\nSubpart 6 of part C of title IV of the Public Health Service Act ( 42 U.S.C. 285f et seq. ) is amended by adding at the end the following:\n447E. Prohibition on research causing significant pain or distress to dogs and cats (a) In general The Director of NIH may not conduct or support any research that causes significant pain or distress to a dog or cat. (b) Definition In this section, the term research that causes significant pain or distress includes any study that includes an assignment of pain category D or E, as defined by the Pain and Distress Categories of the Department of Agriculture (or such successor categories developed pursuant to section 13 of the Animal Welfare Act ( 7 U.S.C. 2143 )). .\n##### (b) Applicability\nThe amendment made by subsection (a) applies beginning on the date that is 90 days after the date of enactment of this Act.",
      "versionDate": "2025-07-23",
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
        "name": "Health",
        "updateDate": "2025-09-17T17:22:11Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4698ih.xml"
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
      "title": "PAAW Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PAAW Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Animal Abuse and Waste Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to prohibit the Director of the National Institutes of Health from conducting or funding research that causes significant pain or distress to a dog or cat, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:48:35Z"
    }
  ]
}
```
