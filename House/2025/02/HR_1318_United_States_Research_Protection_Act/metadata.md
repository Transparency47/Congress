# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1318?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1318
- Title: United States Research Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 1318
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-02-04T04:11:37Z
- Update date including text: 2026-02-04T04:11:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-03-24 14:37:13 - Floor: Mr. Babin moved to suspend the rules and pass the bill.
- 2025-03-24 14:37:22 - Floor: Considered under suspension of the rules. (consideration: CR H1201-1202)
- 2025-03-24 14:37:23 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1318.
- 2025-03-24 14:51:30 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1201)
- 2025-03-24 14:51:30 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1201)
- 2025-03-24 14:51:31 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-03-25 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-03-24 14:37:13 - Floor: Mr. Babin moved to suspend the rules and pass the bill.
- 2025-03-24 14:37:22 - Floor: Considered under suspension of the rules. (consideration: CR H1201-1202)
- 2025-03-24 14:37:23 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1318.
- 2025-03-24 14:51:30 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1201)
- 2025-03-24 14:51:30 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1201)
- 2025-03-24 14:51:31 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-03-25 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1318",
    "number": "1318",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "K000403",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Kennedy, Mike [R-UT-3]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "United States Research Protection Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:11:37Z",
    "updateDateIncludingText": "2026-02-04T04:11:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-03-24",
      "actionTime": "14:51:31",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-03-24",
      "actionTime": "14:51:30",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1201)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-03-24",
      "actionTime": "14:51:30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1201)",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-03-24",
      "actionTime": "14:37:23",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 1318.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-03-24",
      "actionTime": "14:37:22",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H1201-1202)",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-03-24",
      "actionTime": "14:37:13",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mr. Babin moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-03-25T16:18:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-13T14:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1318ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1318\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Kennedy of Utah (for himself and Ms. Stevens ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the Research and Development, Competition, and Innovation Act to clarify the definition of foreign country for purposes of malign foreign talent recruitment restriction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States Research Protection Act .\n#### 2. Clarification of definition of foreign country for purposes of malign foreign talent recruitment restriction\nParagraph (4) of section 10638 of title VI of division B of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; 42 U.S.C. 19237 ) is amended\u2014\n**(1)**\nby inserting of concern after foreign country each place such term appears;\n**(2)**\nby striking means\u2014 and all that follows through any program, position, or activity and inserting means any program, position, or activity ;\n**(3)**\nby striking subparagraph (B);\n**(4)**\nby redesignating clauses (i) through (ix) as subparagraphs (A) through (I), respectively, and moving such subparagraphs, as so redesignated, two ems to the left;\n**(5)**\nin the matter preceding subparagraph (A), as so redesignated, by striking directly provided and inserting whether directly or indirectly provided ; and\n**(6)**\nin subparagraph (I), as so redesignated, by striking ; and and inserting a period.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1318rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 1318\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Received; read twice and referred to the Committee on Commerce, Science, and Transportation\nAN ACT\nTo amend the Research and Development, Competition, and Innovation Act to clarify the definition of foreign country for purposes of malign foreign talent recruitment restriction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States Research Protection Act .\n#### 2. Clarification of definition of foreign country for purposes of malign foreign talent recruitment restriction\nParagraph (4) of section 10638 of title VI of division B of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; 42 U.S.C. 19237 ) is amended\u2014\n**(1)**\nby inserting of concern after foreign country each place such term appears;\n**(2)**\nby striking means\u2014 and all that follows through any program, position, or activity and inserting means any program, position, or activity ;\n**(3)**\nby striking subparagraph (B);\n**(4)**\nby redesignating clauses (i) through (ix) as subparagraphs (A) through (I), respectively, and moving such subparagraphs, as so redesignated, two ems to the left;\n**(5)**\nin the matter preceding subparagraph (A), as so redesignated, by striking directly provided and inserting whether directly or indirectly provided ; and\n**(6)**\nin subparagraph (I), as so redesignated, by striking ; and and inserting a period.",
      "versionDate": "2025-03-25",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1318eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1318\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo amend the Research and Development, Competition, and Innovation Act to clarify the definition of foreign country for purposes of malign foreign talent recruitment restriction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States Research Protection Act .\n#### 2. Clarification of definition of foreign country for purposes of malign foreign talent recruitment restriction\nParagraph (4) of section 10638 of title VI of division B of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; 42 U.S.C. 19237 ) is amended\u2014\n**(1)**\nby inserting of concern after foreign country each place such term appears;\n**(2)**\nby striking means\u2014 and all that follows through any program, position, or activity and inserting means any program, position, or activity ;\n**(3)**\nby striking subparagraph (B);\n**(4)**\nby redesignating clauses (i) through (ix) as subparagraphs (A) through (I), respectively, and moving such subparagraphs, as so redesignated, two ems to the left;\n**(5)**\nin the matter preceding subparagraph (A), as so redesignated, by striking directly provided and inserting whether directly or indirectly provided ; and\n**(6)**\nin subparagraph (I), as so redesignated, by striking ; and and inserting a period.",
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
            "name": "Employee hiring",
            "updateDate": "2025-03-25T14:25:08Z"
          },
          {
            "name": "International scientific cooperation",
            "updateDate": "2025-03-25T14:25:08Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-03-25T14:25:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-17T14:42:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1318",
          "measure-number": "1318",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1318v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>United States Research Protection Act</strong></p><p>This bill clarifies the definition of a\u00a0<em>malign foreign talent recruitment program</em> under the Research and Development, Competition, and Innovation Act.<em>\u00a0</em></p><p>The Research and Development, Competition, and Innovation Act, which was included in the CHIPS and Science Act, prohibits researchers who receive federal funds from participating in malign foreign talent recruitment programs, in which foreign countries incentivize or compensate researchers for activities that present a conflict\u00a0of\u00a0interest for the researcher or that are otherwise unauthorized (e.g., sharing proprietary information without proper authorization).</p><p>The bill clarifies that these restrictions apply to programs that are sponsored by a foreign country of concern, including China, Iran, North Korea, and Russia. The bill also clarifies that malign foreign talent recruitment programs may involve direct or indirect compensation or incentives from such\u00a0countries.</p>"
        },
        "title": "United States Research Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1318.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Research Protection Act</strong></p><p>This bill clarifies the definition of a\u00a0<em>malign foreign talent recruitment program</em> under the Research and Development, Competition, and Innovation Act.<em>\u00a0</em></p><p>The Research and Development, Competition, and Innovation Act, which was included in the CHIPS and Science Act, prohibits researchers who receive federal funds from participating in malign foreign talent recruitment programs, in which foreign countries incentivize or compensate researchers for activities that present a conflict\u00a0of\u00a0interest for the researcher or that are otherwise unauthorized (e.g., sharing proprietary information without proper authorization).</p><p>The bill clarifies that these restrictions apply to programs that are sponsored by a foreign country of concern, including China, Iran, North Korea, and Russia. The bill also clarifies that malign foreign talent recruitment programs may involve direct or indirect compensation or incentives from such\u00a0countries.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr1318"
    },
    "title": "United States Research Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Research Protection Act</strong></p><p>This bill clarifies the definition of a\u00a0<em>malign foreign talent recruitment program</em> under the Research and Development, Competition, and Innovation Act.<em>\u00a0</em></p><p>The Research and Development, Competition, and Innovation Act, which was included in the CHIPS and Science Act, prohibits researchers who receive federal funds from participating in malign foreign talent recruitment programs, in which foreign countries incentivize or compensate researchers for activities that present a conflict\u00a0of\u00a0interest for the researcher or that are otherwise unauthorized (e.g., sharing proprietary information without proper authorization).</p><p>The bill clarifies that these restrictions apply to programs that are sponsored by a foreign country of concern, including China, Iran, North Korea, and Russia. The bill also clarifies that malign foreign talent recruitment programs may involve direct or indirect compensation or incentives from such\u00a0countries.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr1318"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1318ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1318rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1318eh.xml"
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
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "United States Research Protection Act",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-03-28T11:23:18Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "United States Research Protection Act",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-03-25T05:38:19Z"
    },
    {
      "title": "United States Research Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States Research Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Research and Development, Competition, and Innovation Act to clarify the definition of foreign country for purposes of malign foreign talent recruitment restriction, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T09:18:22Z"
    }
  ]
}
```
