# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/769?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/769
- Title: United States Research Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 769
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-02-04T04:11:37Z
- Update date including text: 2026-02-04T04:11:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-07-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-45.
- 2025-07-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-45.
- 2025-07-22 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 123.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-07-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-45.
- 2025-07-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-45.
- 2025-07-22 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 123.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/769",
    "number": "769",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "United States Research Protection Act of 2025",
    "type": "S",
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
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 123.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-45.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-45.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
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
        "item": [
          {
            "date": "2025-07-22T17:01:29Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-30T14:00:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-27T16:50:02Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "UT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s769is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 769\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Cornyn (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Research and Development, Competition, and Innovation Act to clarify the definition of foreign country for purposes of malign foreign talent recruitment restriction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States Research Protection Act of 2025 .\n#### 2. Clarification of definition of foreign country for purposes of malign foreign talent recruitment restriction\nParagraph (4) of section 10638 of title VI of division B of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19237 ) is amended\u2014\n**(1)**\nby inserting of concern after foreign country each place such term appears;\n**(2)**\nby striking means\u2014 and all that follows through any program, position, or activity and inserting means any program, position, or activity ;\n**(3)**\nby striking subparagraph (B);\n**(4)**\nby redesignating clauses (i) through (ix) as subparagraphs (A) through (I), respectively, and moving such subparagraphs, as so redesignated, two ems to the left;\n**(5)**\nin the matter preceding subparagraph (A), as so redesignated, by striking directly provided and inserting whether directly or indirectly provided ; and\n**(6)**\nin subparagraph (I), as so redesignated, by striking ; and and inserting a period.",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s769rs.xml",
      "text": "II\nCalendar No. 123\n119th CONGRESS\n1st Session\nS. 769\n[Report No. 119\u201345]\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Cornyn (for himself, Mr. Padilla , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nJuly 22, 2025 Reported by Mr. Cruz , without amendment\nA BILL\nTo amend the Research and Development, Competition, and Innovation Act to clarify the definition of foreign country for purposes of malign foreign talent recruitment restriction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States Research Protection Act of 2025 .\n#### 2. Clarification of definition of foreign country for purposes of malign foreign talent recruitment restriction\nParagraph (4) of section 10638 of title VI of division B of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19237 ) is amended\u2014\n**(1)**\nby inserting of concern after foreign country each place such term appears;\n**(2)**\nby striking means\u2014 and all that follows through any program, position, or activity and inserting means any program, position, or activity ;\n**(3)**\nby striking subparagraph (B);\n**(4)**\nby redesignating clauses (i) through (ix) as subparagraphs (A) through (I), respectively, and moving such subparagraphs, as so redesignated, two ems to the left;\n**(5)**\nin the matter preceding subparagraph (A), as so redesignated, by striking directly provided and inserting whether directly or indirectly provided ; and\n**(6)**\nin subparagraph (I), as so redesignated, by striking ; and and inserting a period.",
      "versionDate": "2025-07-22",
      "versionType": "Reported in Senate"
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
            "updateDate": "2025-03-25T14:25:26Z"
          },
          {
            "name": "International scientific cooperation",
            "updateDate": "2025-03-25T14:25:26Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-03-25T14:25:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-21T16:51:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s769",
          "measure-number": "769",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s769v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>United States Research Protection Act of 2025</strong></p><p>This bill clarifies the definition of a\u00a0<em>malign foreign talent recruitment program</em> under the Research and Development, Competition, and Innovation Act.<em>\u00a0</em></p><p>The Research and Development, Competition, and Innovation Act, which was included in the CHIPS and Science Act, prohibits researchers who receive federal funds from participating in malign foreign talent recruitment programs, in which foreign countries incentivize or compensate researchers for activities that present a conflict\u00a0of\u00a0interest for the researcher or that are otherwise unauthorized (e.g., sharing proprietary information without proper authorization).</p><p>The bill clarifies that these restrictions apply to programs that are sponsored by a foreign country of concern, including China, Iran, North Korea, and Russia. The bill also clarifies that malign foreign talent recruitment programs may involve direct or indirect compensation or incentives from such\u00a0countries.</p>"
        },
        "title": "United States Research Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s769.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>United States Research Protection Act of 2025</strong></p><p>This bill clarifies the definition of a\u00a0<em>malign foreign talent recruitment program</em> under the Research and Development, Competition, and Innovation Act.<em>\u00a0</em></p><p>The Research and Development, Competition, and Innovation Act, which was included in the CHIPS and Science Act, prohibits researchers who receive federal funds from participating in malign foreign talent recruitment programs, in which foreign countries incentivize or compensate researchers for activities that present a conflict\u00a0of\u00a0interest for the researcher or that are otherwise unauthorized (e.g., sharing proprietary information without proper authorization).</p><p>The bill clarifies that these restrictions apply to programs that are sponsored by a foreign country of concern, including China, Iran, North Korea, and Russia. The bill also clarifies that malign foreign talent recruitment programs may involve direct or indirect compensation or incentives from such\u00a0countries.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s769"
    },
    "title": "United States Research Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>United States Research Protection Act of 2025</strong></p><p>This bill clarifies the definition of a\u00a0<em>malign foreign talent recruitment program</em> under the Research and Development, Competition, and Innovation Act.<em>\u00a0</em></p><p>The Research and Development, Competition, and Innovation Act, which was included in the CHIPS and Science Act, prohibits researchers who receive federal funds from participating in malign foreign talent recruitment programs, in which foreign countries incentivize or compensate researchers for activities that present a conflict\u00a0of\u00a0interest for the researcher or that are otherwise unauthorized (e.g., sharing proprietary information without proper authorization).</p><p>The bill clarifies that these restrictions apply to programs that are sponsored by a foreign country of concern, including China, Iran, North Korea, and Russia. The bill also clarifies that malign foreign talent recruitment programs may involve direct or indirect compensation or incentives from such\u00a0countries.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s769"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s769is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s769rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "United States Research Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T12:03:19Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "United States Research Protection Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-07-24T01:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "United States Research Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Research and Development, Competition, and Innovation Act to clarify the definition of foreign country for purposes of malign foreign talent recruitment restriction, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:37Z"
    }
  ]
}
```
