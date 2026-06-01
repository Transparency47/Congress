# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1234?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1234
- Title: To direct the Librarian of Congress to promote the more cost-effective, efficient, and expanded availability of the Annotated Constitution and pocket-part supplements by replacing the hardbound versions with digital versions.
- Congress: 119
- Bill type: HR
- Bill number: 1234
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-04-04T18:19:55Z
- Update date including text: 2025-04-04T18:19:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-03-31 16:20:40 - Floor: Mrs. Bice moved to suspend the rules and pass the bill.
- 2025-03-31 16:20:57 - Floor: Considered under suspension of the rules. (consideration: CR H1345
- 2025-03-31 16:20:58 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1234.
- 2025-03-31 16:30:28 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1345-1346)
- 2025-03-31 16:30:28 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote.
- 2025-03-31 16:30:32 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-04-01 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-03-31 16:20:40 - Floor: Mrs. Bice moved to suspend the rules and pass the bill.
- 2025-03-31 16:20:57 - Floor: Considered under suspension of the rules. (consideration: CR H1345
- 2025-03-31 16:20:58 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1234.
- 2025-03-31 16:30:28 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1345-1346)
- 2025-03-31 16:30:28 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote.
- 2025-03-31 16:30:32 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-04-01 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1234",
    "number": "1234",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "To direct the Librarian of Congress to promote the more cost-effective, efficient, and expanded availability of the Annotated Constitution and pocket-part supplements by replacing the hardbound versions with digital versions.",
    "type": "HR",
    "updateDate": "2025-04-04T18:19:55Z",
    "updateDateIncludingText": "2025-04-04T18:19:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-03-31",
      "actionTime": "16:30:32",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-03-31",
      "actionTime": "16:30:28",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1345-1346)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-03-31",
      "actionTime": "16:30:28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote.",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-03-31",
      "actionTime": "16:20:58",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 1234.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-03-31",
      "actionTime": "16:20:57",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H1345",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-03-31",
      "actionTime": "16:20:40",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mrs. Bice moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-04-01T16:13:36Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-12T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "OH"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1234ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1234\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mrs. Bice (for herself, Mr. Morelle , Mr. Carey , and Mrs. Torres of California ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo direct the Librarian of Congress to promote the more cost-effective, efficient, and expanded availability of the Annotated Constitution and pocket-part supplements by replacing the hardbound versions with digital versions.\n#### 1. Repeal requirement for Congressional Research Service to prepare Annotated Constitution and supplements in hardbound version\n##### (a) Repeal\nThe first section of Public Law 91\u2013589 ( 2 U.S.C. 168 ) is amended\u2014\n**(1)**\nby striking the Librarian of Congress and inserting (a) subject to subsection (b), the Librarian of Congress ; and\n**(2)**\nby adding at the end the following new subsection:\n(b) (1) Upon the completion of the October 2031 term of the Supreme Court and upon the completion of each tenth October term of the Supreme Court thereafter, the Librarian of Congress shall have prepared a digital decennial revised edition of the Constitution Annotated, which shall contain annotations of all decisions theretofore rendered by the Supreme Court construing provisions of the Constitution, in place of the hardbound decennial revised edition of the Constitution Annotated described in subsection (a)(3). (2) Upon the completion of the October 2025 term of the Supreme Court and upon the completion of each subsequent October term of the Supreme Court beginning in an odd-numbered year (the final digit of which is not a 1), the Librarian shall have prepared a digital cumulative pocket-part supplement to the most recent decennial revised edition of the Constitution Annotated, which shall contain cumulative annotations of all such decisions rendered by the Supreme Court which were not included in the most recent revised edition of the Constitution Annotated, in place of the hardbound editions of the cumulative pocket-part supplement described in subsection (a)(4). .\n##### (b) Ensuring availability of digital versions\nSection 2 of Public Law 91\u2013589 ( 2 U.S.C. 168a ) is amended\u2014\n**(1)**\nby striking All hardbound and inserting (a) All hardbound ; and\n**(2)**\nby adding at the end the following new subsection:\n(b) (1) The digital decennial revised editions of the Constitution Annotated prepared under subsection (b)(1) of the first section of this Joint Resolution and the digital cumulative pocket-part supplements prepared under subsection (b)(2) of the first section of this Joint Resolution shall be available at a public website of the Library of Congress. (2) The Librarian of Congress shall ensure the continuing availability of the documents referred to in paragraph (1) to Congress and the public. .\n##### (c) Repeal of additional printing requirements\n**(1) Mandatory printing of additional copies**\nSection 3 of Public Law 91\u2013589 ( 2 U.S.C. 168b ) is amended\u2014\n**(A)**\nby striking There shall be printed and inserting (a) There shall be printed ; and\n**(B)**\nby adding at the end the following new subsection:\n(b) Subsection (a) does not apply after completion of the October 2025 term of the Supreme Court, and the Librarian of Congress shall provide the decennial revised editions of the Constitution Annotated and the cumulative pocket part supplements prepared under this Joint Resolution exclusively in a digital format available at a public website of the Library of Congress. .\n**(2) Printing of additional copies pursuant to concurrent resolution**\nSection 4 of Public Law 91\u2013589 ( 2 U.S.C. 168c ) is repealed.",
      "versionDate": "2025-02-12",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1234rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 1234\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Received; read twice and referred to the Committee on Rules and Administration\nAN ACT\nTo direct the Librarian of Congress to promote the more cost-effective, efficient, and expanded availability of the Annotated Constitution and pocket-part supplements by replacing the hardbound versions with digital versions.\n#### 1. Repeal requirement for Congressional Research Service to prepare Annotated Constitution and supplements in hardbound version\n##### (a) Repeal\nThe first section of Public Law 91\u2013589 ( 2 U.S.C. 168 ) is amended\u2014\n**(1)**\nby striking the Librarian of Congress and inserting (a) subject to subsection (b), the Librarian of Congress ; and\n**(2)**\nby adding at the end the following new subsection:\n(b) (1) Upon the completion of the October 2031 term of the Supreme Court and upon the completion of each tenth October term of the Supreme Court thereafter, the Librarian of Congress shall have prepared a digital decennial revised edition of the Constitution Annotated, which shall contain annotations of all decisions theretofore rendered by the Supreme Court construing provisions of the Constitution, in place of the hardbound decennial revised edition of the Constitution Annotated described in subsection (a)(3). (2) Upon the completion of the October 2025 term of the Supreme Court and upon the completion of each subsequent October term of the Supreme Court beginning in an odd-numbered year (the final digit of which is not a 1), the Librarian shall have prepared a digital cumulative pocket-part supplement to the most recent decennial revised edition of the Constitution Annotated, which shall contain cumulative annotations of all such decisions rendered by the Supreme Court which were not included in the most recent revised edition of the Constitution Annotated, in place of the hardbound editions of the cumulative pocket-part supplement described in subsection (a)(4). .\n##### (b) Ensuring availability of digital versions\nSection 2 of Public Law 91\u2013589 ( 2 U.S.C. 168a ) is amended\u2014\n**(1)**\nby striking All hardbound and inserting (a) All hardbound ; and\n**(2)**\nby adding at the end the following new subsection:\n(b) (1) The digital decennial revised editions of the Constitution Annotated prepared under subsection (b)(1) of the first section of this Joint Resolution and the digital cumulative pocket-part supplements prepared under subsection (b)(2) of the first section of this Joint Resolution shall be available at a public website of the Library of Congress. (2) The Librarian of Congress shall ensure the continuing availability of the documents referred to in paragraph (1) to Congress and the public. .\n##### (c) Repeal of additional printing requirements\n**(1) Mandatory printing of additional copies**\nSection 3 of Public Law 91\u2013589 ( 2 U.S.C. 168b ) is amended\u2014\n**(A)**\nby striking There shall be printed and inserting (a) There shall be printed ; and\n**(B)**\nby adding at the end the following new subsection:\n(b) Subsection (a) does not apply after completion of the October 2025 term of the Supreme Court, and the Librarian of Congress shall provide the decennial revised editions of the Constitution Annotated and the cumulative pocket part supplements prepared under this Joint Resolution exclusively in a digital format available at a public website of the Library of Congress. .\n**(2) Printing of additional copies pursuant to concurrent resolution**\nSection 4 of Public Law 91\u2013589 ( 2 U.S.C. 168c ) is repealed.",
      "versionDate": "2025-04-01",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1234eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1234\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo direct the Librarian of Congress to promote the more cost-effective, efficient, and expanded availability of the Annotated Constitution and pocket-part supplements by replacing the hardbound versions with digital versions.\n#### 1. Repeal requirement for Congressional Research Service to prepare Annotated Constitution and supplements in hardbound version\n##### (a) Repeal\nThe first section of Public Law 91\u2013589 ( 2 U.S.C. 168 ) is amended\u2014\n**(1)**\nby striking the Librarian of Congress and inserting (a) subject to subsection (b), the Librarian of Congress ; and\n**(2)**\nby adding at the end the following new subsection:\n(b) (1) Upon the completion of the October 2031 term of the Supreme Court and upon the completion of each tenth October term of the Supreme Court thereafter, the Librarian of Congress shall have prepared a digital decennial revised edition of the Constitution Annotated, which shall contain annotations of all decisions theretofore rendered by the Supreme Court construing provisions of the Constitution, in place of the hardbound decennial revised edition of the Constitution Annotated described in subsection (a)(3). (2) Upon the completion of the October 2025 term of the Supreme Court and upon the completion of each subsequent October term of the Supreme Court beginning in an odd-numbered year (the final digit of which is not a 1), the Librarian shall have prepared a digital cumulative pocket-part supplement to the most recent decennial revised edition of the Constitution Annotated, which shall contain cumulative annotations of all such decisions rendered by the Supreme Court which were not included in the most recent revised edition of the Constitution Annotated, in place of the hardbound editions of the cumulative pocket-part supplement described in subsection (a)(4). .\n##### (b) Ensuring availability of digital versions\nSection 2 of Public Law 91\u2013589 ( 2 U.S.C. 168a ) is amended\u2014\n**(1)**\nby striking All hardbound and inserting (a) All hardbound ; and\n**(2)**\nby adding at the end the following new subsection:\n(b) (1) The digital decennial revised editions of the Constitution Annotated prepared under subsection (b)(1) of the first section of this Joint Resolution and the digital cumulative pocket-part supplements prepared under subsection (b)(2) of the first section of this Joint Resolution shall be available at a public website of the Library of Congress. (2) The Librarian of Congress shall ensure the continuing availability of the documents referred to in paragraph (1) to Congress and the public. .\n##### (c) Repeal of additional printing requirements\n**(1) Mandatory printing of additional copies**\nSection 3 of Public Law 91\u2013589 ( 2 U.S.C. 168b ) is amended\u2014\n**(A)**\nby striking There shall be printed and inserting (a) There shall be printed ; and\n**(B)**\nby adding at the end the following new subsection:\n(b) Subsection (a) does not apply after completion of the October 2025 term of the Supreme Court, and the Librarian of Congress shall provide the decennial revised editions of the Constitution Annotated and the cumulative pocket part supplements prepared under this Joint Resolution exclusively in a digital format available at a public website of the Library of Congress. .\n**(2) Printing of additional copies pursuant to concurrent resolution**\nSection 4 of Public Law 91\u2013589 ( 2 U.S.C. 168c ) is repealed.",
      "versionDate": "",
      "versionType": "Engrossed in House"
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
            "name": "Books and print media",
            "updateDate": "2025-04-02T13:09:43Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-04-02T13:09:43Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2025-04-02T13:09:43Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-02T13:09:43Z"
          },
          {
            "name": "Library of Congress",
            "updateDate": "2025-04-02T13:09:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-03-13T13:29:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1234",
          "measure-number": "1234",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1234v00",
            "update-date": "2025-03-26"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill replaces the requirement for the Library of Congress to prepare hardbound versions of the Constitution Annotated and supplements with a requirement for the Library to instead prepare digital versions and publish them online.</p><p>The new requirement applies to the supplement after the Supreme Court term beginning October 2025 and all subsequent editions.</p>"
        },
        "title": "To direct the Librarian of Congress to promote the more cost-effective, efficient, and expanded availability of the Annotated Constitution and pocket-part supplements by replacing the hardbound versions with digital versions."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1234.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill replaces the requirement for the Library of Congress to prepare hardbound versions of the Constitution Annotated and supplements with a requirement for the Library to instead prepare digital versions and publish them online.</p><p>The new requirement applies to the supplement after the Supreme Court term beginning October 2025 and all subsequent editions.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1234"
    },
    "title": "To direct the Librarian of Congress to promote the more cost-effective, efficient, and expanded availability of the Annotated Constitution and pocket-part supplements by replacing the hardbound versions with digital versions."
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill replaces the requirement for the Library of Congress to prepare hardbound versions of the Constitution Annotated and supplements with a requirement for the Library to instead prepare digital versions and publish them online.</p><p>The new requirement applies to the supplement after the Supreme Court term beginning October 2025 and all subsequent editions.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1234"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1234ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1234rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1234eh.xml"
        }
      ],
      "type": "Engrossed in House"
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
      "title": "To direct the Librarian of Congress to promote the more cost-effective, efficient, and expanded availability of the Annotated Constitution and pocket-part supplements by replacing the hardbound versions with digital versions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T12:48:37Z"
    },
    {
      "title": "To direct the Librarian of Congress to promote the more cost-effective, efficient, and expanded availability of the Annotated Constitution and pocket-part supplements by replacing the hardbound versions with digital versions.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:05:51Z"
    }
  ]
}
```
