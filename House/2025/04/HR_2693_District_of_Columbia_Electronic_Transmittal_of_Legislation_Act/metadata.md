# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2693?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2693
- Title: District of Columbia Electronic Transmittal of Legislation Act
- Congress: 119
- Bill type: HR
- Bill number: 2693
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-02-11T22:06:16Z
- Update date including text: 2026-02-11T22:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-07 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-07 - IntroReferral: Sponsor introductory remarks on measure. (CR E287)
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-07 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-07 - IntroReferral: Sponsor introductory remarks on measure. (CR E287)
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2693",
    "number": "2693",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "District of Columbia Electronic Transmittal of Legislation Act",
    "type": "HR",
    "updateDate": "2026-02-11T22:06:16Z",
    "updateDateIncludingText": "2026-02-11T22:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E287)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
        "item": [
          {
            "date": "2025-09-10T16:38:47Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-07T16:00:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-07T16:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2693ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2693\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the District of Columbia Home Rule Act to permit the Chairman of the Council of the District of Columbia to transmit Acts of the District of Columbia to Congress in electronic form.\n#### 1. Short title\nThis Act may be cited as the District of Columbia Electronic Transmittal of Legislation Act .\n#### 2. Permitting District of Columbia to transmit Acts of District in electronic form\n##### (a) Acts of Council\nSection 602(c) of the District of Columbia Home Rule Act (sec. 1\u2013206.02(c), D.C. Official Code) is amended by adding at the end the following new paragraph:\n(4) The Chairman of the Council may transmit an Act under this subsection in such form as the Chairman may choose, including electronic form. .\n##### (b) Charter amendments\nSection 303 of such Act (sec. 1\u2013203.03, D.C. Official Code) is amended by adding at the end the following new subsection:\n(e) The Chairman of the Council may submit an Act under this section in such form as the Chairman may choose, including electronic form. .\n#### 3. Acceptance by House and Senate\n##### (a) Acceptance\nFor purposes of determining whether the Chairman of the Council of the District of Columbia has transmitted an Act to Congress pursuant to section 602(c) of the District of Columbia Home Rule Act (sec. 1\u2013206.02(c), D.C. Official Code) or has submitted an Act to Congress pursuant to section 303 of such Act (sec. 1\u2013203.03, D.C. Official Code), the House of Representatives and Senate shall treat such an Act which the Chairman transmits or submits in electronic form in the same manner as an Act which the Chairman submits in paper form.\n##### (b) Exercise of rulemaking authority\nThis section is enacted by Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the Senate and House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House in the case of Acts described in subsection (a), and supersede other rules only to the extent that it is inconsistent with such rules; and\n**(2)**\nwith full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.",
      "versionDate": "2025-04-07",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computers and information technology",
            "updateDate": "2025-09-16T14:08:56Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-16T14:08:56Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-09-16T14:08:56Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-16T14:08:56Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-09-16T14:08:56Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-09-16T14:08:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-27T15:40:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-07",
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
          "measure-id": "id119hr2693",
          "measure-number": "2693",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-07",
          "originChamber": "HOUSE",
          "update-date": "2025-09-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2693v00",
            "update-date": "2025-09-09"
          },
          "action-date": "2025-04-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>District of Columbia Electronic Transmittal of Legislation Act</strong></p><p>This bill authorizes the District of Columbia (DC) Council to transmit legislation, including amendments to the DC Charter, to Congress by electronic means. (Current law requires most nonemergency DC legislation to be transmitted to Congress for\u00a0a period of congressional review.)</p>"
        },
        "title": "District of Columbia Electronic Transmittal of Legislation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2693.xml",
    "summary": {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>District of Columbia Electronic Transmittal of Legislation Act</strong></p><p>This bill authorizes the District of Columbia (DC) Council to transmit legislation, including amendments to the DC Charter, to Congress by electronic means. (Current law requires most nonemergency DC legislation to be transmitted to Congress for\u00a0a period of congressional review.)</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hr2693"
    },
    "title": "District of Columbia Electronic Transmittal of Legislation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>District of Columbia Electronic Transmittal of Legislation Act</strong></p><p>This bill authorizes the District of Columbia (DC) Council to transmit legislation, including amendments to the DC Charter, to Congress by electronic means. (Current law requires most nonemergency DC legislation to be transmitted to Congress for\u00a0a period of congressional review.)</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hr2693"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2693ih.xml"
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
      "title": "District of Columbia Electronic Transmittal of Legislation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-17T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "District of Columbia Electronic Transmittal of Legislation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the District of Columbia Home Rule Act to permit the Chairman of the Council of the District of Columbia to transmit Acts of the District of Columbia to Congress in electronic form.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T05:18:37Z"
    }
  ]
}
```
