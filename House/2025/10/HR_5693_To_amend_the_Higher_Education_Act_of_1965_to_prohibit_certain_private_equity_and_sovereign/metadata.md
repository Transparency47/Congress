# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5693?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5693
- Title: PROTECT Act
- Congress: 119
- Bill type: HR
- Bill number: 5693
- Origin chamber: House
- Introduced date: 2025-10-06
- Update date: 2025-12-12T16:55:08Z
- Update date including text: 2025-12-12T16:55:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-06: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-10-06: Introduced in House

## Actions

- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5693",
    "number": "5693",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001322",
        "district": "5",
        "firstName": "Michael",
        "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
        "lastName": "Baumgartner",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "PROTECT Act",
    "type": "HR",
    "updateDate": "2025-12-12T16:55:08Z",
    "updateDateIncludingText": "2025-12-12T16:55:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-06",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-06",
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
          "date": "2025-10-06T19:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5693ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5693\nIN THE HOUSE OF REPRESENTATIVES\nOctober 6, 2025 Mr. Baumgartner introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to prohibit certain private-equity and sovereign wealth fund agreements involving intercollegiate athletics.\n#### 1. Short title\nThis Act may be cited as the Protect College Sports from Private Equity and Foreign Influence Act or the PROTECT Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIntercollegiate athletics are conducted under the auspices of nonprofit institutions of higher education and, when properly governed, promote student development, campus life, community identity, and broad public engagement in education\u2014benefits that constitute a public good aligned with the educational missions those institutions are chartered to serve.\n**(2)**\nIntercollegiate athletics generate billions of dollars in revenue annually through national media contracts, sponsorships, and ticket sales that span multiple States, creating a significant impact on interstate commerce.\n**(3)**\nPublic institutions of higher education are financed and supported by taxpayers through direct appropriations, tax-exempt status, subsidized Federal student aid, and tax-advantaged debt, and therefore have a heightened obligation to ensure that institutional assets\u2014including intercollegiate athletics programs and facilities\u2014are managed for public benefit and student welfare rather than private enrichment.\n**(4)**\nAgreements that convey ownership, revenue-sharing, control rights, or security interests in intercollegiate athletics to private equity, hedge funds, or similar vehicles are inherently conflicted, create pressure to maximize short-term cash flows at the expense of educational and Title IX obligations, and risk extracting wealth from publicly supported institutions and their students\u2014undermining transparency, accountability, and the public purposes for which those institutions exist.\n#### 3. Program participation agreements\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ) is amended by adding at the end the following:\n(30) Prohibition on private-capital and sovereign wealth agreements involving intercollegiate athletics (A) As a condition of eligibility under this title, an institution shall not enter into, maintain, or permit any agreement with a private capital firm or a sovereign wealth fund that\u2014 (i) transfers, assigns, pledges, or otherwise conveys to such firm or fund any ownership, profit, net-revenue, or gross-revenue interest arising from the institution\u2019s intercollegiate athletics program, including media, sponsorship, licensing, ticketing, premium seating, data, or other commercial rights; (ii) grants such firm or fund control rights over athletics decisions, institutional branding, scheduling, personnel, or student participation; or (iii) establishes a joint venture, new entity, or other agreement through which such firm or fund receives any share of, or any interest in, athletics-related revenues or rights, including licensing and merchandising rights, or athletics facilities or related real property including any leasehold, sublease, concession, easement, mortgage, deed of trust, lien, or similar property interest. (B) Exceptions Subparagraph (A) shall not apply to: (i) fee-for-service contracts for discrete services; (ii) charitable contributions, gifts, or grants; (iii) tax-exempt bond financings or lease-purchase agreements with governmental units or \u00a7501(c)(3) conduit issuers that do not convey revenue interests or control rights to a private capital firm; or (iv) sponsorships or advertising agreements that provide brand placement without revenue-sharing or control. (C) Conference and affiliate coverage An institution shall ensure compliance with this paragraph for any agreement entered by an athletics conference, media-rights consortium, or other affiliate that allocates, assigns, or encumbers the institution\u2019s athletics-related revenues or rights. (D) Collectives and controlled entities This paragraph applies to any collective, foundation, affiliate, or separate legal entity that is directly or indirectly owned, controlled, or operated by the institution or its athletics department. (E) Certification and disclosure The Secretary shall require annual program participation agreement certification that the institution and its affiliates have not entered into any agreement described under subparagraph (A) and shall require public disclosure of all agreements relying on an exception under subparagraph (B). (F) Definitions For purposes of this paragraph: (i) Private capital firm The term private capital firm means (I) a hedge fund or private equity fund as those terms are defined in 12 U.S.C. \u00a71851(h)(2), (II) a private fund as defined in 15 U.S.C. \u00a7 80b\u20132(a)(29), and (III) any investment adviser (as defined in 15 U.S.C. \u00a7 80b\u20132(a)(11)) that advises a fund described in subclause (I) or (II). (ii) Control rights The term control rights includes consent, veto, or approval rights over budgets, hiring, scheduling, competition, branding, or strategic decisions; or other rights to assume or direct management or operations of an intercollegiate athletics program or athletics facility. (iii) Intercollegiate athletics program The term intercollegiate athletics program includes teams, departments, conferences, media or data rights, ticketing and premium seating, sponsorships, licensing and merchandising, and athletics facilities used primarily for intercollegiate varsity sports competition. (iv) Sovereign wealth fund The term sovereign wealth fund means an investment fund owned or controlled by a foreign state, an agency or instrumentality of a foreign state (as defined in 28 U.S.C. \u00a71603), or an agent of a foreign principal (as defined in 22 U.S.C. \u00a7611). (G) Transition Agreements in effect on the date of enactment shall be brought into compliance or terminated not later than 24 months after such date. No agreement may be renewed or extended except in compliance with this paragraph. (H) Rulemaking The Secretary of Education shall issue regulations to carry out this paragraph after consultation with the Secretary of the Treasury and the Securities and Exchange Commission; and shall, to the maximum extent practicable, harmonize such regulations with definitions and interpretations under the Federal securities laws. .",
      "versionDate": "2025-10-06",
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
        "name": "Education",
        "updateDate": "2025-12-12T16:55:08Z"
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
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5693ih.xml"
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
      "title": "PROTECT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-15T02:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-15T02:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect College Sports from Private Equity and Foreign Influence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-15T02:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to prohibit certain private-equity and sovereign wealth fund agreements involving intercollegiate athletics.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-15T02:18:14Z"
    }
  ]
}
```
