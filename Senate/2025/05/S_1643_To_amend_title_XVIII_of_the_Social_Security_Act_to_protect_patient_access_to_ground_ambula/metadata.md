# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1643
- Title: Protecting Access to Ground Ambulance Medical Services Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1643
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-12-02T12:03:45Z
- Update date including text: 2025-12-02T12:03:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1643",
    "number": "1643",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Protecting Access to Ground Ambulance Medical Services Act of 2025",
    "type": "S",
    "updateDate": "2025-12-02T12:03:45Z",
    "updateDateIncludingText": "2025-12-02T12:03:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-05-07T19:30:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "ME"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "LA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "VT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "WV"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "OR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "NH"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "TN"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "VA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "OK"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "MS"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "WV"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NV"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "AR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-03",
      "state": "VT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NM"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1643is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1643\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Ms. Cortez Masto (for herself, Ms. Collins , Mr. Cassidy , Mr. Welch , Mrs. Capito , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to protect patient access to ground ambulance services under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Protecting Access to Ground Ambulance Medical Services Act of 2025 .\n#### 2. Protecting patient access to Medicare ground ambulance services\n##### (a) Super rural ambulance\nSection 1834(l)(12)(A) of the Social Security Act ( 42 U.S.C. 1395m(l)(12)(A) ) is amended\u2014\n**(1)**\nin the first sentence, by striking October 1, 2025 and inserting January 1, 2028 ; and\n**(2)**\nby adding at the end the following new sentence: In the case of services furnished on or after October 1, 2025, and before January 1, 2028, such percent increase shall be 26.7 percent. .\n##### (b) Ground ambulance\nSection 1834(l)(13)(A) of the Social Security Act ( 42 U.S.C. 1395m(l)(13)(A) ) is amended\u2014\n**(1)**\nin the matter preceding clause (i), by striking October 1, 2025 and inserting January 1, 2028 ;\n**(2)**\nin clause (i), by inserting , or 4.3 percent if such service is furnished on or after October 1, 2025, and before January 1, 2028 after 2025 ; and\n**(3)**\nin clause (ii), by inserting , or 3.4 percent if such service is furnished on or after October 1, 2025, and before January 1, 2028 after 2025 .",
      "versionDate": "2025-05-07",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-20T14:43:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-07",
    "originChamber": "Senate",
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
          "measure-id": "id119s1643",
          "measure-number": "1643",
          "measure-type": "s",
          "orig-publish-date": "2025-05-07",
          "originChamber": "SENATE",
          "update-date": "2025-06-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1643v00",
            "update-date": "2025-06-04"
          },
          "action-date": "2025-05-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Access to Ground Ambulance Medical Services Act of 2025</strong></p><p>This bill extends a specialized rate increase for Medicare payment of ground ambulance services in rural areas until January 1, 2028, and provides for a higher rate increase for services furnished between October 1, 2025, and January 1, 2028.</p>"
        },
        "title": "Protecting Access to Ground Ambulance Medical Services Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1643.xml",
    "summary": {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Access to Ground Ambulance Medical Services Act of 2025</strong></p><p>This bill extends a specialized rate increase for Medicare payment of ground ambulance services in rural areas until January 1, 2028, and provides for a higher rate increase for services furnished between October 1, 2025, and January 1, 2028.</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119s1643"
    },
    "title": "Protecting Access to Ground Ambulance Medical Services Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Access to Ground Ambulance Medical Services Act of 2025</strong></p><p>This bill extends a specialized rate increase for Medicare payment of ground ambulance services in rural areas until January 1, 2028, and provides for a higher rate increase for services furnished between October 1, 2025, and January 1, 2028.</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119s1643"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1643is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Protecting Access to Ground Ambulance Medical Services Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T12:03:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Access to Ground Ambulance Medical Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to protect patient access to ground ambulance services under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:17Z"
    }
  ]
}
```
