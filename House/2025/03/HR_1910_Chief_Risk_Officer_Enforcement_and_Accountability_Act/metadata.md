# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1910?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1910
- Title: Chief Risk Officer Enforcement and Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 1910
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2026-01-23T16:44:16Z
- Update date including text: 2026-01-23T16:44:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1910",
    "number": "1910",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Chief Risk Officer Enforcement and Accountability Act",
    "type": "HR",
    "updateDate": "2026-01-23T16:44:16Z",
    "updateDateIncludingText": "2026-01-23T16:44:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "GA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "TX"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1910ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1910\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Casten (for himself, Mr. Sherman , Mr. David Scott of Georgia , Mr. Green of Texas , and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Financial Stability Act of 2010 to require certain large banking institutions to have a Chief Risk Officer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chief Risk Officer Enforcement and Accountability Act .\n#### 2. Chief risk officer\nSection 165(h) of the Financial Stability Act of 2010 ( 12 U.S.C. 5365(h) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nby striking that is a publicly traded company and each place such term appears; and\n**(B)**\nby inserting , and appoint a chief risk officer, as set forth in paragraph (4) after as set forth in paragraph (3) each place such term appears;\n**(2)**\nby redesignating paragraph (4) as paragraph (7); and\n**(3)**\nby inserting after paragraph (3) the following:\n(4) Chief risk officer (A) In general A chief risk officer required by this subsection shall be appointed by a company from among individuals with experience in identifying, assessing, and managing risk exposures of large, complex financial firms. (B) Responsibilities A chief risk officer shall be responsible for overseeing the following: (i) The establishment of risk limits on an enterprise-wide basis and the monitoring of compliance with such limits. (ii) The implementation of and ongoing compliance with the policies and procedures establishing risk-management governance, risk-management procedures, and risk-control infrastructure for the global operations of the company. (iii) The development and implementation of the processes and systems for implementing and monitoring compliance with the policies and procedures described under clause (ii), including\u2014 (I) processes and systems for identifying and reporting risks and risk-management deficiencies, including regarding emerging risks, and ensuring effective and timely implementation of actions to address emerging risks and risk-management deficiencies for the global operations of the company; (II) processes and systems for establishing managerial and employee responsibility for risk management; (III) processes and systems for ensuring the independence of the risk-management function; and (IV) processes and systems to integrate risk management and associated controls with management goals and the compensation structure of the company for the global operations of the company. (iv) The management of risks and risk controls within the parameters of the company\u2019s risk-control framework, and monitoring and testing of the company\u2019s risk controls. (C) Reporting responsibilities A chief risk officer shall\u2014 (i) report directly to both the risk committee described under paragraph (3) and the chief executive officer of the company; and (ii) be responsible for reporting risk-management deficiencies and emerging risks to the risk committee described under paragraph (3) and resolving risk-management deficiencies in a timely manner. (D) Vacancies (i) Notification to regulators With respect to a chief risk officer required by this subsection, if the office of a chief risk officer becomes vacant, the company shall\u2014 (I) not later than 24 hours after such vacancy occurs, notify the primary financial regulatory agency of the company, the primary financial regulatory agency of any depository institution subsidiary of the company, and any State agency with supervisory authority over the company or any depository institution subsidiary of the company of such vacancy; and (II) not later than 7 days after such vacancy occurs, submit a plan to the primary financial regulatory agency of the company, the primary financial regulatory agency of any depository institution subsidiary of the company, and any State agency with supervisory authority over the company or any depository institution subsidiary of the company on how the company will search for and promptly hire a well-qualified chief risk officer to fill the vacancy. (ii) Failure to fill vacancy With respect to a vacancy described under clause (i), if the company does not fill the vacancy within 60 days of the vacancy occurring\u2014 (I) the company shall notify the public, including on the website of the company, that the vacancy has existed for more than 60 days; and (II) the total assets of the company may not exceed the total assets of the company on the date the vacancy occurred until such time as the vacancy is filled. (5) Application to large banks with no bank holding company The primary financial regulatory agencies shall issue regulations requiring each bank that does not have a bank holding company and that has total consolidated assets of not less than $50,000,000,000 to establish a risk committee, as set forth in paragraph (3) and appoint a chief risk officer, as set forth in paragraph (4). (6) Primary financial regulatory agency for certain nonbank financial companies For purposes of this subsection, the primary financial regulatory agency for a nonbank financial company supervised by the Board of Governors shall be the Board of Governors. .",
      "versionDate": "2025-03-06",
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
        "updateDate": "2025-03-25T14:36:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119hr1910",
          "measure-number": "1910",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1910v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Chief Risk Officer Enforcement and Accountability Act </strong></p><p>This bill expands which financial companies must establish a risk committee and appoint a chief risk officer and provides statutory authority for requiring large bank holding companies to appoint a chief risk officer. Chief risk officers are responsible for the establishment of risk limits, monitoring compliance, and reporting any deficiencies to the risk committee. Risk committees are responsible for the oversight of the risk management practices\u00a0of the entire company.</p><p>Currently, large bank holding companies that are publicly traded are required to establish risk committees and, by regulation, have chief risk officers. Under the bill, risk committees and chief risk officers are also required for (1) privately\u00a0held large bank holding companies, and (2) large banks that do not have a holding company. Additionally, the bill requires companies to notify regulators\u00a0if the chief risk officer position is vacant within 24 hours of when the vacancy occurs. If the vacancy lasts 60 days or more,\u00a0the company\u2019s assets are capped at the amount held at the time the vacancy occurred.\u00a0</p><p>Further, the bill allows the Federal Reserve Board to require smaller bank holding companies to establish a risk committee and appoint a chief risk officer. Currently, the board is allowed to require smaller bank companies that are publicly traded to establish risk committees.</p>"
        },
        "title": "Chief Risk Officer Enforcement and Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1910.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Chief Risk Officer Enforcement and Accountability Act </strong></p><p>This bill expands which financial companies must establish a risk committee and appoint a chief risk officer and provides statutory authority for requiring large bank holding companies to appoint a chief risk officer. Chief risk officers are responsible for the establishment of risk limits, monitoring compliance, and reporting any deficiencies to the risk committee. Risk committees are responsible for the oversight of the risk management practices\u00a0of the entire company.</p><p>Currently, large bank holding companies that are publicly traded are required to establish risk committees and, by regulation, have chief risk officers. Under the bill, risk committees and chief risk officers are also required for (1) privately\u00a0held large bank holding companies, and (2) large banks that do not have a holding company. Additionally, the bill requires companies to notify regulators\u00a0if the chief risk officer position is vacant within 24 hours of when the vacancy occurs. If the vacancy lasts 60 days or more,\u00a0the company\u2019s assets are capped at the amount held at the time the vacancy occurred.\u00a0</p><p>Further, the bill allows the Federal Reserve Board to require smaller bank holding companies to establish a risk committee and appoint a chief risk officer. Currently, the board is allowed to require smaller bank companies that are publicly traded to establish risk committees.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr1910"
    },
    "title": "Chief Risk Officer Enforcement and Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Chief Risk Officer Enforcement and Accountability Act </strong></p><p>This bill expands which financial companies must establish a risk committee and appoint a chief risk officer and provides statutory authority for requiring large bank holding companies to appoint a chief risk officer. Chief risk officers are responsible for the establishment of risk limits, monitoring compliance, and reporting any deficiencies to the risk committee. Risk committees are responsible for the oversight of the risk management practices\u00a0of the entire company.</p><p>Currently, large bank holding companies that are publicly traded are required to establish risk committees and, by regulation, have chief risk officers. Under the bill, risk committees and chief risk officers are also required for (1) privately\u00a0held large bank holding companies, and (2) large banks that do not have a holding company. Additionally, the bill requires companies to notify regulators\u00a0if the chief risk officer position is vacant within 24 hours of when the vacancy occurs. If the vacancy lasts 60 days or more,\u00a0the company\u2019s assets are capped at the amount held at the time the vacancy occurred.\u00a0</p><p>Further, the bill allows the Federal Reserve Board to require smaller bank holding companies to establish a risk committee and appoint a chief risk officer. Currently, the board is allowed to require smaller bank companies that are publicly traded to establish risk committees.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr1910"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1910ih.xml"
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
      "title": "Chief Risk Officer Enforcement and Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chief Risk Officer Enforcement and Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Financial Stability Act of 2010 to require certain large banking institutions to have a Chief Risk Officer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:18:26Z"
    }
  ]
}
```
