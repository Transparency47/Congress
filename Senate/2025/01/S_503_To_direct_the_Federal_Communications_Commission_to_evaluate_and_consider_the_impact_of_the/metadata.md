# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/503?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/503
- Title: NET Act
- Congress: 119
- Bill type: S
- Bill number: 503
- Origin chamber: Senate
- Introduced date: 2025-02-10
- Update date: 2026-04-09T14:21:08Z
- Update date including text: 2026-04-09T14:21:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in Senate
- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-05-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-66.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-66.
- 2025-09-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 171.
- 2025-11-04 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S7904-7905; text: CR S7905)
- 2025-11-04 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-11-07 - Floor: Message on Senate action sent to the House.
- 2025-11-10 12:02:53 - Floor: Received in the House.
- 2025-11-10 12:03:00 - Floor: Held at the desk.
- Latest action: 2025-02-10: Introduced in Senate

## Actions

- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-05-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-66.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-66.
- 2025-09-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 171.
- 2025-11-04 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S7904-7905; text: CR S7905)
- 2025-11-04 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-11-07 - Floor: Message on Senate action sent to the House.
- 2025-11-10 12:02:53 - Floor: Received in the House.
- 2025-11-10 12:03:00 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/503",
    "number": "503",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "NET Act",
    "type": "S",
    "updateDate": "2026-04-09T14:21:08Z",
    "updateDateIncludingText": "2026-04-09T14:21:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-11-10",
      "actionTime": "12:03:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-11-10",
      "actionTime": "12:02:53",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S7904-7905; text: CR S7905)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 171.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-66.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-29",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-66.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-02-10",
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
      "actionDate": "2025-02-10",
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
            "date": "2025-09-29T19:36:56Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-21T16:04:27Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-11T00:02:25Z",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "KS"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "WV"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s503is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 503\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2025 Mr. Hickenlooper (for himself, Mr. Moran , Mrs. Capito , and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Federal Communications Commission to evaluate and consider the impact of the telecommunications network equipment supply chain on the deployment of universal service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Network Equipment Transparency Act or the NET Act .\n#### 2. Telecommunications supply chain consideration\n##### (a) In general\nSection 13(b) of the Communications Act of 1934 ( 47 U.S.C. 163(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (3), (4), and (5) as paragraphs (4), (5), and (6), respectively; and\n**(2)**\nby inserting after paragraph (2) the following:\n(3) assess, to the extent that data is available to the Commission, how the availability of network equipment may have impacted the deployment of advanced telecommunications capability during the applicable reporting period; .\n##### (b) Rule of construction\nNothing in the amendments made by subsection (a) shall be construed to require any provider of advanced telecommunications capability to provide the Federal Communications Commission more information than was required for the purpose of section 13 of the Communications Act of 1934 ( 47 U.S.C. 163 ) as in effect on the day before the date of enactment of this Act.\n##### (c) Technical and conforming amendments\nSection 13 of the Communications Act of 1934 ( 47 U.S.C. 163 ), as amended by subsection (a), is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (5), as so redesignated, by striking (3) and inserting (4) ; and\n**(B)**\nin paragraph (6), as so redesignated, by striking (4) and inserting (5) ;\n**(2)**\nin subsection (c), by striking (b)(4) and inserting (b)(5) ; and\n**(3)**\nin subsection (d)(3), by striking (b)(3) and inserting (b)(4) .",
      "versionDate": "2025-02-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s503rs.xml",
      "text": "II\nCalendar No. 171\n119th CONGRESS\n1st Session\nS. 503\n[Report No. 119\u201366]\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2025 Mr. Hickenlooper (for himself, Mr. Moran , Mrs. Capito , and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nSeptember 29, 2025 Reported by Mr. Cruz , without amendment\nA BILL\nTo direct the Federal Communications Commission to evaluate and consider the impact of the telecommunications network equipment supply chain on the deployment of universal service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Network Equipment Transparency Act or the NET Act .\n#### 2. Telecommunications supply chain consideration\n##### (a) In general\nSection 13(b) of the Communications Act of 1934 ( 47 U.S.C. 163(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (3), (4), and (5) as paragraphs (4), (5), and (6), respectively; and\n**(2)**\nby inserting after paragraph (2) the following:\n(3) assess, to the extent that data is available to the Commission, how the availability of network equipment may have impacted the deployment of advanced telecommunications capability during the applicable reporting period; .\n##### (b) Rule of construction\nNothing in the amendments made by subsection (a) shall be construed to require any provider of advanced telecommunications capability to provide the Federal Communications Commission more information than was required for the purpose of section 13 of the Communications Act of 1934 ( 47 U.S.C. 163 ) as in effect on the day before the date of enactment of this Act.\n##### (c) Technical and conforming amendments\nSection 13 of the Communications Act of 1934 ( 47 U.S.C. 163 ), as amended by subsection (a), is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (5), as so redesignated, by striking (3) and inserting (4) ; and\n**(B)**\nin paragraph (6), as so redesignated, by striking (4) and inserting (5) ;\n**(2)**\nin subsection (c), by striking (b)(4) and inserting (b)(5) ; and\n**(3)**\nin subsection (d)(3), by striking (b)(3) and inserting (b)(4) .",
      "versionDate": "2025-09-29",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s503es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 503\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo direct the Federal Communications Commission to evaluate and consider the impact of the telecommunications network equipment supply chain on the deployment of universal service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Network Equipment Transparency Act or the NET Act .\n#### 2. Telecommunications supply chain consideration\n##### (a) In general\nSection 13(b) of the Communications Act of 1934 ( 47 U.S.C. 163(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (3), (4), and (5) as paragraphs (4), (5), and (6), respectively; and\n**(2)**\nby inserting after paragraph (2) the following:\n(3) assess, to the extent that data is available to the Commission, how the availability of network equipment may have impacted the deployment of advanced telecommunications capability during the applicable reporting period; .\n##### (b) Rule of construction\nNothing in the amendments made by subsection (a) shall be construed to require any provider of advanced telecommunications capability to provide the Federal Communications Commission more information than was required for the purpose of section 13 of the Communications Act of 1934 ( 47 U.S.C. 163 ) as in effect on the day before the date of enactment of this Act.\n##### (c) Technical and conforming amendments\nSection 13 of the Communications Act of 1934 ( 47 U.S.C. 163 ), as amended by subsection (a), is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (5), as so redesignated, by striking (3) and inserting (4) ; and\n**(B)**\nin paragraph (6), as so redesignated, by striking (4) and inserting (5) ;\n**(2)**\nin subsection (c), by striking (b)(4) and inserting (b)(5) ; and\n**(3)**\nin subsection (d)(3), by striking (b)(3) and inserting (b)(4) .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Congressional oversight",
            "updateDate": "2025-05-22T13:39:34Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-22T13:39:34Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-09T14:21:08Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-05-22T13:39:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-12T13:48:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119s503",
          "measure-number": "503",
          "measure-type": "s",
          "orig-publish-date": "2025-02-10",
          "originChamber": "SENATE",
          "update-date": "2025-03-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s503v00",
            "update-date": "2025-03-28"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Network Equipment Transparency Act or the NET Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to report biennially on the impact of network equipment availability on the deployment of advanced telecommunications capabilities (i.e., broadband). This assessment must be included in the FCC\u2019s reports on the state of the communications marketplace, which are submitted to Congress and published publicly every other year.\u00a0</p>"
        },
        "title": "NET Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s503.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Network Equipment Transparency Act or the NET Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to report biennially on the impact of network equipment availability on the deployment of advanced telecommunications capabilities (i.e., broadband). This assessment must be included in the FCC\u2019s reports on the state of the communications marketplace, which are submitted to Congress and published publicly every other year.\u00a0</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119s503"
    },
    "title": "NET Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Network Equipment Transparency Act or the NET Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to report biennially on the impact of network equipment availability on the deployment of advanced telecommunications capabilities (i.e., broadband). This assessment must be included in the FCC\u2019s reports on the state of the communications marketplace, which are submitted to Congress and published publicly every other year.\u00a0</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119s503"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s503is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s503rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s503es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "NET Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T12:03:14Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "NET Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-11-05T10:53:13Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Network Equipment Transparency Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-11-05T10:53:13Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Network Equipment Transparency Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "NET Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NET Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Network Equipment Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Federal Communications Commission to evaluate and consider the impact of the telecommunications network equipment supply chain on the deployment of universal service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:30Z"
    }
  ]
}
```
