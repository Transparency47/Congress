# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1880?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1880
- Title: Broadcast Freedom and Independence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1880
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-01-28T09:05:26Z
- Update date including text: 2026-01-28T09:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1880",
    "number": "1880",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001163",
        "district": "7",
        "firstName": "Doris",
        "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
        "lastName": "Matsui",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Broadcast Freedom and Independence Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-28T09:05:26Z",
    "updateDateIncludingText": "2026-01-28T09:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "DC"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NJ"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "MD"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "AZ"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "OR"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NV"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1880ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1880\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Ms. Matsui (for herself, Ms. Barrag\u00e1n , and Ms. McClellan ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Communications Act of 1934 to clarify that the Federal Communications Commission may not take action against a broadcast licensee or any other person on the basis of viewpoint, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Broadcast Freedom and Independence Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Federal Communications Commission (in this section referred to as the FCC ) was established as an independent agency by the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) for the purpose of regulating interstate and foreign commerce in communication by wire and radio so as to make available, so far as possible, to all the people of the United States, without discrimination on the basis of race, color, religion, national origin, or sex, a rapid, efficient, Nation-wide, and world-wide wire and radio communication service with adequate facilities at reasonable charges\u2026 .\n**(2)**\nCommissioners at the FCC, an independent agency, are confirmed by Congress for specified terms and the President does not have the power to remove them at will.\n**(3)**\nThe independence of the FCC is paramount to the FCC carrying out its mission without political pressure or intimidation.\n**(4)**\nThe FCC\u2019s priorities and agenda must be set by the FCC without undue influence from the President or any advisors to the President who do not work for the FCC.\n**(5)**\nAs established in section 326 of the Communications Act of 1934 ( 47 U.S.C. 326 ), nothing in the FCC\u2019s authority shall be understood or construed to give the Commission the power of censorship over the radio communications or signals transmitted by any radio station, and no regulation or condition shall be promulgated or fixed by the Commission which shall interfere with the right of free speech by means of radio communication .\n**(6)**\nInvestigations and threats of Commission action or inaction must not be used to suppress certain viewpoints or intimidate broadcast licensees into aligning with any political agenda.\n#### 3. Viewpoint protection\nTitle I of the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) is amended by adding at the end the following:\n14. Viewpoint protection (a) Prohibition against retaliation on basis of viewpoint The Commission may not revoke any license or other authorization of, or otherwise take action against, any person on the basis, in whole or in part, of viewpoints broadcast or otherwise disseminated by that person or any person affiliated with that person. (b) Prohibition against conditions on viewpoint in transaction review The Commission may not place on any approval under subsections (a), (b), and (c) of section 214 or section 310(d) any condition with respect to viewpoints broadcast or otherwise disseminated by the person seeking that approval, any successor of that person, or any person affiliated with that person or successor. (c) No effect on certain other authority of Commission Nothing in this section shall be construed to affect the authority of the Commission to take action on the basis of, or to place a condition on an approval described in subsection (b) with respect to\u2014 (1) a violation of\u2014 (A) section 1304 of title 18, United States Code, or conduct that would constitute a violation of that section if content disseminated by means other than radio or television broadcast were disseminated by means of radio or television broadcast; (B) section 1343 of title 18, United States Code; or (C) section 1464 of title 18, United States Code, or conduct that would constitute a violation of that section if content disseminated by means other than radio communication were disseminated by means of radio communication; or (2) the broadcast or other dissemination of content that constitutes incitement under the First Amendment to the Constitution of the United States. .",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-05",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "867",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Broadcast Freedom and Independence Act of 2025",
      "type": "S"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-25T14:46:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1880",
          "measure-number": "1880",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-07-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1880v00",
            "update-date": "2025-07-28"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Broadcast Freedom and Independence Act of 2025</strong></p><p>This bill prohibits the Federal Communications Commission (FCC) from taking action against or imposing certain conditions on individuals on the basis of viewpoints broadcast or disseminated by the individuals or their affiliates.\u00a0</p><p>Specifically, the FCC may not revoke a license or authorization of, or otherwise take action against, an individual or entity on the basis of viewpoints broadcast or otherwise disseminated by the individual or entity or an affiliate thereof. Further, the FCC may not impose conditions on its approval of certain transactions on the basis of viewpoints broadcast or otherwise disseminated by the individual or entity seeking approval of the transaction, or an affiliate thereof.\u00a0</p><p>Under the bill, the FCC retains its authority to take action or impose conditions on the basis of (1) violations of certain existing laws regarding lottery information, fraud, and obscene language; or (2)\u00a0the broadcast or other dissemination of content that constitutes incitement under the First Amendment.\u00a0</p>"
        },
        "title": "Broadcast Freedom and Independence Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1880.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadcast Freedom and Independence Act of 2025</strong></p><p>This bill prohibits the Federal Communications Commission (FCC) from taking action against or imposing certain conditions on individuals on the basis of viewpoints broadcast or disseminated by the individuals or their affiliates.\u00a0</p><p>Specifically, the FCC may not revoke a license or authorization of, or otherwise take action against, an individual or entity on the basis of viewpoints broadcast or otherwise disseminated by the individual or entity or an affiliate thereof. Further, the FCC may not impose conditions on its approval of certain transactions on the basis of viewpoints broadcast or otherwise disseminated by the individual or entity seeking approval of the transaction, or an affiliate thereof.\u00a0</p><p>Under the bill, the FCC retains its authority to take action or impose conditions on the basis of (1) violations of certain existing laws regarding lottery information, fraud, and obscene language; or (2)\u00a0the broadcast or other dissemination of content that constitutes incitement under the First Amendment.\u00a0</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr1880"
    },
    "title": "Broadcast Freedom and Independence Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadcast Freedom and Independence Act of 2025</strong></p><p>This bill prohibits the Federal Communications Commission (FCC) from taking action against or imposing certain conditions on individuals on the basis of viewpoints broadcast or disseminated by the individuals or their affiliates.\u00a0</p><p>Specifically, the FCC may not revoke a license or authorization of, or otherwise take action against, an individual or entity on the basis of viewpoints broadcast or otherwise disseminated by the individual or entity or an affiliate thereof. Further, the FCC may not impose conditions on its approval of certain transactions on the basis of viewpoints broadcast or otherwise disseminated by the individual or entity seeking approval of the transaction, or an affiliate thereof.\u00a0</p><p>Under the bill, the FCC retains its authority to take action or impose conditions on the basis of (1) violations of certain existing laws regarding lottery information, fraud, and obscene language; or (2)\u00a0the broadcast or other dissemination of content that constitutes incitement under the First Amendment.\u00a0</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr1880"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1880ih.xml"
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
      "title": "Broadcast Freedom and Independence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Broadcast Freedom and Independence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Communications Act of 1934 to clarify that the Federal Communications Commission may not take action against a broadcast licensee or any other person on the basis of viewpoint, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:48:34Z"
    }
  ]
}
```
