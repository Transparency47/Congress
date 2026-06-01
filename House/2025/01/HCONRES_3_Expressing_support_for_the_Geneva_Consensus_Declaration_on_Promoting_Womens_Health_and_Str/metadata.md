# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/3?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/3
- Title: Expressing support for the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and urging that the United States rejoin this historic declaration.
- Congress: 119
- Bill type: HCONRES
- Bill number: 3
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-12-05T21:50:40Z
- Update date including text: 2025-12-05T21:50:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-13 - Committee: Submitted in House
- 2025-01-13 - IntroReferral: Submitted in House
- Latest action: 2025-01-13: Submitted in House

## Actions

- 2025-01-13 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-13 - Committee: Submitted in House
- 2025-01-13 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/3",
    "number": "3",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Expressing support for the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and urging that the United States rejoin this historic declaration.",
    "type": "HCONRES",
    "updateDate": "2025-12-05T21:50:40Z",
    "updateDateIncludingText": "2025-12-05T21:50:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "actionCode": "H12100",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:03:10Z",
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "LA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TN"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "IL"
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
      "sponsorshipDate": "2025-01-13",
      "state": "AL"
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
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "KS"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "WI"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "MS"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
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
      "sponsorshipDate": "2025-01-13",
      "state": "MI"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "AL"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MD"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NC"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "GA"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres3ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 3\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Jackson of Texas (for himself, Ms. Foxx , Mr. Higgins of Louisiana , Mr. Fleischmann , Mrs. Miller of Illinois , Mr. Aderholt , Mr. Weber of Texas , Mr. Mann , Mr. Grothman , Mr. Guest , Mr. McCormick , Mr. Moolenaar , Mr. Webster of Florida , Mr. Hudson , Mr. Palmer , Mr. Biggs of Arizona , Mr. Murphy , and Ms. Van Duyne ) submitted the following concurrent resolution; which was referred to the Committee on Foreign Affairs\nCONCURRENT RESOLUTION\nExpressing support for the Geneva Consensus Declaration on Promoting Women\u2019s Health and Strengthening the Family and urging that the United States rejoin this historic declaration.\nThat Congress\u2014\n**(1)**\naffirms the commitments to improve health for women and protect life and the family made in the Geneva Consensus Declaration on Promoting Women\u2019s Health and Strengthening the Family (in this resolution referred to as the Geneva Consensus Declaration ) and applauds the signatory countries for their dedication to advancing women\u2019s health, protecting life at every stage while affirming that there is no international right to abortion, and upholding the importance of the family as foundational to society;\n**(2)**\ndeclares that the principles affirming women\u2019s health and the dignity of every life and the family recognized by the Geneva Consensus Declaration remain universally valid;\n**(3)**\nwelcomes opportunities to strengthen support for the Geneva Consensus Declaration;\n**(4)**\nwill defend the sovereignty of every country to adopt national policies that promote women\u2019s health, protect the right to life, and strengthen the family, as enshrined in the Geneva Consensus Declaration;\n**(5)**\nwill work with the United States executive branch to ensure that the United States does not conduct or fund abortions, abortion lobbying, or coercive family planning in foreign countries, consistent with longstanding Federal law; and\n**(6)**\nurges the signatory countries to the Geneva Consensus Declaration to defend the universal principles affirming the value of every life and the family expressed in the Declaration.",
      "versionDate": "2025-01-13",
      "versionType": "IH"
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
        "actionDate": "2025-01-13",
        "text": "Referred to the Committee on Foreign Relations."
      },
      "number": "4",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A concurrent resolution expressing support for the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and urging that the United States rejoin this historic declaration.",
      "type": "SCONRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-01-28T15:51:27Z"
          },
          {
            "name": "Family planning and birth control",
            "updateDate": "2025-01-28T15:51:43Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-01-28T15:51:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-01-21T12:32:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hconres3",
          "measure-number": "3",
          "measure-type": "hconres",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-02-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres3v00",
            "update-date": "2025-02-04"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This concurrent resolution affirms the commitments in the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and applauds the signatory countries for their dedication to advancing women's health, protecting life at every stage while affirming that there is no international right to abortion, and upholding the importance of the family as foundational to society.</p><p>The resolution also states that Congress will work with the executive branch to ensure that the United States does not conduct or fund abortions, abortion lobbying, or coercive family planning in foreign countries.</p>"
        },
        "title": "Expressing support for the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and urging that the United States rejoin this historic declaration."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres3.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution affirms the commitments in the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and applauds the signatory countries for their dedication to advancing women's health, protecting life at every stage while affirming that there is no international right to abortion, and upholding the importance of the family as foundational to society.</p><p>The resolution also states that Congress will work with the executive branch to ensure that the United States does not conduct or fund abortions, abortion lobbying, or coercive family planning in foreign countries.</p>",
      "updateDate": "2025-02-04",
      "versionCode": "id119hconres3"
    },
    "title": "Expressing support for the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and urging that the United States rejoin this historic declaration."
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution affirms the commitments in the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and applauds the signatory countries for their dedication to advancing women's health, protecting life at every stage while affirming that there is no international right to abortion, and upholding the importance of the family as foundational to society.</p><p>The resolution also states that Congress will work with the executive branch to ensure that the United States does not conduct or fund abortions, abortion lobbying, or coercive family planning in foreign countries.</p>",
      "updateDate": "2025-02-04",
      "versionCode": "id119hconres3"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres3ih.xml"
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
      "title": "Expressing support for the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and urging that the United States rejoin this historic declaration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-14T09:33:17Z"
    },
    {
      "title": "Expressing support for the Geneva Consensus Declaration on Promoting Women's Health and Strengthening the Family and urging that the United States rejoin this historic declaration.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-14T09:05:31Z"
    }
  ]
}
```
