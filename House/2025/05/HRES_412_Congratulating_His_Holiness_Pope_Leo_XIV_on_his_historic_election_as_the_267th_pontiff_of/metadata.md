# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/412?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/412
- Title: Congratulating His Holiness Pope Leo XIV on his historic election as the 267th pontiff of the Holy Roman Catholic Church and the first American pontiff.
- Congress: 119
- Bill type: HRES
- Bill number: 412
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2025-06-09T14:34:59Z
- Update date including text: 2025-06-09T14:34:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-05-14 - IntroReferral: Submitted in House
- 2025-05-14 - IntroReferral: Submitted in House
- Latest action: 2025-05-14: Submitted in House

## Actions

- 2025-05-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-05-14 - IntroReferral: Submitted in House
- 2025-05-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/412",
    "number": "412",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001235",
        "district": "2",
        "firstName": "Riley",
        "fullName": "Rep. Moore, Riley M. [R-WV-2]",
        "lastName": "Moore",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Congratulating His Holiness Pope Leo XIV on his historic election as the 267th pontiff of the Holy Roman Catholic Church and the first American pontiff.",
    "type": "HRES",
    "updateDate": "2025-06-09T14:34:59Z",
    "updateDateIncludingText": "2025-06-09T14:34:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:02:30Z",
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MI"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MT"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MO"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "TX"
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
      "sponsorshipDate": "2025-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "OH"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "OK"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MI"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "TN"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "WI"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "FL"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NJ"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "AR"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "FL"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "TX"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "CO"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NE"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "VA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "IA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "PA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "TN"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
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
      "sponsorshipDate": "2025-05-19",
      "state": "PA"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "MO"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "WI"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres412ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 412\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Moore of West Virginia (for himself, Mr. Suozzi , Mr. Barrett , Mr. Zinke , Mrs. Wagner , Mr. McCaul , Mr. Bresnahan , Mr. Rulli , Mrs. Bice , Mrs. McClain , Mr. Rose , Mr. Steil , Mr. Messmer , Mr. Gimenez , Mr. Smith of New Jersey , Mr. Hill of Arkansas , Mr. Rutherford , Mr. Tony Gonzales of Texas , Mr. Hurd of Colorado , Mr. Bacon , Mrs. Kiggans of Virginia , Mrs. Miller-Meeks , and Mr. Stauber ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nCongratulating His Holiness Pope Leo XIV on his historic election as the 267th pontiff of the Holy Roman Catholic Church and the first American pontiff.\nThat the House of Representatives\u2014\n**(1)**\ncongratulates His Holiness Pope Leo XIV on his election as the 267th pope of the Roman Catholic Church and the first American to serve in this sacred role;\n**(2)**\nrecognizes the historic significance of his election for the American Catholic community;\n**(3)**\ncommends Pope Leo XIV for a lifetime of service, humility, missionary zeal, and commitment to embodying Christ\u2019s mercy and pastoral care; and\n**(4)**\nextends our prayers to Pope Leo XIV as he begins his pontificate and shepherds the world\u2019s 1,400,000,000 Catholics with wisdom and grace.",
      "versionDate": "2025-05-14",
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
        "updateDate": "2025-06-09T14:34:59Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres412ih.xml"
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
      "title": "Congratulating His Holiness Pope Leo XIV on his historic election as the 267th pontiff of the Holy Roman Catholic Church and the first American pontiff.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T09:36:18Z"
    },
    {
      "title": "Congratulating His Holiness Pope Leo XIV on his historic election as the 267th pontiff of the Holy Roman Catholic Church and the first American pontiff.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T08:11:43Z"
    }
  ]
}
```
