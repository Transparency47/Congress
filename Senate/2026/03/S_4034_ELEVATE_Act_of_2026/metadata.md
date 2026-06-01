# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4034?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4034
- Title: ELEVATE Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4034
- Origin chamber: Senate
- Introduced date: 2026-03-10
- Update date: 2026-03-26T18:18:26Z
- Update date including text: 2026-03-26T18:18:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-10: Introduced in Senate
- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-03-10: Introduced in Senate

## Actions

- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-10",
    "latestAction": {
      "actionDate": "2026-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4034",
    "number": "4034",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "ELEVATE Act of 2026",
    "type": "S",
    "updateDate": "2026-03-26T18:18:26Z",
    "updateDateIncludingText": "2026-03-26T18:18:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-10",
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
      "actionDate": "2026-03-10",
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
          "date": "2026-03-10T14:17:04Z",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4034is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4034\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2026 Mr. Ricketts (for himself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Securities Exchange Act of 1934 to specify certain registration statement contents for emerging growth companies, to permit issuers to file draft registration statements with the Securities and Exchange Commission for confidential review, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Encouraging Local Emerging Ventures and Economic Growth Act of 2026 or the ELEVATE Act of 2026 .\n#### 2. Registration statements\nSection 12(b) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78l(b) ) is amended\u2014\n**(1)**\nin paragraph (1), by redesignating subparagraphs (A) through (L) as clauses (i) through (xii), respectively;\n**(2)**\nby redesignating paragraphs (1), (2), and (3) as subparagraphs (A), (B), and (C), respectively;\n**(3)**\nby inserting (1) after (b) ;\n**(4)**\nin the matter preceding subparagraph (A) of paragraph (1), as so redesignated, by striking shall contain\u2014 and inserting shall contain the following: ;\n**(5)**\nin paragraph (1)(A)(xi), as so redesignated, by striking years, and inserting years (or, in the case of an emerging growth company, not more than the two preceding fiscal years), ;\n**(6)**\nin paragraph (1)(C), as so redesignated, by striking paragraph (1)(I) and inserting subparagraph (A)(ix) ; and\n**(7)**\nby adding at the end the following:\n(2) (A) Any issuer may confidentially submit to the Commission a draft registration statement for confidential nonpublic review by the staff of the Commission prior to public filing of that registration statement, provided that the initial confidential submission and all amendments to that confidential submission shall be publicly filed with the Commission not later than 10 days before the applicable security is listed on a national securities exchange. (B) Notwithstanding any other provision of this title, the Commission shall not be compelled to disclose any information provided to or obtained by the Commission pursuant to this paragraph. (C) For purposes of section 552 of title 5, United States Code, this paragraph shall be considered a statute described in subsection (b)(3)(B) of such section 552. (D) Information described in or obtained pursuant to this paragraph shall be deemed to constitute confidential information for purposes of section 24. .",
      "versionDate": "2026-03-10",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-03-26T18:18:26Z"
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
      "date": "2026-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4034is.xml"
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
      "title": "ELEVATE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ELEVATE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Encouraging Local Emerging Ventures and Economic Growth Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Securities Exchange Act of 1934 to specify certain registration statement contents for emerging growth companies, to permit issuers to file draft registration statements with the Securities and Exchange Commission for confidential review, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T03:48:27Z"
    }
  ]
}
```
