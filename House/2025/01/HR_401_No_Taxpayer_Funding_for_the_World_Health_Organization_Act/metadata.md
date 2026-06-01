# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/401?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/401
- Title: No Taxpayer Funding for the World Health Organization Act
- Congress: 119
- Bill type: HR
- Bill number: 401
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2025-12-11T09:07:38Z
- Update date including text: 2025-12-11T09:07:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/401",
    "number": "401",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "No Taxpayer Funding for the World Health Organization Act",
    "type": "HR",
    "updateDate": "2025-12-11T09:07:38Z",
    "updateDateIncludingText": "2025-12-11T09:07:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:02:25Z",
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "LA"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "AZ"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TN"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "GA"
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
      "sponsorshipDate": "2025-01-14",
      "state": "MI"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "SC"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MO"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TN"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "AL"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "FL"
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
      "sponsorshipDate": "2025-01-14",
      "state": "WY"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "UT"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "VA"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr401ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 401\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Mr. Roy (for himself, Mr. Higgins of Louisiana , Mr. Biggs of Arizona , Ms. Tenney , Mr. Ogles , Ms. Greene of Georgia , Mr. Moolenaar , Mr. Norman , Mr. Burlison , Mrs. Harshbarger , Mr. Fallon , Mr. Moore of Alabama , Mrs. Luna , and Ms. Hageman ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit United States assessed and voluntary contributions to the World Health Organization.\n#### 1. Short title\nThis Act may be cited as the No Taxpayer Funding for the World Health Organization Act .\n#### 2. Prohibition on assessed and voluntary contributions to the World Health Organization\nNotwithstanding any other provision of law, effective on the date of the enactment of this Act, the United States may not provide any assessed or voluntary contributions to the World Health Organization.",
      "versionDate": "2025-01-14",
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
        "updateDate": "2025-02-20T15:03:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119hr401",
          "measure-number": "401",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr401v00",
            "update-date": "2025-02-27"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>No Taxpayer Funding for the World Health Organization Act</b></p> <p>This bill prohibits the United States from providing any assessed or voluntary contributions to the World Health Organization.</p>"
        },
        "title": "No Taxpayer Funding for the World Health Organization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr401.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><b>No Taxpayer Funding for the World Health Organization Act</b></p> <p>This bill prohibits the United States from providing any assessed or voluntary contributions to the World Health Organization.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr401"
    },
    "title": "No Taxpayer Funding for the World Health Organization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><b>No Taxpayer Funding for the World Health Organization Act</b></p> <p>This bill prohibits the United States from providing any assessed or voluntary contributions to the World Health Organization.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr401"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr401ih.xml"
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
      "title": "No Taxpayer Funding for the World Health Organization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Taxpayer Funding for the World Health Organization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit United States assessed and voluntary contributions to the World Health Organization.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:48:31Z"
    }
  ]
}
```
