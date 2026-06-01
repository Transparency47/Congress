# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1833?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1833
- Title: Leadership in CET Act
- Congress: 119
- Bill type: S
- Bill number: 1833
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2025-12-05T22:08:04Z
- Update date including text: 2025-12-05T22:08:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1833",
    "number": "1833",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Leadership in CET Act",
    "type": "S",
    "updateDate": "2025-12-05T22:08:04Z",
    "updateDateIncludingText": "2025-12-05T22:08:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T17:18:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "VT"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "AL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1833is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1833\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mrs. Blackburn (for herself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Under Secretary of Commerce for Intellectual Property and Director of the United States Patent and Trademark Office to establish and carry out a pilot program to expedite the examination of applications for certain patents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Leadership in Critical and Emerging Technologies Act or the Leadership in CET Act .\n#### 2. Pilot program for expediting examination of certain critical and emerging technology patent applications\n##### (a) Definitions\nIn this section:\n**(1) Covered application**\nThe term covered application means an application for patent that contains at least 1 claimed invention directed to an eligible critical or emerging technology.\n**(2) Director**\nThe term Director means the Under Secretary of Commerce for Intellectual Property and Director of the Office.\n**(3) Eligible critical or emerging technology**\nThe term eligible critical or emerging technology means\u2014\n**(A)**\nan artificial intelligence capability relating to\u2014\n**(i)**\nmachine learning;\n**(ii)**\ndeep learning;\n**(iii)**\nreinforcement learning;\n**(iv)**\nsensory perception or recognition;\n**(v)**\nan artificial intelligence assurance or assessment technique;\n**(vi)**\na foundation model;\n**(vii)**\na generative artificial intelligence system or multimodal or large language model;\n**(viii)**\na synthetic data approach for training, tuning, or testing;\n**(ix)**\nplanning, reasoning, or decision making; or\n**(x)**\nthe improvement of artificial intelligence safety, trust, security, or responsible use;\n**(B)**\nsemiconductor design or an electronic design automation tool; or\n**(C)**\na quantum information science capability relating to\u2014\n**(i)**\nquantum computing;\n**(ii)**\nmaterials, isotopes, or fabrication techniques for quantum devices;\n**(iii)**\nquantum sensing; or\n**(iv)**\nquantum communications or networking.\n**(4) Expedite**\nThe term expedite means, with respect to a covered application, to advance that covered application out of turn through the use of a petition to make special.\n**(5) Office**\nThe term Office means the United States Patent and Trademark Office.\n**(6) Pilot program**\nThe term pilot program means the pilot program established under subsection (b).\n##### (b) Establishment\nNot later than 1 year after the date of enactment of this Act, the Director shall establish a pilot program to expedite the examination, under section 131 of title 35, United States Code, of covered applications.\n##### (c) Purpose\nThe purpose of the pilot program shall be to encourage innovation by, and the leadership of, the United States with respect to critical or emerging technologies by ensuring that covered applications receive prompt consideration.\n##### (d) Implementation\nIn carrying out the pilot program, the Director may\u2014\n**(1)**\nby regulation, and in addition to the requirements under subsection (e), prescribe the conditions under which a covered application shall be accepted and examined under the pilot program, including\u2014\n**(A)**\nthe requirements to participate in the pilot program;\n**(B)**\ninternal processing by the Office of covered applications under the pilot program;\n**(C)**\nrequirements for restriction or unity of inventions identified in covered applications;\n**(D)**\nthe period during which the applicant submitting the covered application may reply with respect to an action taken by the Office with respect to the covered application;\n**(E)**\nstandards relating to a reply described in subparagraph (D);\n**(F)**\nstandards or procedures governing\u2014\n**(i)**\nany amendment, affidavit, or other evidence filed after a final action taken by the Office with respect to the covered application; and\n**(ii)**\nany process for appeal with respect to a final action described in clause (i); and\n**(G)**\nthe withdrawal, by an applicant, of a covered application submitted under the pilot program;\n**(2)**\nwaive\u2014\n**(A)**\nthe petition fee described in section 1.102(d) of title 37, Code of Federal Regulations, or any successor regulation; or\n**(B)**\nany other requirement of the Office relating to the accelerated examination program or the prioritized examination program; and\n**(3)**\nconsult with the Attorney General, the Secretary of Defense, the Secretary of State, the Secretary of the Treasury, the Director of National Intelligence, or the head of any other Federal agency, as may be appropriate to carry out the pilot program.\n##### (e) Qualifying applications\nTo best achieve the purpose of the pilot program, the Director shall ensure that a covered application satisfies the following requirements to qualify for the pilot program:\n**(1)**\nThe applicant submitting the covered application\u2014\n**(A)**\nis not a foreign entity of concern, as defined in section 9901 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 ); and\n**(B)**\ncertifies in the covered application that the inventor or any joint inventor with respect to any claimed invention in the covered application has not been named as the inventor or joint inventor with respect to more than 4 other covered applications submitted under the pilot program.\n**(2)**\nThe covered application is a noncontinuing, nonprovisional application for an original utility patent filed under section 111(a) of title 35, United States Code, that does not claim any domestic benefit under section 120, 121, 365(c), or 386(c) of that title.\n##### (f) Termination\n**(1) In general**\nThe pilot program shall terminate on the earlier of the following:\n**(A)**\nThe date that is 5 years after the date on which the Director first accepts a covered application for participation in the pilot program.\n**(B)**\nThe date on which the Director has accepted 15,000 covered applications for participation in the pilot program, without regard to whether those covered applications have been expedited under the pilot program.\n**(2) Renewal**\nIf the pilot program terminates under paragraph (1)(B), the Director may renew the pilot program for the shorter of the following:\n**(A)**\nAn additional 5-year period, beginning on the date on which the pilot program terminates under paragraph (1)(B).\n**(B)**\nAn additional period\u2014\n**(i)**\nbeginning on the date on which the pilot program terminates under paragraph (1)(B); and\n**(ii)**\nending on the date on which the Director has accepted an additional 15,000 covered applications for participation in the pilot program, without regard to whether those covered applications have been expedited under the pilot program.\n**(3) Notice of renewal**\nThe Director shall notify the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives of the intent of the Director to renew the pilot program under paragraph (2) not later than the date that is the earlier of the following:\n**(A)**\nThe date that is 60 days before the date described in paragraph (1)(A).\n**(B)**\nThe date that is 30 days after the date on which the Director has accepted 12,000 covered applications for participation in the pilot program, without regard to whether those covered applications have been expedited under the pilot program.\n##### (g) Public availability of information\nThe Director shall make publicly available in an easily accessible location on the website of the Office information about the pilot program, including\u2014\n**(1)**\nthe number of covered applications submitted under the pilot program;\n**(2)**\nthe number of covered applications described in paragraph (1) that the Director has accepted for participation in the pilot program; and\n**(3)**\nthe number of patents that have been issued for inventions claimed in covered applications expedited under the pilot program.\n##### (h) Report to Congress\n**(1) In general**\nNot later than 180 days after the date on which the pilot program terminates (including any renewal of the pilot program under subsection (f)(2)), the Director shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that assesses the impact and effectiveness of the pilot program based on all available data.\n**(2) Applicability**\nThe collection of any data for the purposes of carrying out paragraph (1) shall be exempt from subchapter I of chapter 35 of title 44, United States Code (commonly referred to as the Paperwork Reduction Act ).",
      "versionDate": "2025-05-21",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-05-21",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3539",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Leadership in CET Act",
      "type": "HR"
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
        "name": "Commerce",
        "updateDate": "2025-06-02T14:19:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-21",
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
          "measure-id": "id119s1833",
          "measure-number": "1833",
          "measure-type": "s",
          "orig-publish-date": "2025-05-21",
          "originChamber": "SENATE",
          "update-date": "2025-08-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1833v00",
            "update-date": "2025-08-15"
          },
          "action-date": "2025-05-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Leadership in Critical and Emerging Technologies Act or the Leadership in CET Act</strong></p><p>This bill directs the U.S. Patent and Trademark Office (USPTO) to establish and carry out a pilot program to expedite the patent examination process for patents involving critical or emerging technologies (i.e., artificial intelligence, semiconductor design, or quantum information science). The USPTO must report to Congress on the impact and effectiveness of the pilot program.</p>"
        },
        "title": "Leadership in CET Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1833.xml",
    "summary": {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Leadership in Critical and Emerging Technologies Act or the Leadership in CET Act</strong></p><p>This bill directs the U.S. Patent and Trademark Office (USPTO) to establish and carry out a pilot program to expedite the patent examination process for patents involving critical or emerging technologies (i.e., artificial intelligence, semiconductor design, or quantum information science). The USPTO must report to Congress on the impact and effectiveness of the pilot program.</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119s1833"
    },
    "title": "Leadership in CET Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Leadership in Critical and Emerging Technologies Act or the Leadership in CET Act</strong></p><p>This bill directs the U.S. Patent and Trademark Office (USPTO) to establish and carry out a pilot program to expedite the patent examination process for patents involving critical or emerging technologies (i.e., artificial intelligence, semiconductor design, or quantum information science). The USPTO must report to Congress on the impact and effectiveness of the pilot program.</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119s1833"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1833is.xml"
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
      "title": "Leadership in CET Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-24T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Leadership in CET Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Leadership in Critical and Emerging Technologies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Under Secretary of Commerce for Intellectual Property and Director of the United States Patent and Trademark Office to establish and carry out a pilot program to expedite the examination of applications for certain patents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:27Z"
    }
  ]
}
```
