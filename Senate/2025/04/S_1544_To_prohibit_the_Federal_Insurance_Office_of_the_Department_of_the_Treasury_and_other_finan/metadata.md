# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1544?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1544
- Title: Insurance Data Protection Act
- Congress: 119
- Bill type: S
- Bill number: 1544
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2026-03-09T21:02:31Z
- Update date including text: 2026-03-09T21:02:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1544",
    "number": "1544",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001319",
        "district": "",
        "firstName": "Katie",
        "fullName": "Sen. Britt, Katie Boyd [R-AL]",
        "lastName": "Britt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Insurance Data Protection Act",
    "type": "S",
    "updateDate": "2026-03-09T21:02:31Z",
    "updateDateIncludingText": "2026-03-09T21:02:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T23:30:20Z",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "SC"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "SD"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "ID"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "NC"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "LA"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "TN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "WY"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "IN"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "ND"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1544is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1544\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mrs. Britt (for herself, Mr. Scott of South Carolina , Mr. Rounds , Mr. Crapo , Mr. Tillis , Mr. Kennedy , Mr. Hagerty , Ms. Lummis , Mr. Ricketts , Mr. Banks , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo prohibit the Federal Insurance Office of the Department of the Treasury and other financial regulators from collecting data directly from an insurance company.\n#### 1. Short title\nThis Act may be cited as the Insurance Data Protection Act .\n#### 2. Repeal of subpoena and enforcement authority\nSection 313(e) of title 31, United States Code, is amended by striking paragraph (6).\n#### 3. Confidentiality by Federal Insurance Office\nSection 313(e)(5) of title 31, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by inserting after Office the following: , or the sharing of any nonpublicly available data and information with or by the Office among any other Federal agency, any State insurance regulator (or any agent of such a regulator), or any other entity, ;\n**(2)**\nin subparagraph (C)(ii), by inserting any privilege described in subparagraph (A) or after including ; and\n**(3)**\nin subparagraph (D), by inserting including the exceptions under that section, after United States Code, .\n#### 4. Limitation on subpoenas by the Office of Financial Research\nSection 153(f)(1) of the Financial Stability Act of 2010 ( 12 U.S.C. 5343(f)(1) ) is amended, in the matter preceding subparagraph (A), by inserting after financial company the following: (other than an insurance company, as defined in section 201(a)) .\n#### 5. Confidentiality by financial regulators\n##### (a) In general\nThe Financial Stability Act of 2010 ( 12 U.S.C. 5311 et seq. ) is amended by adding at the end the following:\nD Treatment of data collected from insurance companies 181. Treatment of data collected from insurance companies by financial regulators (a) Definitions In this section: (1) Covered entity The term covered entity means a nonbank financial company that is an insurance company. (2) Financial regulator The term financial regulator means the Commission, the Commodity Futures Trading Commission, the Council, the Federal banking agencies, and the Office of Financial Research. (3) Insurance company The term insurance company has the meaning given the term in section 201(a). (b) Advance coordination (1) In general (A) Pre-collection Before collecting any data or information pursuant to this title or title II from a covered entity, a financial regulator shall coordinate with each relevant Federal agency, State insurance regulator, and other Federal or State regulatory agency, and with any publicly available source, to determine if the data or information to be collected is available from, and may be obtained in a timely manner by, that agency, regulator, or regulatory agency, individually or collectively, or that publicly available source. (B) Determinations (i) Information available If a financial regulator, under subparagraph (A), determines that the data or information described in that subparagraph is available, and may be obtained in a timely manner, from an agency, regulator, regulatory agency, or source described in that subparagraph, the financial regulator shall obtain the data or information from that agency, regulator, regulatory agency, or source. (ii) Information unavailable If a financial regulator, under subparagraph (A) determines that the data or information described in that subparagraph is not available, the financial regulatory may collect that data or information from the applicable covered entity only if the financial regulator complies with the requirements of subchapter I of chapter 35 of title 44, United States Code (commonly referred to as the \u2018Paperwork Reduction Act \u2019), in collecting that data or information. (2) Authority to provide information Notwithstanding any other provision of law, for the purposes of paragraph (1), each relevant Federal agency and State insurance regulator or other Federal or State regulatory agency may provide to a financial regulator data or information described in that paragraph. (c) Confidentiality (1) Retention of privilege The sharing by a covered entity of any nonpublicly available data or information with a financial regulator under this title or title II shall not constitute a waiver of, or otherwise affect, any privilege arising under Federal or State law (including the rules of any Federal or State court) to which the data or information is otherwise subject. (2) Continued application of prior confidentiality agreements Any requirement under Federal or State law to the extent otherwise applicable, or any requirement pursuant to a written agreement in effect between the original source of any nonpublicly available data or information and the source of that data or information to a financial regulator, regarding the privacy or confidentiality of any data or information in the possession of the source to a financial regulator, shall continue to apply to that data or information after the data or information has been provided under this section to the financial regulator. (3) Information-sharing agreement Any data or information obtained by a financial regulator may be made available to State insurance regulators, individually or collectively, through an information-sharing agreement that\u2014 (A) shall comply with applicable Federal law; and (B) shall not constitute a waiver of, or otherwise affect, any privilege under Federal or State law (including any privilege described in paragraph (1) and the rules of any Federal or State court) to which the data or information is otherwise subject. (4) Agency disclosure requirements Section 552 of title 5, United States Code, including the exceptions under that section, shall apply to any data or information submitted to a financial regulator by a covered entity under this section. .\n##### (b) Technical amendment\nThe table of contents in section 1(b) of the Dodd-Frank Wall Street Reform and Consumer Protection Act ( Public Law 111\u2013203 ) is amended by inserting after the item relating to section 176 the following:\nSubtitle D\u2014Treatment of data collected from insurance companies Sec. 181. Treatment of data collected from insurance companies by financial regulators. .",
      "versionDate": "2025-04-30",
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
        "actionDate": "2025-05-15",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3437",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Insurance Data Protection Act",
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
        "updateDate": "2025-05-21T12:19:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
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
          "measure-id": "id119s1544",
          "measure-number": "1544",
          "measure-type": "s",
          "orig-publish-date": "2025-04-30",
          "originChamber": "SENATE",
          "update-date": "2026-03-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1544v00",
            "update-date": "2026-03-09"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Insurance Data Protection Act</strong></p><p>This bill limits the ability of federal entities to compel insurance companies to share information.</p><p>Specifically, the bill eliminates the subpoena power of the Federal Insurance Office. Under current law, the office has the power to subpoena information from insurers to, among other purposes, identify issues that could contribute to a systemic crisis in the insurance industry or the U.S. financial system.</p><p>The bill also eliminates the ability of the Office of Financial Research to subpoena insurance companies.</p><p>When seeking to collect insurance company data under specified consumer protection laws, a financial regulator must obtain the data from other regulators or from publicly available sources if possible. Otherwise, the financial regulator may only collect this data directly from the insurance company if the regulator complies with the Paperwork Reduction Act.\u00a0 \u00a0</p>"
        },
        "title": "Insurance Data Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1544.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Insurance Data Protection Act</strong></p><p>This bill limits the ability of federal entities to compel insurance companies to share information.</p><p>Specifically, the bill eliminates the subpoena power of the Federal Insurance Office. Under current law, the office has the power to subpoena information from insurers to, among other purposes, identify issues that could contribute to a systemic crisis in the insurance industry or the U.S. financial system.</p><p>The bill also eliminates the ability of the Office of Financial Research to subpoena insurance companies.</p><p>When seeking to collect insurance company data under specified consumer protection laws, a financial regulator must obtain the data from other regulators or from publicly available sources if possible. Otherwise, the financial regulator may only collect this data directly from the insurance company if the regulator complies with the Paperwork Reduction Act.\u00a0 \u00a0</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119s1544"
    },
    "title": "Insurance Data Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Insurance Data Protection Act</strong></p><p>This bill limits the ability of federal entities to compel insurance companies to share information.</p><p>Specifically, the bill eliminates the subpoena power of the Federal Insurance Office. Under current law, the office has the power to subpoena information from insurers to, among other purposes, identify issues that could contribute to a systemic crisis in the insurance industry or the U.S. financial system.</p><p>The bill also eliminates the ability of the Office of Financial Research to subpoena insurance companies.</p><p>When seeking to collect insurance company data under specified consumer protection laws, a financial regulator must obtain the data from other regulators or from publicly available sources if possible. Otherwise, the financial regulator may only collect this data directly from the insurance company if the regulator complies with the Paperwork Reduction Act.\u00a0 \u00a0</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119s1544"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1544is.xml"
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
      "title": "Insurance Data Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T11:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Insurance Data Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Federal Insurance Office of the Department of the Treasury and other financial regulators from collecting data directly from an insurance company.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:27Z"
    }
  ]
}
```
