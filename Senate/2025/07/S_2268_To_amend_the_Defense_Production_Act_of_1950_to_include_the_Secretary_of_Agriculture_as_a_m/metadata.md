# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2268?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2268
- Title: Agricultural Risk Review Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2268
- Origin chamber: Senate
- Introduced date: 2025-07-14
- Update date: 2026-04-23T14:07:30Z
- Update date including text: 2026-04-23T14:07:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-14: Introduced in Senate
- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-14: Introduced in Senate

## Actions

- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2268",
    "number": "2268",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Agricultural Risk Review Act of 2025",
    "type": "S",
    "updateDate": "2026-04-23T14:07:30Z",
    "updateDateIncludingText": "2026-04-23T14:07:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-14",
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
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T20:52:55Z",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MD"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "WY"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "PA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "MI"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2268is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2268\nIN THE SENATE OF THE UNITED STATES\nJuly 14, 2025 Mr. Cramer (for himself, Ms. Alsobrooks , Ms. Lummis , and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Defense Production Act of 1950 to include the Secretary of Agriculture as a member of the Committee on Foreign Investment in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Agricultural Risk Review Act of 2025 .\n#### 2. Inclusion of the Secretary of Agriculture on the Committee on Foreign Investment in the United States\nSection 721(k) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(k) ) is amended by adding at the end the following:\n(8) Inclusion of the Secretary of Agriculture The Secretary of Agriculture shall be a member of the Committee with respect to a covered transaction that involves\u2014 (A) agricultural land; (B) agriculture biotechnology; or (C) the agriculture industry, including agricultural transportation, storage, and processing. .\n#### 3. Consideration of certain agricultural land transactions\nSection 721(b)(1) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(b)(1) ) is amended by adding at the end the following:\n(I) Consideration of certain agricultural land transactions (i) In general After receiving notification from the Secretary of Agriculture of a reportable agricultural land transaction, the Committee shall determine\u2014 (I) whether the transaction is a covered transaction; and (II) if the Committee determines that the transaction is a covered transaction, whether the Committee should initiate a review pursuant to subparagraph (D), or take another action authorized under this section, with respect to the reportable agricultural land transaction. (ii) Reportable agricultural land transaction In this subparagraph, the term reportable agricultural land transaction means a transaction\u2014 (I) that the Secretary of Agriculture has reason to believe is a covered transaction, based on information from or in cooperation with the intelligence community; (II) that involves the acquisition of an interest in agricultural land by a foreign person of the People\u2019s Republic of China, the Democratic People\u2019s Republic of Korea, the Russian Federation, or the Islamic Republic of Iran; and (III) with respect to which a person is required to submit a report to the Secretary of Agriculture under section 2(a) of the Agricultural Foreign Investment Disclosure Act of 1978. (iii) Sunset The requirements under this subparagraph shall terminate, with respect to a foreign person of the respective foreign country, on the date that the People\u2019s Republic of China, the Democratic People\u2019s Republic of Korea, the Russian Federation, or the Islamic Republic of Iran, as the case may be, is removed from the list of foreign adversaries in section 791.4 of title 15, Code of Federal Regulations. .",
      "versionDate": "2025-07-14",
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
        "actionDate": "2026-04-15",
        "text": "Placed on the Union Calendar, Calendar No. 529."
      },
      "number": "7688",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DPA Modernization Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-21",
        "text": "Placed on the Union Calendar, Calendar No. 537."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
    },
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-24",
        "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1713",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Agricultural Risk Review Act of 2025",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-07-29T22:11:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-14",
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
          "measure-id": "id119s2268",
          "measure-number": "2268",
          "measure-type": "s",
          "orig-publish-date": "2025-07-14",
          "originChamber": "SENATE",
          "update-date": "2025-07-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2268v00",
            "update-date": "2025-07-30"
          },
          "action-date": "2025-07-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Agricultural Risk Review Act of 2025</strong></p><p>This bill makes changes to the Committee on Foreign Investment in the United States (CFIUS), including by requiring CFIUS to determine whether a national security review is necessary for reportable agricultural land transactions that are referred by the Department of Agriculture (USDA). (CFIUS oversees the national security risks of certain foreign investment in the United States. CFIUS has the authority to review covered transactions, which include\u00a0mergers, acquisitions, and takeovers that could result in foreign control of a U.S. business; certain investments in businesses involved in critical technologies, critical infrastructure, or sensitive personal data; and certain real estate transactions.)</p><p>Specifically, the bill directs CFIUS to, after receiving notification from USDA, determine (1) whether a reportable agricultural land transaction is a covered transaction, and (2) whether CFIUS should initiate a national security review or take another action with respect to the transaction.\u00a0</p><p><em>Reportable</em><em> agricultural land transaction</em> means a transaction (1) that USDA has reason to believe\u00a0is a covered transaction, based on information from or in cooperation with\u00a0the intelligence community; (2) that involves the acquisition of an interest in agricultural land by a foreign person of China, North Korea, Russia, or Iran; and (3) with respect to which a foreign person is required to submit a report to USDA regarding their agricultural land transactions.</p><p>The bill also expands CFIUS to include the Secretary of Agriculture for covered transactions that involve agricultural land, agricultural biotechnology, or the agriculture industry (e.g., agricultural transportation, storage, and processing).</p>"
        },
        "title": "Agricultural Risk Review Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2268.xml",
    "summary": {
      "actionDate": "2025-07-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Agricultural Risk Review Act of 2025</strong></p><p>This bill makes changes to the Committee on Foreign Investment in the United States (CFIUS), including by requiring CFIUS to determine whether a national security review is necessary for reportable agricultural land transactions that are referred by the Department of Agriculture (USDA). (CFIUS oversees the national security risks of certain foreign investment in the United States. CFIUS has the authority to review covered transactions, which include\u00a0mergers, acquisitions, and takeovers that could result in foreign control of a U.S. business; certain investments in businesses involved in critical technologies, critical infrastructure, or sensitive personal data; and certain real estate transactions.)</p><p>Specifically, the bill directs CFIUS to, after receiving notification from USDA, determine (1) whether a reportable agricultural land transaction is a covered transaction, and (2) whether CFIUS should initiate a national security review or take another action with respect to the transaction.\u00a0</p><p><em>Reportable</em><em> agricultural land transaction</em> means a transaction (1) that USDA has reason to believe\u00a0is a covered transaction, based on information from or in cooperation with\u00a0the intelligence community; (2) that involves the acquisition of an interest in agricultural land by a foreign person of China, North Korea, Russia, or Iran; and (3) with respect to which a foreign person is required to submit a report to USDA regarding their agricultural land transactions.</p><p>The bill also expands CFIUS to include the Secretary of Agriculture for covered transactions that involve agricultural land, agricultural biotechnology, or the agriculture industry (e.g., agricultural transportation, storage, and processing).</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119s2268"
    },
    "title": "Agricultural Risk Review Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Agricultural Risk Review Act of 2025</strong></p><p>This bill makes changes to the Committee on Foreign Investment in the United States (CFIUS), including by requiring CFIUS to determine whether a national security review is necessary for reportable agricultural land transactions that are referred by the Department of Agriculture (USDA). (CFIUS oversees the national security risks of certain foreign investment in the United States. CFIUS has the authority to review covered transactions, which include\u00a0mergers, acquisitions, and takeovers that could result in foreign control of a U.S. business; certain investments in businesses involved in critical technologies, critical infrastructure, or sensitive personal data; and certain real estate transactions.)</p><p>Specifically, the bill directs CFIUS to, after receiving notification from USDA, determine (1) whether a reportable agricultural land transaction is a covered transaction, and (2) whether CFIUS should initiate a national security review or take another action with respect to the transaction.\u00a0</p><p><em>Reportable</em><em> agricultural land transaction</em> means a transaction (1) that USDA has reason to believe\u00a0is a covered transaction, based on information from or in cooperation with\u00a0the intelligence community; (2) that involves the acquisition of an interest in agricultural land by a foreign person of China, North Korea, Russia, or Iran; and (3) with respect to which a foreign person is required to submit a report to USDA regarding their agricultural land transactions.</p><p>The bill also expands CFIUS to include the Secretary of Agriculture for covered transactions that involve agricultural land, agricultural biotechnology, or the agriculture industry (e.g., agricultural transportation, storage, and processing).</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119s2268"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2268is.xml"
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
      "title": "Agricultural Risk Review Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-10T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Agricultural Risk Review Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Defense Production Act of 1950 to include the Secretary of Agriculture as a member of the Committee on Foreign Investment in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T02:18:20Z"
    }
  ]
}
```
