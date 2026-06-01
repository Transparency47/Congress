# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8079?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8079
- Title: Diesel Truck Liberation Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8079
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-04-23T08:06:59Z
- Update date including text: 2026-04-23T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-25: Introduced in House

## Actions

- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8079",
    "number": "8079",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001129",
        "district": "10",
        "firstName": "Mike",
        "fullName": "Rep. Collins, Mike [R-GA-10]",
        "lastName": "Collins",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Diesel Truck Liberation Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-23T08:06:59Z",
    "updateDateIncludingText": "2026-04-23T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T14:02:35Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AL"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "WY"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "OH"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "WI"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "MS"
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
      "sponsorshipDate": "2026-04-13",
      "state": "AL"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8079ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8079\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Mr. Collins (for himself, Mr. Moore of Alabama , Ms. Hageman , Mrs. Luna , Mr. Taylor , Mr. Wied , and Mr. Ezell ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the enforcement of laws relating to the installation, certification, and maintenance of emissions control devices under the Clean Air Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Diesel Truck Liberation Act of 2026 .\n#### 2. Prohibition on enforcement of emissions control device laws\n##### (a) In general\nNotwithstanding any other provision of law, including title II of the Clean Air Act ( 42 U.S.C. 7521 et seq. ), no Federal law (including regulations and Executive orders) may require a manufacturer, importer, or distributor of motor vehicles or motor vehicle engines to install, certify, or maintain any emissions control device or onboard diagnostic system on any motor vehicle or motor vehicle engine.\n##### (b) No authority\nThe Administrator of the Environmental Protection Agency may not promulgate or enforce any requirement under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) (including a regulation promulgated under that Act) or any other Federal law (including regulations) that requires the installation or maintenance of emissions control devices or onboard diagnostic systems on motor vehicles or motor vehicle engines.\n##### (c) No liability\nNotwithstanding any other provision of law, no person or entity shall be subject to civil or criminal liability under any Federal law (including regulations) for the manufacture, sale, importation, purchase, use, or modification of a motor vehicle or motor vehicle engine that does not contain an emissions control device or onboard diagnostic system.\n##### (d) Repeal of regulations\nAny regulation promulgated under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) or any other Federal law related to the installation, modification, or removal of emissions control devices or onboard diagnostic systems on motor vehicles or motor vehicle engines shall have no force or effect.\n##### (e) Vacatur; expungement\nWith respect to any of the conduct described in this section for which criminal or civil liability has attached\u2014\n**(1)**\nany criminal penalty of imprisonment shall be vacated; and\n**(2)**\nany record of a finding with respect to that criminal or civil liability shall be expunged.",
      "versionDate": "2026-03-25",
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
        "actionDate": "2025-10-14",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "3007",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Diesel Truck Liberation Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2026-04-14T13:38:27Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8079ih.xml"
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
      "title": "Diesel Truck Liberation Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Diesel Truck Liberation Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the enforcement of laws relating to the installation, certification, and maintenance of emissions control devices under the Clean Air Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T03:48:29Z"
    }
  ]
}
```
