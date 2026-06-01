# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6655?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6655
- Title: CFTC Charitable Organization Exemption Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6655
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-05-16T08:07:29Z
- Update date including text: 2026-05-16T08:07:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6655",
    "number": "6655",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001232",
        "district": "6",
        "firstName": "April",
        "fullName": "Rep. McClain Delaney, April [D-MD-6]",
        "lastName": "McClain Delaney",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "CFTC Charitable Organization Exemption Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:29Z",
    "updateDateIncludingText": "2026-05-16T08:07:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:06:16Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6655ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6655\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mrs. McClain Delaney (for herself and Mr. Messmer ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo exempt charitable organizations from commodity trading regulations and registration requirements.\n#### 1. Short title\nThis Act may be cited as the CFTC Charitable Organization Exemption Act of 2025 .\n#### 2. Exemption of qualified charitable organizations from regulation as commodity pool operators\nSection 4m of the Commodity Exchange Act ( 7 U.S.C. 6m ) is amended to read as follows:\n4m. Use of mails or other means or instrumentalities of interstate commerce by commodity trading advisors and commodity pool operators (a) Prohibition It shall be unlawful for any commodity trading advisor or commodity pool operator, unless registered under this Act, to make use of the mails or any means or instrumentality of interstate commerce in connection with business as the commodity trading advisor or commodity pool operator. (b) Exceptions (1) In general Subsection (a) shall not apply to a commodity trading advisor whose commodity trading advice is solely incidental to the conduct of that person\u2019s business, and who is a\u2014 (A) dealer, processor, broker, or seller in cash market transactions of any commodity specifically set forth in section 2(a) of this Act before the enactment of the Commodity Futures Trading Commission Act of 1974 (or products thereof); or (B) nonprofit, voluntary membership, general farm organization, that provides advice on the sale or purchase of any commodity specifically set forth in section 2(a) of this Act before the enactment of the Commodity Futures Trading Commission Act of 1974. (2) Charitable organization Subsection (a) shall not apply to any commodity trading advisor or commodity pool operator that is\u2014 (A) a charitable organization, as defined in section 3(c)(10)(D) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133(c)(10)(D) ), or a trustee, director, officer, employee, or volunteer of such a charitable organization acting within the scope of the employment or duties of the person with the organization, whose advisory or pool activities are conducted only on behalf of, or with respect to, 1 or more of\u2014 (i) any such charitable organization; or (ii) an investment trust, syndicate, or similar form of enterprise excluded from the definition of investment company pursuant to section 3(c)(10) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133(c)(10) ), or the trustees, administrators, settlors (or potential settlors), or beneficiaries of the foregoing; or (B) any plan, company, or account described in section 3(c)(14) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133(c)(14) ), any person or entity who establishes or maintains such a plan, company, or account, or any trustee, director, officer, employee, or volunteer for any of the foregoing plans, persons, or entities acting within the scope of the employment or duties of the person with the organization, whose advisory or pool activities are conducted only on behalf of, or with respect to, any investment trust, syndicate, or similar form of enterprise excluded from the definition of investment company pursuant to section 3(c)(14) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133(c)(14) ). (3) Small commodity trading advisors Subsection (a) shall not apply to any commodity trading advisor who, during the course of the preceding 12 months, has not furnished commodity trading advice to more than 15 persons and who does not hold themselves out generally to the public as a commodity trading advisor. (4) SEC-registered (A) In general Subsection (a) shall not apply to any commodity trading advisor that is registered with the Securities and Exchange Commission as an investment adviser whose business does not consist primarily of acting as a commodity trading advisor and that does not act as a commodity trading advisor to any commodity pool that is primarily engaged in trading commodity interests. (B) Engaged primarily For purposes of this paragraph, a commodity trading advisor or a commodity pool shall be considered to be engaged primarily in the business of being a commodity trading advisor or commodity pool if it is or holds itself out to the public as being engaged primarily, or proposes to engage primarily, in the business of advising on commodity interests or investing, reinvesting, owning, holding, or trading in commodity interests, respectively. (C) Commodity interests For purposes of this paragraph, commodity interests shall include contracts of sale of a commodity for future delivery, options on such contracts, security futures, swaps, leverage contracts, foreign exchange, spot and forward contracts on physical commodities, and any monies held in an account used for trading commodity interests. (5) Subject to proceedings A person described in paragraphs (1) and (2) shall be subject to proceedings under section 14. (c) Relationship to other law Nothing in this Act shall relieve any person of any obligation or duty, or affect the availability of any right or remedy available to the Securities and Exchange Commission or any private party arising under the Securities Act of 1933 ( 15 U.S.C. 77a et seq. ) or the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. ) governing the issuance, offer, purchase, or sale of securities of a commodity pool, or of persons engaged in transactions with respect to the securities, or reporting by a commodity pool. (d) Disclosure concerning exempted charitable organizations A commodity trading advisor or commodity pool operator that is an organization or person described in subsection (b)(2)(A) of this section to or of any investment trust, syndicate, or similar form of enterprise excluded from the definition of investment company pursuant to section 3(c)(10)(B) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133(c)(10)(B) ) shall provide disclosure in accordance with section 7(e) of that Act ( 15 U.S.C. 80a\u20137(e) ). .",
      "versionDate": "2025-12-11",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2026-01-08T15:24:00Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6655ih.xml"
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
      "title": "CFTC Charitable Organization Exemption Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CFTC Charitable Organization Exemption Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To exempt charitable organizations from commodity trading regulations and registration requirements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:26Z"
    }
  ]
}
```
