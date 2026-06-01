# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/732?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/732
- Title: Protecting American Agriculture from Foreign Adversaries Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 732
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-07-24T14:29:23Z
- Update date including text: 2025-07-24T14:29:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/732",
    "number": "732",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Protecting American Agriculture from Foreign Adversaries Act of 2025",
    "type": "S",
    "updateDate": "2025-07-24T14:29:23Z",
    "updateDateIncludingText": "2025-07-24T14:29:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T22:56:57Z",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "WI"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "WY"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "IN"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s732is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 732\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Marshall (for himself, Ms. Baldwin , Mr. Barrasso , and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Defense Production Act of 1950 with respect to foreign investments in United States agriculture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting American Agriculture from Foreign Adversaries Act of 2025 .\n#### 2. Inclusion of Secretary of Agriculture on Committee on Foreign Investment in United States and consideration of certain agricultural land transactions\n##### (a) Inclusion on the committee\nSection 721(k) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(k) ) is amended by adding at the end the following:\n(8) Inclusion of the Secretary of Agriculture The Secretary of Agriculture shall be a member of the Committee with respect to a covered transaction that involves\u2014 (A) agricultural land; (B) agriculture biotechnology; or (C) the agriculture industry, including agricultural\u2014 (i) transportation; (ii) storage; and (iii) processing. .\n##### (b) Consideration of certain agricultural land transactions\nSection 721(b)(1) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(b)(1) ) is amended by adding at the end the following:\n(I) Consideration of certain agricultural land transactions (i) In general After receiving notification from the Secretary of Agriculture of a reportable agricultural land transaction, the Committee shall determine\u2014 (I) whether the transaction is a covered transaction; and (II) if the Committee determines that the transaction is a covered transaction, whether the Committee should initiate a review pursuant to subparagraph (D), or take another action authorized under this section, with respect to the reportable agricultural land transaction. (ii) Sunset The requirements under this subparagraph shall terminate, with respect to a foreign person of a covered country, on the date on which that country is removed from the list of foreign adversaries set forth in section 791.4 of title 15, Code of Federal Regulations. (iii) Definitions In this subparagraph: (I) Covered country The term covered country means the People\u2019s Republic of China, the Democratic People\u2019s Republic of Korea, the Russian Federation, or the Islamic Republic of Iran. (II) Reportable agricultural land transaction The term reportable agricultural land transaction means a transaction\u2014 (aa) that the Secretary of Agriculture has reason to believe is a covered transaction; (bb) that involves the acquisition of an interest in agricultural land by a foreign person of a covered country; and (cc) with respect to which a person is required to submit a report to the Secretary of Agriculture under section 2(a) of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501(a) ). .",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-02-25",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committees on Foreign Affairs, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1576",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting American Agriculture from Foreign Adversaries Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Asia",
            "updateDate": "2025-07-24T14:28:38Z"
          },
          {
            "name": "China",
            "updateDate": "2025-07-24T14:28:33Z"
          },
          {
            "name": "Department of Agriculture",
            "updateDate": "2025-07-24T14:29:18Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-07-24T14:28:54Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-07-24T14:29:23Z"
          },
          {
            "name": "Iran",
            "updateDate": "2025-07-24T14:29:02Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-07-24T14:28:29Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2025-07-24T14:28:58Z"
          },
          {
            "name": "North Korea",
            "updateDate": "2025-07-24T14:28:43Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-07-24T14:28:50Z"
          },
          {
            "name": "U.S. and foreign investments",
            "updateDate": "2025-07-24T14:29:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-13T19:24:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119s732",
          "measure-number": "732",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-06-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s732v00",
            "update-date": "2025-06-23"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting American Agriculture from Foreign Adversaries Act of 2025</strong></p><p>This bill makes changes to the Committee on Foreign Investment in the United States (CFIUS), including by requiring CFIUS to determine whether a national security review is necessary for reportable agricultural land transactions that are referred by the Department of Agriculture (USDA). (CFIUS oversees the national security risks of certain foreign investment in the United States. CFIUS has the authority to review covered transactions, which include\u00a0mergers, acquisitions, and takeovers that could result in foreign control of a U.S. business; certain investments in businesses involved in critical technologies, critical infrastructure, or sensitive personal data; and certain real estate transactions.)</p><p>Specifically, the bill directs CFIUS to, after receiving notification from USDA, determine (1) whether a reportable agricultural land transaction is a covered transaction, and (2) whether CFIUS should initiate a national security review or take another action with respect to the transaction.\u00a0</p><p><em>Reportable</em><em> agricultural land transaction</em> means a transaction (1) that USDA has reason to believe is a covered transaction; (2) that involves the acquisition of an interest in agricultural land by a foreign person of China, North Korea, Russia, or Iran; and (3) with respect to which a foreign person is required to submit a report to USDA regarding their agricultural land transactions.</p><p>The bill also expands the membership of CFIUS to include the Secretary of Agriculture for covered transactions that involve agricultural land, agricultural biotechnology, or the agriculture industry (e.g., agricultural transportation, storage, and processing).</p>"
        },
        "title": "Protecting American Agriculture from Foreign Adversaries Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s732.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting American Agriculture from Foreign Adversaries Act of 2025</strong></p><p>This bill makes changes to the Committee on Foreign Investment in the United States (CFIUS), including by requiring CFIUS to determine whether a national security review is necessary for reportable agricultural land transactions that are referred by the Department of Agriculture (USDA). (CFIUS oversees the national security risks of certain foreign investment in the United States. CFIUS has the authority to review covered transactions, which include\u00a0mergers, acquisitions, and takeovers that could result in foreign control of a U.S. business; certain investments in businesses involved in critical technologies, critical infrastructure, or sensitive personal data; and certain real estate transactions.)</p><p>Specifically, the bill directs CFIUS to, after receiving notification from USDA, determine (1) whether a reportable agricultural land transaction is a covered transaction, and (2) whether CFIUS should initiate a national security review or take another action with respect to the transaction.\u00a0</p><p><em>Reportable</em><em> agricultural land transaction</em> means a transaction (1) that USDA has reason to believe is a covered transaction; (2) that involves the acquisition of an interest in agricultural land by a foreign person of China, North Korea, Russia, or Iran; and (3) with respect to which a foreign person is required to submit a report to USDA regarding their agricultural land transactions.</p><p>The bill also expands the membership of CFIUS to include the Secretary of Agriculture for covered transactions that involve agricultural land, agricultural biotechnology, or the agriculture industry (e.g., agricultural transportation, storage, and processing).</p>",
      "updateDate": "2025-06-23",
      "versionCode": "id119s732"
    },
    "title": "Protecting American Agriculture from Foreign Adversaries Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting American Agriculture from Foreign Adversaries Act of 2025</strong></p><p>This bill makes changes to the Committee on Foreign Investment in the United States (CFIUS), including by requiring CFIUS to determine whether a national security review is necessary for reportable agricultural land transactions that are referred by the Department of Agriculture (USDA). (CFIUS oversees the national security risks of certain foreign investment in the United States. CFIUS has the authority to review covered transactions, which include\u00a0mergers, acquisitions, and takeovers that could result in foreign control of a U.S. business; certain investments in businesses involved in critical technologies, critical infrastructure, or sensitive personal data; and certain real estate transactions.)</p><p>Specifically, the bill directs CFIUS to, after receiving notification from USDA, determine (1) whether a reportable agricultural land transaction is a covered transaction, and (2) whether CFIUS should initiate a national security review or take another action with respect to the transaction.\u00a0</p><p><em>Reportable</em><em> agricultural land transaction</em> means a transaction (1) that USDA has reason to believe is a covered transaction; (2) that involves the acquisition of an interest in agricultural land by a foreign person of China, North Korea, Russia, or Iran; and (3) with respect to which a foreign person is required to submit a report to USDA regarding their agricultural land transactions.</p><p>The bill also expands the membership of CFIUS to include the Secretary of Agriculture for covered transactions that involve agricultural land, agricultural biotechnology, or the agriculture industry (e.g., agricultural transportation, storage, and processing).</p>",
      "updateDate": "2025-06-23",
      "versionCode": "id119s732"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s732is.xml"
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
      "title": "Protecting American Agriculture from Foreign Adversaries Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting American Agriculture from Foreign Adversaries Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Defense Production Act of 1950 with respect to foreign investments in United States agriculture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:18Z"
    }
  ]
}
```
