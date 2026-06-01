# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/421?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/421
- Title: Resolution memorializing law enforcement officers killed in the line of duty.
- Congress: 119
- Bill type: HRES
- Bill number: 421
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-04-07T16:45:25Z
- Update date including text: 2026-04-07T16:45:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-05-15 - IntroReferral: Submitted in House
- 2025-05-15 - IntroReferral: Submitted in House
- Latest action: 2025-05-15: Submitted in House

## Actions

- 2025-05-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-05-15 - IntroReferral: Submitted in House
- 2025-05-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/421",
    "number": "421",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000591",
        "district": "3",
        "firstName": "Michael",
        "fullName": "Rep. Guest, Michael [R-MS-3]",
        "lastName": "Guest",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Resolution memorializing law enforcement officers killed in the line of duty.",
    "type": "HRES",
    "updateDate": "2026-04-07T16:45:25Z",
    "updateDateIncludingText": "2026-04-07T16:45:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:06:40Z",
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
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "LA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NH"
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
      "sponsorshipDate": "2025-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MS"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "UT"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "SC"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MO"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NE"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WI"
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
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
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
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MN"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AL"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AL"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WV"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres421ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 421\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Guest (for himself, Ms. Letlow , Mr. Pappas , Mr. Fitzpatrick , Mr. Kelly of Mississippi , Mr. Owens , Ms. Mace , Mr. McDowell , Mr. Thompson of Pennsylvania , Mrs. Wagner , Mr. Bacon , Mr. Wied , Mr. McCaul , Mr. Moolenaar , Ms. Salazar , Mr. Rouzer , Mr. Stauber , Mr. Walberg , Mr. Weber of Texas , Mr. Rogers of Alabama , Mr. Aderholt , Mr. Tony Gonzales of Texas , Mr. Moore of West Virginia , Mr. Moore of North Carolina , and Mr. Bean of Florida ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nResolution memorializing law enforcement officers killed in the line of duty.\nThat the House of Representatives\u2014\n**(1)**\nacknowledges that police officers and other law enforcement personnel, especially those who have made the ultimate sacrifice, should be remembered and honored;\n**(2)**\nexpresses unwavering support for law enforcement officers across the United States in the pursuit of preserving safe and secure communities;\n**(3)**\nrecognizes the need to ensure that law enforcement officers have the equipment, training, and resources that are necessary in order to protect the health and safety of the officers while the officers protect the public;\n**(4)**\nrecognizes the law enforcement community for continual unseen acts of sacrifice and heroism; and\n**(5)**\nexpresses condolences and solemn appreciation to the loved ones of each law enforcement officer who has made the ultimate sacrifice in the line of duty.",
      "versionDate": "2025-05-15",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-23T12:20:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-15",
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
          "measure-id": "id119hres421",
          "measure-number": "421",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-15",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres421v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-05-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for police officers and other law enforcement personnel.</p> <p>The resolution further recognizes</p> <ul> <li> law enforcement officers across the United States in the pursuit of preserving safe and secure communities;</li> <li>the need to ensure that such officers have the equipment, training, and resources necessary to protect their health and safety while they are protecting the public; and</li> <li>the law enforcement community for acts of sacrifice and heroism.</li> </ul> <p>The resolution expresses condolences and appreciation to the loved ones of each law enforcement officer who has made the ultimate sacrifice in the line of duty.</p>"
        },
        "title": "Resolution memorializing law enforcement officers killed in the line of duty."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres421.xml",
    "summary": {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for police officers and other law enforcement personnel.</p> <p>The resolution further recognizes</p> <ul> <li> law enforcement officers across the United States in the pursuit of preserving safe and secure communities;</li> <li>the need to ensure that such officers have the equipment, training, and resources necessary to protect their health and safety while they are protecting the public; and</li> <li>the law enforcement community for acts of sacrifice and heroism.</li> </ul> <p>The resolution expresses condolences and appreciation to the loved ones of each law enforcement officer who has made the ultimate sacrifice in the line of duty.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres421"
    },
    "title": "Resolution memorializing law enforcement officers killed in the line of duty."
  },
  "summaries": [
    {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for police officers and other law enforcement personnel.</p> <p>The resolution further recognizes</p> <ul> <li> law enforcement officers across the United States in the pursuit of preserving safe and secure communities;</li> <li>the need to ensure that such officers have the equipment, training, and resources necessary to protect their health and safety while they are protecting the public; and</li> <li>the law enforcement community for acts of sacrifice and heroism.</li> </ul> <p>The resolution expresses condolences and appreciation to the loved ones of each law enforcement officer who has made the ultimate sacrifice in the line of duty.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres421"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres421ih.xml"
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
      "title": "Resolution memorializing law enforcement officers killed in the line of duty.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T09:03:19Z"
    },
    {
      "title": "Resolution memorializing law enforcement officers killed in the line of duty.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T08:06:26Z"
    }
  ]
}
```
