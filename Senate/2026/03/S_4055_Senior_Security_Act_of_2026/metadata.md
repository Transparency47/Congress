# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4055?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4055
- Title: Senior Security Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4055
- Origin chamber: Senate
- Introduced date: 2026-03-11
- Update date: 2026-04-02T19:49:45Z
- Update date including text: 2026-04-02T19:49:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-11: Introduced in Senate
- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-03-11: Introduced in Senate

## Actions

- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-11",
    "latestAction": {
      "actionDate": "2026-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4055",
    "number": "4055",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Senior Security Act of 2026",
    "type": "S",
    "updateDate": "2026-04-02T19:49:45Z",
    "updateDateIncludingText": "2026-04-02T19:49:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-11",
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
          "date": "2026-03-11T18:10:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "ME"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4055is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4055\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2026 Mr. Kim (for himself, Ms. Collins , Mrs. Gillibrand , and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo create an interdivisional taskforce at the Securities and Exchange Commission for senior investors.\n#### 1. Short title\nThis Act may be cited as the National Senior Investor Initiative Act of 2026 or the Senior Security Act of 2026 .\n#### 2. Senior Investor Taskforce\nSection 4 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78d ) is amended by adding at the end the following:\n(k) Senior Investor Taskforce (1) Establishment There is established within the Commission the Senior Investor Taskforce (in this subsection referred to as the Taskforce ). (2) Director of the Taskforce The head of the Taskforce shall be the Director, who shall\u2014 (A) report directly to the Chairman; and (B) be appointed by the Chairman, in consultation with the Commission, from among individuals\u2014 (i) currently employed by the Commission or from outside of the Commission; and (ii) having experience in advocating for the interests of senior investors. (3) Staffing The Chairman shall ensure that\u2014 (A) the Taskforce is staffed sufficiently to carry out fully the requirements of this subsection; and (B) such staff shall include individuals from the Division of Enforcement, the Office of Compliance Inspections and Examinations, and the Office of Investor Education and Assistance. (4) No compensation for members of Taskforce All members of the Taskforce appointed under paragraph (2) or (3) shall serve without compensation in addition to that received for their services as officers or employees of the United States. (5) Minimizing duplication of efforts In organizing and staffing the Taskforce, the Chairman shall take such actions as may be necessary to minimize the duplication of efforts within the divisions and offices described in paragraph (3)(B) and any other divisions, offices, or taskforces of the Commission. (6) Functions of the Taskforce The Taskforce shall\u2014 (A) identify challenges that senior investors encounter, including problems associated with financial exploitation and cognitive decline; (B) identify areas in which senior investors would benefit from changes in the regulations of the Commission or the rules of self-regulatory organizations; (C) coordinate, as appropriate, with other offices within the Commission, other taskforces that may be established within the Commission, self-regulatory organizations, and the Elder Justice Coordinating Council; and (D) consult, as appropriate, with State securities and law enforcement authorities, State insurance regulators, and other Federal agencies. (7) Report The Taskforce, in coordination, as appropriate, with the Office of the Investor Advocate and self-regulatory organizations, and in consultation, as appropriate, with State securities and law enforcement authorities, State insurance regulators, and Federal agencies, shall issue a report every 2 years to the Committee on Banking, Housing, and Urban Affairs and the Special Committee on Aging of the Senate and the Committee on Financial Services of the House of Representatives, the first of which shall not be issued until after the report described in section 3 of the National Senior Investor Initiative Act of 2026 has been submitted and considered by the Taskforce, containing\u2014 (A) appropriate statistical information and full and substantive analysis; (B) a summary of recent trends and innovations that have impacted the investment landscape for senior investors; (C) a summary of regulatory initiatives that have concentrated on senior investors and industry practices related to senior investors; (D) key observations, best practices, and areas needing improvement involving senior investors identified during examinations, enforcement actions, and investor education outreach; (E) a summary of the most serious issues encountered by senior investors, including issues involving financial products and services; (F) an analysis with regard to existing policies and procedures of brokers, dealers, investment advisers, and other market participants related to senior investors and senior investor-related topics and whether these policies and procedures need to be further developed or refined; (G) recommendations for such changes to the regulations, guidance, and orders of the Commission and self-regulatory organizations and such legislative actions as may be appropriate to resolve problems encountered by senior investors; and (H) any other information, as determined appropriate by the Director of the Taskforce. (8) Request for reports The Taskforce shall make any report issued under paragraph (7) available to a Member of Congress who requests such a report. (9) Sunset The Taskforce shall terminate after the end of the 10-year period beginning on the date of enactment of this subsection. (10) Senior investor defined In this subsection, the term senior investor means an investor over the age of 65. (11) Use of existing funds The Commission shall use existing funds to carry out this subsection. .\n#### 3. GAO study\n##### (a) Study\nNot later than 2 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress and the Senior Investor Taskforce established under subsection (k) of section 4 of the Securities Exchange Act ( 15 U.S.C. 78d ), as added by section 2 of this Act, the results of a study of financial exploitation of senior citizens.\n##### (b) Contents\nThe study required under subsection (a) shall include information with respect to\u2014\n**(1)**\neconomic costs of the financial exploitation of senior citizens\u2014\n**(A)**\nassociated with losses by victims that were incurred as a result of the financial exploitation of senior citizens;\n**(B)**\nincurred by State and Federal agencies, law enforcement and investigatory agencies, public benefit programs, public health programs, and other public programs as a result of the financial exploitation of senior citizens;\n**(C)**\nincurred by the private sector as a result of the financial exploitation of senior citizens; and\n**(D)**\nany other relevant costs that\u2014\n**(i)**\nresult from the financial exploitation of senior citizens; and\n**(ii)**\nthe Comptroller General determines are necessary and appropriate to include in order to provide Congress and the public with a full and accurate understanding of the economic costs resulting from the financial exploitation of senior citizens in the United States;\n**(2)**\nthe frequency of senior financial exploitation and correlated or contributing factors, including\u2014\n**(A)**\ninformation about the percentage of senior citizens financially exploited each year; and\n**(B)**\ninformation about factors contributing to increased risk of exploitation, including such factors as race, social isolation, income, net worth, religion, region, occupation, education, home-ownership, illness, and loss of spouse; and\n**(3)**\npolicy responses and reporting of senior financial exploitation, including\u2014\n**(A)**\nthe degree to which the financial exploitation of senior citizens is unreported to authorities;\n**(B)**\nthe reasons that financial exploitation may be unreported to authorities;\n**(C)**\nto the extent that suspected elder financial exploitation is currently being reported to authorities\u2014\n**(i)**\ninformation regarding which Federal, State, and local agencies are receiving reports, including adult protective services, law enforcement, industry, regulators, and professional licensing boards;\n**(ii)**\ninformation regarding what information is being collected by such agencies; and\n**(iii)**\ninformation regarding the actions that are taken by such agencies upon receipt of the report and any limits on the agencies\u2019 ability to prevent exploitation, such as jurisdictional limits, a lack of expertise, resource challenges, or limiting criteria with regard to the types of victims they are permitted to serve;\n**(D)**\nan analysis of gaps that may exist in empowering Federal, State, and local agencies to prevent senior exploitation or respond effectively to suspected senior financial exploitation; and\n**(E)**\nan analysis of the legal hurdles that prevent Federal, State, and local agencies from effectively partnering with each other and private professionals to effectively respond to senior financial exploitation.\n##### (c) Senior citizen defined\nIn section, the term senior citizen means an individual over the age of 65.",
      "versionDate": "2026-03-11",
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
        "actionDate": "2025-07-22",
        "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1469",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Senior Security Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-30T15:34:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-11",
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
          "measure-id": "id119s4055",
          "measure-number": "4055",
          "measure-type": "s",
          "orig-publish-date": "2026-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4055v00",
            "update-date": "2026-04-02"
          },
          "action-date": "2026-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>National Senior Investor Initiative Act of 2026 or the Senior Security Act of 2026</strong></p><p>This bill establishes the Senior Investor Taskforce within the Securities and Exchange Commission. The taskforce must report on topics relating to investors over the age of 65, including industry trends and serious issues impacting such investors, and make recommendations for legislative or regulatory actions to address problems encountered by senior investors.</p><p>The Government Accountability Office must report on the financial exploitation of senior citizens.</p>"
        },
        "title": "Senior Security Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4055.xml",
    "summary": {
      "actionDate": "2026-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>National Senior Investor Initiative Act of 2026 or the Senior Security Act of 2026</strong></p><p>This bill establishes the Senior Investor Taskforce within the Securities and Exchange Commission. The taskforce must report on topics relating to investors over the age of 65, including industry trends and serious issues impacting such investors, and make recommendations for legislative or regulatory actions to address problems encountered by senior investors.</p><p>The Government Accountability Office must report on the financial exploitation of senior citizens.</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119s4055"
    },
    "title": "Senior Security Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>National Senior Investor Initiative Act of 2026 or the Senior Security Act of 2026</strong></p><p>This bill establishes the Senior Investor Taskforce within the Securities and Exchange Commission. The taskforce must report on topics relating to investors over the age of 65, including industry trends and serious issues impacting such investors, and make recommendations for legislative or regulatory actions to address problems encountered by senior investors.</p><p>The Government Accountability Office must report on the financial exploitation of senior citizens.</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119s4055"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4055is.xml"
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
      "title": "Senior Security Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Senior Security Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "National Senior Investor Initiative Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to create an interdivisional taskforce at the Securities and Exchange Commission for senior investors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T04:03:32Z"
    }
  ]
}
```
