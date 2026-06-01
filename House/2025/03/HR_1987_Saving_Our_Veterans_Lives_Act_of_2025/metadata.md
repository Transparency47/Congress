# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1987?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1987
- Title: Saving Our Veterans Lives Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1987
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-05-14T08:08:11Z
- Update date including text: 2026-05-14T08:08:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Oversight and Investigations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1987",
    "number": "1987",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Saving Our Veterans Lives Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:11Z",
    "updateDateIncludingText": "2026-05-14T08:08:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-12T15:30:50Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
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
      "sponsorshipDate": "2025-03-10",
      "state": "PA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "OH"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "RI"
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
      "sponsorshipDate": "2025-06-23",
      "state": "PA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "NY"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "FL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MS"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MN"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "WA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NM"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CT"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "WI"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "NY"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "PA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "IL"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NV"
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
      "sponsorshipDate": "2025-12-03",
      "state": "CT"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "DC"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NH"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1987ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1987\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Deluzio (for himself, Mr. James , Mr. Fitzpatrick , and Mr. Landsman ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to establish a program to furnish to certain individuals items used for the secure storage of firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Saving Our Veterans Lives Act of 2025 .\n#### 2. Program of Department of Veterans Affairs to furnish to veterans and certain former members of the Armed Forces items used for secure storage of firearms\n##### (a) In general\nSubchapter II of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section:\n1720M. Program to furnish to veterans and certain former members of the Armed Forces items intended to be used for the secure storage of firearms (a) In general (1) The Secretary shall carry out a program to provide to an eligible individual, upon the request of such eligible individual\u2014 (A) a covered item, or a redeemable voucher to aid in the distribution of a covered item; and (B) information with respect to the benefits of, and options for, secure firearm storage. (2) In distributing covered items to eligible individuals pursuant to such program, the Secretary is authorized to work with eligible entities that have expertise and business knowledge with respect to secure firearm storage and secure firearm storage devices. (b) Annual report Not later than one year after the date of the enactment of the Saving Our Veterans Lives Act of 2025 , and on an annual basis thereafter, the Secretary shall submit to the appropriate congressional committees a report that includes, with respect to the period covered by the report\u2014 (1) a description of the how the program\u2014 (A) functions; and (B) promotes the secure storage of firearms; (2) the number of\u2014 (A) covered items distributed pursuant to the program; (B) redeemable vouchers distributed pursuant to the program; and (C) such redeemable vouchers redeemed for a covered item; (3) efforts made to increase the outreach with respect to such program to veterans not enrolled in the system of annual patient enrollment established and operated under section 1705 of this title; (4) a description of any obstacles, if any, to increasing such outreach; and (5) a description of additional steps, if any, the Secretary intends to implement during the one-year period beginning on the date of the submission of the report to improve the processes by which eligible individuals receive a covered item pursuant to the program. (c) Definitions In this section: (1) The term appropriate congressional committees means\u2014 (A) the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate; and (B) the Committees on Appropriations of the House of Representatives and the Senate. (2) The term covered item means a lockbox that\u2014 (A) is used for the secure storage of a firearm and ammunition; (B) is designed, intended, and marketed to prevent unauthorized access to a firearm or ammunition; (C) may be unlocked only by means of a key, combination, or other similar means; (D) is in compliance with the applicable standard of American Society for Testing and Materials F2456\u201320; (E) is manufactured in the United States; and (F) is not eligible or intended for commercial or individual resale. (3) The term eligible individual means\u2014 (A) a veteran; and (B) an eligible individual described in subsection (b) of section 1720I of this title. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by adding after the item relating to section 1720L the following new item:\n1720M. Program to furnish to eligible individuals items intended to be used for the secure storage of firearms. .\n##### (c) Education and training\nThe Secretary of Veterans Affairs shall\u2014\n**(1)**\nin consultation with representatives of organizations and agencies that are subject to a memorandum of understanding with the Secretary with respect to the prevention of suicide among former members of the Armed Forces (including the reserve components) and other such entities as the Secretary determines appropriate\u2014\n**(A)**\ndevelop an informational video on secure storage of firearms as a suicide prevention strategy; and\n**(B)**\npublish such informational video on an internet website of the Department; and\n**(2)**\npublish information to inform individuals who participate in the program under section 1720M of title 38, United States Code (as added by subsection (a)) that any item intended to be used for the secure storage of a firearm furnished pursuant to such program is not eligible or intended for commercial or individual resale.\n##### (d) Public education campaign\n**(1) In general**\nThe Secretary shall design and carry out a public education campaign to educate individuals eligible to participate in the program under section 1720M of title 38, United States Code (as added by subsection (a)), to inform such individuals\u2014\n**(A)**\nof the availability of items intended to be used for the secure storage of a firearms under such program; and\n**(B)**\nthat participation in such program does not affect the rights of an individual with respect to the lawful ownership of a firearm.\n**(2) Collaboration authorized**\nIn carrying out such campaign, the Secretary may collaborate with organizations that have expertise with respect to secure firearm storage and secure firearm storage devices.\n##### (e) Authorization of appropriations\nThere are authorized to be appropriated to the Secretary $5,000,000 for each of fiscal years 2026 through 2036 to carry out\u2014\n**(1)**\nthis section; and\n**(2)**\nthe program under section 1720M of title 38, United States Code (as added by subsection (a)).\n##### (f) Rule of construction\nNothing in this Act, or the amendments made by this Act, may be construed to\u2014\n**(1)**\ncollect personally identifiable information of an individual who participates in the program under section 1720M of title 38, United States Code (as added by subsection (a)) for the purposes of tracking firearm ownership;\n**(2)**\nrequire any such individual to register a firearm with the Department of Veterans Affairs, or any other Federal, state, tribal or local unit of Government;\n**(3)**\nrequire mandatory firearm storage for any such individual;\n**(4)**\nprohibit any such individual from purchasing, owning, or possessing a firearm under section 922 of title 18, United States Code;\n**(5)**\ndiscourage the lawful ownership of firearms; or\n**(6)**\ncreate or maintain a list of individuals that participate in such program.",
      "versionDate": "2025-03-10",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-10",
        "text": "Committee on Veterans' Affairs. Hearings held."
      },
      "number": "926",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Saving Our Veterans Lives Act of 2025",
      "type": "S"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T15:14:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hr1987",
          "measure-number": "1987",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1987v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Saving Our Veterans Lives Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a program to provide, upon request, a firearm lockbox (or voucher for such item) to eligible individuals. Currently, there is a pilot program under which certain veterans may be prescribed a lockbox by a VA clinician.</p><p>The VA must also provide information with respect to the benefits of and options for secure firearm storage.</p><p>The VA must develop an informational video on the secure storage of firearms as a suicide prevention strategy and publish the video on its website. Additionally, the VA must publish information to inform individuals who participate in the lockbox program that such lockboxes are not for resale.</p><p>The VA must also implement a public education campaign to educate eligible individuals about the availability of lockboxes under the program and that participation in the program does not affect the rights of an individual with respect to the lawful ownership of a firearm.</p>"
        },
        "title": "Saving Our Veterans Lives Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1987.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Saving Our Veterans Lives Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a program to provide, upon request, a firearm lockbox (or voucher for such item) to eligible individuals. Currently, there is a pilot program under which certain veterans may be prescribed a lockbox by a VA clinician.</p><p>The VA must also provide information with respect to the benefits of and options for secure firearm storage.</p><p>The VA must develop an informational video on the secure storage of firearms as a suicide prevention strategy and publish the video on its website. Additionally, the VA must publish information to inform individuals who participate in the lockbox program that such lockboxes are not for resale.</p><p>The VA must also implement a public education campaign to educate eligible individuals about the availability of lockboxes under the program and that participation in the program does not affect the rights of an individual with respect to the lawful ownership of a firearm.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119hr1987"
    },
    "title": "Saving Our Veterans Lives Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Saving Our Veterans Lives Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a program to provide, upon request, a firearm lockbox (or voucher for such item) to eligible individuals. Currently, there is a pilot program under which certain veterans may be prescribed a lockbox by a VA clinician.</p><p>The VA must also provide information with respect to the benefits of and options for secure firearm storage.</p><p>The VA must develop an informational video on the secure storage of firearms as a suicide prevention strategy and publish the video on its website. Additionally, the VA must publish information to inform individuals who participate in the lockbox program that such lockboxes are not for resale.</p><p>The VA must also implement a public education campaign to educate eligible individuals about the availability of lockboxes under the program and that participation in the program does not affect the rights of an individual with respect to the lawful ownership of a firearm.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119hr1987"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1987ih.xml"
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
      "title": "Saving Our Veterans Lives Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Saving Our Veterans Lives Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to establish a program to furnish to certain individuals items used for the secure storage of firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:18:24Z"
    }
  ]
}
```
