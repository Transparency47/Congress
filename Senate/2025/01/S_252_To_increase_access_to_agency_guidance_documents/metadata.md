# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/252?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/252
- Title: GOOD Act
- Congress: 119
- Bill type: S
- Bill number: 252
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2025-11-20T12:03:20Z
- Update date including text: 2025-11-20T12:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/252",
    "number": "252",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "J000293",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Johnson, Ron [R-WI]",
        "lastName": "Johnson",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "GOOD Act",
    "type": "S",
    "updateDate": "2025-11-20T12:03:20Z",
    "updateDateIncludingText": "2025-11-20T12:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T20:21:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ND"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IA"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "OK"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MO"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "KS"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MT"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "UT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "WY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "FL"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ND"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ID"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s252is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 252\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Johnson (for himself, Mr. Cramer , Ms. Ernst , Mr. Lankford , Mr. Tillis , Mrs. Blackburn , Mr. Budd , Mr. Schmitt , Mr. Marshall , Mr. Sheehy , Mr. Lee , Ms. Lummis , Mr. Scott of Florida , Mr. Hoeven , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo increase access to agency guidance documents.\n#### 1. Short title\nThis Act may be cited as the Guidance Out Of Darkness Act or the GOOD Act .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(2) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(3) Guidance document**\n**(A) Definition**\nThe term guidance document \u2014\n**(i)**\nmeans an agency statement of general applicability (other than a rule that has the force and effect of law promulgated in accordance with the notice and comment procedures under section 553 of title 5, United States Code) that\u2014\n**(I)**\ndoes not have the force and effect of law; and\n**(II)**\nis designated by an agency official as setting forth\u2014\n**(aa)**\na policy on a statutory, regulatory, or technical issue; or\n**(bb)**\nan interpretation of a statutory or regulatory issue; and\n**(ii)**\nmay include\u2014\n**(I)**\na memorandum;\n**(II)**\na notice;\n**(III)**\na bulletin;\n**(IV)**\na directive;\n**(V)**\na news release;\n**(VI)**\na letter;\n**(VII)**\na blog post;\n**(VIII)**\na no-action letter;\n**(IX)**\na speech by an agency official; and\n**(X)**\nany combination of the items described in subclauses (I) through (IX).\n**(B) Rule of construction**\nThe term guidance document \u2014\n**(i)**\nshall be construed broadly to effectuate the purpose and intent of this Act; and\n**(ii)**\nshall not be limited to the items described in subparagraph (A)(ii).\n#### 3. Publication of guidance documents on the internet\n##### (a) In general\nSubject to subsection (d), on the date on which an agency issues a guidance document, the agency shall publish the guidance document in accordance with the requirements under subsection (c).\n##### (b) Previously issued guidance documents\nSubject to subsection (d), not later than 180 days after the date of enactment of this Act, each agency shall publish, in accordance with the requirements under subsection (c), any guidance document issued by that agency that is in effect on that date.\n##### (c) Single location\n**(1) In general**\nAll guidance documents published under subsections (a) and (b) by an agency shall be published in a single location on an internet website designated by the Director under paragraph (4).\n**(2) Agency internet websites**\nEach agency shall, for guidance documents published by the agency under subsections (a) and (b), publish a hyperlink on the internet website of the agency that provides access to the guidance documents at the location described in paragraph (1).\n**(3) Organization**\n**(A) In general**\nThe guidance documents described in paragraph (1) shall be\u2014\n**(i)**\ncategorized as guidance documents; and\n**(ii)**\nfurther divided into subcategories as appropriate.\n**(B) Agency internet websites**\nThe hyperlinks described in paragraph (2) shall be prominently displayed on the internet website of the agency.\n**(4) Designation**\nNot later than 90 days after the date of enactment of this Act, the Director shall designate an internet website on which guidance documents shall be published under subsections (a) and (b).\n##### (d) Documents and information exempt from disclosure under FOIA\nIf a guidance document issued by an agency is a document that is exempt from disclosure under section 552(b) of title 5, United States Code (commonly known as the Freedom of Information Act ), or contains information that is exempt from disclosure under that section, that document or information, as the case may be, shall not be subject to the requirements under this Act.\n##### (e) Rescinded guidance documents\nOn the date on which a guidance document issued by an agency is rescinded, or, in the case of a guidance document that is rescinded pursuant to a court order, not later than the date on which the order is entered, the agency shall, at the location described in subsection (c)(1)\u2014\n**(1)**\nmaintain the rescinded guidance document; and\n**(2)**\nindicate\u2014\n**(A)**\nthat the guidance document is rescinded;\n**(B)**\nif the guidance document was rescinded pursuant to a court order, the case number of the case in which the order was entered; and\n**(C)**\nthe date on which the guidance document was rescinded.",
      "versionDate": "2025-01-24",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-06-13T18:08:32Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-13T18:08:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-01T21:10:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119s252",
          "measure-number": "252",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s252v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Guidance Out Of Darkness Act or the GOOD Act</b></p> <p>This bill establishes requirements concerning the posting of agency guidance documents. Specifically, an agency must publish guidance documents online on the dates they are issued, publish all of its guidance documents that are in effect in a single location on a designated website, display a hyperlink on its website that provides access to the guidance documents on such website, and indicate on such website if a guidance document has been rescinded.</p> <p>The documents must be categorized as guidance documents and further divided into subcategories. </p>"
        },
        "title": "GOOD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s252.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Guidance Out Of Darkness Act or the GOOD Act</b></p> <p>This bill establishes requirements concerning the posting of agency guidance documents. Specifically, an agency must publish guidance documents online on the dates they are issued, publish all of its guidance documents that are in effect in a single location on a designated website, display a hyperlink on its website that provides access to the guidance documents on such website, and indicate on such website if a guidance document has been rescinded.</p> <p>The documents must be categorized as guidance documents and further divided into subcategories. </p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s252"
    },
    "title": "GOOD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Guidance Out Of Darkness Act or the GOOD Act</b></p> <p>This bill establishes requirements concerning the posting of agency guidance documents. Specifically, an agency must publish guidance documents online on the dates they are issued, publish all of its guidance documents that are in effect in a single location on a designated website, display a hyperlink on its website that provides access to the guidance documents on such website, and indicate on such website if a guidance document has been rescinded.</p> <p>The documents must be categorized as guidance documents and further divided into subcategories. </p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s252"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s252is.xml"
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
      "title": "GOOD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GOOD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guidance Out Of Darkness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase access to agency guidance documents.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:27Z"
    }
  ]
}
```
