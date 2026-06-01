# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6997?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6997
- Title: Community Passport Services Access Act
- Congress: 119
- Bill type: HR
- Bill number: 6997
- Origin chamber: House
- Introduced date: 2026-01-09
- Update date: 2026-04-29T08:06:58Z
- Update date including text: 2026-04-29T08:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-09: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-01-09: Introduced in House

## Actions

- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-09",
    "latestAction": {
      "actionDate": "2026-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6997",
    "number": "6997",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000302",
        "district": "13",
        "firstName": "John",
        "fullName": "Rep. Joyce, John [R-PA-13]",
        "lastName": "Joyce",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Community Passport Services Access Act",
    "type": "HR",
    "updateDate": "2026-04-29T08:06:58Z",
    "updateDateIncludingText": "2026-04-29T08:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-09",
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
      "actionCode": "Intro-H",
      "actionDate": "2026-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-09",
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
          "date": "2026-01-09T14:00:15Z",
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
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "MD"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NJ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "PA"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CT"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CT"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CT"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NE"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NV"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6997ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6997\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2026 Mr. Joyce of Pennsylvania (for himself, Ms. Dean of Pennsylvania , Mr. Fitzpatrick , Ms. Houlahan , Mr. Smucker , Mr. Bresnahan , and Ms. Scanlon ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Passport Act of June 4, 1920, to authorize certain public libraries to collect and retain a fee for the execution of a passport application.\n#### 1. Short title\nThis Act may be cited as the Community Passport Services Access Act .\n#### 2. Authorization of certain public libraries to collect and retain execution fee for passport application\n##### (a) In general\nSubsection (a) of the Passport Act of June 4, 1920 ( 22 U.S.C. 214(a) ), is amended by adding at the end the following new paragraph:\n(4) The Secretary of State may authorize a public library, organized as a non-governmental organization, non-profit, charitable organization, or trust, to serve as a passport acceptance facility and to collect and retain the execution fee for a passport accepted by such public library, if such public library is in compliance with the regulations prescribed by the Secretary of State for the acceptance and execution of a passport application. .\n##### (b) Authorization of prior public libraries which served as passport acceptance facilities\n**(1) In general**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of State shall authorize each public library to serve as a passport acceptance facility and to collect and retain an execution fee for a passport accepted by such library, if, before the date of the enactment of this Act, such public library\u2014\n**(A)**\nserved as a passport acceptance facility; and\n**(B)**\nwas in compliance with the regulations prescribed by the Secretary of State for the acceptance and execution of a passport application.\n**(2) Report**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of State shall submit a report to the relevant congressional committees which includes\u2014\n**(A)**\ndocumentation of compliance with the requirements of paragraph (1); or\n**(B)**\nif such Secretary does not comply with paragraph (1), an explanation for such noncompliance.\n##### (c) Conforming amendment\nSubsection (a)(1) of such Act ( 22 U.S.C. 214(a)(1) ) is amended\u2014\n**(1)**\nby striking State officials or the United States Postal Service and inserting a State or local government, the United States Postal Service, or a public library which meet the requirements described in paragraph (4) ; and\n**(2)**\nby striking by such officials or by that Service. and inserting by such State or local government, Service, or public library.",
      "versionDate": "2026-01-09",
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
        "name": "International Affairs",
        "updateDate": "2026-02-27T20:05:01Z"
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
      "date": "2026-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6997ih.xml"
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
      "title": "Community Passport Services Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T08:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Passport Services Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T08:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Passport Act of June 4, 1920 to authorize certain public libraries to collect and retain a fee for the execution of a passport application.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T08:48:32Z"
    }
  ]
}
```
